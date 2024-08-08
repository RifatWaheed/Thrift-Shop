from sqlalchemy.orm import Session
from app.users import models, schemas


def createUser(req: schemas.User, db: Session):
    userDict = req.model_dump()
    db_user = models.users(**userDict)
    


def updateUser(req: schemas.User, db: Session):
    pass


def saveUser(req: schemas.User, db: Session):
    if req.pkID > 0:
        responseObject = updateUser(req, db)
    else:
        responseObject = createUser(req, db)
    return responseObject
