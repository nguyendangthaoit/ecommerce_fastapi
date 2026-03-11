from app.models.user_model import User
from app.core.database import SessionLocal


class UserRepository:

    @staticmethod
    def get_by_email(email: str):
        db = SessionLocal()
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def create(user_data):
        db = SessionLocal()
        user = User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
