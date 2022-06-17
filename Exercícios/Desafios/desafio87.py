ma = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

s_prs = s_3c = m_2l = 0

for l in range(0, 3):
    
    for c in range(0, 3):
        
        ma[l][c] = int(input(f'Escolha o valor da posição [{l}, {c}]: '))
        
print('\n')

for l in range(0, 3):

    for c in range(0, 3):

        if ma[l][c] % 2 == 0:

            s_prs += ma[l][c]
            
for c in range(0, 3):
    
    if ma[1][c] > m_2l:
        
        m_2l = ma[1][c]
            
for l in range(0, 3):
    
    s_3c += ma[l][2]

for i in range(0, 3):
    
    for c in range(0, 3):
        
        print(f'[{ma[i][c]:^5}]', end='')
    
    print()
        
print(f'\nOs a soma de todos os pares foi {s_prs}')
print(f'A soma des números da terceira coluna foi {s_3c}')
print(f'O maior da segunda linha foi o {m_2l}')