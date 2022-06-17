def area(a, b):
    return a * b

print(f'{"Controle de Terreno":^50}')

cm = float(input('Comprimento (m): '))
lg = float(input('Largura (m): '))

print(f'A área de um terreno {cm} x {lg} é {area(cm, lg)}m²')