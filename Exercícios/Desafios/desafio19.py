from random import randint

# Poderia ser também usado apenas random.choice(vetor, neste caso alunos)
sorteado = randint(0, 3)

alunos = ['João', 'Maria', 'Kauê', 'Heberty']

print('{}, vá limpar a lousa!'.format(alunos[sorteado]))