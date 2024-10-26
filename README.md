# API_DADOS_EMBRAPA

> API para consulta de dados da Embrapa sobre a vitivinicultura no Brasil, com cache para lidar com a indisponibilidade do site de origem dos dados.

---

## Índice
1. [Introdução](#introdução)
2. [Pré-requisitos](#pré-requisitos)
3. [Instalação](#instalação)
4. [Uso](#uso)
5. [Configuração](#configuração)
6. [Estrutura do Projeto](#estrutura-do-projeto)
7. [Tecnologias Utilizadas](#tecnologias-utilizadas)
8. [Contribuição](#contribuição)
9. [Licença](#licença)
10. [Contato](#contato)

---

## Introdução

Este projeto foi criado como parte do TECH CHALLENGE da fase 1 da Pós Tech da FIAP em Machine Learning Engineering. A **API_DADOS_EMBRAPA** fornece uma interface para acessar dados sobre vitivinicultura coletados do site da Embrapa. Além disso, utiliza cache para garantir a disponibilidade dos dados quando o site de origem estiver offline.

---

## Pré-requisitos

- **Python 3.10 ou superior**
- [Poetry](https://python-poetry.org/) para gerenciamento de dependências
- Conta no [Railway](https://railway.app/) ou outra plataforma de deploy para hospedar a API

---

## Instalação

Para instalar e executar o projeto localmente:

1. Clone o repositório:
   git clone https://github.com/vagnerfabiog/fiap
   cd API_DADOS_EMBRAPA

2. Instale as dependências com o Poetry:
    poetry install

3. Configure as variáveis de ambiente:
    Crie um arquivo .env na raiz do projeto baseado no .env.example e adicione variáveis como SECRET_KEY e ACCESS_TOKEN_EXPIRE_MINUTES.

---

## Uso

Após a instalação, você pode iniciar o servidor localmente:
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    
    Acesse a aplicação no navegador em http://127.0.0.1:8000 ou visualize a documentação da API no Swagger em http://127.0.0.1:8000/docs

    Exemplos de Endpoints
    POST /token: Gera um token JWT para autenticação. Usuario e senha a serem utilizadas para obtencao do Token: Usuario: user1  Senha: senha123
    GET /dados: Retorna os dados vitivinícolas da Embrapa.
    GET /dados/producao: Consulta dados específicos de produção.

---

## Configuração
Variáveis de ambiente não são necessárias.


## Estrutura do Projeto

.
├── app/
│   ├── main.py              # Arquivo principal da aplicação
│   ├── config.py            # Configurações globais
│   ├── routes/              # Pastas para as rotas da API
│   ├── jwt/                 # Autenticação e autorização com JWT
│   ├── utils/               # Utilitários como cache e manipulação de dados
│   └── tests/               # Testes unitários e de integração
├── README.md
├── .env.example             # Exemplo de variáveis de ambiente
└── pyproject.toml           # Configuração do Poetry


---

## Tecnologias Utilizadas

Este projeto foi construído com as seguintes tecnologias:

FastAPI - Framework web para construir APIs rápidas e eficientes.
Uvicorn - Servidor ASGI para execução da aplicação.
Poetry - Gerenciador de dependências e ambientes virtuais.
BeautifulSoup - Para scraping de dados da web.
Railway - Plataforma de deploy e hospedagem (opcional).

---

## Contribuição

Faça um fork do projeto.
Crie uma nova branch para sua funcionalidade (git checkout -b feature/nova-funcionalidade).
Faça o commit das suas alterações (git commit -m 'Adiciona nova funcionalidade').
Faça o push para a branch (git push origin feature/nova-funcionalidade).
Abra um Pull Request.

---

## Licença
Este projeto está licenciado sob a licença MIT. 

---
## Contato
Desenvolvido por Diego / Vagner / Fabio - Entre em contato!


