from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.application.services.todo_service import ToDoService
from app.core.security import get_current_user
from app.infrastructure.db.session import get_db
from app.infrastructure.repositories.sqlalchemy_todo_repository import (
    SQLAlchemyToDoRepository,
)

router = APIRouter()


class CreateToDoRequest(BaseModel):
    title: str
    user_id: UUID


class ToDoResponse(BaseModel):
    id: UUID
    title: str
    user_id: UUID
    completed: bool
    created_at: str


@router.get("/todos", response_model=List[ToDoResponse])
def list_todos(
    q: str = "",
    limit: int = 10,
    offset: int = 0,
    user_id=Depends(get_current_user),
    db=Depends(get_db),
):
    service = ToDoService(SQLAlchemyToDoRepository(db))
    todos = service.search_todos(user_id, q=q, limit=limit, offset=offset)
    return [t.__dict__ for t in todos]


@router.get("/todos", response_model=List[ToDoResponse])
def list_todos(user_id=Depends(get_current_user), db=Depends(get_db)):
    service = ToDoService(SQLAlchemyToDoRepository(db))
    todos = service.list_by_user(user_id)
    return [t.__dict__ for t in todos]


@router.get("/todos/stats")
def todo_stats(user_id=Depends(get_current_user), db=Depends(get_db)):
    service = ToDoService(SQLAlchemyToDoRepository(db))
    return service.get_stats(user_id)
