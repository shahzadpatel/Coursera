'''
Using Regular Expressions we find all the numebrs in the file and find
their sum
'''

import re
f = open('regex_sum_236861.txt', 'r')
l1 = list()
for line in f:
     y = re.findall('[0-9]+', line)
     if len(y) >= 1:
         for i in range(len(y)):
             l1.append(int(y[i]))
         print(l1)

total = sum(l1)
print("The sum of all the numbers in the text file is= " +str(total))
