import sqlite3

conn1 = sqlite3.connect("paises.db")
cursor1 = conn1.cursor()
cursor1.execute('''
    CREATE TABLE IF NOT EXISTS paises (
        nome_comum TEXT,
        nome_oficial TEXT,
        capital TEXT,
        continente TEXT,
        regiao TEXT,
        sub_regiao TEXT,
        populacao INTEGER,
        area REAL,
        moeda_nome TEXT,
        moeda_simbolo TEXT,
        idioma_principal TEXT,
        fuso_horario TEXT,
        bandeira_url TEXT
    )
''')
conn1.commit()
conn1.close()

conn2 = sqlite3.connect("livraria.db")
cursor2 = conn2.cursor()
cursor2.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        titulo TEXT,
        preco TEXT,
        avaliacao TEXT,
        disponibilidade TEXT
    )
''')
conn2.commit()
conn2.close()

print("Bancos de dados criados com sucesso.")
