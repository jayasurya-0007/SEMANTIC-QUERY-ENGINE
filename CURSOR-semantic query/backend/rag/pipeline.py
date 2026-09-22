import os
import re
import uuid
import hashlib
from typing import Iterable

import chromadb
from chromadb.config import Settings


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 80) -> list[str]:
    cleaned = clean_text(text)
    if not cleaned:
        return []
    chunks: list[str] = []
    start = 0
    step = max(1, chunk_size - overlap)
    while start < len(cleaned):
        end = min(len(cleaned), start + chunk_size)
        chunks.append(cleaned[start:end])
        start += step
    return chunks


class RagEngine:
    def __init__(self) -> None:
        vector_dir = os.getenv("CHROMA_DIR", "backend/data/vector_store")
        self.client = chromadb.PersistentClient(path=vector_dir, settings=Settings(anonymized_telemetry=False))
        self.collection = self.client.get_or_create_collection(name="semantic_query_chunks")
        self.embed_model = None
        model_name = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
        try:
            from sentence_transformers import SentenceTransformer

            self.embed_model = SentenceTransformer(model_name)
        except Exception:
            self.embed_model = None

    def _embeddings(self, texts: Iterable[str]) -> list[list[float]]:
        texts_list = list(texts)
        if self.embed_model is not None:
            vectors = self.embed_model.encode(texts_list, normalize_embeddings=True)
            return [vector.tolist() for vector in vectors]

        # Deterministic fallback embedding for offline/runtime-constrained environments.
        vectors: list[list[float]] = []
        for text in texts_list:
            digest = hashlib.sha256(text.encode("utf-8")).digest()
            vec = [((byte / 255.0) * 2.0) - 1.0 for byte in digest]  # 32 dims
            vectors.append(vec)
        return vectors

    def index_document(self, user_id: int, source_id: int, source_name: str, text: str) -> int:
        chunks = chunk_text(text)
        if not chunks:
            return 0
        ids = [str(uuid.uuid4()) for _ in chunks]
        metadatas = [
            {
                "user_id": str(user_id),
                "source_id": str(source_id),
                "source_name": source_name,
                "chunk_index": str(index),
            }
            for index, _ in enumerate(chunks)
        ]
        embeddings = self._embeddings(chunks)
        self.collection.add(ids=ids, documents=chunks, metadatas=metadatas, embeddings=embeddings)
        return len(chunks)

    def retrieve(self, user_id: int, question: str, k: int = 4) -> list[dict]:
        query_embedding = self._embeddings([question])[0]
        result = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k,
            where={"user_id": str(user_id)},
        )
        docs = result.get("documents", [[]])[0]
        metas = result.get("metadatas", [[]])[0]
        if not docs:
            return []
        return [{"text": doc, "meta": meta} for doc, meta in zip(docs, metas)]
