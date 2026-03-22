from app.models.product_model import Product
from sqlalchemy.orm import Session


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db  # Giữ session ở cấp độ instance

    def get_all(self):
        return self.db.query(Product).all()

    def create(self, product_data):
        product = Product(**product_data.dict())
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def get_by_id(self, pro_id):
        return self.db.query(Product).filter(Product.id == pro_id).first()
