import os

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

menu = '''

    [1] - Soma
    [2] - Subtração
    [3] - Multiplicação
    [4] - Divisão
    [0] - Sair do Programa

'''


op = int(input(menu))

while op != 0:

    if op == 1:

        print('\n {}'.format(n1 + n2))
        op = int(input(menu))

    if op == 2:

        print('\n {}'.format(n1 - n2))
        op = int(input(menu))        

    if op == 3:

        print('\n {}'.format(n1 * n2))
        op = int(input(menu))        

    if op == 4:

        print('\n {}'.format(n1 / n2))
        op = int(input(menu))        
        