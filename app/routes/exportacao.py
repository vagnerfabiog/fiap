from fastapi import APIRouter
from app.services.dados_embrapa import obter_dados2

router = APIRouter()

@router.get('/exportacao/vinhos')
async def obter_exportacao_vinho():
    """
    Busca dados do país na tabela de exportacão de vinhos da Embrapa e retorna como JSON.
    """
    data = obter_dados2('exportacao_vinhos')
    return data

@router.get('/exportacao/espumantes')
async def obter_exportacao_espumante():
    """
    Busca dados do país na tabela de exportacão de espumantes da Embrapa e retorna como JSON.
    """
    data = obter_dados2('exportacao_espumantes')
    return data

@router.get('/exportacao/uvas_frescas')
async def obter_exportacao_uvas_frescas():
    """
    Busca dados do país na tabela de exportacão de uvas frescas da Embrapa e retorna como JSON.
    """
    data = obter_dados2('exportacao_uvas_frescas')
    return data

@router.get('/exportacao/suco_uva')
async def obter_exportacao_suco_uva():
    """
    Busca dados do país na tabela de exportacão de suco de uva da Embrapa e retorna como JSON.
    """
    data = obter_dados2('exportacao_suco_uva')
    return data

