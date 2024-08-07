from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from . import models, schemas
from app.products import cruds

router = APIRouter(prefix="/products", tags=["products"])

        
@router.get('/getAllProducts', response_model= List[schemas.Product])
def getAllProducts(db: Session = Depends(get_db)):
    resp = db.query(models.Product).all()
    return resp

@router.post('/saveProduct', response_model=schemas.ProductResponseForSave)
def saveProduct(req: schemas.Product , db:Session = Depends(get_db)):
    resp = cruds.saveProduct(db,req)
    if not resp:
        raise HTTPException(status_code=404, detail=f"Product with {req.pkID} not found")
    return resp
