from datetime import datetime as dt

tb = {}
ano = dt.now().year

tb['Nome'] = input('Nome: ')
tb['Nascimento'] = int(input('Ano de nascimento: '))
tb['Idade'] = ano - tb['Nascimento']
tb['Carteira'] = int(input('Nº da Carteira: '))

print()

if tb['Carteira'] != 0:
    
    tb['Contratação'] = int(input('Ano de contratação: '))
    tb['Salario'] = float(input('Salário: R$'))
    tb['Aposentadoria'] = tb['Idade'] + ((tb['Contratação'] + 35) - ano)

    for k, v in tb.items():

        print(f'{k}: {v}')

else:

    print(tb)