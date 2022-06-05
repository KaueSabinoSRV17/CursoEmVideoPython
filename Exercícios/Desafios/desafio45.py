# Jokenpo | Pedra Papel Tesoura

import random

op = ['Pedra', 'Papel', 'Tesoura']

CPU = random.randint(0, 2)

Player = int(input('Digite 0 para {}\n1 para {}\n2 para {}\n'.format(op[0], op[1], op[3])))

if CPU == Player:

    print('{} x {}\nEmpate!'.format(op[Player], op[CPU]))

elif CPU == 0 and Player == 1:

    print('{} X {}\nVitória do CPU!'.format(op[Player], op[CPU]))

elif CPU == 1 and Player == 2:

    print('{} X {}\nVitória do Player!'.format(op[Player], op[CPU]))