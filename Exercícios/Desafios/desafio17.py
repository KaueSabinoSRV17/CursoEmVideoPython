import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

h = math.hypot(co, ca)

print('\n \n Para resolver este problema precisamos usar o teorema de Pitágoras, que diz que o quadrado do cateto oposto (neste caso {:.2f})  mais o quadrado do cateto adjacente (neste caso {:.2f}) vai dar o quadrado da hipotenusa. Ao tirar a raiz quadrada, chegaremos no valor da hipotenusa (o seu resultado foi {:.2f})'.format(co, ca, h))