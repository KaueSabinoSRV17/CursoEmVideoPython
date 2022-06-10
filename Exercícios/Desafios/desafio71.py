vl = int(input('Quanto sacar: '))
tt = vl
cd = 50
tc = 0

while True:
    
    if tt >= cd:
        
        tt -= cd
        tc += 1
        
    else:
        
        if tc > 0:
            
            print(f'Total de {tc}cédulas de R${cd}')
            
        if cd == 50:
            
            cd = 20
            
        elif cd == 20:
            
            cd = 10
            
        elif cd == 10:
            
            cd = 1
            
        tc = 0
        
        if tt == 0:
            
            break