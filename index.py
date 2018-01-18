import requests
import re

#http://www.tsu.ru/help/contacts.php
#http://space-monkey.ru
#http://mosigra.ru
#http://my.mail.ru
site = requests.get('http://my.mail.ru').text
pattern = re.compile(r'\w+\.*-*_*\w*\.*-*_*\w*@\w+\.*-*_*\w*\.\w{2,10}')
emails = list(set(pattern.findall(site)))
exceptions = [] #добавляем исключения
pattern_mail_ru = re.compile(r'@Mail\.')


with open('email.csv', 'w') as file:
	for email in emails:
		if not pattern_mail_ru.findall(email) and email not in exceptions:
			file.write(email + '\n')
			print(email)
	file.close()