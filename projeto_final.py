import extrair_paises
import extrair_livros
import gerar_relatorio

def main():
    print("🔍 Extraindo dados dos países...")
    extrair_paises.salvar_paises()

    print("\n📚 Coletando dados dos livros...")
    extrair_livros.salvar_livros()

    print("\n📄 Gerando relatório final...")
    nome = input("Digite seu nome para o relatório: ")
    gerar_relatorio.gerar_relatorio(nome)

if __name__ == "__main__":
    main()
