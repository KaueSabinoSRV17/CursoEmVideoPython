sxs = ['M', 'F']

hmv = 0

nhmv = ''

md = 0

m_20 = 0

sId = 0

for i in range(0, 4):

    print('{}ª Pessoa'.format(i+1))

    nm = input('Qual o seu nome? ')
    id = int(input('Qual a sua idade? '))
    sx = input('Qual o seu sexo? M/F: ').upper()

    if sx != sxs[0] and sx != sxs[1]:

        print('Sexo Inválido')

        sx = ''

    if sx == sxs[0] and id > hmv:

        hmv = id

        nhmv = nm

    if sx == sxs[1] and id < 20:

        m_20 += 1

    sId += id

md = sId / i
    
print('''

    A média de idade foi {:.2f}

    O homem mais velho foi o {}, com {} anos

    Tivemos {} mulheres menores de 20 anos

'''.format(md, nhmv, hmv, m_20))