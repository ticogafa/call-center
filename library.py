import os
os.system('cls')
book_money = 0
library = {}
os.system('cls')
while True:
    
    print("Biblioteca de Livros")
    print("1 - Adicionar um livro")
    print("2 - Visualizar livros")
    print("3 - Atualizar informações do livro")
    print("4 - Excluir um livro")
    print("5 - Sair")

    choice = input("Escolha uma opção: ")
    os.system('cls')

    if choice == '1':
        book_name = input("Digite o nome do livro: ")
        book_author = input("Digite o autor do livro: ")
        book_category = input("Digite a categoria do livro: ")
        book_price = float(input("Digite o preço do livro: "))
        os.system('cls')

        book_info = {
            "autor": book_author,
            "categoria": book_category,
            "preço": book_price
        }

        library[book_name] = book_info

    elif choice == '2':
        os.system('cls')
        print("Biblioteca de livros:")
        book_money = sum(book_info['preço'] for book_info in library.values())
        for book, book_info in library.items():
            print(f"Nome do livro: {book}")
            print(f"Autor: {book_info['autor']}")
            print(f"Categoria: {book_info['categoria']}")
            print(f"Preço: {book_info['preço']}")
            print()
        print(f"Total gasto na biblioteca: {book_money}")

    elif choice == '3':
        book_modify = input("Digite o nome do livro que você quer atualizar as informações: ")
        if book_modify in library:
            new_book_name = input("Redigite o nome do livro: ")
            book_author = input("Redigite o autor do livro: ")
            book_category = input("Redigite a categoria do livro: ")
            book_price = float(input("Redigite o preço do livro: "))
            library[book_modify]["autor"] = book_author
            library[book_modify]["categoria"] = book_category
            library[book_modify]["preço"] = book_price
            if new_book_name != book_modify:
                library[new_book_name] = library.pop(book_modify)
        else:
            print(f"O livro {book_modify} não está na biblioteca, digite outro livro")

    elif choice == '4':
        book_remove = input("Digite o nome do livro que você deseja remover: ")
        if book_remove in library:
            library.pop(book_remove)
            os.system('cls')
            print('Livro removido!')
        else:
            print(f"O livro {book_remove} não está na biblioteca, digite outro livro")

    elif choice == '5':
        break
    else:
        print("Opção inválida. Digite um número de 1 a 5.")
