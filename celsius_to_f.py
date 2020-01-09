"""Programa para converter temperatura em Celsius para Farenheit"""


def c2f(celsius):
    '''Conversao de Celsius para Farenheint'''
    return (9.0 / 5.0) * celsius + 32

def exib_f(celsius):
    '''imprime conversao de temperatura'''
    print (celsius, "celsius =", c2f(celsius), 'Farenheit')

# executa funcao para converter 40, 20 e -40 Celsius para o equivalente em Farenheit

exib_f(40)
exib_f(20)
exib_f(-40)
