from random import randint as rd
from operator import itemgetter as get
from time import sleep

def dad():
    return rd(1, 6)

jogo = {
    'João': dad(),
    'Pedro': dad(),
    'Kaue': dad(),
    'Gália': dad()
}

rk = []

for k, v in jogo.items():

    sleep(.5)
    print(f'O Jogador {k} tirou {v} no dado')

rk = sorted(jogo.items(), key=get(1), reverse=True)

print('\n')

for i, v in enumerate(rk):

    sleep(.5)
    print(f'O {i}º lugar vai para: {v[0]}, que tirou {v[1]}')