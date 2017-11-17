import requests
import re

#http://www.tsu.ru/help/contacts.php
#http://space-monkey.ru
#http://mosigra.ru
site = requests.get('http://www.tsu.ru/help/contacts.php')
content = site.text.split(' ')

result = []

for value in content:
    mask = re.findall(r'mailto:(\w+@\w+.\w+)', value)
    if mask:
        result.append(*mask)
        result = list(set(result))

for i in range(len(result)):
    print(i+1,result[i]) 