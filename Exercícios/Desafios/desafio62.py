n = float(input('Digite o primeiro termo da P.A: '))
p = int(input('Digite a razão desejada: '))
c = 0
t = 1

print(n, end=' -> ')

while t != 0:

    while c < 9:
    
        n += p
        
        c += 1
        
        if c != 9:

            print(n, end=' -> ')
        
        else: 

            print(n, end='')

    t = int(input('\nQuantos termos a mais vamos mostrar? '))

    for i in range(0, t):

        n += p
        c += 1

        if i != t - 1:

            print(n, end=' -> ')

        else:

            print(n, end='')

print('A PA foi demonstrada em {} termos'.format(c+1))