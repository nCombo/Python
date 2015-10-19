#!/usr/bien/env python
#-*- coding: utf-8 -*-

from lxml import etree

xmlFile = etree.parse("data.xml")
for star in xmlFile.xpath("/users/user/nom"):
    print (star.text)
    
for starAttr in xmlFile.xpath("/users/user"):
    print (starAttr.get("data-id"))
    
for starMetier in xmlFile.xpath("/users/user[metier='Veterinaire']/nom"):
    print(starMetier.text)
    
