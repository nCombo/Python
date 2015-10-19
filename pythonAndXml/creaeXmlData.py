#!/usr/bien/env python
#-*- coding: utf-8 -*-

from lxml import etree

users = etree.Element("users")
user = etree.SubElement(users, "user")
user.set("id", "101")
nom = etree.SubElement(user, "nom")
nom.text = "Jackson"
metier = etree.SubElement(user, "metier")
metier.text = "Danseur"

xmlData = etree.tostring(users, pretty_print=True)

c = xmlData
print (c)

with open('xmlData.xml', 'a') as xmlData:
    contenu = xmlData.write('ser')

print (contenu)
