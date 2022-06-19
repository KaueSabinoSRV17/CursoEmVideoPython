def avg(a, b):

    return a / b

ps = []
ds = {}
ids = []

while True:

    ds['Nome'] = input('Nome: ')
    ds['Idade'] = int(input('Idade: '))

    while ds['Idade'] < 0 or ds['Idade'] > 100:

        ds['Idade'] = int(input('DIGITE UMA IDADE VÁLIDA: '))

    ds['Sexo'] = input('Sexo [M/F]: ').upper()[0]

    while ds['Sexo'] not in 'fFmM':

        ds['Sexo'] = input('DIGITE APENAS M OU F: ').upper()[0]

    ids.append(ds['Idade'])

    ps.append(ds.copy())
    ds.clear()

    op = input('Deseja continuar? [S/N]: ')

    if op in 'nN':

        break

if len(ps) == 1:

    md = 0

else:

    md = avg(sum(ids), len(ids))

print(f'\n{"Estatísticas":^20}')

print(f'Foram cadastradas {len(ps)} pessoas')
print(f'A média de idade foi {md}')

print(f'\n{"Lista de Mulheres":^20}')

for p in ps:

    if p['Sexo'] in 'fF':

        print()

        for k, v in p.items():

            print(f'{k}: {v}')
            
            
print(f'\n{"Lista de Idades Acima da Média":^20}')

if p['Idade'] > md:

    print()

    for k, v in p.items():

        print(f'{k}: {v}')