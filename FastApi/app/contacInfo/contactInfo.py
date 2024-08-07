from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from . import models, schemas

router = APIRouter(prefix="/contactInfo", tags=["contactInfo"])


@router.get("/getAllContactInfos", response_model=List[schemas.ContactInfo])
def getAllContactInfos(db: Session = Depends(get_db)):
    resp = db.query(models.ContactInfo).all()
    return resp

@router.post("/getContactInfoByID", response_model=schemas.ContactInfo)
def getContactInfoByID(req: schemas.GetContactInfoByIDRequestModel, db: Session = Depends(get_db)):
    resp = db.query(models.ContactInfo).filter(models.ContactInfo.pkID == req.pkID).first()
    if not resp:
        raise HTTPException(status_code=404, detail=f"ContactInfo with {req.pkID} not found")
    return resp
