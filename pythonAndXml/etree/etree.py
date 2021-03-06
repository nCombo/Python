'''
Created on 27 janv. 2016

@author: combo
'''
#!:usr/bin/env python
# *coding : utf-8*

import xml.etree.ElementTree as ET

tree = ET.parse('dataInput.xml')
root = tree.getroot()
print("la racine est : ", root)

for child in root:
    print(child.tag, child.attrib)
    print(root[0][1].text)
    
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
    
for country in root.findall('country'):
    rank = country.find('rank').text 
    name = country.get('name')
    print("le pays \"",name,"\" a le rang", rank)

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('update','yes')

for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
        
   
tree.write('dataInputModified.xml')
    