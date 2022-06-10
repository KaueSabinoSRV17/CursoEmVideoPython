bs = 'Palmeiras', 'Corinthians', 'Athetico-PR', 'Atlético-MG', 'Coritiba', 'São Paulo', 'Internacional', 'Fluminense', 'América-MG', 'Santos', 'Bragantino', 'Ceará SC', 'Goiás', 'Flamengo', 'Botafogo', 'Avaí', 'Cuiabá', 'Atlético-GO', 'Juventude', 'Fortaleza'

print('Os primeiros 5 colocados foram: \n')

for i in range(0, 5):
    
    print (bs[i])

print('\nOs 4 últimos colocados foram: \n')

for i in range(19, 15, -1):
    
    print(bs[i])

print(f'\nOs times em ordem alfabética são: {sorted(bs)}')

if 'Chapecoense' not in bs:

    print('A Chapecoense não está no top 20 do Brasileirâo!')

else:

    print(f'A Chapecoense está na posição {bs.index("Chapecoense")}')