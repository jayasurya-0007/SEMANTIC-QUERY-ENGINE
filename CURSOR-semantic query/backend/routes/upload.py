from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from pydantic import BaseModel, HttpUrl
from sqlalchemy.orm import Session

from auth.security import get_current_user
from database.db import get_db
from database.models import SourceDocument, User
from rag.loaders import extract_text_from_url, parse_uploaded_file
from rag.pipeline import RagEngine

router = APIRouter(tags=["upload"])
rag_engine = RagEngine()


class UrlUploadRequest(BaseModel):
    url: HttpUrl


@router.post("/upload")
async def upload_source(
    source_type: str = Form(...),
    text: str | None = Form(default=None),
    url: str | None = Form(default=None),
    file: UploadFile | None = File(default=None),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    source_type = source_type.lower().strip()
    source_name = "text-input"
    raw_text = ""

    if source_type == "text":
        if not text or not text.strip():
            raise HTTPException(status_code=400, detail="Text input is empty.")
        raw_text = text.strip()
    elif source_type == "url":
        if not url:
            raise HTTPException(status_code=400, detail="URL is required.")
        try:
            raw_text = extract_text_from_url(url)
            source_name = url
        except Exception as exc:
            raise HTTPException(status_code=400, detail=f"Could not fetch URL: {exc}") from exc
    elif source_type == "file":
        if not file:
            raise HTTPException(status_code=400, detail="File is required.")
        data = await file.read()
        try:
            raw_text, parsed_type = parse_uploaded_file(file.filename or "upload.txt", data)
            source_name = file.filename or f"upload.{parsed_type}"
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid source_type.")

    if not raw_text:
        raise HTTPException(status_code=400, detail="No extractable text found.")

    source = SourceDocument(user_id=user.id, source_type=source_type, name=source_name, raw_text=raw_text)
    db.add(source)
    db.commit()
    db.refresh(source)

    chunk_count = rag_engine.index_document(user.id, source.id, source.name, raw_text)
    return {"source_id": source.id, "chunks_indexed": chunk_count}
