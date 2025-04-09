from uuid import UUID

from app.core.security import create_token, hash_password, verify_password
from app.domain.models.user import User
from app.infrastructure.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, email: str, password: str):
        user = User(email=email, hashed_password=hash_password(password))
        self.repo.save(user)
        return user

    def login(self, email: str, password: str):
        user_model = self.repo.find_by_email(email)
        if not user_model or not verify_password(password, user_model.hashed_password):
            return None
        return create_token(user_model.id)

    def get_stats(self, user_id: UUID):
        todos = self.repo.list_by_user(user_id)
        total = len(todos)
        completed = sum(t.done for t in todos)
        pending = total - completed
        return {"total": total, "completed": completed, "pending": pending}
