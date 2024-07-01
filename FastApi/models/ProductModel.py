from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Product(BaseModel):
    pkID: int
    name: str
    price: float
    stockQty: int
    categoryID: int
    unitID: int
    unitName: str
    isCombinationProduct: bool
    combinationProductID: int
    decription: str
    keywords: str
    imageID: int
    createdDate: datetime
    createdByID: int
    createdByName: Optional[str]
    modifiedDate: datetime
    modifiedByID: int
    modifiedByName: Optional[str]