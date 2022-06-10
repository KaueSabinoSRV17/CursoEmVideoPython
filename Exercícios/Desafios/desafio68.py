from random import randint as rd

ops = ['Par', 'Impar']

v = 0


while True:

    CPU = rd(0, 10)

    P1 = int(input('Tente um número! '))

    rs = P1 + CPU

    op = str(input('Par ou Ímpar? ')).strip().upper()[0]

    if op in 'iIpP':

        if op in 'iI':

            op = ops[1]

        elif op in 'pP':

            op = ops[0]

    else:

        print('Digite apenas Par ou Ímpar!')

    if rs % 2 == 0:

        if op == 'Par':

            print(f'Você ganhou! o resultado foi {rs}, que é um número par!')
            v += 1

        else: 

            print(f'Você perdeu! o resultado foi {rs}, que é um número ímpar!')
            break

    else:

        if op == 'Impar':

            print(f'Você ganhou! o resultado foi {rs}, que é um número ímpar!')
            v += 1

        else:

            print(f'Você perdeu! o resultado foi {rs}, que é um número par')
            break

if v > 1:

    print(f'Fim de Jogo, você ganhou {v} vezes')

else:

    print(f'Fim de Jogo, você ganhou apenas {v} vez')