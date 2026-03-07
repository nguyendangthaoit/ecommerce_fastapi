
from app.models.product_model import Product
from app.core.database import SessionLocal

class ProductRepository:

    @staticmethod
    def get_all():
        db = SessionLocal()
        return db.query(Product).all()

    @staticmethod
    def create(product_data):
        db = SessionLocal()
        product = Product(**product_data.dict())
        db.add(product)
        db.commit()
        db.refresh(product)
        return product
