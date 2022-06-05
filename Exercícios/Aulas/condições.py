"""
    Aula 10 - Condições Simples

    Esta aula vai falar sobre condições no Python

    As condições vao acontecer quando precisaarmos verificar uma condição. dependendo do resultado desta condição vamos executar um bloco de comando, ou outro bloco, dependendo de outro resultado

    Para começar o if, vamos colorar if (condição) mais :, depois o bloco verdadeio identado para dentro
    
    Aula 12 - Condições Aninhadas

    Começamos a usar novas condições quando houver mais de 2 caminhos possíveis a serem seguidos

    para usar uma condição aninhada, o else if é simplificado para elif
    
"""

esc = int(input('Digite 1 para blocos verdade, 2 para um elif e qualquer outro número para blocos falsos: '))

if esc != 1:

    print('Este bloco é um bloco falso, a condição estipulada não foi atendida')

elif esc == 2:

    print('Atendemos uma condição de elif!')

else: 

    print('Este bloco é um bloco verdade. A condição foi atendida')

