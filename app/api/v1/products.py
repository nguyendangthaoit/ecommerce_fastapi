
from fastapi import APIRouter
from app.schemas.product_schema import ProductCreate
from app.services.product_service import ProductService

router = APIRouter()

@router.get("/")
def get_products():
    return ProductService.get_products()

@router.post("/")
def create_product(product: ProductCreate):
    return ProductService.create_product(product)
