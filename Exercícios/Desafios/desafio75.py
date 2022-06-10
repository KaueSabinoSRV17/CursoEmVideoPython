c9 = p3 = np = 0

nms = int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: '))

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

    print(f'\nTivemos {c9} números 9\nNão houve nenhum número 3\nOs números pares digitados foram: ', end='')

    for n in nms:
    
        if n % 2 == 0:

            print(f'{n}', end=' ')