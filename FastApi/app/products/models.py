from app.database import Base
from sqlalchemy import Column, Integer, String, BigInteger, Boolean, DateTime
from sqlalchemy.sql import func


class Product(Base):
    __tablename__ = "products"

    pkID = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    skuCode = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    stockQty = Column(BigInteger, nullable=False, default=0)
    categoryID = Column(Integer, nullable=False)
    unitID = Column(Integer, nullable=True)
    unitName = Column(String, nullable=True)
    isCombinationProduct = Column(Boolean, nullable=True)
    combinationProductID = Column(BigInteger, nullable=True)
    description = Column(String, nullable=True)
    itemSerialNo = Column(String, nullable=True)
    keywords = Column(String, nullable=True)
    imageID = Column(BigInteger, nullable=True)
    createdDate = Column(DateTime, default=func.now(), nullable=False)
    modifiedDate = Column(DateTime, default=func.now(), nullable=False)
    createdByID = Column(Integer, nullable=False)
    createdByName = Column(String, nullable=True)
    modifiedByID = Column(Integer, nullable=False)
    modifiedByName = Column(String, nullable=True)
    isDiscountApplicable = Column(Boolean, nullable=True)
