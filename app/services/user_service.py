from app.repositories.user_repository import UserRepository
from app.utils.hashing import hash_password
from app.tasks.email_task import send_user_email


class UserService:

    @staticmethod
    def register(user):
        user_data = user.model_dump()  # convert Pydantic -> dict
        user_data["hashed_password"] = hash_password(user.password)
        user_data.pop("password")  # remove plain password
        created_user = UserRepository.create(user_data)
        send_user_email.delay(user.email, created_user.id)

        return created_user
