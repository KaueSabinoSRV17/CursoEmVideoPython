vls = []

c = 0

while True:

    n = int(input('Digite um valor para inserir na lista: '))

    if n not in vls:

        vls.append(n)
        c += 1

    else:

        print('Valor já cadastrado')
        c += 1

    op = input('Quer continuar? [S/N] ').strip().upper()

    while op not in 'nNsS':

        op = input('DIGITE APENAS SIM OU NÃO!').strip()

    if op in 'nN':

        break

vls.sort(reverse=True)

if 5 in vls:

    print(f'Foram digitados {c}, cadastrados {len(vls)} números, ordenados inversamente\n{vls}\nO valor 5 está na lista!')

else:

    print(f'Foram digitados {c}, cadastrados {len(vls)} números, ordenados inversamente\n{vls}\nO valor 5 está na NÃO está na lista!')