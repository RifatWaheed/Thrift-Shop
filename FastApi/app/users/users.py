from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. database import get_db
from . import models
from . import schemas
from . import cruds
from passlib.context import CryptContext

router = APIRouter(prefix="/users", tags=["users"])


@router.get('/getAllUsers' , response_model= List[schemas.UserResponse])
def getAllUsers(db: Session = Depends(get_db) ):
    dbResp = db.query(models.Users).all()
    if not dbResp:
        raise HTTPException(status_code=404, detail=f"No data found")
    resp = [schemas.UserResponse.model_validate(i) for i in dbResp]
    return resp


@router.post('/createUser', response_model= schemas.UserResponse)
def createUser(req : schemas.User , db: Session = Depends(get_db)):
    resp = cruds.saveUser(req,db)
    
