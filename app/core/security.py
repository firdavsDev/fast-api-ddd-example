from datetime import datetime, timedelta
from uuid import UUID

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def hash_password(pw: str):
    return pwd_ctx.hash(pw)


def verify_password(raw, hashed):
    return pwd_ctx.verify(raw, hashed)


def create_token(user_id: UUID) -> str:
    exp = datetime.utcnow() + timedelta(hours=1)
    return jwt.encode(
        {"sub": str(user_id), "exp": exp}, settings.JWT_SECRET, algorithm="HS256"
    )


def get_current_user(token: str = Depends(oauth2_scheme)) -> UUID:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        return UUID(payload["sub"])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
