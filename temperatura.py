"""Rotinas de conversao de temperatura"""

def c2f(celsius):
    '''Conversao de Celsius para Farenheint'''
    return (9.0 / 5.0) * celsius + 32

def f2c(faren):
    '''Conversao de Farenheint para Celsius'''
    return (faren - 32) * (5.0 / 9.0)

