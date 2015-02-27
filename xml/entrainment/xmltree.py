import xml.etree.ElementTree as ET


tree = ET.parse('/home/combo/Pydev/xml/corpustest/2.v91-008.tei.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

for persName in root.findall('persName'):
    forename = persName.find('forename').text 
    surname = persName.find('surname').text
    print(forename, surname)
    
