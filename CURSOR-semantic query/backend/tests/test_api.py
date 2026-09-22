import io
import os
import tempfile
from collections import defaultdict

from fastapi.testclient import TestClient

os.environ["SQLITE_DB_PATH"] = tempfile.NamedTemporaryFile(suffix=".db", delete=False).name
os.environ["CHROMA_DIR"] = tempfile.mkdtemp()
os.environ["JWT_SECRET_KEY"] = "test-secret"

from main import app  # noqa: E402


class FakeRagEngine:
    def __init__(self):
        self.store = defaultdict(list)

    def index_document(self, user_id, source_id, source_name, text):
        chunks = [text[i : i + 100] for i in range(0, len(text), 100)] or [text]
        for chunk in chunks:
            self.store[user_id].append({"text": chunk, "meta": {"source_id": str(source_id), "source_name": source_name}})
        return len(chunks)

    def retrieve(self, user_id, question, k=4):
        candidates = self.store.get(user_id, [])
        hits = [item for item in candidates if any(token.lower() in item["text"].lower() for token in question.split())]
        return (hits or candidates)[:k]


class FakeGemini:
    def generate_answer(self, question, context):
        if not context.strip():
            return "I don't have enough information in the provided sources."
        return f"Context-backed answer for: {question}"


def get_token(client):
    email = "user@example.com"
    password = "password123"
    client.post("/signup", json={"email": email, "password": password})
    response = client.post("/login", json={"email": email, "password": password})
    return response.json()["access_token"]


def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}


def test_auth_signup_login():
    client = TestClient(app)
    signup = client.post("/signup", json={"email": "a@a.com", "password": "password123"})
    assert signup.status_code == 200
    login = client.post("/login", json={"email": "a@a.com", "password": "password123"})
    assert login.status_code == 200
    assert "access_token" in login.json()


def test_upload_text_and_sources(monkeypatch):
    from routes import upload as upload_route

    upload_route.rag_engine = FakeRagEngine()
    client = TestClient(app)
    token = get_token(client)
    response = client.post(
        "/upload",
        headers=auth_headers(token),
        data={"source_type": "text", "text": "FastAPI with retrieval augmented generation."},
    )
    assert response.status_code == 200
    assert response.json()["chunks_indexed"] >= 1

    sources = client.get("/sources", headers=auth_headers(token))
    assert sources.status_code == 200
    assert len(sources.json()) >= 1


def test_upload_invalid_file_type(monkeypatch):
    from routes import upload as upload_route

    upload_route.rag_engine = FakeRagEngine()
    client = TestClient(app)
    token = get_token(client)
    file_data = io.BytesIO(b"hello")
    response = client.post(
        "/upload",
        headers=auth_headers(token),
        data={"source_type": "file"},
        files={"file": ("bad.csv", file_data, "text/csv")},
    )
    assert response.status_code == 400


def test_query_uses_context(monkeypatch):
    from routes import query as query_route
    from routes import upload as upload_route

    fake = FakeRagEngine()
    upload_route.rag_engine = fake
    query_route.rag_engine = fake
    query_route.gemini = FakeGemini()

    client = TestClient(app)
    token = get_token(client)
    client.post(
        "/upload",
        headers=auth_headers(token),
        data={"source_type": "text", "text": "Vector databases store embeddings for semantic search."},
    )
    response = client.post("/query", headers=auth_headers(token), json={"question": "What stores embeddings?", "top_k": 3})
    assert response.status_code == 200
    payload = response.json()
    assert "Context-backed answer" in payload["answer"]
    assert len(payload["sources"]) >= 1
    assert payload["response_time_ms"] >= 0


def test_query_missing_context(monkeypatch):
    from routes import query as query_route

    query_route.rag_engine = FakeRagEngine()
    query_route.gemini = FakeGemini()
    client = TestClient(app)
    token = get_token(client)
    response = client.post("/query", headers=auth_headers(token), json={"question": "No data", "top_k": 3})
    assert response.status_code == 404


def test_tts_endpoint(monkeypatch):
    class FakeGTTS:
        def __init__(self, text, lang):
            self.text = text
            self.lang = lang

        def save(self, path):
            with open(path, "wb") as handle:
                handle.write(b"mp3")

    from routes import tts as tts_route

    tts_route.gTTS = FakeGTTS
    client = TestClient(app)
    token = get_token(client)
    response = client.post("/tts", headers=auth_headers(token), json={"text": "Hello world", "lang": "en"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "audio/mpeg"


def test_missing_api_key_error():
    from routes import query as query_route
    from routes import upload as upload_route

    class FailGemini:
        def generate_answer(self, question, context):
            raise RuntimeError("Missing GEMINI_API_KEY in environment.")

    fake = FakeRagEngine()
    upload_route.rag_engine = fake
    query_route.rag_engine = fake
    query_route.gemini = FailGemini()

    client = TestClient(app)
    token = get_token(client)
    client.post(
        "/upload",
        headers=auth_headers(token),
        data={"source_type": "text", "text": "Seed text for context"},
    )
    response = client.post("/query", headers=auth_headers(token), json={"question": "seed", "top_k": 1})
    assert response.status_code == 500


def test_empty_upload_text():
    client = TestClient(app)
    token = get_token(client)
    response = client.post("/upload", headers=auth_headers(token), data={"source_type": "text", "text": "   "})
    assert response.status_code == 400
