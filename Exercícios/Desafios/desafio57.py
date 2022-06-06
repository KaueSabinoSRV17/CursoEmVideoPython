# Leitor de sexo

sx = input('Digite seu sexo [M/F]: ').upper()

while sx != 'M' and sx != 'F':

    print('Valor inválido, tente novamente!')

    sx = input('Digite seu sexo [M/F]: ').upper()

print('Valor correto!')