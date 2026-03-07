
from fastapi import APIRouter
from app.api.v1 import products, users, auth

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(products.router, prefix="/products", tags=["Products"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
