"""Exemplos de uso das rotinas de conversao de temperura do modulo temperatura"""

import temperatura

def exib_f(celsius):
    '''imprime conversao de temperatura de celsius para farenheit'''
    print (celsius, "celsius =", temperatura.c2f(celsius), 'Farenheit')
def exib_F(faren):
    '''imprime conversao de temperatura de farenheit pare celsius'''
    print (faren, "Farenheit=", temperatura.f2c(faren), 'Celsius')

# executa funcao para converter 40, 20 e -40 Celsius para o equivalente em Farenheit
exib_f(40)
exib_f(20)
exib_f(-40)

# executa funcao para converter 32, -40, 0 Farenheit para o equivalente em Celsius

exib_F(32)
exib_F(-40)
exib_F(0)





