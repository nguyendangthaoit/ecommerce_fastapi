from sqlalchemy import Column, Integer, String, Float, DateTime
from app.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    brand = Column(String)
    company = Column(String)
    quantity = Column(Integer)
    expired = Column(DateTime)
