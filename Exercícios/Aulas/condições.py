# Esta aula vai falar sobre condições no Python

# As condições vao acontecer quando precisaarmos verificar uma condição. dependendo do resultado desta condição vamos executar um bloco de comando, ou outro bloco, dependendo de outro resultado

# Para começar o if, vamos colorar if (condição) mais :, depois o bloco verdadeio identado para dentro

esc = int(input('Digite 1 para blocos verdade, e qualquer outro número para blocos falsos: '))

if esc != 1:

    print('Este bloco é um bloco falso, a condição estipulada não foi atendida')

else: 

    print('Este bloco é um bloco verdade. A condição foi atendida')