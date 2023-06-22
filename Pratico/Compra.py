'''
O objetivo desse código e simular uma Loja online onde é possivel cadastrar,visualizar os produtos,adicionar produtos,visualizar o carrinho
finalizar a compra,visualizar seu historico de compras e por fim sair.
'''

import json
import datetime

# Função para exibir o menu de opções
def exibir_menu():
    print("\n===== BEM-VINDO À LOJA ONLINE =====")
    print("1. Cadastrar produto")
    print("2. Visualizar produtos")
    print("3. Adicionar produto ao carrinho")
    print("4. Visualizar carrinho")
    print("5. Finalizar compra")
    print("6. Visualizar histórico de compras")
    print("0. Sair")

# Função para cadastrar um produto
def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    produto = {"nome": nome, "preco": preco}
    produtos.append(produto)

# Função para visualizar os produtos disponíveis
def visualizar_produtos():
    if len(produtos) > 0:
        for produto in produtos:
            print(f"Nome: {produto['nome']}, Preço: R${produto['preco']}")
    else:
        print("Não há produtos disponíveis.")

# Função para adicionar um produto ao carrinho
def adicionar_produto_carrinho():
    visualizar_produtos()
    num_produto = int(input("Digite o número do produto a ser adicionado ao carrinho: "))

    if 1 <= num_produto <= len(produtos):
        produto = produtos[num_produto - 1]
        carrinho.append(produto)

# Função para visualizar o carrinho de compras
def visualizar_carrinho():
    if len(carrinho) > 0:
        for produto in carrinho:
            print(f"Nome: {produto['nome']}, Preço: R${produto['preco']}")
    else:
        print("O carrinho está vazio.")

# Função para finalizar a compra
def finalizar_compra():
    if len(carrinho) > 0:
        total = 0
        for produto in carrinho:
            total += produto['preco']
        print(f"Total: R${total}")
    else:
        print("O carrinho está vazio.")

# Função para visualizar o historico de compra
def visualizar_historico_compras():
    print("\n===== HISTÓRICO DE COMPRAS =====")
    if len(historico_compras) > 0:
        for compra in historico_compras:
            print(f"Data/Hora: {compra['data_hora']}")
            print(f"Total: R${compra['total']}")
            print("Produtos:")
            for produto in compra['produtos']:
                print(f"Nome: {produto['nome']}, Preço: R${produto['preco']}")
            print("-----")

        else:
            print("Não há histórico de compras.")

# Listas para armazenar os produtos, carrinho e histórico de compras
produtos = []
carrinho = []
historico_compras = []

# Loop principal do programa
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        visualizar_produtos()
    elif opcao == "3":
        adicionar_produto_carrinho()
    elif opcao == "4":
        visualizar_carrinho()
    elif opcao == "5":
        finalizar_compra()
    elif opcao == "6":
        visualizar_historico_compras()
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Escolha novamente.")

# Salvar os dados em arquivos JSON
with open("produtos.json", "w") as file:
    json.dump(produtos, file)

with open("historico_compras.json", "w") as file:
    json.dump(historico_compras, file)

