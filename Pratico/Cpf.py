'''Este código verifica a validade de um número de cartão de crédito  e exibe se o cartão é válido ou inválido.
'''
# Solicita ao usuário os 16 dígitos do cartão
digitosCartao = input("Digite os 16 dígitos do seu cartão: ")

multiplicador = 2
DV = "0"
soma = 0

# Percorre cada dígito do número do cartão, exceto o último
for i in digitosCartao[:-1]:
    # Multiplica o dígito pelo multiplicador (começa com 2)
    aux = int(i) * multiplicador

    # Se o resultado da multiplicação for maior que 9, subtrai 9
    if aux > 9:
        aux -= 9

    # Adiciona o resultado à soma total
    soma += aux

    # Alterna entre os multiplicadores 1 e 2
    if multiplicador == 2:
        multiplicador = 1
    else:
        multiplicador = 2

# Calcula o dígito verificador (DV)
if soma % 10 > 0:
    DV = str(10 - soma % 10)

# Verifica se o DV corresponde ao último dígito do número do cartão
if DV == digitosCartao[-1:]:
    print(f'O cartão {digitosCartao} é válido.')
else:
    print(f"O cartão {digitosCartao} é inválido. O correto seria {digitosCartao[:-1] + DV}")
