p = 's'
n = ''
c = s = md = ma = mn = 0

while p in 'sS':

    n = float(input('DIgite quantos números quiser para analisar (999 para parar o programa): '))

    p = str(input('Você quer continuar [S/N]?').strip()[0])
    
    s += n

    c += 1

    md = s / c

    if c == 1:

        ma = mn = n

    elif n > ma:

        ma = n

    else:

        mn = n
    
print('Você digitou {} números, que resultaram em uma soma de {}, com uma média de {}. o Maior foi {} e o Menor foi {}'.format(c, s, md, ma, mn))