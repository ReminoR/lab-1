import requests
import re

#http://www.tsu.ru/help/contacts.php
#http://space-monkey.ru
#http://mosigra.ru
site = requests.get('http://mosigra.ru')
content = site.text.split(' ,')

pattern = re.compile(r'[A-Za-z0-9]+\.*[A-Za-z0-9_-]+\.*[A-Za-z0-9_-]+@[A-Za-z0-9_-]+\.*[A-Za-z0-9_-]*\.[A-Za-z0-9]{2,10}')
result = []

for i in range(len(content)):
	result = pattern.findall(content[i])
result = list(set(result))


for i in range(len(result)):
    print(i+1, result[i])