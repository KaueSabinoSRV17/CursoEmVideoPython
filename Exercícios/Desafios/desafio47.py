s = 0

for i in range(0, 501):

    if i % 3 == 0 and i % 2 == 1:

        s += i

print('A soma de todos os número ímpares divisíveis por 3 entre 0 e 500 é {}'.format(s))