# Projeto: Controle de Estoque - Algoritmos e Programação I
# Integrantes: Pedro Henrique Leite - Gabriel Nobrega Neri - Cauê Lemos Garcia

# Importa uma biblioteca que permite utilizar o recurso "sys.exit()", que foi usado para a criação da função de encerrar o programa.
import sys

# Função para cadastrar um novo produto.
def cadastrar_produto(lista_produtos):
    # Solicita o nome, código e quantidade do novo produto ao usuário.
    nome = input("Digite o nome do produto a ser cadastrado: ")
    codigo = input("Digite o código do produto a ser cadastrado: ")
    quantidade = int(input("Digite a quantidade deste produto a ser cadastrado: "))

    # Cria um dicionário para armazenar as informações do produto.
    produto = {"nome": nome, "codigo": codigo, "quantidade": quantidade}

    # Adiciona o produto cadastrado à lista de produtos.
    lista_produtos.append(produto)

    # Exibe uma mensagem de sucesso.
    print("Produto cadastrado com sucesso!", "\n")

# Função para consultar um produto existente.
def consultar_produto(lista_produtos):
    # Solicita o código do produto a ser consultado.
    codigo = input("Digite o código do produto a ser consultado: ")

    # Variável para indicar se o produto foi encontrado ou não.
    encontrado = False

    # Percorre a lista de produtos em busca do produto com o código fornecido.
    for produto in lista_produtos:
        if produto["codigo"] == codigo:
            # Exibe as informações do produto encontrado.
            print("Produto encontrado:")
            print("→ Nome:", produto["nome"])
            print("→ Código:", produto["codigo"])
            print("→ Quantidade:", produto["quantidade"], "\n")
            encontrado = True
            break

    # Se o produto não foi encontrado, exibe uma mensagem de erro e retorna ao menu.
    if not encontrado:
        print("Produto não encontrado.", "\n")

# Função para atualizar as informações de um produto existente.
def atualizar_produto(lista_produtos):
    # Solicita o código do produto a ser atualizado.
    codigo = input("Digite o código do produto a ser atualizado: ")

    # Variável para indicar se o produto foi encontrado ou não.
    encontrado = False

    # Percorre a lista de produtos em busca do produto com o código fornecido.
    for produto in lista_produtos:
        if produto["codigo"] == codigo:
            # Exibe as informações do produto encontrado.
            print("Produto encontrado:")
            print("→ Nome:", produto["nome"])
            print("→ Código:", produto["codigo"])
            print("→ Quantidade:", produto["quantidade"])

            # Solicita as novas informações para atualizar o produto, no caso o nome e a quantidade.
            novo_nome = input("Digite o novo nome do produto a ser atualizado: ")
            if novo_nome:
                produto["nome"] = novo_nome

            nova_quantidade = input("Digite a nova quantidade do produto a ser atualizado: ")
            if nova_quantidade:
                produto["quantidade"] = int(nova_quantidade)

            # Exibe uma mensagem de sucesso.
            print("Produto atualizado com sucesso!", "\n")
            encontrado = True
            break

    # Se o produto não foi encontrado, exibe uma mensagem de erro e retorna ao menu.
    if not encontrado:
        print("Produto não encontrado.", "\n")

# Função para excluir um produto do estoque.
def excluir_produto(lista_produtos):
    # Solicita o código do produto a ser excluído.
    codigo = input("Digite o código do produto a ser excluído: ")

    # Variável para indicar se o produto foi encontrado ou não.
    encontrado = False

    # Percorre a lista de produtos em busca do produto com o código fornecido.
    for produto in lista_produtos:
        if produto["codigo"] == codigo:
            # Remove o produto da lista de produtos.
            lista_produtos.remove(produto)

            # Exibe uma mensagem de sucesso
            print("Produto excluído com sucesso!", "\n")
            encontrado = True
            break

    # Se o produto não foi encontrado, exibe uma mensagem de erro e retorna ao menu.
    if not encontrado:
        print("Produto não encontrado.", "\n")

# Função para gerar um relatório dos produtos cadastrados.
def relatorio_produtos(lista_produtos): # Função para gerar um relatório dos produtos cadastrados.
    # Verifica se há produtos cadastrados.
    if not lista_produtos:
        # Se não houver produtos cadastrados, exibe uma mensagem informando.
        print("Não há produtos cadastrados.", "\n")
    else:
        # Se houver produtos cadastrados, exibe o relatório de produtos.
        print("Relatório de Produtos:")
        for produto in lista_produtos:
            print("→ Nome:", produto["nome"])
            print("→ Código:", produto["codigo"])
            print("→ Quantidade:", produto["quantidade"], "\n")

# Função para encerrar o programa.
def encerrar_programa():
    # Solicita a confirmação do usuário para encerrar o programa.
    confirmacao = input("Tem certeza de que deseja encerrar o programa? (S/N): ").upper()

    # Verifica se a entrada do usuário é válida.
    while confirmacao not in ("S", "N"):
        confirmacao = input("Entrada inválida. Responda com 'Sim' ou 'Não': ").upper()

    # Se o usuário confirmar, encerra o programa. Caso contrário, retorna ao menu principal.
    if confirmacao == "S":
        print("O programa está sendo encerrado...", "\n")
        sys.exit()
    elif confirmacao == "N":
        print("Certo. Voltando para o menu...", "\n")

# Função principal que exibe o menu e realiza as operações escolhidas pelo usuário.
def menu(lista_produtos):
    while True:
        print("---- Menu - Controle de Estoque ----")
        print("1. Cadastrar produto")
        print("2. Consultar produto")
        print("3. Atualizar produto")
        print("4. Excluir produto")
        print("5. Relatório dos produtos")
        print("6. Encerrar o programa")
    
        # Solicita ao usuário a opção desejada.
        opcao = input("Digite o número da opção desejada: ")

        print("------------------------------------")

        # Com base na opção selecionada, chama a função correspondente.
        if opcao == "1":
            cadastrar_produto(lista_produtos)
        elif opcao == "2":
            consultar_produto(lista_produtos)
        elif opcao == "3":
            atualizar_produto(lista_produtos)
        elif opcao == "4":
            excluir_produto(lista_produtos)
        elif opcao == "5":
            relatorio_produtos(lista_produtos)
        elif opcao == "6":
            encerrar_programa()
        else:
            print("Opção inválida. Por favor, digite uma opção válida.", "\n")

# Cria uma lista vazia para armazenar os produtos.
lista_produtos = []

# Chama a função de menu para iniciar o programa.
menu(lista_produtos)