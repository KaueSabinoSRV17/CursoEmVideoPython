n = int(input('Digite o número da tabuada desejada: '))

for i in range(0, 11):

    print('{} X {:2} = {}'.format(n, i, n * i))