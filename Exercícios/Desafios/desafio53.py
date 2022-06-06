frs = input('Digite uma frase: ').strip()

pl = frs.split()

jn = ''.join(pl)

c = -1

inv = ''

for i in range(len(jn) - 1, -1, -1):

    inv += jn[i]

print(jn, inv)

if jn == inv:

    print('Esta frase é um palíndromo!')

else:

    print('Esta frase não é um palíndromo!')