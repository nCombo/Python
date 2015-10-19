# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:28:18 2015

@author: combo
"""

from lxml import etree


xmlFile = etree.parse("annuaire.xml")
for balise in xmlFile.xpath("/annuaire/personne"):
    nom = balise.xpath("nom")
    prenom = balise.xpath("prenom")
    
    print ("mon contact s'appelle "+ nom[0].text + prenom[0].text)
    print("il est affilié au département " + balise.get("dpmt"))
    print("le nom de la balise en cours est : "+ balise.tag)

    

    
