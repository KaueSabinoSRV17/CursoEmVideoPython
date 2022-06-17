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

from cgi import test


cmd = ('Hambuguer', 'Suco', 'Pizza', 'Pudim')

for i in range (0, len(cmd)):

    print(f'Feito com range: {cmd[i]}')

for c in cmd:

    print(f'Feito sem range {cmd}')

for p, c in enumerate(cmd):

    print(f'Feito com enumarate: {cmd} na posição {p}. O enumerate é usado para podermos trabalhar tanto com a posição quanto com a lista em si')

# É possível também somar tuplas!

lts = ('a', 'b', 'c', 'd')

nms = (1, 2, 3)

alfnum = lts + nms

for char in alfnum:

    print(f'{char}', end=' ')

print(f'\nPodemos acessar os valores de forma contrária: \n{cmd[-1]}\n e também combinando fatiamento: \n{cmd[-2:]}\n no caso acima, foi acessado a partir do segundo valor da direita para a esquerda até o final')

print(f'Podemos também procurar um valor na tupla e descobrir em qual posição ele aparece pela primeira vez: {cmd.index("Suco")}\nFoi o valor acima é a posição em que Suco aparece pela primeira vez nesta tupla')


"""

    Aula 17 - Listas

    Tuplas não podem ser mudadas em tempo de execução. Para isso, vamos usar Listas

    Para adicionar ao final de uma lista, usamos o comando .append(NovoValor)

    Para adicionar sem ser no final da lista, usamos insert(posição desejada, valor desejado)

    Podemos mudar um valor atirbuindo um novo valor como uma variável

    Para apagar, podemos dar um .pop() para apagar sempre o último elemento, del lista[posião] ou lista.remove('Valor a ser excluido')

    Para declarar uma lista rápidamente podemos usar fazer assim: lista = list(range(inicio, fim))

    Podemos ordenar de forma padrão ou inversa com sort() ou sort(reverse = True)

"""

dcm = [4, 5, 1, 6, 7, 9, 3, 2,]

dcm.append(0)

print(f'A lista sem ordem, com o valor zero adicionado após a declaração: ')

for i in dcm:

    print(i)

dcm.sort()

print(f'A lista ordenada de forma convencional: ')

for i in dcm:

    print(i)

print(f'A lista ordenada de forma reversa, sem o zero: ')

dcm.remove(0)

dcm.sort(reverse=True)

for i in dcm:

    print(i)

"""

    Aula 17 - Listas dentro de listas

    Podemosw colocar listas dentro de listas. Para acessar um valor dentro de uma lista dentro de outra, usamos dois índices listaMaior[listaMenor][valor]

"""

teste = []

teste.append('Kauê')

teste.append(19)

pessoas = []

pessoas.append(teste)

teste[0] = 'Maria'

teste[1] = 38

pessoas.append(teste[:])

print(pessoas)

"""

    Aula 19 = Dicionários

    Dicionários são listas com índices literais

    podem ser declarados com {}

    exemplo:

    {
        'índice' = valor
    }

    devemos printar os valores escrevendo os índices com ''

    podemos adicionar elementos automaticamante assim: dicionario['novoElemento'] = valor

    podemos deletar um elemneto usando del dicionario['elemento']

    em laços, podemos acessar as keys(), items() e values()

"""


filmes = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

print(f'\nEstes são os valores dos filmes \n{filmes.values()}')

print(f'\nAs keys são estas \n{filmes.keys()}')

print(f'\n\nEstes são todos os items \n{filmes.items()}')

print(f'\nO nome do filme é {filmes["titulo"]}, o ano de lançamento é {filmes["ano"]} e o diretor é {filmes["diretor"]}')

print(f'\nVamos agora usar um for para exibir tudo na tela: \n')

for k, v in filmes.items():

    print(f'{k}: {v}')

filmes['avaliação'] = 5.0

print(f'Adicionei um elemento de avaliação, sem usar append. ele está apresentado aqui \n\nNota do filme: {filmes["avaliação"]}')