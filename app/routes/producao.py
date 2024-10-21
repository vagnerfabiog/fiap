from fastapi import APIRouter
from app.services.dados_embrapa import obter_dados

router = APIRouter()

@router.get('/producao')
async def obter_producao():
    data = obter_dados('producao')
    return data
