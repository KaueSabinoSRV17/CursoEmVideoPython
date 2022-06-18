from time import sleep

def cont(i, f, p):

    print(f'Contando de {i} até {f} indo de {p} em {p}: ')

    if p < 0:

        p *= -1

    if p == 0:

        p = 1

    if i < f:

        c = i
        while c <= f:

            print(c, end=' ', flush=True) 
            c += p

    else:

        c = i
        while c >= f:

            print(c, end=' ', flush=True) 
            c -= p


    print('FIM')


cont(1, 10, 1)
cont(10, 0, 2)

i = int(input('Sua vez. Digite o início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

cont(i, f, p)