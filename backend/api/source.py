from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.source import Source, Summary
from models.database import get_db

router = APIRouter()

@router.get("/")
def list_sources(db: Session = Depends(get_db)):
    return db.query(Source).all()

@router.post("/")
def add_source(source: dict, db: Session = Depends(get_db)):
    new_source = Source(**source)
    db.add(new_source)
    db.commit()
    db.refresh(new_source)
    return new_source

