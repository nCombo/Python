#!/usr/bien/env python
#-*- coding: utf-8 -*-

import xml.etree.ElementTree as etree
from lxml import etree
import lxml.etree

NSMAP = {None: 'http://www.w3.org/2005/Atom'}

new_feed = lxml.etree.Element('feed', nsmap=NSMAP)

new_feed.set('{http://www.w3.org/XML/1998/namespace}lang', 'en')

title = lxml.etree.SubElement(new_feed, 'title',attrib={'type':'html'})

title.text = 'Programme Python pour lxml'

print(lxml.etree.tounicode(new_feed,pretty_print=True)) 

with open('dataXml3.xml', 'a') as fichier3:
    content = fichier3.write('')
