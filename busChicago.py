daves_latitudes = 41.98062
daves_longitude = -87.668452

from xml.etree.ElementTree import parse
doc = parse('rt22.xml')



import urllib
candidates = ('1865', '1383')

def distance(lat1, lat2):
    'return distance between two lats'
    return 69*abs(lat1 - lat2)

def monitor():
    u = urllib.urlopen('http://ctabusstracker.com/bustime/\map/getBusesForRoute.jsp?route=22')
    doc1 = parse(u)
    
for bus in doc.findall('bus'):
     busid = bus.findtext('id')
     if busid in candidates:
         lat = float(bus.findtext('lat'))
         dis = distance(lat, daves_lattitude)
         print(busid, dis, 'miles')
print('-'*10)


import time
while True:
    monitor()
    time.sleep(60)
                               
import csv
