ano = int(input('Digite o ano a ser verificado: '))

divid4 = ano % 4 == 0

divid100 = ano % 100 == 0

divid400 = ano % 400 == 0

if divid4 == True and divid100 == True and divid400 == True:

    print('É um ano bissexto')

else: print('Não é Bissexto')