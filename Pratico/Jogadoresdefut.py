'''Neste código, os dados dos jogadores são coletados, armazenados e exibidos.
A cada iteração do loop, um jogador é adicionado à lista de jogadores com seu nome, quantidade de partidas jogadas,
número de gols em cada partida e total de gols. Após a entrada dos dados,
é solicitada a continuação do programa. Após a coleta de todos os jogadores,
os dados são exibidos em forma de tabela. Em seguida, é possível fazer consultas individuais dos jogadores e exibir os detalhes dos gols em cada partida.'''


jogador = {} # Dicionário vazio para armazenar os dados do jogador atual
gol = [] # Lista vazia para armazenar o número de gols em cada partida
jogadores = [] # Lista para armazenar os dados de todos os jogadores
while True:
    jogador['nome'] = str(input('Nome do jogador:'))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou:'))
    gol.clear()
    for j in range(0, partidas):
        a = int(input(f'Quantos gols na partidas {j+1}: '))
        gol.append(a)
        jogador['gols'] = gol[:]
        jogador['total'] = sum(gol)
    jogadores.append(jogador.copy())
    while True:
        r = str(input('Voce quer continuar:[S/N]:')).upper()[0]
        if r in 'SN':
            break
        print('Erro!responda apenas s ou n.')
    if r == 'N':
        break
print(jogadores)
print('-=' * 30)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'* 40)
for k,v in enumerate(jogadores):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)
while True:
    busca=int(input('Mostrar dados de qual jogador: (999 para parar):'))
    if busca == 999:
        break
    if busca>= len(jogadores):
        print(f'Erro!Não existe jogador com código {busca}!')
    else:
        print(f'-- Levantamento do jogador {jogadores[busca]["nome"]}:')
        for i,g in enumerate(jogadores[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols. ')
    print('-'*40)
print('<<Volte sempre>>')