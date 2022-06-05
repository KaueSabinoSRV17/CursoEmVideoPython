# Cálculo de IMC

alt = float(input('Digite a altura: '))

ps = float(input('Digite o peso: '))

imc = ps / (alt * alt)

op = ['Abaixo de Peso', 'Peso ideal', 'Sobrepeso', 'Obesidade', 'Obesidade Mórbida']

if imc < 18.5:

    print(op[0])

elif imc >= 18.5 and imc <= 25:

    print(op[1])

elif imc > 25 and imc <= 30:

    print(op[2])

elif imc > 30 and imc <= 40:

    print(op[3])

else:

    print(op[4])