# Fatorial com repetição While


n = int(input('Resultado com while: '))

r = n - 1

while r > 0:

    n = n * r

    print('{}'.format(r), end=' x ')
    r -= 1

print(n)

n = int(input('Resultado com for: '))

print(n, end='')

for i in range(n - 1, 1, -1):

    n *= i

    print(' x {}'.format(i), end='')

print(' = {}'.format(n))