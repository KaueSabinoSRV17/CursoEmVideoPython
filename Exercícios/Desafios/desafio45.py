# Jokenpo | Pedra Papel Tesoura

import random
import time

op = ['Pedra', 'Papel', 'Tesoura']

rs = ['Temos um empate!', 'O Jogador ganhou!', 'O CPU ganhou!', 'O jogador escolheu uma opção inválida!', 'O CPU escolheu uma opção inválida!']

CPU = random.randint(0, 2)

Player = int(input('Pense em {} (0), {} (1) ou {} (2): '.format(op[0], op[1], op[2])))

linha = '-=-' * 20

time.sleep(.5)

print('JO')

time.sleep(.5)

print('KEN')

time.sleep(.5)

print('PO!')

if CPU == 0:

    if Player == 0:

        i = 0

    elif Player == 1:

        i = 1

    elif Player == 2:

        i = 2

    else:

        i = 3

elif CPU == 1:

    if Player == 0:

        i = 2

    elif Player == 1:

        i = 0

    elif Player == 2:

        i = 2

    else:

        i = 3

elif CPU == 2:

    if Player == 0:

        i = 1

    elif Player == 1:

        i = 2

    elif Player == 2:

        i = 0

    else:

        i = 3

else:

    print(rs[4])

print(linha)

print(rs[i])

print('O Jogador jogou {}\nO CPU jogou {}'.format(op[Player], op[CPU]))

print(linha)