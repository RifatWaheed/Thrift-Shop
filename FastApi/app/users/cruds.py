from sqlalchemy.orm import Session
from . import models, schemas,auth
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


def createUser(req: schemas.User, db: Session):
    userDict = req.model_dump()
    pkID = userDict.get('pkID')
    userDict['password'] = auth.pwd_context.hash(userDict['password'])

    if not pkID or pkID == 0:  # Checks for None or 0
        userDict.pop('pkID', None)

    db_user = models.Users(**userDict)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    


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
    pkID = reqForAuth.get('pkID')

    if not pkID or pkID == 0:  # Checks for None or 0
        reqForAuth.pop('pkID', None)

    authUser = models.Users(**reqForAuth)
    authUser.password = auth.pwd_context.hash(authUser.password)
    db.add(authUser)
    db.commit()
    db.refresh(authUser)
    return authUser
