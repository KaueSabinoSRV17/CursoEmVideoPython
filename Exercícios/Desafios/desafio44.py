# Cálculo de desconto

prd = float(input('Digite o valor do produto: '))

op = ['A vista no dinheiro ou cheque', 'a vista no cartao', '2 x no cartao', '3 x no cartao ou mais']

esc = int(input('Digite:\n0 para pagar {}\n1 para pagar {}\n2 para pagar em {}\n3 para pagar em {}\n'.format(op[0], op[1], op[2], op[3])))

vld = esc < 4

if vld:

    if esc == 0:

        prd = prd - (prd / 100 * 10)

        print('O total da compra será {}R$'.format(prd))

    elif esc == 1:

        prd = prd - (prd / 100 * 5)

        print('O total da compra será {}R$'.format(prd))

    elif esc == 2:

        print('O total da compra será {}R$, feito em duas parcelas'.format(prd))

    else:

        prc = int(input('Em quantas parcelas deseja fazer? '))

        prd = (prd / 100 * 20) + prd

        print('O total da compra será {}R$, feito em {} parcelas'.format(prd, prc))

else:

    print('Opção inválida')