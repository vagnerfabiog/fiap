import os
import json
import requests
from bs4 import BeautifulSoup
import hashlib

# Diretório onde os arquivos de cache serão armazenados
CACHE_DIR = "cache_dados"
os.makedirs(CACHE_DIR, exist_ok=True)  # Cria o diretório de cache se ele não existir

def gerar_nome_arquivo_cache(url: str) -> str:
    """Gera um nome de arquivo único para uma URL usando hash SHA-256."""
    hash_url = hashlib.sha256(url.encode()).hexdigest()
    return os.path.join(CACHE_DIR, f"{hash_url}.json")

def salvar_cache(url: str, dados):
    """Salva os dados no arquivo de cache específico para a URL."""
    cache_file = gerar_nome_arquivo_cache(url)
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def carregar_cache(url: str):
    """Carrega os dados do arquivo de cache específico para a URL, se existir."""
    cache_file = gerar_nome_arquivo_cache(url)
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def get_table_data(url: str) -> dict:
    """Extrai dados de uma tabela específica da página HTML com cache."""
    try:
        # Tenta fazer a requisição
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para status de erro HTTP

        # Processa a resposta se a requisição for bem-sucedida
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='tb_base tb_dados')
        data = {}
        current_category = None

        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) == 2:
                if cells[0].get('class') == ['tb_item']:  # Categoria principal
                    current_category = cells[0].text.strip()
                    data[current_category] = {}
                elif cells[0].get('class') == ['tb_subitem']:  # Subcategoria
                    subcategory = cells[0].text.strip()
                    volume = cells[1].text.strip()
                    data[current_category][subcategory] = volume

        salvar_cache(url, data)  # Salva os dados no cache
        return data

    except requests.RequestException:
        # Caso ocorra uma falha na requisição, carrega os dados do cache
        print("Erro ao acessar o site, carregando dados do cache...")
        cache = carregar_cache(url)
        if cache:
            return cache
        else:
            raise RuntimeError("Erro ao acessar o site e nenhum cache disponível.")

def get_table_data2(url: str) -> dict:
    """Extrai dados de uma tabela específica da página HTML com cache."""
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='tb_base tb_dados')
        data = {}

        for row in table.find_all('tr')[1:]:
            cells = row.find_all('td')
            country = cells[0].text.strip()
            quantity = cells[1].text.strip()
            value = cells[2].text.strip()
            data[country] = {'quantidade': quantity, 'valor': value}

        salvar_cache(url, data)
        return data

    except requests.RequestException:
        print("Erro ao acessar o site, carregando dados do cache...")
        cache = carregar_cache(url)
        if cache:
            return cache
        else:
            raise RuntimeError("Erro ao acessar o site e nenhum cache disponível.")
