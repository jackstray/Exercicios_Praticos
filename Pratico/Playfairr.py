# Define o alfabeto usado na cifra Playfair, sem incluir as letras J e K (são tratadas como a mesma letra)
alfabeto = "ABCDEFGHILOMNOPQRSTUVWXYZ"

# Define a função que retorna a matriz de Playfair a partir de uma chave
def gerar_matriz(chave):
    # Remove espaços e letras duplicadas da chave
    chave = re.sub(r"[^a-zA-Z]", "", chave.upper())
    chave = chave.replace("J", "I").replace("K", "I")
    chave = "".join(sorted(set(chave), key=chave.index))

    # Adiciona as letras restantes do alfabeto à chave, ignorando as letras J e K
    alfabeto_sem_jk = alfabeto.replace("J", "").replace("K", "")
    matriz = list(chave)
    for letra in alfabeto_sem_jk:
        if letra not in matriz:
            matriz.append(letra)

    # Transforma a lista em uma matriz 5x5
    matriz = [matriz[i:i+5] for i in range(0, 25, 5)]
    return matriz

# Define a função que divide a mensagem em pares de letras e adiciona uma letra fictícia no final, se necessário
def dividir_mensagem(mensagem):
    mensagem = re.sub(r"[^a-zA-Z]", "", mensagem.upper())
    mensagem = mensagem.replace("J", "I").replace("K", "I")
    pares = re.findall(r"(..)", mensagem)
    if pares[-1] == pares[-2]:
        pares[-1] = pares[-1] + "X"
    elif len(pares[-1]) == 1:
        pares[-1] = pares[-1] + "X"
    return pares

# Define a função que encontra as coordenadas de uma letra na matriz de Playfair
def encontrar_coordenadas(matriz, letra):
    for i, linha in enumerate(matriz):
        for j, coluna in enumerate(linha):
            if coluna == letra:
                return i, j

# Define a função que realiza a cifra de Playfair
def cifrar_playfair(mensagem, chave):
    matriz = gerar_matriz(chave)
    pares = dividir_mensagem(mensagem)
    cifrado = ""
    for par in pares:
        x1, y1 = encontrar_coordenadas(matriz, par[0])
        x2, y2 = encontrar_coordenadas(matriz, par[1])
        if x1 == x2:
            cifrado += matriz[x1][(y1+1)%5] + matriz[x2][(y2+1)%5]
        elif y1 == y2:
            cifrado += matriz[(x1+1)%5][y1] + matriz[(x2+1)%5][y2]
        else:
            cifrado += matriz[x1][y2] + matriz[x2][y1]
    return cifrado

# Exemplo de uso: pede ao usuário uma mensagem e uma chave, e cifra a mensagem usando a cifra de Playfair
mensagem = input("Digite a mensagem a ser cifrada: ")
chave = input("Digite a chave da cifra de Playfair: ")
cifrado = cifrar_playfair(mensagem, chave)
print("Mensagem cifrada: " + cifrado)

