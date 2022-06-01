n = int(input('Digite um número inteiro entre 0 e 9999: '))

m = n // 1000 % 10

c = n // 100 % 10

d = n // 10 % 10

u = n % 10

print('Unidade: {} \nDezena: {}\n Centena: {}\n Milhar: {}'.format(u, d, c, m))