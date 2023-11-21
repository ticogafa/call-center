#Parte 1
import os

def salvar_biblioteca(biblioteca):
    with open('biblioteca.txt', 'w') as arquivo:
        for livro, info in biblioteca.items():
            arquivo.write(f"{livro},{info['autor']},{info['categoria']},{info['preço']}\n")

def carregar_biblioteca():
    biblioteca_carregada = {}
    categorias_carregadas = {}
    try:
        with open('biblioteca.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
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
                else:
                    print(f"Os dados da linha não estão completos: {dados}")
    except FileNotFoundError:
        print("Arquivo 'biblioteca.txt' não encontrado.")
    return biblioteca_carregada, categorias_carregadas

def adicionar_livro(biblioteca, categorias):
    nome_livro = input("Digite o nome do livro: ")
    autor_livro = input("Digite o autor do livro: ")
    categoria_livro = input("Digite a categoria do livro: ")
# Parte 2    
    while True:
        try:
            preco_livro = float(input("Digite o preço do livro: "))
            break
        except ValueError:
            print("Preço inválido. Tente novamente.")

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

    print("Livro adicionado com sucesso!")

def visualizar_livros(biblioteca, categorias):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Biblioteca de livros por categoria:")
    dinheiro_total = sum(info['preço'] for info in biblioteca.values())
    for categoria, livros in categorias.items():
        print(f"Categoria: {categoria}")
        for livro in livros:
            # Verifica se o livro ainda está na biblioteca antes de tentar acessá-lo
            if livro in biblioteca:
                informacao_livro = biblioteca[livro]
                print(f"Nome do livro: {livro}")
                print(f"Autor: {informacao_livro['autor']}")
                print(f"Preço: {informacao_livro['preço']}")
                print()
            else:
                print(f"O livro '{livro}' não está mais na biblioteca.")
    print(f"Total gasto na biblioteca: {dinheiro_total}")

def atualizar_informacoes(biblioteca, categorias):
    modificar_livro = input("Digite o nome do livro que você quer atualizar as informações: ")
    if modificar_livro in biblioteca:
        novo_nome = input("Redigite o nome do livro: ")

        if novo_nome != modificar_livro and novo_nome in biblioteca:
            print("Este nome já está sendo usado por outro livro. Escolha outro nome.")
            return

        autor_livro = input("Redigite o autor do livro: ")
        nova_categoria = input("Redigite a categoria do livro: ")
# Parte 3      
        while True:
            try:
                preco_livro = float(input("Digite o preço do livro: "))
                break
            except ValueError:
                print("Preço inválido. Tente novamente.")

        informacao_livro = {
            "autor": autor_livro,
            "categoria": nova_categoria,
            "preço": preco_livro
        }

        # Verifica se a categoria foi alterada
        if nova_categoria != biblioteca[modificar_livro]["categoria"]:
            # Remove o livro da categoria anterior
            categorias[biblioteca[modificar_livro]["categoria"]].remove(modificar_livro)
            
            # Adiciona o livro à nova categoria
            categorias[nova_categoria] = categorias.get(nova_categoria, []) + [novo_nome]

        biblioteca[novo_nome] = informacao_livro

        if novo_nome != modificar_livro:
            del biblioteca[modificar_livro]

        print('Informações atualizadas!')

        # Salva as alterações imediatamente após a atualização
        salvar_biblioteca(biblioteca)
    else:
        print(f"O livro {modificar_livro} não está na biblioteca, digite outro livro")


def excluir_livro(biblioteca, categorias):
    remover_livro = input("Digite o nome do livro que você deseja remover: ")
    if remover_livro in biblioteca:
        categoria_livro = biblioteca[remover_livro]["categoria"]
        biblioteca.pop(remover_livro)
        categorias[categoria_livro].remove(remover_livro)
        if len(categorias[categoria_livro]) == 0:
            del categorias[categoria_livro]
        print('Livro removido!')
    else:
        print(f"O livro {remover_livro} não está na biblioteca, digite outro livro")
#Parte 4
def extrato_por_categoria(biblioteca, categorias):
    categoria_escolhida = input("Digite a categoria para ver o extrato: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if categoria_escolhida in categorias:
        livros_categoria = categorias[categoria_escolhida]
        dinheiro_categoria = sum([biblioteca[livro]['preço'] for livro in livros_categoria])
        print(f"Extrato da categoria: {categoria_escolhida}")
        for livro in categorias[categoria_escolhida]:
            informacao_livro = biblioteca[livro]
            print(f"Nome do livro: {livro}")
            print(f"Autor: {informacao_livro['autor']}")
            print(f"Preço: {informacao_livro['preço']}")
            print()
        print(f"Total gasto na categoria: {dinheiro_categoria}")
    else:
        print(f"A categoria {categoria_escolhida} não contém livros na biblioteca.")

def main():
    biblioteca, categorias = carregar_biblioteca()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Biblioteca de Livros")
        print("1 - Adicionar um livro")
        print("2 - Visualizar livros por categoria")
        print("3 - Atualizar informações do livro")
        print("4 - Excluir um livro")
        print("5 - Visualizar extrato por categoria")
        print("6 - Sair")

        escolha = input("Escolha uma opção: ")

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
            salvar_biblioteca(biblioteca)
            print("Até a próxima, boa leitura :)")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 6.")

if __name__ == "__main__":
    main()
