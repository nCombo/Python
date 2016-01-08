'''
Created on 31 oct. 2015

@author: combo
'''

from xml.etree import ElementTree


doc = ElementTree.parse('exemple.xml')

racine = doc.getroot()

print(racine.tag)


#titres = doc.getchildren('TEI/teiHeader/fileDsc/titleStmt')
#print(titres)
#for t in titres:
   #titre = t.find('title').text
   #type(t)

with open('exemple.xml', 'r') as f:
    data = f.readlines()

    for line in data:
        words = line.split()
        print( words)
    
    racine = doc.getroot()

    print(racine.tag)   
    
    titres = doc.find('titleStmt')
    for t in titres:
        titre = t.find('title').text
        print(titre)
        
if __name__ == '__main__':
    pass