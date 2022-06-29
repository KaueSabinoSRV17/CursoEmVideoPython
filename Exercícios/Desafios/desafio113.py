from time import process_time_ns


def readInt(msg):

    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('Erro: Digite apenas números inteiros válidos')
            continue

        except (KeyboardInterrupt):
            print('Programa interrompido')
            return 0

        else:   
            return f'O valor inteiro foi {n}'

def readFloat(msg):
    
    while True:
        
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print('Erro: Digite apenas números reais!')
            continue

        except (KeyboardInterrupt):
            print('Programa Interrompido')
            return 0

        else:
            return f'O valor real foi {n}'


print(readInt('Digite um número inteiro: '))
print(readFloat('Digite um valor real: '))