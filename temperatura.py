"""Rotinas de conversao de temperatura"""

def c2f(celsius):
    '''Conversao de Celsius para Farenheint'''
    return (9.0 / 5.0) * celsius + 32

def f2c(faren):
    '''Conversao de Farenheint para Celsius'''
    return (faren - 32) * (5.0 / 9.0)

def c2k(celsius):
    '''Conversao de Celsius para Kelvin'''
    return (celsius + 273.15)

def k2c(kelvin):
    '''Conversao de Kelvin para Celsius'''
    return (kelvin - 273.15)

