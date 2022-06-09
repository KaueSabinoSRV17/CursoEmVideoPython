# Fatorial com repetição While


n = int(input('Digite o número que iremos usar na fatorial: '))

r = 0

while n != 1:

    r = n * n

    n = n - 1

print(r)