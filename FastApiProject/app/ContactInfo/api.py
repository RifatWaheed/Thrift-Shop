from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from . import models, schemas

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/contactinfo", response_model=List[schemas.ContactInfo])
def get_all_contact_info(db: Session = Depends(get_db)):
    contact_info = db.query(models.ContactInfo).all()
    return contact_info