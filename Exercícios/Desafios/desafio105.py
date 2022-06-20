def boletim(* n, sit=False):

    s = 0

    if sit == True:

        for v in n:

            s += v

        md = s / len(n)

        if md < 5:

            return f'A média do aluno foi {md}, e ele está REPROVADO'

        if md <= 7:

            return f'A média do aluno foi {md}, e ele está de RECUPERAÇÃO'

        else: 

            return f'A média do aluno foi {md}, e ele está APROVADO!'

    else:

        for v in n:

            s += v

        md = s / len(n)

        return(f'A média do aluno foi {md}')


boletim(5, 10, 3, 5, sit=True)