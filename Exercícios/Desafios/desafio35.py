r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))

possivel = r3 > r1 - r2 and r3 < r1 + r2

if possivel:

    print('Podemos fazer um triângulo!')

else: 

    print('Não é possível fazer um triângulo')