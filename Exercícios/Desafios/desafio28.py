import random

n = random.randint(0, 5)

cht = int(input('Chute qual número o computador pensou: '))

if cht == n:

    print('Parabéns, você acertou!')

else:

    print('Você errou!')