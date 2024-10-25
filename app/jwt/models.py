from pydantic import BaseModel

class User(BaseModel):
    username: str
    full_name: str
    email: str
    password: str  # senha em texto puro
    disabled: bool = False

# Banco de dados falso de usuários
fake_users_db = {
    "user1": {
        "username": "user1",
        "full_name": "Primeiro usuario",
        "email": "user1@example.com",
        "password": "senha123",  # senha em texto puro
        "disabled": False,
    }
}
