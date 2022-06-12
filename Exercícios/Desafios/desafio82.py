nms = []
pa = []
ip = []

while True:

    nms.append(int(input('Digite um número para cadastrar: ')))

    op = input('Quer continuar? [S/N] ').strip()

    while op not in 'nNsS':

        op = input('DIGITE APENAS SIM OU NÃO: ').strip()

    if op in 'nN':

        break

for i in nms:

    if i % 2 == 0:

        pa.append(i)

    else:

        ip.append(i)

nms.sort()
pa.sort()
ip.sort()

print(f'Todos os números cadastrados são estes: \n{nms}\nTodos os números pares são estes: \n{pa}\nE todos os números ímpares são estes: \n{ip}\n')