# Emprestimo Bancário

# Entrada de dados do usuário

sal = float(input('Qual a sua renda mensal? \n'))

cs = float(input('Qual o valor do imóvel desejado? \n'))

ans = int(input('Você irá pagar o imóvel durante quantos anos? \n'))

# processamento de valores

ms = ans * 12

prs = cs / ms

pct = sal / 100 * 30

podeSerFinanciado = prs > pct

# saída com teste condicional

if podeSerFinanciado:

    print('Empréstimo negado\n')

else: 

    print('Empréstimo aprovado\n')