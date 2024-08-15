from sqlalchemy.orm import Session
from . import models, schemas,auth
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

def createUser(req: schemas.User, db: Session):
    pass
    # userDict = req.model_dump()
    # db_user = models.Users(**userDict)
    


def updateUser(req: schemas.User, db: Session):
    pass


def saveUser(req: schemas.User, db: Session):
    if req.pkID > 0:
        responseObject = updateUser(req, db)
    else:
        responseObject = createUser(req, db)
    return responseObject


def saveUserForAuth(req: schemas.User, db: Session):
    reqForAuth = req.model_dump()
    authUser = models.Users(**reqForAuth)
    authUser.password = auth.pwd_context.hash(authUser.password)

    db.add(authUser)
    db.commit()
    db.refresh(authUser)

