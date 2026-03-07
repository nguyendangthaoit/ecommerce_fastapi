
from app.repositories.user_repository import UserRepository

class UserService:

    @staticmethod
    def get_users():
        return UserRepository.get_all()

    @staticmethod
    def create_user(user):
        return UserRepository.create(user)
