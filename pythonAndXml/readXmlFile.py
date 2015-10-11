# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 23:55:00 2015

@author: combo
"""

from xml.dom import minidom
doc = minidom.parse('contacts.xml')

root = doc.documentElement

attributes = root.childNodes[1].hasAttributes()

c = root.childNodes[1]

newdoc = minidom.Document()
newroot = newdoc.createElement('root')
rootattr = newdoc.createAttribute('name')
rootattr.nodeValue = 'foo'
