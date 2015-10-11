# -*- coding: utf-8 -*-

from calculatrice import CalculatriceEtendue

calc = CalculatriceEtendue()

print
ligne=raw_input(">>> ")
while ligne!='OFF':
    calc(ligne)
    ligne=raw_input(">>> ")