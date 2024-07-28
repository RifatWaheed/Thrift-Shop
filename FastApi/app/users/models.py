from app.database import Base
from sqlalchemy import Column, Integer, String, BigInteger, Boolean, DateTime
from sqlalchemy.sql import func


class users(Base):
    __tablename__: "users"
    pkID = Column(Integer, primary_key=True, index=True)
    userName = Column(String, unique=True, nullable=False)
    password = Column (String, nullable=False)
    email = Column (String, unique=True, nullable=False)
    createdDate = Column(DateTime, default=func.now(), nullable=False)
    modifiedDate = Column(DateTime, default=func.now(), nullable=False)
    createdByID = Column(Integer, nullable=False)
    createdByName = Column(String, nullable=True)
    modifiedByID = Column(Integer, nullable=False)
    modifiedByName = Column(String, nullable=True)

