#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Calcular se uma determindada pessoa deve pagar imposto.
    Base de cálculo: 1.200
"""
# Exercício 3.4 pág 45 - Livro: "Intro à Prog com Python"

_salario = 1300
_isento = 1200

_imposto = _salario > _isento
print(_imposto)

"""
    Calcular o resultado da expressão, utilizando os valore:
    a = 1   ;   b = 2
    a = 10  ;   b = 3
    1 = 5   ;   b = 1
    """
# Exercício 3.5 pág 45 - Livro: "Intro à Prog com Python"

_a = 1
_b = 2
_c = True
_d = False

_a > _b and _c or _d

"""
Decidir se o aluno foi aprovado.
Requisito: todas as médias > 7.
Total de matérias: 3
"""

# Exercício 3.6 pág 45 - Livro: "Intro à Prog com Pýthon"

_materia1 = 7.1
_materia2 = 7.1
_materia3 = 8
_media = 7

_aprovado = _materia1 > _media and _materia2 > _media and _materia3 > _media
print(_aprovado)

# Opção 2

_materia1 = 7
_materia2 = 9
_materia3 = 9

_media = ((_materia1 + _materia2 + _materia3) / 3)
print(_media > 7)
