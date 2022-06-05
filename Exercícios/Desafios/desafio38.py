# Teste maior, menor e igual

op = ['Primeiro', 'Segundo']

n1 = float(input('Digite o {} número: '.format(op[0].lower())))

n2 = float(input('Digite o {}: '.format(op[1].lower())))

if n1 > n2:

    print('O {} número é maior'.format(op[0]))

elif n2 > n1:

    print('O {} número é maior'.format(op[1]))

else: 

    print('Ambos os números são iguaiis')