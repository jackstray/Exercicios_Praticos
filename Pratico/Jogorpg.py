'''Neste código, é implementado um programa de batalha entre dois jogadores.
Ele importa o módulo random para gerar valores aleatórios. Os jogadores são criados através da função criar_jogador(), onde cada jogador recebe um nome e tem sua vida e ataque gerados aleatoriamente.
A função batalhar() realiza a batalha entre os dois jogadores, reduzindo a vida de cada um até que um deles seja derrotado (vida <= 0). O programa principal cria o Jogador 1, cria o Jogador 2 e inicia a batalha entre eles.
'''

import random

# Função para criar um jogador com nome, vida e ataque aleatórios
def criar_jogador():
    nome = input("Digite o nome do jogador: ")
    vida = random.randint(50, 100)
    ataque = random.randint(5, 15)
    jogador = {"nome": nome, "vida": vida, "ataque": ataque}
    return jogador

# Função para realizar uma batalha entre dois jogadores
def batalhar(jogador1, jogador2):
    print(f"\nBatalha entre {jogador1['nome']} e {jogador2['nome']}!")

    while True:
        # Jogador1 ataca Jogador2
        dano = random.randint(1, jogador1['ataque'])
        jogador2['vida'] -= dano
        print(f"{jogador1['nome']} atacou {jogador2['nome']} causando {dano} pontos de dano.")

        if jogador2['vida'] <= 0:
            print(f"{jogador2['nome']} foi derrotado!")
            break

        # Jogador2 ataca Jogador1
        dano = random.randint(1, jogador2['ataque'])
        jogador1['vida'] -= dano
        print(f"{jogador2['nome']} atacou {jogador1['nome']} causando {dano} pontos de dano.")

        if jogador1['vida'] <= 0:
            print(f"{jogador1['nome']} foi derrotado!")
            break

    print("Batalha encerrada.")

# Criação do Jogador 1
print("Jogador 1:")
jogador1 = criar_jogador()

# Criação do Jogador 2
print("\nJogador 2:")
jogador2 = criar_jogador()

# Início da batalha entre Jogador 1 e Jogador 2
batalhar(jogador1, jogador2)