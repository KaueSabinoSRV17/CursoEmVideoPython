cores = (
    '\033[m', # sem cor
    '\033[0;30;41m', # vermelho
)

op = ''

def titulo(msg, cor):

    tm = len(msg) + 4

    print(cores[cor])
    print('~' * tm)
    print(f'  {msg}')
    print('~' * tm)
    print(cores[cor])

while op != '.exit':

    titulo('Interactive HelPY', cor[1])

    op = input('Função ou Biblioteca do Python> ')
    help(op)