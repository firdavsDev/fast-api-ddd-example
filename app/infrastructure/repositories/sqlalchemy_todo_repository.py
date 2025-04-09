from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from app.domain.models.todo import ToDo
from app.domain.repositories.todo_repository import ToDoRepository
from app.infrastructure.db.models import ToDoModel


class SQLAlchemyToDoRepository(ToDoRepository):
    def __init__(self, db: Session):
        self.db = db

    def save(self, todo: ToDo):
        model = ToDoModel(**todo.__dict__)
        self.db.add(model)
        self.db.commit()

    def get_all(self, user_id: UUID):
        rows = self.db.query(ToDoModel).filter_by(user_id=user_id).all()
        return [ToDo(**row.__dict__) for row in rows]

    def search(
        self, user_id: UUID, q: str = "", limit: int = 10, offset: int = 0
    ) -> List[ToDoModel]:
        query = self.db.query(ToDoModel).filter(ToDoModel.user_id == user_id)
        if q:
            query = query.filter(ToDoModel.title.ilike(f"%{q}%"))
        return query.offset(offset).limit(limit).all()
