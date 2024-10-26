from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from app.jwt.models import User, fake_users_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Função para criar token JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Função para verificar a senha (sem hash)
def verify_password(plain_password, stored_password):
    return plain_password == stored_password

# Função para obter usuário do banco de dados
def get_user(db, username: str) -> Optional[User]:
    user_dict = db.get(username)
    if user_dict:
        return User(**user_dict)  # Retorna uma instância de User
    return None

# Função para autenticar o usuário
def authenticate_user(username: str, password: str) -> Optional[User]:
    user = get_user(fake_users_db, username)
    if not user or not verify_password(password, user.password):
        return None
    return user
