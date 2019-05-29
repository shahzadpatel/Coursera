'''
We use the BeautifulSoup library to find the sum of all the numbers in the 
span tag of the entered URL
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
l = list()
tags = soup('span')
for tag in tags:
    str = ''.join(tag)
    num = int(str)
    l.append(num)
    
print(l)
print(sum(l))