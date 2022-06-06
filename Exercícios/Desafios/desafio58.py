import random
import time

n = random.randint(0, 5)

linha = '-=-' * 20

c = 0

print(linha)

print('PROCESSANDO.....')

print(linha)

time.sleep(2)

cht = int(input('Chute qual número o computador pensou: '))

print(linha)

while cht != n:

    if cht == n:

        print('Parabéns, você acertou!')

    else:

        n - random.randint(0, 5)

        c += 1

        print('Você errou! Pensei em {} não em {}'.format(n, cht))

        cht = int(input('Tente mais uma vez: '))

print(linha)