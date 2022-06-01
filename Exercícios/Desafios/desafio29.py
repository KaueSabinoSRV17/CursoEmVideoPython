vel = float(input('Digite a velocidade do carro: '))

mlt = (vel - 80) * 7

if vel > 80:

    print('Você foi multado! \nO valor da multa foi calculado em R${}'.format(mlt))

else:

    print('Você esta livre de multas!')