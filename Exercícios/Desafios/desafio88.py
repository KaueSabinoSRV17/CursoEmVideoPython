from random import randint as rd
from time import sleep

jgs = []
jg = []
lh = '-=' * 20
tt = 'MEGA SENA'
c = 0

print(lh)
print(f'{tt:^40}')
print(lh)

op = int(input('Quantos jogos vamos tirar? '))

for i in range(0, op):

    c = 0

    while c <= 6:

        n = rd(0, 60)

        if n not in jg:

            jg.append(rd(0, 60))

            c += 1
        

    jgs.append(jg[:])

    jg.clear()

for j in jgs:

    j.sort()

for i, j in enumerate(jgs):

    sleep(1)
    print(f'Jogo {i}: {j}')