
vls = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > vls[-1]:
        vls.append(n)
    else:
        ps = 0
        while ps < len(vls):
            vls.insert(ps, n)
            break
        ps += 1
print(vls)