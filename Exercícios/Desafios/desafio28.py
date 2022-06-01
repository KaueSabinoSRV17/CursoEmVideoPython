import random

n = random.randint(0, 10)

cht = int(input('Chute qual número o computador pensou: '))

if cht == n:

    print('Parabéns, você acertou!')

else:

    print('Você errou!')