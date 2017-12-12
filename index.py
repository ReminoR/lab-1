import requests
import re

#http://www.tsu.ru/help/contacts.php
#http://space-monkey.ru
#http://mosigra.ru
site = requests.get('http://mosigra.ru').text
pattern = re.compile(r'\w+\.*-*_*\w*\.*-*_*\w*@\w+\.*-*_*\w*\.\w{2,10}')
emails = list(set(pattern.findall(site)))


with open('email.csv', 'w') as file:
	for i in emails:
		file.write(i)
		file.write('\n')
	file.close()
