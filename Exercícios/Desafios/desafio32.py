import datetime

ano = int(input('Digite o ano a ser verificado (Digite 0 para verificar o ano atual): '))

if ano == 0:

    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

    print('É um ano bissexto')

else: 
    
    print('Não é Bissexto')