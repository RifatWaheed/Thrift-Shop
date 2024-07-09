from sqlalchemy import Column, Integer, String
from app.database import Base

class ContactInfo(Base):
    __tablename__ = 'contactInfo'

    pkID = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
