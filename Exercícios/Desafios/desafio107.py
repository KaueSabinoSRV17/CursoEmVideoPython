def metade(n):

    return formatMon(n / 2)

def dobro(n):

    return formatMon(n * 2)

def aumento(n, t):

    return formatMon(n + (n / 100) * t)

def reducao(n, t):

    return formatMon(n - (n / 100) * t)

def formatMon(n, md = 'R$'):
    
    return f'{md}{n:.2f}'.replace('.', ',')

def resumo(v, a, d):

    lh = "-" * 30
    
    print(f'{lh}\n{"RESUMO DE MOEDAS":^30}\n{lh}\n{"Preço analisado:":<20}{formatMon(v)}\n{"Dobro do Preço:":<20}{dobro(v):<10}\n{"Metade do Preço:":<20}{metade(v):<10}\n{f"{a}% de aumento:":<20}{aumento(v, a):<10}\n{f"{d}% de redução:":<20}{reducao(v, d):<10}\n{lh}')

def moedaValida(v):

    if v.isalpha():

        print(f'ERRO: {v} é um preço inválido.')
    
resumo(
    float(input('Digite um valor monetário: ')),
    int(input('Porcentagem de aumento: ')),
    int(input('Porcentagem de redução: '))
)