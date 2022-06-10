ct = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'

while True:

    op = int(input('Digite um valor entre 0 e 20 para ser mostrado por extenso: '))

    while op > 20 or op < 0:

        op = int(input(f'DIGITE APENAS UM VALOR ENTRE 0 E 20! '))

    print(f'{op} por extenso é igual a {ct[op]}')

    dlg = input('Deseja continuar? [S/N]: ')

    while dlg not in 'nNsS':

        dlg = input('DIGITE APENAS SIM OU NÃO: ')

    if dlg in 'nN':
        break

print('FIm. Volte sempre!')