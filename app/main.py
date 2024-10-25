from fastapi import FastAPI, Depends, HTTPException
from app.routes.comercializacao import router as comercializacao_router
from app.routes.importacao import router as importacao_router
from app.routes.exportacao import router as exportacao_router
from app.routes.producao import router as producao_router
from app.routes.home import router as home_router
from app.routes.processamento import router as processamento_router
from app.jwt.auth import authenticate_user, create_access_token
from app.jwt.dependencies import get_current_user
from app.jwt.config import ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

app = FastAPI()

# Descrição completa que será exibida no Swagger UI
description = """
API de Consultas - Embrapa 🏞️

Esta API permite consultar dados relevantes sobre a produção, processamento, comercialização, importação e exportação relacionados ao setor vitivinícola. 


- **Usuário de teste:** `user1`
- **Senha de teste:** `senha123`

Sinta-se à vontade para explorar a documentação e testar os endpoints.
"""

# Criação da aplicação FastAPI com configurações personalizadas
app = FastAPI(
    title="API de Consultas - Embrapa",
    description=description,
    version="1.0.0",
    contact={
        "name": "Diego / Vagner / Fabio",
        "email": "ra@fiap.com.br",
    },
  
)


# Rota de login para gerar o token
@app.post("/token", summary="Obter Token JWT", description="Este endpoint retorna o token para acesso as APIs")
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

# Incluindo as rotas com as dependências de autenticação nas rotas protegidas
app.include_router(comercializacao_router, dependencies=[Depends(get_current_user)])
app.include_router(importacao_router, dependencies=[Depends(get_current_user)])
app.include_router(exportacao_router, dependencies=[Depends(get_current_user)])
app.include_router(home_router)
app.include_router(producao_router, dependencies=[Depends(get_current_user)])
app.include_router(processamento_router, dependencies=[Depends(get_current_user)])
