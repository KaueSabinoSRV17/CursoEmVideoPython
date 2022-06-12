vls = []

while True:

    n = int(input('Digite um valor para cadastrar na lista: '))

    if n not in vls:

        vls.append(n)

    else:

        print('Número já cadastrado')

    op = input('Quer cadastrar mais um número? ').strip().upper()

    while op not in 'nNsS':

        op = input('Digite apenas sim ou não! ').strip().upper()

    if op in 'nN':

        break

vls.sort()

print('Os valores únicos ordenados são estes: ')

for i in vls:

    print(i)