# -*- coding: utf-8 -*-

import operateurs
from analyseur import analyse

res = 0

def calcule(chaine):
    global res
    opList, numList = analyse(chaine)
    print "( %s %s )" % (opList,numList)
    for op, num in zip(opList, numList):
            if op=='=': res = num
            else: res = operateurs.operations[op](res,num)
    print res

