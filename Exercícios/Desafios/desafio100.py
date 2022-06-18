from random import randint as rd
from time import sleep

def sorteia():

    for i in range(0, 5):

        n = rd(10, 100)
        st.append(n)
    
    print('Sorteando 5 números: ', end=' ')

    for v in st:

        sleep(.5)
        print(v, end=' ', flush=True)    
        nms.append(v)

    print()

    for v in nms:

        print(v, end=' ')

def somaPar(v):

    s = 0

    for n in v:

        if n % 2 == 0:

            s += n


    print(f' A soma dos números sorteados pares foi {s}')


nms = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = []

sorteia()
somaPar(st)