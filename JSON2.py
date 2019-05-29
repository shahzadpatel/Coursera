'''
We use the JSON library to the number of people who commented from the URL and
the sum of the number of comments from each user
'''

import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter url- ')
data = urllib.request.urlopen(address).read()

info = json.loads(data)
print('User count:', len(info))

sum = 0
count = 0
for item in info["comments"]:
    sum = sum + int(item["count"])
    count = count + 1
    
print("Count: " +str(count))
print("Sum: " +str(sum))