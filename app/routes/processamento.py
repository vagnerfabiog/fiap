from fastapi import APIRouter
from app.services.dados_embrapa import obter_dados

router = APIRouter()

#Essas rotas servem dados de processamento

@router.get('/processamento/viniferas')
async def obter_processamento_vinifera():
    data = obter_dados('processamento_viniferas')
    return data

@router.get('/processamento/americanas_hibridas')
async def obter_processamento_americanas_hibridas():
    data = obter_dados('processamento_americanas')
    return data

@router.get('/processamento/uvas')
async def obter_processamento_uvas():
    data = obter_dados('processamento_uvas')
    return data

@router.get('/processamento/sem_classificacao')
async def obter_processamento_sem_classificacao():
    data = obter_dados('processamento_sem_classificacao')
    return data
