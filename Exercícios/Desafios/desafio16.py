import math

n = float(input('Digite um número decimal: '))

nf = math.floor(n)

print('O número, sem suas casas decimais é {:.0f}'.format(nf))