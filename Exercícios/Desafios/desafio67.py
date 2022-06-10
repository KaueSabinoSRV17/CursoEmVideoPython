while True:
    
    n = int(input('Escolha a tabuada: '))
    
    print('-' * 20)

    if n < 0:

        break

    else:
    
        for i in range(0, 10):

            print(f'{n} x {i:2} = {n * i}')
    
    print('-' * 20)
