c = s = 0

while True:
    
    n = float(input('Digite um valor: '))
    
    if n == 999:
        break

    s += n
    c += 1

print(f'Você digitou {c} números, resultando em uma soma {s}')