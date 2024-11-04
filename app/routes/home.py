from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse
import os

router = APIRouter()

# Função para servir a página HTML na rota '/'
@router.get("/", response_class=HTMLResponse)
async def home():
    # Caminho absoluto para o index.html
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html_path = os.path.join(current_dir, "templates", "index.html")

    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        return Response(content=html_content, media_type="text/html")
    except FileNotFoundError:
        return Response(content="<h1>Erro 404: Página não encontrada</h1>", status_code=404, media_type="text/html")

# Inicie o servidor com uvicorn nome_do_arquivo:app --reload
