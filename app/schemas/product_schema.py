from pydantic import BaseModel
from datetime import datetime


class ProductCreate(BaseModel):
    name: str
    price: float
    brand: str
    company: str
    quantity: int
    expired: datetime
