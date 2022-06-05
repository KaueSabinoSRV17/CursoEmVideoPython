# Média avançada

n1 = float(input('Digite a primeira nota: '))

n2 = float(input('Digite a segunda nota: '))

md = (n1 + n2) / 2

vld = n1 <= 10 and n2 <= 10

if vld:

    if md < 5:

        print('O aluno foi Reprovado! Sua média foi {}'.format(md))

    elif md >= 5 and md < 7:

        print('O aluno está de Recuperação! Sua média foi {}'.format(md))
    
    else:

        print('O aluno está aprovado com média {}!'.format(md))

else: 

    print('Não digite notas maiores do que 10!')