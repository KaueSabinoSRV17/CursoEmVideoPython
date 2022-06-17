ma = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    
    for c in range(0, 3):

        ma[l][c] = int(input(f'Escolha o valor da posição [{l}, {c}]: '))
        
print('\n')

for i in range(0, 3):

    for c in range(0, 3):
    
        print(f'[{ma[i][c]:^6}]', end='')
    
    print()