fb = [0, 1]

t = int(input('Digite quantos termos teremos na sequência: '))

nv = 0

ul = 0

pn = 0

if t <= 2:
    
        print('{} -> {}'.format(fb[0], fb[1]))

else:

    for i in range(0, t):
        
        ul = fb[len(fb) - 1]
        pn = fb[len(fb) - 2]

        nv = ul + pn
        fb.append(nv)
        print(fb[i], end='')

    