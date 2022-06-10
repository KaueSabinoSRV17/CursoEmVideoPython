"""
    For

    Devemos usar repetições para todo código que vai se repetir por muito tempo. em todas as situações, devemos evitar a repetição de código

    Segundo a necessidade, podemos combinar repetições e condições, de todas as formas que acharmos melhor.

"""

for c in range(0, 11):

    print(c)

print('FIM - Feito em For')

# Neste código, por exemplo, podemos repetir a exibição de diversos números


"""

    Aula 12 - While

    Devemos usar while quando não sabemos o limite das repetições

"""

i = 0

while i < 10:

    i += 1

    print(i)

print('Fim - Usando o While')

"""

    Aula 15 - Comando break

    podemos interromper toda a execução do laço antes de sua condição se tornar verdade, através de um break

"""

while True:

    p = input('Denovo? [S/N]')

    if p in 'nN':
        break