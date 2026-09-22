import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.db import Base, engine
from routes.auth import router as auth_router
from routes.query import router as query_router
from routes.sources import router as sources_router
from routes.tts import router as tts_router
from routes.upload import router as upload_router

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Semantic Query Engine", version="1.0.0")

allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://localhost:3000")
origins = [item.strip() for item in allowed_origins.split(",") if item.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(upload_router)
app.include_router(query_router)
app.include_router(sources_router)
app.include_router(tts_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
