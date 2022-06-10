vg = 'a', 'e', 'i', 'o', 'u'

c = 0

pl = (
    'Curso',
    'Gratis',
    'Burguer King',
    'Teste',
    'Python'
)

for p in pl:

    print(f'\nNa palavra {p} temos ' , end='')

    for l in p:

        if l.lower() in 'aeiou':

            print(l)