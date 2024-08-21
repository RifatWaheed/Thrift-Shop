import datetime

from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from typing import List
from .. database import get_db
from . import models
from . import schemas
from . import cruds
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
from datetime import datetime, timedelta
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

router = APIRouter(prefix='/auth', tags=['auth'],)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


class Token(BaseModel):
    accessToken: str
    tokenType: str


class TokenModel (BaseModel):
    accessToken: str
    tokenType: str


@router.post('/createUser', status_code=status.HTTP_201_CREATED)
def createUser(req: schemas.User, db: Session = Depends(get_db)):
    resp = cruds.saveUserForAuth(req, db)


@router.post('/token', response_model=Token)
def loginForAccessToken(req: schemas.User, db: Session = Depends(get_db)):
    user = authenticateUser(req.email, req.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
    token = createAccessToken(req.email, req.pkID, timedelta=timedelta(minutes=20))
    return {'accessToken': token, 'token': 'bearer'}


def createAccessToken(email: EmailStr, pkID: int, timedelta: timedelta):
    encode = {'sub': email, 'id': pkID}
    expires = datetime.now() + timedelta
    encode.update({'exp':expires})
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


def authenticateUser(email, password, db: Session):
    user = db.query(models.Users).filter(str(models.Users.email) == email).first()
    if not user:
        return False
    if not pwd_context.verify(password, user.password):
        return False
    return user
