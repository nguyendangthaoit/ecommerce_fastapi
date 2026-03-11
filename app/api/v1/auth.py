from fastapi import APIRouter
from app.schemas.user_schema import UserCreate, UserLogin
from app.services.user_service import UserService
from app.services.auth_service import AuthService

router = APIRouter()


@router.post("/register")
def register(user: UserCreate):
    return UserService.register(user)


@router.post("/login")
def login(user: UserLogin):
    return AuthService.login(user)
