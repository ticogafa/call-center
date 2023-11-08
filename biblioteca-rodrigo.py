import os
os.system('cls')
def modificar(biblioteca, modificar_livro):
    novo_nome = input("Redigite o nome do livro: ")
    autor_livro = input("Redigite o autor do livro: ")
    nova_categoria = input("Redigite a categoria do livro: ")
    preco_livro = float(input("Redigite o preço do livro: "))
    biblioteca[modificar_livro]["categoria"] = nova_categoria
    biblioteca[modificar_livro]["autor"] = autor_livro
    biblioteca[modificar_livro]["preço"] = preco_livro
    return novo_nome, autor_livro, nova_categoria, preco_livro

modificar_livro = input("Digite o nome do livro que você quer atualizar as informações: ")
if modificar_livro in biblioteca:
    novo_nome = modificar()
    autor_livro = modificar()
    nova_categoria=modificar()
    preco_livro= modificar()
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