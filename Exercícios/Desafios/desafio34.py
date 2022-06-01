sal = float(input('Digite o salário que será aumentado: '))

amt1 = 15
amt2 = 10

if sal > 1250:

    sal += sal / 100 * amt2

    print('Você terá um aumento de {}%. O novo salário é: R${}'.format(amt2, sal))

else: 

    sal += sal / 100 * amt1

    print('Você terá um aumento de {}%. O novo salário é: R${}'.format(amt1, sal))