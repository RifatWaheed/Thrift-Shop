from pydantic import BaseModel as PydanticBaseModel, EmailStr
from datetime import datetime
from app.products.schemas import BaseClass, AuditTrailModel
from typing import Optional

class UsersBaseModel(PydanticBaseModel):
    userName: str
    password: str
    email: EmailStr
    lastPassswords: str
    lastPassswordChangeDate: datetime
    passwordExpireDate: datetime
    ipAddress: str

class User(BaseClass, AuditTrailModel, UsersBaseModel):

    class Config:
        from_attributes = True


class UserResponse(PydanticBaseModel):
    pkID: int
    userName: str
    email: EmailStr
    createdDate: Optional[datetime] = None
    modifiedDate: Optional[datetime] = None
    createdByID: Optional[int] = None
    modifiedByID: Optional[int] = None
    createdByName: Optional[str] = None
    modifiedByName: Optional[str] = None

    
    class Config:
        from_attributes = True
