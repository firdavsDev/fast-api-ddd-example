from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from app.domain.models.todo import ToDo


class ToDoRepository(ABC):
    @abstractmethod
    def save(self, todo: ToDo):
        pass

    @abstractmethod
    def get_all(self, user_id: UUID) -> List[ToDo]:
        pass
