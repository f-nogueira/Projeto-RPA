import requests
from bs4 import BeautifulSoup
import sqlite3

def coletar_livros():
    url = "https://books.toscrape.com/"
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.text, "html.parser")

    livros = soup.select("article.product_pod")[:10]
    dados = []

    for livro in livros:
        titulo = livro.h3.a["title"]
        preco = livro.select_one(".price_color").text
        avaliacao = livro.p["class"][1]
        disponibilidade = livro.select_one(".instock.availability").text.strip()
        dados.append((titulo, preco, avaliacao, disponibilidade))

    return dados

def salvar_livros():
    livros = coletar_livros()
    conn = sqlite3.connect("livraria.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO livros VALUES (?, ?, ?, ?)", livros)
    conn.commit()
    conn.close()
    print("Dados dos livros salvos com sucesso.")

if __name__ == "__main__":
    salvar_livros()
