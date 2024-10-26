from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from app.jwt.auth import oauth2_scheme
from app.config import SECRET_KEY, ALGORITHM
from app.jwt.models import User, fake_users_db
from app.jwt.auth import get_user

# Função para obter o usuário atual usando o JWT
async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username)
    if user is None:
        raise credentials_exception
    return user
