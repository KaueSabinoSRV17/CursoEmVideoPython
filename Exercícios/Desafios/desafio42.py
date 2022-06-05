# Triângulos possíveis com tipos

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

possivel = r3 > r1 - r2 and r3 < r1 + r2

if possivel:

    print('Podemos fazer um triângulo!')

    if r1 == r2 and r1 == r3:

        print('O triângulo será Equilátero!')

    elif r1 == r2 or r1 == r3 or r2 == r3:

        print('O triângulo será Isósceles!')

    else: 

        print('O triângulo será Escaleno!')

else: 

    print('Não é possível fazer um triângulo')