frs = input('Digite uma frase qualquer: ').strip()

low = frs.lower()

qtd = low.count('a')

pri = low.find('a') + 1

ult = low.rfind('a') + 1

print('A letra A aparece {} vezes nesta frase, primairamente na posição {} e pela última vez na posição {}'.format(qtd, pri, ult))