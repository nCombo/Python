# -*- coding: utf-8 -*-

from calculatrice import Calculatrice

calc = Calculatrice()
calc.init()

print
ligne=raw_input(">>> ")
while ligne!='OFF':
    calc.calcule(ligne)
    ligne=raw_input(">>> ")