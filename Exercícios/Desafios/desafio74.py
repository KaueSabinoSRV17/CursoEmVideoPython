from random import randint as nal

nms = nal(0, 999),  nal(0, 999),  nal(0, 999),  nal(0, 999)

ord = sorted(nms)

print('A listagem foi a seguinte: \n')

for i in ord:
    print(i)

print(f'\nO maior foi {ord[-1]} e o menor foi o {ord[0]}')