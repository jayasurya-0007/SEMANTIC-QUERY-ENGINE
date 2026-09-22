import os
import uuid

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from gtts import gTTS
from pydantic import BaseModel, Field

from auth.security import get_current_user
from database.models import User

router = APIRouter(tags=["tts"])


class TTSRequest(BaseModel):
    text: str = Field(min_length=1, max_length=4000)
    lang: str = Field(default="en")


@router.post("/tts")
def text_to_speech(payload: TTSRequest, user: User = Depends(get_current_user)):
    del user
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Text is empty.")

    out_dir = "backend/data/audio"
    os.makedirs(out_dir, exist_ok=True)
    file_name = f"{uuid.uuid4()}.mp3"
    file_path = os.path.join(out_dir, file_name)

    tts = gTTS(text=payload.text.strip(), lang=payload.lang)
    tts.save(file_path)
    return FileResponse(file_path, media_type="audio/mpeg", filename=file_name)
