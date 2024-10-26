from fastapi import FastAPI, Depends, HTTPException
from app.routes.comercializacao import router as comercializacao_router
from app.routes.importacao import router as importacao_router
from app.routes.exportacao import router as exportacao_router
from app.routes.producao import router as producao_router
from app.routes.home import router as home_router
from app.routes.processamento import router as processamento_router
from app.jwt.auth import authenticate_user, create_access_token
from app.jwt.dependencies import get_current_user
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.jwt.auth_routes import router as auth_router  
from app.config import API_DESCRIPTION, API_TITLE, API_VERSION, CONTACT_INFO


app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION,
    contact=CONTACT_INFO,
)

# Registro das rotas de autenticação
app.include_router(auth_router)
 # Incluindo as rotas com as dependências de autenticação nas rotas protegidas
app.include_router(comercializacao_router, dependencies=[Depends(get_current_user)])
app.include_router(importacao_router, dependencies=[Depends(get_current_user)])
app.include_router(exportacao_router, dependencies=[Depends(get_current_user)])
app.include_router(home_router)
app.include_router(producao_router, dependencies=[Depends(get_current_user)])
app.include_router(processamento_router, dependencies=[Depends(get_current_user)])
