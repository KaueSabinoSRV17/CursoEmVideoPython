def voto(ano):

    from datetime import datetime as dt

    atual = dt.today().year

    idade = atual - ano

    if idade < 16:

        return f'NEGADO O VOTO. PESSOA COM {idade} anos'

    elif 16 <= idade < 18 or idade > 65:

        return f'VOTO OPCIONAL PESSOA COM {idade} anos'

    else:

        return f'VOTO OBRIGATÓRIO PESSOA COM {idade} anos'

    
print(voto(int(input('Digite o ano do seu nascimento: '))))