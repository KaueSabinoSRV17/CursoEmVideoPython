c9 = p3 = np = 0

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

nms = n1, n2, n3 , n4

for i in nms:

    if i == 9:

        c9 += 1

for i in nms:

    if i % 2 == 0:

        np += 1

if 3 in nms:

    p3 = nms.index(3)

    print(f'\nTivemos {c9} números 9\nO primeiro número 3 apareceu na {p3+1}ª posição\nTivemos {np} números pares')

else:

    print(f'\nTivemos {c9} números 9\nNão houve nenhum número 3\nTivemos {np} números pares')