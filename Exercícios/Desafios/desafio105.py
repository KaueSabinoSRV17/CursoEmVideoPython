def boletim(* n, sit=False):

    """
    
        Função que calcula média e situação de um aluno, a partir da entrada de notas

        param n: notas do aluno, quantas forem necessárias
        param sit: Determina se vamos retornar ou não a situação do aluno, onde médias menores que 5 é REPROVADO, menores que 7 RECUPERAÇÃO e maior que 7 APROVADO
        returns: dicionários com todos os resultados
    
    """

    s = 0

    if sit == True:

        for v in n:

            s += v

        md = s / len(n)

        if md < 5:

            return {
                'notas': n,
                'média': md,
                'situacao': "REPROVADO"
            }

        if md <= 7:

            return {
                'notas': n,
                'média': md,
                'situacao': "RECUPERAÇÃO"
            }

        else: 

            return {
                'notas': n,
                'média': md,
                'situacao': 'APROVADO'
            }

    else:

        for v in n:

            s += v

        md = s / len(n)

        return {
            'notas': n,
            'média': md
        }

print(boletim(5, 10, 3, 5, sit=True))