'''
This program gets the data from the entered URL that contains the XML file of 
the numebr of 'comments' each 'name' has entered and finds the sum. 
'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter url- ')
data = urllib.request.urlopen(address).read()

tree = ET.fromstring(data)
counts = tree.findall('comments/comment/count')

total = 0
for count in counts:
    total += int(count.text)

print ('Total: ', str(total))