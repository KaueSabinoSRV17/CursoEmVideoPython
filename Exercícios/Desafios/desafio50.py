s = 0
c = 0

for i in range(0, 6):

    n = int(input('Digite um número (faltam {}): '.format(6 - i)))

    if n % 2 == 0:

        c += 1
        s += n

    else: 

        print('\nNúmero impar. Não será considerado na conta\n')

print('A soma dos {} números considerados foi {}'.format(c, s))