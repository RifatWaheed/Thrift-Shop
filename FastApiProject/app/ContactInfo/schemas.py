from pydantic import BaseModel
from typing import Optional

class ContactInfo(BaseModel):
    pk_id: int
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None

    class Config:
        from_attributes = True