from sqlalchemy import Column,Integer
from .database import Base

class Products(Base):
    __tablename__ = "products"

    pk_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    