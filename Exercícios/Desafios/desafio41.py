# Categorias de Natação

import datetime

atual = datetime.date.today().year

nasc = int(input('Digite o ano de nascimento do atleta: '))

id = atual - nasc

ct = ['Mirim', 'Infantil', 'Junior', 'Senior', 'Master']

if id <= 9:

    print('O atleta estará na categoria {}'.format(ct[0]))

elif id <= 14:

    print('O atleta estará na categoria {}'.format(ct[1]))

elif id <= 19:

    print('O atleta estará na categoria {}'.format(ct[2]))

elif id == 20:

    print('O atleta estará na categoria {}'.format(ct[3]))

else: 

    print('O atleta estará na categoria {}'.format(ct[4]))