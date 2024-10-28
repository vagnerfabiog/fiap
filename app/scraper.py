import os
import json
import requests
from bs4 import BeautifulSoup
import hashlib
from app.services.redis_cache import salvar_cache, carregar_cache

def get_table_data(url: str) -> dict:
    """Extrai dados de uma tabela específica da página HTML com cache."""
    # Primeiro, tenta carregar os dados do cache Redis
    cache = carregar_cache(url)
    if cache:
        print("Carregando dados do cache Redis...")
        return cache

    # Se não houver cache, faz a requisição e processa os dados
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para status de erro HTTP
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

        salvar_cache(url, data)  # Salva os dados no Redis
        return data

    except requests.RequestException:
        # Caso ocorra uma falha na requisição, tenta carregar os dados do cache
        print("Erro ao acessar o site, carregando dados do cache...")
        cache = carregar_cache(url)
        if cache:
            return cache
        else:
            raise RuntimeError("Erro ao acessar o site e nenhum cache disponível.")

def get_table_data2(url: str) -> dict:
    """Extrai dados de uma tabela específica da página HTML com cache."""
    # Primeiro, tenta carregar os dados do cache Redis
    cache = carregar_cache(url)
    if cache:
        print("Carregando dados do cache Redis...")
        return cache

    # Se não houver cache, faz a requisição e processa os dados
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
