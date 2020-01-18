"""Exemplos de uso das rotinas de conversao de temperura do modulo temperatura"""

import temperatura

def exib_f(celsius):
    '''imprime conversao de temperatura'''
    print (celsius, "celsius =", temperatura.c2f(celsius), 'Farenheit')

# executa funcao para converter 40, 20 e -40 Celsius para o equivalente em Farenheit
exib_f(40)
exib_f(20)
exib_f(-40)
