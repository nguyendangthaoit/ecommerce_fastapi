from app.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo  # Service dùng Repo để làm việc với DB

    def get_products(self):
        return self.repo.get_all()

    def create_product(self, product):
        return self.repo.create(product)

    def get_product_by_id(self, pro_id):
        return self.repo.get_by_id(pro_id)
