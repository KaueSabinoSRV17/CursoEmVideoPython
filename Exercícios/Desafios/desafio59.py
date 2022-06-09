import os

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
linha = '-==-' * 20

menu = '''

    [1] - Soma
    [2] - Subtração
    [3] - Multiplicação
    [4] - Divisão
    [5] - Maior
    [6] - Novos Números
    [0] - Sair do Programa

'''


op = int(input('''

{}

{}

{}

'''.format(linha, menu, linha)))

while op != 0:

    if op == 1:

        print('\n {}'.format(n1 + n2))
        op = int(input(menu))

    elif op == 2:

        print('\n {}'.format(n1 - n2))
        op = int(input(menu))        

    elif op == 3:

        print('\n {}'.format(n1 * n2))
        op = int(input(menu))        

    elif op == 4:

        print('\n {}'.format(n1 / n2))
        op = int(input(menu))

    elif op == 5:

        if n1 > n2:

            mr = n1

        if n1 < n2:

            mr = n2

        print('O maior foi {}'.format(mr))        

        op = int(input(menu))

    elif op == 6:

        print('Informe novos números novamente: ')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))

        op = int(input(menu))
    
    else:

        print('Opção Inválida! Digite entre uma das opções descritas no menu')
        op = int(input(menu))

print('Fim')
