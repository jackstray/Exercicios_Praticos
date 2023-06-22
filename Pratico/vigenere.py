def cifra_de_vigenere(mensagem, chave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    cifra = ''
    chave_completa = ''
    cont = 0
    for letra in mensagem:
        if letra in alfabeto:
            chave_completa += chave[cont % len(chave)]
            cont += 1
        else:
            chave_completa += letra
    for i in range(len(mensagem)):
        if mensagem[i] in alfabeto:
            soma = alfabeto.index(mensagem[i]) + alfabeto.index(chave_completa[i])
            cifra += alfabeto[soma % 26]
        else:
            cifra += mensagem[i]
    return cifra

mensagem = 'deus'
chave = 'segredo'

cifra = cifra_de_vigenere(mensagem, chave)

print(cifra)