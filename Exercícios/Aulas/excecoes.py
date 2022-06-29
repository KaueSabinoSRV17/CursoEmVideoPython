"""

    Aula 23 - Tratamento de Exceção

    Erro não são apenas sintáticos. podemos escrever por exemplo um print certo, pedindo uma variável para ser printada, mas se a mesma não estiver inicializada, o comando terá uma exceção

    Para podermos tratar um processo com execção, vamos usar uma estrutura try, except

"""

try:

    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))

except (ValueError, TypeError):

    print('Erro: Problemas com Tipagens das variáveis')

except KeyboardInterrupt:

    print('Não houve dados informados')

else:

    print(n1, n2)