"""Rotinas de teste das funcoes do modulo temperatura"""

import temperatura

def test_c2f():
    """#Test da funcao que converte graus celsius para farenheint"""
    assert temperatura.c2f(3) == 37.4

def test_f2c():
    """#Test da funcao que converte farenheint para graus celsius"""
    assert temperatura.f2c(32) == 0

def test_c2k():
    """#Test da funcao que converte celsius para kelvin"""
    assert temperatura.c2k(0) == 273.15

def test_k2c():
    """#Test da funcao que converte kelvin para celsius"""
    assert temperatura.k2c(273.15) == 0