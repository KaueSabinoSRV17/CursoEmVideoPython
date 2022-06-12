ex = input('Digite uma expressão matemática com parênteses: ')

c1 = c2 = 0

p = []

for s in ex:

    if s == '(':

        p.append('(')

    elif s == ')':

        if len(p) > 0:

            p.pop()

        else:

            p.append(')')

            break

if len(p) == 0:

    print('Expressão válida')

else:

    print('Expressão inválida')