from pydantic import BaseModel
from typing import Optional

class ContactInfoBase(BaseModel):
    pkID: int
    name: str

class ContactInfoCreate(ContactInfoBase):
    pkID: int  # Assuming this field is required for the search operation

class ContactInfo(ContactInfoBase):
    phone: Optional[str] = None
    email: Optional[str] = None

    class Config:
        from_attributes = True
        
class GetContactInfoByIDRequestModel(BaseModel):
    pkID:int
