# Parte 1
import os

def print_linha_embelezada():
    tamanho_terminal = 70
    linha = '-' * tamanho_terminal
    print(f"\n{linha}\n")

def salvar_biblioteca(biblioteca):
    with open('biblioteca.txt', 'w') as arquivo:
        for livro, info in biblioteca.items():
            arquivo.write(f"{livro}|{info['autor']}|{info['categoria']}|{info['preço']}\n")

def carregar_biblioteca():
    biblioteca_carregada = {}
    categorias_carregadas = {}
    try:
        with open('biblioteca.txt', 'r', encoding="utf8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split('|')
                if len(dados) == 4:
                    nome_livro, autor_livro, categoria_livro, preco_livro = dados
                    try:
                        preco_livro = float(preco_livro)
                        info_livro = {
                            "autor": autor_livro,
                            "categoria": categoria_livro,
                            "preço": preco_livro
                        }
                        biblioteca_carregada[nome_livro] = info_livro

                        # Atualiza as categorias
                        if categoria_livro in categorias_carregadas:
                            categorias_carregadas[categoria_livro].append(nome_livro)
                        else:
                            categorias_carregadas[categoria_livro] = [nome_livro]
                    except ValueError:
                        print(f"Erro ao converter o preço do livro {nome_livro}.")
                        print_linha_embelezada()
                else:
                    print(f"Os dados da linha não estão completos: {dados}")
                    print_linha_embelezada()
    except FileNotFoundError:
        print("Arquivo 'biblioteca.txt' não encontrado.")
        print_linha_embelezada()
    return biblioteca_carregada, categorias_carregadas
#Parte 2
def adicionar_livro(biblioteca, categorias):
    nome_livro = input("Digite o nome do livro: ")
    print_linha_embelezada()
    autor_livro = input("Digite o autor do livro: ")
    print_linha_embelezada()
    categoria_livro = input("Digite a categoria do livro: ")
    print_linha_embelezada()

    while True:
        try:
            preco_livro = float(input("Digite o preço do livro: "))
            print_linha_embelezada()
            break
        except ValueError:
            print_linha_embelezada()
            print("Preço inválido. Tente novamente.")
            print_linha_embelezada()

    informacao_livro = {
        "autor": autor_livro,
        "categoria": categoria_livro,
        "preço": preco_livro
    }

    biblioteca[nome_livro] = informacao_livro

    if categoria_livro in categorias:
        categorias[categoria_livro].append(nome_livro)
    else:
        categorias[categoria_livro] = [nome_livro]
    print_linha_embelezada()
    print("Livro adicionado com sucesso!")
    print_linha_embelezada()

def visualizar_livros(biblioteca, categorias):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Biblioteca de livros por categoria:")
    print_linha_embelezada()
    dinheiro_total = sum(info['preço'] for info in biblioteca.values())
    for categoria, livros in categorias.items():
        print(f"Categoria: {categoria}")
        print_linha_embelezada()
        for livro in livros:
            # Verifica se o livro ainda está na biblioteca antes de tentar acessá-lo
            if livro.lower() in map(str.lower, biblioteca.keys()):
                informacao_livro = biblioteca[livro]
                print(f"Nome do livro: {livro}")
                
                print(f"Autor: {informacao_livro['autor']}")
                
                print(f"Preço: {informacao_livro['preço']}")
                print()
                print_linha_embelezada()
            else:
                print(f"O livro '{livro}' não está mais na biblioteca.")
                print_linha_embelezada()
    print(f"Total gasto na biblioteca: {dinheiro_total:.2f}")
    print_linha_embelezada()
#Parte 3
def atualizar_informacoes(biblioteca, categorias):
    modificar_livro = input("Digite o nome do livro que você quer atualizar as informações: ").lower()
    print_linha_embelezada()
    if modificar_livro in map(str.lower, biblioteca.keys()):
        nome_livro = [livro for livro in biblioteca.keys() if livro.lower() == modificar_livro][0]

        autor_livro = input("Redigite o autor do livro: ")
        print_linha_embelezada()
        nova_categoria = input("Redigite a categoria do livro: ")
        print_linha_embelezada()

        while True:
            try:
                preco_livro = float(input("Digite o preço do livro: "))
                print_linha_embelezada()
                break
            except ValueError:
                print("Preço inválido. Tente novamente.")
                print_linha_embelezada()

        informacao_livro = {
            "autor": autor_livro,
            "categoria": nova_categoria,
            "preço": preco_livro
        }

        if nova_categoria != biblioteca[nome_livro]["categoria"]:
            categorias[biblioteca[nome_livro]["categoria"]].remove(nome_livro)
            categorias[nova_categoria] = categorias.get(nova_categoria, []) + [nome_livro]

        biblioteca[nome_livro] = informacao_livro

        print('Informações atualizadas!')
        print_linha_embelezada()
        salvar_biblioteca(biblioteca)
    else:
        print(f"O livro {modificar_livro} não está na biblioteca, digite outro livro")
        print_linha_embelezada()
#Parte 4
def excluir_livro(biblioteca, categorias):
    remover_livro = input("Digite o nome do livro que você deseja remover: ").lower()
    print_linha_embelezada()
    if remover_livro in map(str.lower, biblioteca.keys()):
        nome_livro = [livro for livro in biblioteca.keys() if livro.lower() == remover_livro][0]
        categoria_livro = biblioteca[nome_livro]["categoria"]
        biblioteca.pop(nome_livro)
        categorias[categoria_livro].remove(nome_livro)
        if len(categorias[categoria_livro]) == 0:
            del categorias[categoria_livro]
        print('Livro removido!')
        print_linha_embelezada()
    else:
        print(f"O livro {remover_livro} não está na biblioteca, digite outro livro")
        print_linha_embelezada()

def extrato_por_categoria(biblioteca, categorias):
    categoria_escolhida = input("Digite a categoria para ver o extrato: ").lower()
    print_linha_embelezada()
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        # Convertendo as chaves (categorias) para minúsculas para busca insensível a maiúsculas/minúsculas
        categorias_lower = {key.lower(): categorias[key] for key in categorias.keys()}
        
        if categoria_escolhida in categorias_lower:
            livros_categoria = categorias_lower[categoria_escolhida]
            dinheiro_categoria = sum([biblioteca[livro]['preço'] for livro in livros_categoria])
            print(f"Extrato da categoria: {categoria_escolhida}")
            print_linha_embelezada()
            for livro in livros_categoria:
                informacao_livro = biblioteca[livro]
                print(f"Nome do livro: {livro}")
                
                print(f"Autor: {informacao_livro['autor']}")
                
                print(f"Preço: {informacao_livro['preço']}")
                print()
                print_linha_embelezada()
            print(f"Total gasto na categoria: {dinheiro_categoria:.2f}")
            print_linha_embelezada()
        else:
            print(f"A categoria {categoria_escolhida} não contém livros na biblioteca.")
            print_linha_embelezada()
    except KeyError:
        print("Categoria inválida")

def extrato_por_autor(biblioteca, categorias):
    autor_busca = input("Digite o nome do autor que deseja buscar: ").lower()
    print_linha_embelezada()
    os.system('cls' if os.name == 'nt' else 'clear')
    found_books = False
    for livro, informacao_livro in biblioteca.items():
        if informacao_livro['autor'].lower() == autor_busca:

            print(f"\nLivros do autor {informacao_livro['autor']}")
            print_linha_embelezada()
            print(f"\nNome do livro: {livro}")
            
            print(f"Categoria: {informacao_livro['categoria']}")
            
            print(f"Preço: {informacao_livro['preço']}")
            print()
            print_linha_embelezada()
            found_books = True

    if not found_books:
        print(f"Não foram encontrados livros do autor {autor_busca} na biblioteca.")
        print_linha_embelezada()
#Parte 5
def main():
    biblioteca, categorias = carregar_biblioteca()

    while True:
        
        print("Biblioteca de Livros")
        print("1 - Adicionar um livro")
        print("2 - Visualizar livros por categoria")
        print("3 - Atualizar informações do livro")
        print("4 - Excluir um livro")
        print("5 - Visualizar extrato por categoria")
        print("6 - Visualizar livros por autor")
        print("7 - Sair")
        print_linha_embelezada()

        escolha = input("Escolha uma opção: ")

        print_linha_embelezada()

        if escolha == '1':
            adicionar_livro(biblioteca, categorias)
        elif escolha == '2':
            visualizar_livros(biblioteca, categorias)
        elif escolha == '3':
            atualizar_informacoes(biblioteca, categorias)
        elif escolha == '4':
            excluir_livro(biblioteca, categorias)
        elif escolha == '5':
            extrato_por_categoria(biblioteca, categorias)
        elif escolha == '6':
            extrato_por_autor(biblioteca, categorias)
        elif escolha == '7':
            salvar_biblioteca(biblioteca)
            print("Até a próxima, boa leitura :)")
            print_linha_embelezada()
            break
        else:
            print("Opção inválida. Digite um número de 1 a 7.")
            print_linha_embelezada()

if __name__ == "__main__":
    main()
