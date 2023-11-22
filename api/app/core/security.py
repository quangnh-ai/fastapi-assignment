import jwt
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta

from core.config import (
    AUTHENTICATE_ALGORITHM,
    AUTHENTICATE_SECRET_KEY,
    AUTHENTICATE_TOKEN_URL
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=AUTHENTICATE_TOKEN_URL)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, AUTHENTICATE_SECRET_KEY, algorithm=AUTHENTICATE_ALGORITHM)
    return encoded_jwt
