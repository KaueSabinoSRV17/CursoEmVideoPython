aluno = {}

aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média: '))

if aluno['media'] < 7:

    aluno['situacao'] = 'Reprovado'

else:

    aluno['situacao'] = 'Aprovado'

print(f'O nome é igual a {aluno["nome"]}, a média é igual a {aluno["media"]} e a situação é {aluno["situacao"]}')