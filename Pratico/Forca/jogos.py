import forca
import adivinhacao
def jogar():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Adivinhação (2) Forca")

    jogo = int(input("Qual jogo? "))

    if (jogo == 2):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 1):
        print("Jogando adivinhação")
        adivinhacao.jogar()
if(__name__ == "__main__"):
    jogar()