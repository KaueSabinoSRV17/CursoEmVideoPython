"""

    Aula 20 - Funçoes

    Podemos definir funções personalizadas no python com o comando def. 

    ex: def funcao(parãmetros):
        código

    
    Aula 21 - Help, Docstrings, etc.

    Podemos fazer documentação em nossas funções

    colocar valores padrôes atribuindo valores aos parãmetros reais

    Variáveis declaradas dentro de uma função não são acessíveis fora dela, mas variáveis declaradas fora de funções são acessíveis dentro dela
    (Podemos ter variáveis com nomes idênticos, mais escopos diferentes. isso a não ser que escrevamos global variável na declaração da função)

    por úlitmo, podemos retornar valores

"""

def cont(i, f, p):

    """

        Função para contar valores

        parâmetro i = ínicio
        parâmetro f = fim
        parâmetro p = passo (de quanto em quanto vamos contar)
        return = sem retorno

    """

    print(f'Contando de {i} até {f} indo de {p} em {p}: ')

    if p < 0:

        p *= -1

    if p == 0:

        p = 1

    if i < f:

        c = i
        while c <= f:

            print(c, end=' ', flush=True) 
            c += p

    else:

        c = i
        while c >= f:

            print(c, end=' ', flush=True) 
            c -= p


    print('FIM')

help(cont)