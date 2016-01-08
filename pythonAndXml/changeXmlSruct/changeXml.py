'''
#!:usr/bin/env python
# *coding : utf-8*

Created on 28 oct. 2015

@author: combo
'''

from lxml import etree

file = etree.parse("exemple.xml")
print("==Begin ==")

for utilisateur in file.xpath("/users/user"):
    print(utilisateur.get("data-id"))
    

for metier in file.xpath("/users/user"):
    nomMetier = metier.find("metier")
    print(nomMetier.text)

for noeudEnfant in file.xpath("/users"):
    nomEnfant = noeudEnfant.getchildren()
    print(nomEnfant)
if __name__ == '__main__':
    pass