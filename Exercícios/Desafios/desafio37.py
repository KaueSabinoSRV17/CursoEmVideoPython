import math

op = ['Decimal', 'Binário', 'Octal', 'Hexadecimal']

esc = int(input('Digite 1 para converter {}, 2 para {} e 3 para {}: '.format(op[1], op[2], op[3])))

vld = esc < 4

if vld:

    n = int(input('Digite o número que será convertido: '))

    if esc == 1:

        print(bin(n))

    elif esc == 2:

        print(oct(n))

    elif esc == 3:
        
        print(hex(n))

else: 

    print('Opção inválida')