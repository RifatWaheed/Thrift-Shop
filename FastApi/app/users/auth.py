from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from typing import List
from .. database import get_db
from . import models
from . import schemas
from . import cruds
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

router = APIRouter(prefix='/auth', tags=['auth'],)

SECRET_KEY = "lotabhara.com"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


class TokenModel (BaseModel):
    accessToken: str
    tokenType: str

@router.post('/createUser', status_code=status.HTTP_201_CREATED)
def createUser(req: schemas.User, db: Session = Depends(get_db)):
    resp = cruds.saveUserForAuth(req, db)

