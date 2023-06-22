import random

def jogar():
    print ("Bem vindo ao jogo de adivinhação")

    numero_secreto = random.randrange(1, 101)
    total = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total=20
    elif(nivel == 2):
        total=10
    else:
        total=5

    for cont in range (1,total + 1):
        print ("Tentativa {} de {}".format(cont, total))
        chute_str = input ("Digite um número entre 1 e 100: ")
        chute = int(chute_str)
        if chute < 1 or chute > 100 :
            print("Você deve digitar um número entre 1 e 100")
            continue
        acertou = numero_secreto == chute
        maior = numero_secreto < chute
        menor = numero_secreto > chute
        if acertou :
            print("Você acertou!")
            break
        else:
            if maior:
                print("Você errou, chutou para cima")
            elif menor:
                print("Você errou, chutou para baixo")
            perdidos = abs(numero_secreto - chute)
            pontos = pontos - perdidos
    print(f"O número secreto era {numero_secreto}")
    print(f"Você fez {pontos} pontos")
    print("Fim do jogo")
    
if(__name__ == "__main__"):
    jogar()
