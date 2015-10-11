# -*- coding: utf-8 -*-
"""
Module définissant l'ensemble des opérateurs de notre calculatrice.

"""
from __future__ import division

def addition(a, b):
    """
    réalise l'addition de deux nombres.

    :param a: premier nombre à additionner
    :param b: deuxième nombre à additionner
    :return: addition 

    >>> addition(3, 2)
    5
    """
    return a + b

def multiplication(a, b):
    """
    réalise la multiplication de deux nombres.

    :param a: premier nombre à multiplier
    :param b: deuxième nombre à multiplier
    :return: multiplication

    >>> multiplication(3, 2.)
    6.0
    """
    return a*b

def soustraction(a, b):
    """
    réalise la soustraction de deux nombres.

    :param a: premier nombre à soustraire
    :param b: deuxième nombre à soustraire
    :return: addition 

    >>> soustraction(3, 2.)
    1.0
    """
    return a - b

def division(a, b):
    """
    réalise la division réelle de deux nombres.

    :param a: premier nombre à diviser
    :param b: deuxième nombre à diviser
    :return: addition 

    .. warning:: Attention à la division par zéro !!

    >>> division(3, 2.)
    1.5
    """
    return a/b

if __name__ == "__main__":
    print addition(3, 2)
