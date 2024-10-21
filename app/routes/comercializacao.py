from fastapi import APIRouter
from app.services.dados_embrapa import obter_dados

router = APIRouter()

@router.get('/comercializacao')
async def obter_comercializacao():
    """
    Busca dados do país na tabela de comercialização da Embrapa e retorna como JSON.
    """
    data = obter_dados('comercializacao')
    return data
