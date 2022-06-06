# Peso de 5 pessoas

ma = 0

mn = 0

for i in range(0, 5):

    ps = float(input('Digite um peso em Kg (faltam {}): '.format(5 - i)))

    if ps > ma:

        ma = ps

    else:

        mn = ps

print('O maior peso foi {:.2f}Kg e o menor foi {:.2f}Kg'.format(ma, mn))
