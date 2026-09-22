from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.security import get_current_user
from database.db import get_db
from database.models import SourceDocument, User

router = APIRouter(tags=["sources"])


@router.get("/sources")
def list_sources(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    sources = db.query(SourceDocument).filter(SourceDocument.user_id == user.id).all()
    return [
        {
            "id": source.id,
            "name": source.name,
            "source_type": source.source_type,
            "created_at": source.created_at.isoformat(),
        }
        for source in sources
    ]
