als = []
al = []
lh = '-' * 42

def md(a, b):

    return a / b

while True:

    nm = input('Nome: ')
    
    n1 = int(input('Nota 1: '))

    while n1 > 10 or n1 < 0:

        n1 = int(input('DIGITE APENAS NÚMEROS ENTRE 0 E 10: '))

    n2 = int(input('Nota 2: '))

    while n2 > 10 or n2 < 0:

        n2 = int(input('DIGITE APENAS NÚMEROS ENTRE 0 E 10: '))

    al.append(nm)
    al.append(n1)
    al.append(n2)

    als.append(al[:])
    al.clear()

    op = input('Deseja continuar? ')

    while op not in 'nNsS':

        op = input('DIGITE APENAS SIM OU NÃO: ')

    if op in 'nN':

        break


print(lh)
print('No. |', ' Nome |', ' Média |')
print(lh)

for i, v in enumerate(als):
    
    print(f'{i + 1:<3} |', f' {v[0]:^3} |', f' {md(v[1] + v[2], 2):>4}  |')

print(lh)

while True:

    pq = int(input('Digite o número do aluno para notas detalhadas: '))
    print(lh)

    while pq < 0 or pq > len(als):

        pq = int(input('DIGITE APENAS NÚMEROS QUE ESTEJAM NA TABELA: '))
        print(lh)

    print(f'As notas do {als[pq - 1][0]} foi foram: {als[pq - 1][1]} e {als[pq - 1][2]}')

    print(lh)

    op = input('Deseja continuar? ')
    print(lh)

    while op not in 'nNsS':

        op = input('DIGITE APENAS SIM OU NAO: ')
        print(lh)

    if op in 'nN':

        break

print('FIM DE PROGRAMA')