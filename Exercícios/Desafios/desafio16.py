import math

n = float(input('Digite um número decimal: '))


# A resolução apropriada é trunc no lugar de floor, mas o resultado foi o mesmo
nf = math.floor(n)

print('O número, sem suas casas decimais é {:.0f}'.format(nf))