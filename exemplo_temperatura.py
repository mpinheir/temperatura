"""Exemplos de uso das rotinas de conversao de temperura do modulo temperatura"""

import temperatura

def exib_f(celsius):
    '''imprime conversao de temperatura'''
    print (celsius, "celsius =", temperatura.c2f(celsius), 'Farenheit')
def exib_k(celsius):
    '''imprime conversao de temperatura'''
    print (celsius, "celsius=", temperatura.c2k(celsius), 'Kelvin')

# executa funcao para converter 40, 20 e -40 Celsius para o equivalente em Farenheit
exib_f(40)
exib_f(20)
exib_f(-40)

# executa funcao para converter 50, 10, 0 Celsius para o equivalente em Kelvin

exib_k(50)
exib_k(10)
exib_k(0)





