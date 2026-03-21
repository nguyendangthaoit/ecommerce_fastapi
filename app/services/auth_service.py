from app.utils.hashing import verify_password
from app.core.security import create_access_token
from app.repositories.user_repository import UserRepository
from app.core.logger import logger


class AuthService:

    @staticmethod
    def login(user_data):
        user = UserRepository.get_by_email(user_data.email)

        if not user:
            return None

        if not verify_password(user_data.password, user.hashed_password):
            return None

        token = create_access_token({"user_id": user.id})
        logger.info("loging successfully")

        return {"access_token": token}
