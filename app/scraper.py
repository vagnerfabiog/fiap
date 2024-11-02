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
        
        # Inicializa a estrutura de dados
        data = {}
        current_category = None

        # Itera pelas linhas da tabela
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) == 2:  # Espera exatamente 2 células por linha (nome e valor)
                cell_class = cells[0].get('class', [])

                # Verifica se é uma categoria principal
                if 'tb_item' in cell_class:
                    current_category = cells[0].text.strip()  # Nome da categoria
                    total_value = cells[1].text.strip().replace('.', '')  # Valor total da categoria
                    data[current_category] = {"total": int(total_value), "subitens": {}}  # Cria a estrutura de categoria

                # Verifica se é uma subcategoria e temos uma categoria atual
                elif 'tb_subitem' in cell_class and current_category:
                    subcategory = cells[0].text.strip()  # Nome da subcategoria
                    volume = cells[1].text.strip().replace('.', '')  # Quantidade correspondente
                    volume = int(volume) if volume != '-' else 0  # Converte para inteiro ou 0 se for '-'
                    data[current_category]["subitens"][subcategory] = volume  # Adiciona o subitem

                # Caso seja o "Total" geral
                elif not cell_class:
                    total = cells[1].text.strip().replace('.', '')
                    total = int(total) if total else 0
                    data["Total"] = total  # Armazena o total geral

        # Salva os dados no cache para futuras consultas
        salvar_cache(url, data)
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
        
        # Inicializando o dicionário para armazenar os dados
        data = {"países": []}
        total_importacoes = {}

        # Processamento das linhas da tabela
        for row in table.find_all('tr'):
            cells = row.find_all('td')

            # Verifica se a linha tem exatamente 3 células: País, Quantidade, Valor
            if len(cells) == 3:
                pais = cells[0].text.strip()
                quantidade = cells[1].text.strip().replace('.', '')
                valor = cells[2].text.strip().replace('.', '')

                # Converte '-' em 0 para processamento
                quantidade = int(quantidade) if quantidade != '-' else 0
                valor = int(valor) if valor != '-' else 0

                # Verifica se é a linha do total
                if pais.lower() == "total":
                    total_importacoes["quantidade"] = quantidade
                    total_importacoes["valor"] = valor
                else:
                    # Adiciona os dados do país na lista
                    data["países"].append({
                        "país": pais,
                        "quantidade": quantidade,
                        "valor": valor
                    })
        
        # Adiciona o total ao final
        data["total"] = total_importacoes

        # Salva no cache para futuras consultas
        salvar_cache(url, data)
        return data

    except requests.RequestException:
        print("Erro ao acessar o site, carregando dados do cache...")
        cache = carregar_cache(url)
        if cache:
            return cache
        else:
            raise RuntimeError("Erro ao acessar o site e nenhum cache disponível.")
