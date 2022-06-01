dst = float(input('Digite a distãncia a ser percorrida em KM: '))

if dst <= 200:

    print('O preço será R${}'.format(dst * .5))

else:

    print('O preço será R${}'.format(dst * .45))