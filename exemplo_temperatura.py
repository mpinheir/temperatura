"""Exemplos de uso das rotinas de conversao de temperura do modulo temperatura"""

import temperatura

def exib_c2f(celsius):
    '''imprime conversao de temperatura de celsius para farenheit'''
    print(celsius, "celsius =", temperatura.c2f(celsius), 'Farenheit')
def exib_f2c(faren):
    '''imprime conversao de temperatura de farenheit pare celsius'''
    print(faren, "Farenheit =", temperatura.f2c(faren), 'Celsius')
def exib_c2k(celsius):
    '''imprime conversao de temperatura de celsius para kelvin'''
    print(celsius, "Celsius =", temperatura.c2k(celsius), 'Kelvin')
def exib_k2c(kelvin):
    '''imprime conversao de temperatura de kelvin para celsius'''
    print(kelvin, "Kelvin =", temperatura.k2c, "Celsius")

# executa funcao para converter 40, 20 e -40 Celsius para o equivalente em Farenheit
exib_c2f(40)
exib_c2f(20)
exib_c2f(-40)

# executa funcao para converter 32, -40, 0 Farenheit para o equivalente em Celsius
exib_f2c(32)
exib_f2c(-40)
exib_f2c(0)

# executa funcao para converter 40, 20, -40 Celsius para o equivalente em Kelvin
exib_c2k(40)
exib_c2k(20)
exib_c2k(-40)

# executa funcao para converter 0, 273.15, 65 Kelvin para o equivalente em Celsius
exib_k2c(0)
exib_k2c(273.15)
exib_k2c(373.15)
