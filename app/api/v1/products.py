from fastapi import APIRouter
from app.schemas.product_schema import ProductCreate
from app.services.product_service import ProductService

router = APIRouter()


@router.post("/")
def create_product(product: ProductCreate):
    return ProductService.create_product(product)


@router.get("/")
def get_products(page: int = 1, limit: int = 10):
    return ProductService.get_products()


@router.get("/{product_id}")
def get_product_by_id(product_id: int):
    return {"product_id": product_id}
