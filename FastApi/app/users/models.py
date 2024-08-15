from app.database import Base
from sqlalchemy import Column, Integer, String, BigInteger, Boolean, DateTime
from sqlalchemy.sql import func


class Users(Base):
    __tablename__ = 'users'
    
    pkID = Column(Integer, primary_key=True, index=True)
    userName = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=False)
    role = Column(Integer, nullable=True)
    email = Column(String, unique=True, nullable=False)
    createdDate = Column(DateTime, default=func.now(), nullable=False)
    lastPassswords = Column(String, nullable=True)
    lastPassswordChangeDate = Column(DateTime, nullable=True)
    passwordExpireDate = Column(DateTime, nullable=True)
    ipAddress = Column(String, nullable=True)
    modifiedDate = Column(DateTime, default=func.now(), nullable=False)
    createdByID = Column(Integer, nullable=False)
    createdByName = Column(String, nullable=True)
    modifiedByID = Column(Integer, nullable=False)
    modifiedByName = Column(String, nullable=True)
