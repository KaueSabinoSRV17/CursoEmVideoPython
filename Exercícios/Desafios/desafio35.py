r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

possivel = r3 > r1 - r2 and r3 < r1 + r2

if possivel:

    print('Podemos fazer um triângulo!')

else: 

    print('Não é possível fazer um triângulo')