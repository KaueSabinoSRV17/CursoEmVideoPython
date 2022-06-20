def jogador(gls=0, nm='<desconhecido>'):

    return f'O jogador {nm} fez {gls} na temporada'

n = input('Nome: ')
g= input('Gols: ')

if g.isnumeric():

    g = int(g)

    

else:

    g = 0

if n.strip() == '':

    print(jogador(gls=0))

else:

    print(jogador(g, n))