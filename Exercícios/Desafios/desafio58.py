import random
import time

n = random.randint(0, 5)

tnt = 3

linha = '-=-' * 20

print(linha)

print('PROCESSANDO.....')

print(linha)

time.sleep(2)

cht = int(input('Chute qual número o computador pensou: '))

print(linha)

while tnt > 0:

    if cht == n:

        print('Parabéns, você acertou!')

        tnt = 0

    else:

        tnt -= 1
        print('Você errou! Restam {} tentativas'.format(tnt))

        cht = int(input('Tente novamente: '))

    print(linha)

