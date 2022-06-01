from cgi import print_arguments
import random
import time

n = random.randint(0, 5)

linha = '-=-' * 20

print(linha)

print('PROCESSANDO.....')

print(linha)

time.sleep(2)

cht = int(input('Chute qual número o computador pensou: '))

print(linha)

if cht == n:

    print('Parabéns, você acertou!')

else:

    print('Você errou! Pensei em {} não em {}'.format(n, cht))

print(linha)