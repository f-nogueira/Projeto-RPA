from openpyxl import Workbook
import sqlite3
from datetime import datetime

def gerar_relatorio(nome_aluno="Aluno"):
    data_hoje = datetime.today().strftime("%d/%m/%Y")
    wb = Workbook()


    ws1 = wb.active
    ws1.title = "Países"

    conn = sqlite3.connect("paises.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM paises")
    dados_paises = cursor.fetchall()
    colunas_paises = [desc[0] for desc in cursor.description]
    conn.close()

    ws1.append(["Relatório de Países"])
    ws1.append([f"Aluno: {nome_aluno}", f"Data: {data_hoje}"])
    ws1.append([])
    ws1.append(colunas_paises)
    for linha in dados_paises:
        ws1.append(linha)


    ws2 = wb.create_sheet("Livros")
    conn = sqlite3.connect("livraria.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    dados_livros = cursor.fetchall()
    colunas_livros = [desc[0] for desc in cursor.description]
    conn.close()

    ws2.append(["Relatório de Livros"])
    ws2.append([f"Aluno: {nome_aluno}", f"Data: {data_hoje}"])
    ws2.append([])
    ws2.append(colunas_livros)
    for linha in dados_livros:
        ws2.append(linha)

    wb.save("relatorio_final.xlsx")
    print("✅ Relatório salvo como: relatorio_final.xlsx")

if __name__ == "__main__":
    nome = input("Digite seu nome para o relatório: ")
    gerar_relatorio(nome)
