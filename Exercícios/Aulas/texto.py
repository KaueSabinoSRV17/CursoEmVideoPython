# Para o python, toda cadeia de caracteres (strings) estará sempre entre aspas, simples '' ou duplas "".

frs = input('Digite uma frase, o que quiser!: ')

# Vamos começar o fatiamento de String. Neste comando, você pode escolher um espaço sozinho para ser mostrado

ltr= int(input('Digite qual o espaço a ser mostrado: '))

print('{} é a letra de número {} (Se por acaso aparecer um resulado vazio, você escolheu um espaço em vazio da frase)'.format(frs[ltr], ltr))

# Neste comando, podemos escolher o começo e o final do fatiamento. lembrando que o último caracter a ser exibido será um número atrás do delimitado como final na função. Omitir o número da esquerda do : é o mesmo que escrever 0, e nada depois do : até o final. um segundo : pode ser usado para delimitar de quanto em quanto podemos pular as letras

rng1 = int(input('Digite onde vamos começar o fatiamento: '))

rng2 = int(input('Digite onde vamos terminar o fatiamento: '))

print('A seleção da range é esta: {}'.format(frs[rng1:rng2]))