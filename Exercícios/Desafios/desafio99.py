def mai(* n):

    c = 0
    maior = 0

    for i, v in enumerate(n):

        c += 1

        if i == 0:

            maior = v

        else:

            if v > maior:

                maior = v

    print(f'O maior valor entre os {c} informados foi o: {maior}')

mai(1, 5)

mai(4, 8, 9, 1)