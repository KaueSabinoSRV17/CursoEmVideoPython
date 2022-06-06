import datetime

ms = 0

mn = 0

id = 0

atual = datetime.date.today().year

for i in range(0, 7):

    nasc = int(input('Digite o ano de nascimento (faltam {}): '.format(7 - i)))

    id = atual - nasc

    if id >= 18:

        ms += 1

    else:

        mn += 1

print('Temos {} maiores de idade e {} menores de idade'.format(ms, mn))