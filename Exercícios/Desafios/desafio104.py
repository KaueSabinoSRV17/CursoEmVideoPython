def intInput(n):

    if n.isnumeric():

        return f'Você digitou o número {n}'

    else:
        
        while n.isnumeric() == False:
        
            n = input('ERRO! DIGITE APENAS NÚMEROS! ')
            
        return f'Você digitou o número {n}'

print(intInput(
    input('Digite um número: ')
))
