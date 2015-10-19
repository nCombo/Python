#!/usr/bin/en PYTHON
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:28:18 2015

@author: combo
"""

from lxml import etree


xmlFile = etree.parse("annuaire.xml")
racine = etree.Element("annuaire")
personne1 = etree.SubElement(racine, "personne")
personne1.set("dpmt","sciences")
nom1 = etree.SubElement(personne1,"nom")
nom1.text = "dupond"

file_str= etree.tostring(racine, pretty_print = True)
file_str = "annuaire.xml"

