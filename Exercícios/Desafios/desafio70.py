mb = ''
pmb = 0
m1000 = 0
c = 0
t = 0

while True:

    c += 1

    nm = input('Qual o nome do produto? ')
    pr = float(input('Qual o preço do produto? R$'))
    t += pr

    if c == 1:

        pmb = pr

    else:

        if pr < pmb:

            pmb = pr
            mb = nm

    if pr > 1000:

        m1000 += 1

    op = input('Deseja continuar? [S/N]')

    while op not in 'nNsS':

        op = input('Digite apenas sim ou não!')

    if op in 'nN':

        break

print(f'O total gasto foi R${t:.2f}, onde o produto mais barato foi o {mb}, e foram adquiridos {m1000} produtos acima de R$1000,00')