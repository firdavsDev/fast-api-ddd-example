from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.application.services.auth_service import AuthService
from app.infrastructure.db.session import get_db
from app.infrastructure.repositories.user_repository import UserRepository

router = APIRouter()


class RegisterRequest(BaseModel):
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/register")
def register(body: RegisterRequest, db=Depends(get_db)):
    service = AuthService(UserRepository(db))
    return service.register(body.email, body.password).__dict__


@router.post("/login")
def login(body: LoginRequest, db=Depends(get_db)):
    service = AuthService(UserRepository(db))
    token = service.login(body.email, body.password)
    if not token:
        raise HTTPException(401, "Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}
