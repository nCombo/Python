# -*- coding: utf-8 -*-

from calculatrice import Calculatrice

calc = Calculatrice()

print
ligne=raw_input(">>> ")
while ligne!='OFF':
    calc(ligne)
    ligne=raw_input(">>> ")