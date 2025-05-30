# Projeto de Extração de Dados de Países e Livros 📊📚

## Descrição
Sistema automatizado que extrai dados de países via API REST e informações de livros via web scraping. Todos os dados são armazenados em bancos SQLite e um relatório final é gerado em formato Excel.

## Etapas

### 🔹 Parte 1 – Extração via API REST
- Usuário informa 3 países
- Dados extraídos da API: https://restcountries.com/v3.1/name/{pais}
- Salvos em `paises.db`

### 🔹 Parte 2 – Web Scraping com BeautifulSoup
- Extração dos 10 primeiros livros de https://books.toscrape.com/
- Dados salvos em `livraria.db`

### 🔹 Parte 3 – Relatório Final
- Relatório em Excel gerado com `openpyxl`
- Contém abas para países e livros

## Como usar

1. Crie os bancos:
```bash
python criar_bancos.py

2. Extraia os dados e gere o relatório:
python projeto_final.py
