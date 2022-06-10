from random import randint as nal

n1 = nal(0, 9999)
n2 = nal(0, 9999)
n3 = nal(0, 9999)
n4 = nal(0, 9999)
n5 = nal(0, 9999)

nms = n1, n2, n3, n4, n5

ord = sorted(nms)

print('A listagem foi a seguinte: \n')

for i in ord:
    print(i)

print(f'\nO maior foi {ord[-1]} e o menor foi o {ord[0]}')