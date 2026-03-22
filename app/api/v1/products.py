# app/routers/product_router.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.product_repository import ProductRepository
from app.services.product_service import ProductService
from app.schemas.product_schema import ProductCreate

router = APIRouter()


def get_product_service(db: Session = Depends(get_db)):
    repo = ProductRepository(db)
    return ProductService(repo)


@router.post("/")
def create_product(
    product: ProductCreate, service: ProductService = Depends(get_product_service)
):
    return service.create_product(product)


@router.get("/")
def get_products(
    page: int = 1,
    limit: int = 10,
    service: ProductService = Depends(get_product_service),
):
    return service.get_products()


@router.get("/{pro_id}")
def get_product_by_id(
    pro_id: int, service: ProductService = Depends(get_product_service)
):
    return service.get_product_by_id(pro_id)
