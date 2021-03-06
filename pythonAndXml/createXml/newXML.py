'''
Created on 30 oct. 2015

@author: combo
'''
#!:usr/bin/env python
# *coding : utf-8*


from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from pprint import PrettyPrinter


membership = Element("membership")

users = SubElement(membership, "users")
SubElement(users, "user", name="john")
SubElement(users, "user", name="charles")
SubElement(users, "user", name="peter")

groups = SubElement(membership, "groups")

group = SubElement(groups, "group", name="users")
SubElement(group, "user", name='john')
SubElement(group, "user", name="charles")

group = SubElement(groups, "group", name="administrators")
SubElement(group, "user", name="peter")


#output_file = open("membership.xml", mode='wb')
#output_file.write(bytes('<?xml version="1.0"?>', 'utf-8'))
#output_file.write(bytes("Resulats de mon XML écrit avec python :"))
#output_file.write(ElementTree.tostring(membership))
#output_file.close()

with open('membreship.xml', 'wb') as output_file:
    output_file.write(bytes('<?xml version="1.0"?>', 'utf-8'))
    #output_file.write(bytes("Resulats de mon XML écrit avec python :"))
    output_file.write(ElementTree.tostring(membership))
    #output_file = ElementTree.tostring(membership, pretty_print=True)
    #file_str= etree.tostring(racine, pretty_print = True)

if __name__ == '__main__':
    pass