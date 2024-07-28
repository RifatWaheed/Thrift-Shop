from pydantic import BaseModel as PydanticBaseModel
from datetime import datetime

# Define the BaseModel with common fields
class BaseClass(PydanticBaseModel):
    pkID: int

# Define the AuditTrailModel with audit fields
class AuditTrailModel(PydanticBaseModel):
    createdDate: datetime
    modifiedDate: datetime
    createdByID: int
    modifiedByID: int
    createdByName: str | None = None
    modifiedByName: str | None = None
    
class ProductBaseModel(PydanticBaseModel):
    name: str
    price: int
    stockQty: int
    categoryID: int
    unitID: int | None = None
    unitName: str | None = None
    isCombinationProduct: bool | None = None
    combinationProductID: int | None = None
    description: str | None = None
    itemSerialNo: str | None = None
    keywords: str | None = None
    imageID: int | None = None
    isDiscountApplicable: bool | None = None
    
class Product(BaseClass, AuditTrailModel, ProductBaseModel):
    
    class Config:
        from_attributes = True
        
class ProductResponseForSave(PydanticBaseModel):
    message: str
    product: Product