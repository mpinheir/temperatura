"""Rotinas de teste das funcoes do modulo temperatura"""

import temperatura

def test_c2f():
    """#Test da funcao que converte graus celsius para farenheint"""
    assert temperatura.c2f(3) == 37.4

def test_f2c():
    """#Test da funcao que converte farenheint para graus celsius"""
    assert temperatura.f2c(32) == 0
