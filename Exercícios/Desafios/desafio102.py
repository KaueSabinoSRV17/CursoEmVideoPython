def fat(n, show=False):

    """
    
        Função para retornar o fatorial de um número

        param n: número que terá a fatorial revelada
        param show: Determina mostrar ou não conta que chega no resultado esperado
        returns: fatorial do número
    
    """
    
    if show == True:
        
        f = 1
        
        print(f'{n}', end='')
        
        for i in range (n, 0, -1):
            
            print(f' x {i}', end='')
            f *= i
            
        return f' = {f}'
        
    else: 

        f = 1
    
        for i in range(n, 0, -1):
    
            f *= i
    
        return f

print(fat(5, show=False))