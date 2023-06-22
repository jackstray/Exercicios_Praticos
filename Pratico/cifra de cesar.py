def cesar(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'  # MODELO BR DE ALFABETO
    new_data = ''  # variável que vai receber o texto criptado ou descriptado
    for c in data:  # percorretodo o texto recebido[
        index = alphabet.find(c)  # recebe o index da letra
        if index == -1:
            new_data += c  # caractere não reconhecido,permanece do jeito que está e passa ao próximo
        else:
            new_index = index + key if mode == 1 else index - key  # trata o caractere de acordo com o modo escolhido#
            new_index = new_index % len(alphabet)  # garante que esse valor está dentro do intervalo
            new_data += alphabet[
                        new_index:new_index + 1]  # adiciona o novo caractere,que está na posição calculada,para a variavel

    return new_data


def error(code):  # tratamento de erros
    if code == 1:
        print("Chave inválida")
    else:
        print("Modo inválido")

    r = input("Tentar novamente? S ou N\n")
    if r.lower() == "s":
        main()
    elif r.lower() == "n":
        print("Certo serviço encerrado")
    else:
        print('Mal uso do sistema, programa encerrado')


def main():  # Main
    key = int(input("Qual a chave de encriptação?\n"))
    if key > 26 or key < 0:
        error(1)
    else:
        modo = input('Digite D para decriptar ou E para encriptar uma mensagem: ')
        if modo.lower() == "d":
            modo = 0
            msg = input('Digite a mensagem a ser quebrada:')
            d = cesar(data=msg, key=key, mode=modo)
            print("\n")
            print(f'A mensagem é:{d}')

        elif modo.lower() == "e":
            modo = 1
            msg = input('Digite a mensagem a ser criptada:')
            d = cesar(data=msg, key=key, mode=modo)
            print("\n")
            print(f"A mensagem criptada fica: {d}")
        else:
            error(2)


if __name__ == "__main__":
    main()
