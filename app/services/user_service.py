from app.repositories.user_repository import UserRepository
from app.utils.hashing import hash_password


class UserService:

    @staticmethod
    def register(user):
        hashed = hash_password(user.password)

        user_data = {"email": user.email, "hashed_password": hashed}

        return UserRepository.create(user_data)
