
from app.models.user_model import User
from app.core.database import SessionLocal

class UserRepository:

    @staticmethod
    def get_all():
        db = SessionLocal()
        return db.query(User).all()

    @staticmethod
    def create(user_data):
        db = SessionLocal()
        user = User(**user_data.dict())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
