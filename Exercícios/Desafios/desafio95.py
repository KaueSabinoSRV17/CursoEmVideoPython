tm = []
jg = {}
gls = []
lh = '-' * 50
sg = 0

while True:

    jg['Nome'] = input('Qual o nome do jogador?: ')
    partidas = int(input('Quantas partidas ele jogou? '))

    for i in range (0, partidas):

        gls.append(int(input(f'Quantos gols na {i + 1}ª partida?: ')))

        sg += gls[i]

    jg['Gols'] = gls[:]
    jg['Total'] = sg

    tm.append(jg.copy())
    jg.clear

    op = input('Deseja continuar? [S/N]: ')

    if op in 'nN':

        break

print('-' * 40)

for k, v in enumerate(tm):

    print(f'{k:>3}', end='')

    for d in v.values():

        print(f'{str(d):<15}', end='')
    
    print()
    
print('-' * 40)

while True:

    pq = int(input('Digite o número de um jogador para ser detalhado: '))

    if pq > len(tm):

        pq = int(input('DIGITE APENAS UM NÚMERO DENTRO DO LIMITE DO TIME! '))
    
    for k, v in tm[pq]:

        print(f'{k}: {v}')

    op = input('Deseja continuar? ')