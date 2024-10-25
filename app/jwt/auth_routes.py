from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.jwt.auth import authenticate_user, create_access_token
from app.jwt.config import ACCESS_TOKEN_EXPIRE_MINUTES

# Criar um roteador específico para rotas de autenticação
router = APIRouter()

# Rota de login para gerar o token
@router.post("/token", summary="Obter Token JWT", description="Este endpoint retorna o token para acesso às APIs")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401, detail="Usuário ou senha incorretos"
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
