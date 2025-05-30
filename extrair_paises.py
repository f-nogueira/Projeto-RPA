import requests
import sqlite3

def buscar_pais(nome_pais):
    url = f"https://restcountries.com/v3.1/name/{nome_pais}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print(f"Erro ao buscar dados do país: {nome_pais}")
        return None

    dados = resposta.json()[0]
    return (
        dados["name"]["common"],
        dados["name"]["official"],
        dados.get("capital", ["Não disponível"])[0],
        dados.get("continents", ["Não disponível"])[0],
        dados.get("region", "Não disponível"),
        dados.get("subregion", "Não disponível"),
        dados.get("population", 0),
        dados.get("area", 0),
        list(dados.get("currencies", {}).values())[0].get("name", "Desconhecida"),
        list(dados.get("currencies", {}).values())[0].get("symbol", ""),
        list(dados.get("languages", {}).values())[0] if dados.get("languages") else "Desconhecido",
        dados.get("timezones", ["Desconhecido"])[0],
        dados.get("flags", {}).get("png", "")
    )

def salvar_paises():
    paises = [input(f"Digite o nome do país {i+1}: ") for i in range(3)]
    conn = sqlite3.connect("paises.db")
    cursor = conn.cursor()

    for pais in paises:
        dados = buscar_pais(pais)
        if dados:
            cursor.execute("INSERT INTO paises VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", dados)

    conn.commit()
    conn.close()
    print("Dados dos países salvos com sucesso.")

if __name__ == "__main__":
    salvar_paises()
