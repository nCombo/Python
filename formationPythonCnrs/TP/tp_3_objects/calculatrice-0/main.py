# -*- coding: utf-8 -*-

from calculatrice import calcule

print
ligne=raw_input(">>> ")
while ligne!='OFF':
    calcule(ligne)
    ligne=raw_input(">>> ")
