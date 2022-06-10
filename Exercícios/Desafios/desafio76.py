tp = (
    'Lápis',
    1.75,
    'Borracha',
    2.00,
    'Caderno',
    15.90,
    'Estojo',
    25.00,
    'Transferidor',
    4.20,
    'Compasso',
    9.99,
    'Mochila',
    120.32,
    'Canetas',
    22.30,
    'Livro',
    34.90
    )

lh = '-' * 40
tt = 'LISTAGEM DE PREÇO'
md = 'R$'

print(F'''{lh}
{tt:^40}
{lh}''')

for i in tp:

    if i % 2 == 0:
    
        print(f'{i:<.40}')