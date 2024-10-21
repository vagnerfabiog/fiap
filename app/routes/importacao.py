from fastapi import APIRouter
from app.services.dados_embrapa import obter_dados2

router = APIRouter()

@router.get('/importacao/vinhos')
async def obter_importacao_vinho():
    """
    Busca dados do país na tabela de importacão de vinhos da Embrapa e retorna como JSON.
    """
    data = obter_dados2('importacao_vinhos')
    return data

@router.get('/importacao/espumantes')
async def obter_importacao_espumante():
    """
    Busca dados do país na tabela de importacão de espumantes da Embrapa e retorna como JSON.
    """
    data = obter_dados2('importacao_espumantes')
    return data

@router.get('/importacao/uvas_frescas')
async def obter_importacao_uvas_frescas():
    """
    Busca dados do país na tabela de importacão de uvas frescas da Embrapa e retorna como JSON.
    """
    data = obter_dados2('importacao_uvas_frescas')
    return data

@router.get('/importacao/uvas_passas')
async def obter_importacao_uvas_passas():
    """
    Busca dados do país na tabela de importacão de uvas passas da Embrapa e retorna como JSON.
    """
    data = obter_dados2('importacao_uvas_passas')
    return data

@router.get('/importacao/suco_uva')
async def obter_importacao_suco_uva():
    """
    Busca dados do país na tabela de importacão de suco de uva da Embrapa e retorna como JSON.
    """
    data = obter_dados2('importacao_suco_uva')
    return data