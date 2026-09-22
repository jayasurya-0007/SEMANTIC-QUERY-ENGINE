import time

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from auth.security import get_current_user
from database.db import get_db
from database.models import User
from rag.gemini_client import GeminiClient
from rag.pipeline import RagEngine

router = APIRouter(tags=["query"])
rag_engine = RagEngine()
gemini = GeminiClient()


class QueryRequest(BaseModel):
    question: str = Field(min_length=2)
    top_k: int = Field(default=4, ge=1, le=10)


@router.post("/query")
def query(payload: QueryRequest, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    del db
    start = time.perf_counter()
    matches = rag_engine.retrieve(user.id, payload.question, payload.top_k)
    if not matches:
        raise HTTPException(status_code=404, detail="No relevant context found for this user.")

    context_lines = []
    for item in matches:
        meta = item["meta"]
        marker = f"[source:{meta.get('source_id')}]"
        context_lines.append(f"{marker} {item['text']}")

    context = "\n".join(context_lines)
    try:
        answer = gemini.generate_answer(payload.question, context)
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    elapsed_ms = round((time.perf_counter() - start) * 1000, 2)
    return {"answer": answer, "sources": matches, "response_time_ms": elapsed_ms}
