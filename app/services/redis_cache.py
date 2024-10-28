import redis
import hashlib
import json

redis_client = redis.StrictRedis(
    host='redis-10375.c308.sa-east-1-1.ec2.redns.redis-cloud.com',    
    port=10375,          
    db=0,                  
    password='CzvEqwj7fP10K9QFaWZrpRZ8JxTGB7v8',   
    decode_responses=True   # Configuração para retornar strings em vez de bytes
)


def gerar_chave_cache(url: str) -> str:
    """Gera uma chave única para o cache usando hash SHA-256 da URL."""
    hash_url = hashlib.sha256(url.encode()).hexdigest()
    return f"cache:{hash_url}"

def salvar_cache(url: str, dados):
    """Salva os dados no Redis com uma chave específica para a URL."""
    cache_key = gerar_chave_cache(url)
    redis_client.set(cache_key, json.dumps(dados))  # Armazena os dados no Redis como JSON
    redis_client.expire(cache_key, 3600) # Define uma expiração de 1 hora
   

def carregar_cache(url: str):
    """Carrega os dados do cache Redis, se eles existirem."""
    cache_key = gerar_chave_cache(url)
    cached_data = redis_client.get(cache_key)
    if cached_data:
        return json.loads(cached_data)
    return None