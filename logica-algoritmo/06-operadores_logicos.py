#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
OPERADORES LÓGICOS
Exemplo págs. 57 a 60 - Livro: "Intro à Prog com Python"
08/04/2020
"""

# Operador NOT
print(not True)             # False
print(not False)            # True

# Operador AND
print(True and True)        # True
print(True and False)       # False
print(False and True)       # False
print(False and False)      # False

#  Operador OR
print(True or True)         # True
print(True or False)        # True
print(False or True)        # True
print(False or False)       # False

# Expressões Lógicas
# Ordem de avaliação:
# 0 - Operadores relacionais; Operadores Lógicos: 1 - NOT; 2 - AND; 3 - OR

# Exemplo:
"""
1 - True or False and not True
2 - True or False and False
3 - True or False
"""

salario = 100
idade = 30
print(salario > 1000 and idade > 30)
