a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

mn = a

if b < a and b < c:

    mn = b

if c < a and c < b:

    mn = c

print('O menor valor foi {}'.format(mn))

ma = a

if b > a and b > c:

    ma = b

if c > a and c > b:

    ma = c

print('O maior valor foi {}'.format(ma))