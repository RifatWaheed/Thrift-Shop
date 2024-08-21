from pydantic import BaseModel as PydanticBaseModel, EmailStr
from datetime import datetime
from typing import Optional


class BaseClass(PydanticBaseModel):
    pkID: int


class AuditTrailModel(PydanticBaseModel):
    createdDate: datetime
    modifiedDate: datetime
    createdByID: int
    modifiedByID: int
    createdByName: str | None = None
    modifiedByName: str | None = None


class UsersBaseModel(PydanticBaseModel):
    userName: str
    password: str
    email: EmailStr
    role: Optional[int]
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
    role: Optional[int]
    createdDate: Optional[datetime] = None
    modifiedDate: Optional[datetime] = None
    createdByID: Optional[int] = None
    modifiedByID: Optional[int] = None
    createdByName: Optional[str] = None
    modifiedByName: Optional[str] = None

    class Config:
        from_attributes = True

