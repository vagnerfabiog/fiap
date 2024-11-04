import os

SECRET_KEY = os.getenv("SECRET_KEY", "MachineLearningEngineering")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
ALGORITHM = "HS256"


API_TITLE="API de Consultas - Embrapa"
API_DESCRIPTION = """
API de Consultas - Embrapa 🏞️

Esta API permite consultar dados relevantes sobre a produção, processamento, comercialização, importação e exportação relacionados ao setor vitivinícola. 


- **Usuário de teste:** `user1`
- **Senha de teste:** `senha123`

Sinta-se à vontade para explorar a documentação e testar os endpoints.
"""
API_VERSION="1.0.0"
CONTACT_INFO = {
        "name": "Diego / Vagner",
        "email": "ra@fiap.com.br",
    }
