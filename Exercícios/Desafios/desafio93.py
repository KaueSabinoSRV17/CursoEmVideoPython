jg = {}
gls = []
lh = '-' * 50
sg = 0

jg['Nome'] = input('Qual o nome do jogador?: ')
partidas = int(input('Quantas partidas ele jogou? '))

for i in range (0, partidas):

    gls.append(int(input(f'Quantos gols na {i + 1}ª partida?: ')))

    sg += gls[i]

jg['Gols'] = gls[:]
jg['Total'] = sg

print(lh)
print(jg)
print(lh)

for k, v in jg.items():

    print(f'{k}: {v}')

print(lh)

print(f'O jogador {jg["Nome"]} fez {jg["Total"]} Gols')

for i in range(0, len(jg['Gols'])):

    print(f'Fez {jg["Gols"][i]} gols na {i + 1}ª partida')