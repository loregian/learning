#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Capítulo 3.4.1.2 - Variáveis String - Composição
    Livro: "Intro à Prog com Python"
    Autor: Nilo Ney Coutinho Menezes
"""

"""
%d = números inteiros
%s = string
%f = números decimais
"""

# Inteiros
_idade = 22
print("[%d]" % _idade)
print("[%03d]" % _idade)
print("[%04d]" % _idade)
print("[%3d]" % _idade)
print("[%4d]" % _idade)
print("[%-4d]" % _idade)

# Decimais
print("R$%f" % 5)
print("R$%5.2f" % 5)
print("R$%6.2f" % 5)
print("R$%7.2f" % 5)

print("R$%10.5f" % 5)
print("R$%10.6f" % 5)

# Exemplo 1
print("%s tem %d anos e apenas R$%5.2f no bolso." % ("João", 22, 51.34))

# Exemplo 2
_nome = "João"
_grana = 51.34
# variável _idade está acima

print("%s tem %d anos e R$%f no bolso." % (_nome, _idade, _grana))

# Exemplo 3
print("%s tem %d anos e R$%5.2f no bolso." % (_nome, _idade, _grana))

# Exemplo 4
print("%-10s tem %-3d anos e R$%-5.2f no bolso." % (_nome, _idade, _grana))

# Método FORMAT
_nome2 = "Maria"
_idade2 = 33
_grana2 = 16.18

print("{} tem {} anos e R${} no bolso." .format(_nome2, _idade2, _grana2))
print("{:10} tem {:3} anos e R${:5.2f} no bolso." .format(
    _nome2, _idade2, _grana2))
print("{:12} tem {:03} anos e R${:5.2f} no bolso." .format(
    _nome2, _idade2, _grana2))
print("{:<12} tem {:<3} anos e R${:5.2f} no bolso." .format(
    _nome2, _idade2, _grana2))

# F-STRING - A partir do Python 3.6

print(f"{_nome2} tem {_idade2} e R${_grana2} no bolso")
print(f"{_nome2:12} tem {_idade2:3} e R${_grana2:5.2f} no bolso")
print(f"{_nome2:12} tem {_idade2:03} e R${_grana2:5.2f} no bolso")
print(f"{_nome2:<12s} tem {_idade2:<3} e R${_grana2:5.2f} no bolso")
