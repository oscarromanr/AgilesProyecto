import os
from fastapi import Depends, HTTPException, status
from .app_exceptions import AppException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from dotenv import load_dotenv
from datetime import datetime, timedelta
from typing import Any, Dict, Optional

load_dotenv()

ALGORITHM = os.getenv("ENCRYPTION_ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

def decode_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return AppException.BadRequest(detail="Usuario o contraseña inválidos")
    
def get_current_user(token: str = Depends(oauth2_scheme)):
    username = decode_token(token)
    if username is None:
        raise AppException.Unauthorized(detail="Usuario o contraseña inválidos")
    return username

def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt