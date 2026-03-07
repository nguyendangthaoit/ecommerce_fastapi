
from app.repositories.product_repository import ProductRepository

class ProductService:

    @staticmethod
    def get_products():
        return ProductRepository.get_all()

    @staticmethod
    def create_product(product):
        return ProductRepository.create(product)
