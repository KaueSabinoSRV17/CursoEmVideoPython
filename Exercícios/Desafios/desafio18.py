import math

ang = float(input('Digite o valor de um ângulo: '))

rad = math.radians(ang)

linha = '=' * 30

s = math.sin(rad)
c = math.cos(rad)
t = math.tan(rad)

print(linha)
print('Você digitou o ângulo {:.2f}º.'.format(ang))
print(linha)
print('O valor do seno é {:.2f}º'.format(s))
print(linha)
print('O valor do cosseno é {:.2f}º'.format(c))
print(linha)
print('E por último, o valor da tangente é {:.2f}º'.format(t))