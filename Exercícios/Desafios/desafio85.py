prs = []
imp = []
nms = []

for i in range(0, 7):

    n = int(input(f'Digite o {i + 1}º número: '))

    if n not in prs and n not in imp:

        if n % 2 == 0:

            prs.append(n)

        else:

            imp.append(n)

nms.append(prs[:])
nms.append(imp[:])


nms[0].sort()
nms[1].sort()

print(f'Os pares foram {nms[0]}')
print(f'Os ímpares foram {nms[1]}')