nm = input('Digite seu nome completo: ').strip()

caps = nm.upper()
bx = nm.lower()

palavras = nm.split()
semEspaço = ''.join(palavras)
letrasSemEspaço = len(semEspaço)
priNm = palavras[0]
priLtrs = len(priNm)

print('Seu nome com CAPS LOCK: {} \n Seu nome falando baixinho: {} \n Quantas letras sem contar espaços: {} \n Quantidade de letras no primeiro nome: {}'.format(caps, bx, letrasSemEspaço, priLtrs))