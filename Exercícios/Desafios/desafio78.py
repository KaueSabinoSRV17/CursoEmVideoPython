vls = []

for i in range(0, 4):

    vls.append(int(input('Digite um valor para ser armazenado na lista: ')))

ma = max(vls)
mn = min(vls)

print(f'O maior valor foi {ma}\nO menor valor foi {mn}')

for i, v in enumerate(vls):

    if v == ma:

        print(f'O maior valor estava na {i}ª posição')

    if v == mn:

        print(f'O menor valor estava na {i}ª posição')