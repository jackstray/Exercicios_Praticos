'''
Neste código, é implementado um jogo da velha. A função exibir_tabuleiro() é responsável por exibir o tabuleiro inicial e o estado atual do jogo. A função verificar_vitoria() verifica se o jogador atual venceu o jogo,
analisando todas as combinações possíveis de vitória. A função jogar_jogo_da_velha() inicia e controla o jogo, exibindo o tabuleiro, recebendo as jogadas dos jogadores, verificando a vitória ou empate,
'''

def exibir_tabuleiro(tabuleiro):
    # Exibe o tabuleiro inicial e o estado atual do jogo
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\nTabuleiro atual:")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")

def verificar_vitoria(tabuleiro, jogador):
    # Verifica se o jogador atual venceu o jogo
    comb_vitoria = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    for comb in comb_vitoria:
        if tabuleiro[comb[0]] == tabuleiro[comb[1]] == tabuleiro[comb[2]] == jogador:
            return True
    return False

def jogar_jogo_da_velha():
    # Inicia e controla o jogo da velha
    tabuleiro = [" "] * 9
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)

        posicao = input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")
        if posicao.isdigit() and 1 <= int(posicao) <= 9:
            posicao = int(posicao) - 1
            if tabuleiro[posicao] == " ":
                tabuleiro[posicao] = jogador_atual

                if verificar_vitoria(tabuleiro, jogador_atual):
                    exibir_tabuleiro(tabuleiro)
                    print(f"Jogador {jogador_atual} venceu!")
                    break

                if " " not in tabuleiro:
                    exibir_tabuleiro(tabuleiro)
                    print("Empate!")
                    break

                jogador_atual = "O" if jogador_atual == "X" else "X"
            else:
                print("Posição ocupada. Escolha outra posição.")
        else:
            print("Entrada inválida. Escolha uma posição válida (1-9).")

jogar_jogo_da_velha()
