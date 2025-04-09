from sqlalchemy.orm import Session

from app.domain.models.user import User
from app.infrastructure.db.models import UserModel


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_email(self, email: str) -> UserModel | None:
        return self.db.query(UserModel).filter_by(email=email).first()

    def save(self, user: User):
        model = UserModel(**user.__dict__)
        self.db.add(model)
        self.db.commit()

    def list_by_user(self, user_id: str):
        return self.db.query(UserModel).filter_by(user_id=user_id).all()
