# API Consulta Dados Embrapa

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
- Conta no [Railway](https://railway.app/) como plataforma de deploy para hospedar a API

---

## Instalação

Para instalar e executar o projeto localmente:

### 1. Clone o repositório:
```bash
   git clone https://github.com/vagnerfabiog/fiap
```   

### 2. Inicialize e ative o ambiente virtual

```bash
  python3 -m venv venv
  # Windows
  venv\Scripts\activate
  # Linux
  source venv/bin/activate
```   

### 3. Instale as dependências do projeto com o Poetry

```bash
 poetry install
```

### 4. Inicialize o servidor da API

```bash
uvicorn app.main:app --reload
```   
A documentação pode ser acessada via URL: `http://127.0.0.1:8000/docs`.
---

## Uso

### 1. Testando via plataforma de testes de APIs (ex.: Postman, Insomnia, etc.)

#### Gere um Token JWT

1. Abra o app (ex.: Postman).
2. Crie uma nova requisição HTTP.
3. Configure a requisição:
   - Método: `POST`
   - URL: `http://127.0.0.1:8000/token`
   - Adicione um cabeçalho (Header):
     - Key: `accept`
     - Value: `application/json`
4. Envie a requisição.
5. Você deve receber uma resposta com um token JWT, semelhante a:

    ```json
    {
      "access_token": "SEU_TOKEN_JWT_GERADO",
      "token_type": "bearer"
    }
    ```

6. Copie o valor de `access_token`.

---


#### Usando o Token para acessar um endpoint protegido

1. Crie uma nova requisição HTTP no Postman.
2. Configure a requisição:
    - Método: `GET`
    - URL: `http://127.0.0.1:8000/producao`
    - Adicione os cabeçalhos (Headers):
      - Key: `accept`
      - Value: `application/json`
      - Key: `Authorization`
      - Value: `Bearer SEU_TOKEN_JWT_GERADO`
        - Substitua `SEU_TOKEN_JWT_GERADO` gerado no endpoint /token.

3. Clique em enviar a requisicao.

4. Você deve receber uma resposta semelhante a:

    ```json
  {
    "VINHO DE MESA": {
        "total": 169762429,
        "subitens": {
            "Tinto": 139320884,
            "Branco": 27910299,
            "Rosado": 2531246
        }
    },
    "VINHO FINO DE MESA (VINIFERA)": {
        "total": 46268556,
        "subitens": {
            "Tinto": 23615783,
            "Branco": 20693437,
            "Rosado": 1959336
        }
    }
    }
    ```


## Estrutura do Projeto
.
├── app/
│   ├── main.py              # Arquivo principal da aplicação
│   ├── config.py            # Configurações globais
│   ├── routes/              # Pastas para as rotas da API
│   ├── jwt/                 # Autenticação e autorização com JWT
│   ├── services/            # Utilitários como cache e manipulação de dados
│   └── tests/               # Testes unitários e de integração
├── README.md
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


## Arquitetura do projeto

Segue esturura do projeto.

![arquiteturatechchallenge](diagrama.png)



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
Desenvolvido por Diego / Vagner  - Entre em contato!


