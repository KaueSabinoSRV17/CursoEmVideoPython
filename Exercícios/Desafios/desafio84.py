ds = []
ps = []
mai = men = 0

while True:
    ds.append(input('Nome: '))
    ds.append(float(input('Peso: ')))
    if len(ps) == 0:
        mai = men = ds[1]
    else:
        if ds[1] > mai:
            mai = ds[1]
        if ds[1] < men:
            men = ds[1]
    ps.append(ds[:])
    ds.clear()
    op = input('Continue? [S/N] ')
    if op in 'nN':
        break
print(f'\nO total de pessoas cadastradas foi {len(ps)}')
print(f'\nAs pessoas mais pesadas foram: ')
for p in ps:
    if p[1] == mai:
        print(p[0])
print('\nAs pessoas mais leves foram: ')
for p in ps:
    if p[1] == men:
        print(p[0])