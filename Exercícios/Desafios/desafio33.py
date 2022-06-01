n1 = int(input('Digite o primeiro número: '))

n2 = int(input('Digite o segundo número: '))

n3 = int(input('Digite o terceiro número: '))

if n1 > n2:

    print('O maior número foi {}'.format(n1))

    if n3 > n1:

        print('O maior número foi {}'.format(n3))

else:

    print('O maior número foi {}'.format(n2))

if n1 < n2:

    print('O menor número foi {}'.format(n1))

    if n3 < n1:

        print ('O menor número foi {}'.format(n3))

else:

    print('O menor número foi {}'.format(n2))