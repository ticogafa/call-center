import os
os.system('cls')
def modificar(biblioteca, modificar_livro):
    novo_nome = input("Redigite o nome do livro: ")
    autor_livro = input("Redigite o autor do livro: ")
    nova_categoria = input("Redigite a categoria do livro: ")
    while True:
            try:
                preco_livro = float(input("Digite o preço do livro: "))
                break  # Se o número for válido, saia do loop
            except ValueError:
                print("Preço inválido. Tente novamente.")
    biblioteca[modificar_livro]["categoria"] = nova_categoria
    biblioteca[modificar_livro]["autor"] = autor_livro
    biblioteca[modificar_livro]["preço"] = preco_livro
    return novo_nome, autor_livro, nova_categoria, preco_livro

dinheiro_livro = 0
biblioteca = {}
categorias = {}

while True:#inicamos o código com o while true para rodar enquanto Nathália não pedir para parar.
    
    print("Biblioteca de Livros")
    print("1 - Adicionar um livro")
    print("2 - Visualizar livros por categoria")
    print("3 - Atualizar informações do livro")
    print("4 - Excluir um livro")
    print("5 - Visualizar extrato por categoria")
    print("6 - Sair")

    escolha = input("Escolha uma opção: ")
    os.system('cls')

    if escolha == '1':
        nome_livro = input("Digite o nome do livro: ")
        autor_livro = input("Digite o autor do livro: ")
        categoria_livro = input("Digite a categoria do livro: ")
        while True:
            try:
                preco_livro = float(input("Digite o preço do livro: "))
                break  # Se o número for válido, saia do loop
            except ValueError:
                print("Preço inválido. Tente novamente.")
        informacao_livro = {
            "autor": autor_livro,
            "categoria": categoria_livro,
            "preço": preco_livro#nessa parte criamos uma variável para ler as informações dos livros computando o autores, a categorias e o preços.
        }

        biblioteca[nome_livro] = informacao_livro#criamos um dicionario para salvar os nomes dos livros, com isso não importa quantos ela coloque ficaram salvos a disposição.(duvida é um dicionario msm?)

        if categoria_livro in categorias:
            categorias[categoria_livro].append(nome_livro)
        else:
            categorias[categoria_livro] = [nome_livro]

    elif escolha == '2':#este elif foi utilizado para caso Nathália escola a opção 2.
        os.system('cls')
        print("Biblioteca de livros por categoria:")
        dinheiro_livro = sum(informacao_livro['preço'] for informacao_livro in biblioteca.values())
        for categoria, livros in categorias.items():
            print(f"Categoria: {categoria}")
            for livro in livros:
                informacao_livro = biblioteca[livro]
                print(f"Nome do livro: {livro}")
                print(f"Autor: {informacao_livro['autor']}")
                print(f"Preço: {informacao_livro['preço']}")
                print()
        print(f"Total gasto na biblioteca: {dinheiro_livro}")

    elif escolha == '3':
        modificar_livro = input("Digite o nome do livro que você quer atualizar as informações: ")
        if modificar_livro in biblioteca:
            novo_nome, autor_livro, nova_categoria, preco_livro = modificar(biblioteca, modificar_livro)
        if novo_nome != modificar_livro:
            biblioteca[novo_nome] = biblioteca.pop(modificar_livro)
            if nova_categoria != categoria_livro:
                categorias[nova_categoria] = [novo_nome]
                categorias[categoria_livro].remove(modificar_livro)
                if len(categorias[categoria_livro]) == 0:
                    del categorias[categoria_livro]
        
        if novo_nome != modificar_livro:
            biblioteca[novo_nome] = biblioteca.pop(modificar_livro)
            if nova_categoria != categoria_livro:
                categorias[nova_categoria] = [novo_nome]
                categorias[categoria_livro].remove(modificar_livro)
                if len(categorias[categoria_livro]) == 0:
                    del categorias[categoria_livro]
                os.system('cls')
                print('Informações atualizadas!')
            else:
                print(f"O livro {modificar_livro} não está na biblioteca, digite outro livro")

    elif escolha == '4':
        remover_livro = input("Digite o nome do livro que você deseja remover: ")
        if remover_livro in biblioteca:
            categoria_livro = biblioteca[remover_livro]["categoria"]
            biblioteca.pop(remover_livro)
            categorias[categoria_livro].remove(remover_livro)
            if len(categorias[categoria_livro]) == 0:
                del categorias[categoria_livro]
            os.system('cls')
            print('Livro removido!')
        else:
            print(f"O livro {remover_livro} não está na biblioteca, digite outro livro")

    elif escolha == '5':
        categoria_escolhida = input("Digite a categoria para ver o extrato: ")
        os.system('cls')
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
    
    elif escolha == '6':
        break#o comando break foi utilizado para caso Nathália escolha a opção de parar assim encerrando o código.
    else:
        print("Opção inválida. Digite um número de 1 a 6.")#Caso Nathália não escolha nenhum dos números possibilitados o programa colocara está frase.
