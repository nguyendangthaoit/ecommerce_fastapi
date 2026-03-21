from fastapi import APIRouter
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse
from app.services.user_service import UserService
from app.services.auth_service import AuthService

from fastapi import APIRouter, BackgroundTasks
from app.services.email_service import EmailService

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate):
    return UserService.register(user)


@router.post("/login")
def login(user: UserLogin):
    return AuthService.login(user)


@router.post("/test-email")
def test_email(background_tasks: BackgroundTasks):
    background_tasks.add_task(
        EmailService.send_otp_email, "emailrunapp <emailrunapp@gmail.com>", "123456"  # type: ignore
    )

    return {"message": "Email sent"}
