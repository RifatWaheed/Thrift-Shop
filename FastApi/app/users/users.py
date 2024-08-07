from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
from app.database import get_db
from . import models, schemas
from app.users import cruds


router = APIRouter(prefix="/users", tags=["users"])


@router.get('/getAllUsers' , response_model= List[schemas.UserResponse])
def getAllUsers(db: Session = Depends(get_db) ):
    dbResp = db.query(models.users).all()
    if not dbResp:
        raise HTTPException(status_code=404, detail=f"No data found")
    
    resp = [schemas.UserResponse.model_validate(i) for i in dbResp]
    return resp
