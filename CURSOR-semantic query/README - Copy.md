# Semantic Query Engine (RAG)

Production-ready full-stack app for document-grounded question answering using FastAPI, React, SQLite, ChromaDB, and Gemini.

## Project Structure

- `backend/` FastAPI API, auth, RAG pipeline, tests
- `frontend/` React + Vite UI

## Backend Setup

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload
```

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

- `POST /signup`
- `POST /login`
- `POST /upload`
- `POST /query`
- `GET /sources`
- `POST /tts`

## Testing

```bash
cd backend
pytest -q
```
