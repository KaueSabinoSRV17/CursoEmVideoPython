# Fatorial com repetição While


n = int(input('Digite o número que iremos usar na fatorial: '))

r = n

while r > 0:

    n = n * r

    print('{}'.format(r), end=' x ')
    r -= 1

print(n)