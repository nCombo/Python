#!usr/bin/env PYTHON
from lxml import etree

xmlFile = etree.parse("annuaire.xml")
racine = etree.Element("annuaire")
personne = etree.SubElement(racine,"personne1")
prenom = etree.SubElement(personne, "prenom1")

racine1 = str(racine)
myFile = open("annuaire.xml", "w")
myFile.write(racine)
