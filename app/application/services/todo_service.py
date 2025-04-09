from typing import List
from uuid import UUID

from app.domain.models.todo import ToDo
from app.domain.repositories.todo_repository import ToDoRepository


class ToDoService:
    def __init__(self, repository: ToDoRepository):
        self.repo = repository

    def create(self, title: str, user_id: UUID) -> ToDo:
        todo = ToDo(title, user_id)
        self.repo.save(todo)
        return todo

    def list_by_user(self, user_id: UUID) -> List[ToDo]:
        return self.repo.get_all(user_id)

    def search_todos(
        self, user_id: UUID, q: str = "", limit: int = 10, offset: int = 0
    ):
        return self.repo.search(user_id, q, limit, offset)
