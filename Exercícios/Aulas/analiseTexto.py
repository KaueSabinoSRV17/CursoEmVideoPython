# Uma das atividades mais comuns é analisar strings. vamos começar com a descoberta do comprimento de uma string

str = input('Digite uma frase qualquer: ')

tmn = len(str)

print('O tamanho da frase digitada, contando os espaços, é {}'.format(tmn))

# Podemos também contar quantas vezes uma determinada letra aparece dentro de uma string inteira ou apenas uma fatia dela. Lembre que essa função é Case Sensitive

pes = input('Digite uma letra ou uma frase pequena para contarmos quantas vezes ela apareceu na frase: ')

print('Esta frase ou letra apareceu {} vezes na frase principal'.format(str.count(pes)))

# É possível achar em que número de caracteres uma certa pesquisa começa, com a função find(). caso a pesquisa não corresponda a nada que esteja dentro da string, vamos receber -1 como retorno

find = input('Digite uma frase para locarzarmos dentro da String: ')

print(str.find(find))

# Inaugurando as funções de transformarção, temos a replace, que vai localizar uma string, que é o primeiro parâmetro, e vai substituir por outra, que é o seu segundo parâmetro

fnd = input('Digite o que quer substituir: ')

rep = input('Pelo o que vamos substituir: ')

print('A string ficou deste jeito: {}'.format(str.replace(fnd, rep)))

# Podemos deixar frases por inteiro em mausculas, minusculas, todas as palavras com a primeira letra em maiuscula ou apenas a primeira palavra com a primeira letra em maiuscula

print('A string inteira em maiúscula é fica desta forma: {} \n\n A string inteira em minúsculas é assim: {} \n\n A string com a primeira letra em maiuscula é assim: {} \n\n e todas as palavras com a primeira letra em mausculas é assim: {}'.format(str.upper(), str.lower(), str.title(), str.capitalize()))

# Podemos nos livrar de espaços nas extremidades

print('com espaços temos {} caracteres'.format(len(str)))
s_esp = str.strip()
print('\n sem os espaços das extremidades ficamos com {}'.format(len(s_esp)))

# Podemos dividir todas as palavras de uma frase em um vetor com split() e reagrupalas com um caracter de junção com a função 'qualquer coisa'.join(string)

palavras = str.split()

join = '-'.join(palavras)