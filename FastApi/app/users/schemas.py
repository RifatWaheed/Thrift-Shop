from pydantic import BaseModel as PydanticBaseModel, EmailStr
from datetime import datetime
from app.products.schemas import BaseClass, AuditTrailModel

class UsersBaseModel(PydanticBaseModel):
    userName : str
    password : str
    email : EmailStr

class User(BaseClass,AuditTrailModel,UsersBaseModel):
    
    class Config:
        from_attributes = True

class UserResponse (PydanticBaseModel):
    pkID: int
    userName : str
    email : EmailStr
    createdDate: datetime
    modifiedDate: datetime
    createdByID: int
    modifiedByID: int
    createdByName: str | None = None
    modifiedByName: str | None = None