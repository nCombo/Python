# -*- coding: utf-8 -*-

from calculatrice import CalculatriceEtendue
import pickle, os

nom_fichier = 'main.pkl'
if os.path.exists(nom_fichier):
    fichier = open(nom_fichier,'r')
    calc = pickle.load(fichier)
    fichier.close()
else:
    calc = CalculatriceEtendue()

print
ligne=raw_input(">>> ")
while ligne!='OFF':
    calc(ligne)
    ligne=raw_input(">>> ")
    
fichier = open(nom_fichier,'w')
pickle.dump(calc,fichier)
fichier.close()

