ps_m_18 = 0
hms = 0
m_m_20 = 0
lh = '-' * 20

while True:

    print(lh)
    print('CADASTRE UMA PESSOA!')

    id = int(input('Qual a sua idade? '))
    sx = str(input('Qual o seu sexo? ')).upper().strip()[0]

    while sx not in 'fFmM':

        sx = str(input('Sexo Inválido, digite novamente: ')).upper().strip()[0]

    if sx in 'mM':

        hms += 1

        if id >= 18:

            ps_m_18 += 1

        if sx in 'fF' and id >=20:

            m_m_20 += 1

        op = input('Deseja continuar? [S/N}').upper().strip()[0]

        while op not in 'sSnN':

            op = input('Digite apenas sim ou não! ').upper().strip()[0]

        if op in 'nN':

            break

print(lh)
print(f'Tivemos {ps_m_18} pessoas maiores de 18 anos, {hms} homens e {m_m_20} mulheres maiores de 20 anos')
print(lh)
