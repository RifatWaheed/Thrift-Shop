from pydantic import BaseModel
from typing import Optional

class ContactInfoBase(BaseModel):
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None

class ContactInfoCreate(ContactInfoBase):
    pkID: int  # Assuming this field is required for the search operation

class ContactInfo(ContactInfoBase):
    pkID: int


    class Config:
        from_attributes = True
        
class GetContactInfoByIDRequestModel(BaseModel):
    pkID:int
