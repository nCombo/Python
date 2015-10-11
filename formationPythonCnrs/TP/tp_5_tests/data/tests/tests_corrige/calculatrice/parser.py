# -*- coding: utf-8 -*-
import re

def parser(s):    
    """
    décompose une expression en une liste de nombres
    et une liste d'opérateurs.

    :param s: expression à décomposer

    :return numList: liste des nombres constituant l'expression
    :return opList: liste des opérateurs constituant l'expression

    >>> parser("3 + 2.")
    ([3.0, 2.0], ['+', '+'])
    """
    parse_num = re.compile(r'([.]?\d+\.?\d*)')
    parse_op = re.compile(r'[-+*/]')
    
    numList = map(float, parse_num.findall(s))
    opList = parse_op.findall(s)

    if len(opList) != len(numList):
        opList.insert(0, '+')

    return numList, opList
    
