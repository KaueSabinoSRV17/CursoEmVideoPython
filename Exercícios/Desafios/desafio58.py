import random
import time

n = random.randint(0, 5)

tnt = 1

linha = '-=-' * 20

print(linha)

print('PROCESSANDO.....')

print(linha)

time.sleep(2)

cht = int(input('Chute qual número o computador pensou: '))

print(linha)

while cht != n:

    if cht < n:

        tnt += 1
        cht = int(input('Pensei em algo maior, tente novamente: '))
        print(linha)

    if cht > n:

        tnt += 1
        cht = int(input('Pensei em algo menor, tente novamente: '))
        print(linha)

print('Você acertou! Foram necessárias {} Tentativas!'.format(tnt))