import random

alunos = ['Kauê', 'Heberty', 'Celso', 'Bryan']

# NÃO ARMAZENAR A ORDEM DENTRO DE UMA VARIÁVEL, APENAS RODAR O VETOR DENTRO DA FUNÇAO E PRINTAR ELE MESMO LOGO APÓS
random.shuffle(alunos)

print('Vocês vão apresentar na seguinte ordem: \n {}'.format(alunos))