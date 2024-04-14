while True:
    try:
        import os

        # Função para imprimir uma linha decorativa-------------------------------------------------------------------------------------------
        def print_linha_embelezada():
            tamanho_terminal = 70
            linha = '-' * tamanho_terminal
            print(f"\n{linha}\n") 

        # Função para salvar a biblioteca em um arquivo---------------------------------------------------------------------------------------
        def salvar_biblioteca(biblioteca):
            with open('biblioteca.txt', 'w', encoding="utf-8") as arquivo: # Abrindo o arquivo biblioteca.txt onde ficaram armazenadas as informações ao salvar-
                for livro, info in biblioteca.items():
                    arquivo.write(f"{livro}|{info['autor']}|{info['categoria']}|{info['preço']}\n")

        # Função para carregar a biblioteca de um arquivo-------------------------------------------------------------------------------------
        def carregar_biblioteca():
            biblioteca_carregada = {}
            categorias_carregadas = {}
            try:
                with open('biblioteca.txt', 'r', encoding="utf-8") as arquivo: #Abrindo o arquivo "biblioteca.txt" para buscar livros ---------
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

        # Atualiza as categorias--------------------------------------------------------------------------------------------------------------
                                if categoria_livro in categorias_carregadas:#verificar se a categoria existe, se já existe adiciona o livro a ela.
                                    categorias_carregadas[categoria_livro].append(nome_livro)
                                else:#caso categoria for inexistente será criada uma----------------------------------------------------------
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

        # Função para adicionar um livro à biblioteca-----------------------------------------------------------------------------------------
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
        #Atualiza na biblioteca as informações digitadas pelo usuário-------------------------------------------------------------------------
            biblioteca[nome_livro] = informacao_livro

            if categoria_livro in categorias:
                categorias[categoria_livro].append(nome_livro) 
            else:
                categorias[categoria_livro] = [nome_livro] #Caso a categoria ainda não existir-------------------------------------------------
            print_linha_embelezada()
            print("Livro adicionado com sucesso!")
            print_linha_embelezada()

        # Função para visualizar os livros por categoria--------------------------------------------------------------------------------------
        def visualizar_livros(biblioteca, categorias):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Biblioteca de livros por categoria:")
            print_linha_embelezada()
            dinheiro_total = sum(info['preço'] for info in biblioteca.values())
            for categoria, livros in categorias.items(): 
                print(f"Categoria: {categoria}")
                print_linha_embelezada()
                for livro in livros:
        # Verifica se o livro ainda está na biblioteca antes de tentar acessá-lo-------------------------------------------------------------
                    if livro.lower() in map(str.lower, biblioteca.keys()):
                        informacao_livro = biblioteca[livro]
                        print(f"Nome do livro: {livro}")
                        print(f"Autor: {informacao_livro['autor']}")
                        print(f"Preço: R${informacao_livro['preço']}")
                        print()
                        print_linha_embelezada()
                    else:
                        print(f"O livro '{livro}' não está mais na biblioteca.")
                        print_linha_embelezada()
            print(f"Total gasto na biblioteca: R${dinheiro_total:.2f}")
            print_linha_embelezada()

        # Função para atualizar informações de um livro na biblioteca-----------------------------------------------------------------------
        def atualizar_informacoes(biblioteca, categorias):
            modificar_livro = input("Digite o nome do livro que você quer atualizar as informações: ").lower()
            print_linha_embelezada()
            if modificar_livro in map(str.lower, biblioteca.keys()): #Vendo se o livro está na biblioteca-----------------------------------
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
        #Atualiza na biblioteca as informações digitadas pelo usuário-------------------------------------------------------------------------
                if nova_categoria != biblioteca[nome_livro]["categoria"]: #Vendo se algo mudou para alterar as informações que foram alteradas
                    categorias[biblioteca[nome_livro]["categoria"]].remove(nome_livro)
                    categorias[nova_categoria] = categorias.get(nova_categoria, []) + [nome_livro]

                biblioteca[nome_livro] = informacao_livro

                print('Informações atualizadas!')
                print_linha_embelezada()
                salvar_biblioteca(biblioteca)
            else:
                print(f"O livro {modificar_livro} não está na biblioteca, digite outro livro")
                print_linha_embelezada()

        #Função para excluir um livro da biblioteca------------------------------------------------------------------------------------------
        def excluir_livro(biblioteca, categorias):
            remover_livro = input("Digite o nome do livro que você deseja remover: ").lower()
            print_linha_embelezada()
            if remover_livro in map(str.lower, biblioteca.keys()):
        #A função map permite aplicar uma função a cada item de uma lista e coletar os resultados em um novo iterador, sem alterar a lista original, neste caso foi usado lower em todas as strings. ****
                nome_livro = [livro for livro in biblioteca.keys() if livro.lower() == remover_livro][0]
                categoria_livro = biblioteca[nome_livro]["categoria"]
        #Para cada item na sequência_de_itens, a expressão será aplicada para gerar um novo elemento na lista nova_lista.------------------- 
                biblioteca.pop(nome_livro)
                categorias[categoria_livro].remove(nome_livro)
                if len(categorias[categoria_livro]) == 0:
                    del categorias[categoria_livro]
                print('Livro removido!')
                print_linha_embelezada()
            else:
                print(f"O livro {remover_livro} não está na biblioteca, digite outro livro")
                print_linha_embelezada()
        #Então se o livro que o usuário deseja remover estiver em "livro" ele será removido, caso contrário ele retorna para a aba main.****

        #elif 5
        # Função para extrair informações por categoria---------------------------------------------------------------------------------------
        def extrato_por_categoria(biblioteca, categorias):
            categoria_escolhida = input("Digite a categoria para ver o extrato: ").lower()
            print_linha_embelezada()
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
        # Convertendo as chaves (categorias) para minúsculas para busca insensível a maiúsculas/minúsculas------------------------------------
                categorias_lower = {key.lower(): categorias[key] for key in categorias.keys()}
                
                if categoria_escolhida in categorias_lower:
                    livros_categoria = categorias_lower[categoria_escolhida]
                    dinheiro_categoria = sum([biblioteca[livro]['preço'] for livro in livros_categoria])
                    print(f"Extrato da categoria: {categoria_escolhida}")
                    print_linha_embelezada()
                    for livro in livros_categoria: #Printando na tela os livros por categoria-------------------------------------------------
                        informacao_livro = biblioteca[livro]
                        print(f"Nome do livro: {livro}")
                        print(f"Autor: {informacao_livro['autor']}")
                        print(f"Preço: R${informacao_livro['preço']}")
                        print()
                        print_linha_embelezada()
                    print(f"Total gasto na categoria: R${dinheiro_categoria:.2f}")
                    print_linha_embelezada()
                else:
                    print(f"A categoria {categoria_escolhida} não contém livros na biblioteca.")
                    print_linha_embelezada()
            except KeyError:
                print("Categoria inválida")
        #elif 6
        #Função para extrair informações por autor--------------------------------------------------------------------------------------------
        def extrato_por_autor(biblioteca, categorias):
            autor_busca = input("Digite o nome do autor que deseja buscar: ").lower()
            print_linha_embelezada()
            os.system('cls' if os.name == 'nt' else 'clear')
            found_books = False
            for livro, informacao_livro in biblioteca.items():
                if informacao_livro['autor'].lower() == autor_busca:
        #Ele vai percorrer "informacao_livro" dentro da biblioteca, e conferir se o autor digitado está no banco de dados---------------------
                    print(f"\n{informacao_livro['autor']}:")
                    print_linha_embelezada()
                    print(f"\nNome do livro: {livro}")
                    print(f"Categoria: {informacao_livro['categoria']}")
                    print(f"Preço: R${informacao_livro['preço']}")
                    print()
                    print_linha_embelezada()
                    found_books = True

            if not found_books:
                print(f"Não foram encontrados livros do autor {autor_busca} na biblioteca.")
                print_linha_embelezada()

        # Função principal que controla o menu e as interações com o usuário------------------------------------------------------------------
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
        #Condicionais pra cada ação do usuário, integrado com as defs definidas no início
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
        #A função main é executada somente se o arquivo Python for executado como um programa principal, isso oferece mais flexibilidade para executar apenas partes específicas quando necessário.
        if __name__ == "__main__":
            main()
        break
    except EOFError:
        print("EOFError, nao aperte control antes de letras/numeros")
    continue
