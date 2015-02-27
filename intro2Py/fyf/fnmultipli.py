# -*- coding: utf-8 -*-
"""module table function"""
def table(nb, max=10):
    """Function print multiplication table"""
    i = 0
    while i < max:
        print(i + 1, '*', nb, '=', (i + 1) *nb)
        i += 1
#check the fn in itself thanks __name__
if __name__ == "__main__":
    table(5)
