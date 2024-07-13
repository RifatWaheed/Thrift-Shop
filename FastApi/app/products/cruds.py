from sqlalchemy.orm import Session
from app.products import models, schemas

def createProduct(db : Session,product: schemas.Product):
    productDict = product.model_dump() #it will convert the pydantic model into a dictionary type
    db_product = models.Product(**productDict)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return schemas.ProductResponseForSave(message="A new product has been created successfully", product=db_product)

def updateProduct(db : Session, product: schemas.Product):
    pkID = product.pkID
    
    db_product = db.query(models.Product).filter(models.Product.pkID == pkID).first()
    if db_product:
        for key, value in product.model_dump(exclude_unset=True).items(): #
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
        return schemas.ProductResponseForSave(message="Product has been updated successfully", product=db_product)
    else:
        return None
    

def saveProduct(db: Session, product: schemas.Product):
    responseObj = None
    if(product.pkID>0):
        responseObj = createProduct(db,product)
    else:
        responseObj = updateProduct(db,product)
    return responseObj
