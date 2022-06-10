n = ''
c = 0
s = 0

while n != 999:
    
    n = float(input('Digite quantos números quiser para analisar (999 para parar o programa): '))

    if n != 999:

        c += 1

        s += n
        
print('Você digitou {} números, que resultaram em uma soma de {}'.format(c, s))