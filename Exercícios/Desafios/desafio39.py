# Alistamento Militar

import datetime

atual = datetime.date.today().year

ano = int(input('Digite o ano do seu nascimento: '))

id = atual - ano

if id < 18:

    print('\n Você ainda irá se alistar')

elif id == 18:

    print('Aliste-se já!')

else:

    print('Você está dispensado!')