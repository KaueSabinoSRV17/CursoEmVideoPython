"""

    Aula 16 - Tuplas

    Toda variável simples é apenas um espaço na memória, ou seja, não podemos armazenar mais de um dado em uma variável simples.

    Inicialmente uma variável que armazena mais de um dado é uma tupla

    Os elementos são identificados por índices dentro da tupla

    EX: tupla[0] - Acesso ao primeiro elemento de uma tupla

    podemos tambem fatiar do início ao fim com [x:y]

    e percorrer facilmente de forma contrária com [-x]

    Uma característica importante: NÃO PODEMOS MANIPULAR E MUDAR UMA TUPLA

    uma única exceção é apagar uma tupla com del

"""

cmd = ('Hambuguer', 'Suco', 'Pizza', 'Pudim')

for i in range (0, len(cmd)):

    print(f'Feito com range: {cmd[i]}')

for c in cmd:

    print(f'Feito sem range {cmd}')

for p, c in enumerate(cmd):

    print(f'Feito com enumarate: {cmd} na posição {p}')

# É possível também somar tuplas!

lts = ('a', 'b', 'c', 'd')

nms = (1, 2, 3)

alfnum = lts + nms

for char in alfnum:

    print(f'\n {char}')