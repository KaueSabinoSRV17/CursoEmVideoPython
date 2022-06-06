# Números primos

c = 0

n = int(input('Digite um número: '))

for i in range(n, 0, -1):

    if n % i == 0:

        c += 1

if c > 2:

    print('O número não é Primo!')

else:

    print('O número é Primo!')
