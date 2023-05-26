import time
import urllib.parse
import http.client
import requests
import socket

from Funzioni import portscan,metodi,dvwabrute,myadminbrute

print("_______________________________________")
print("_______________________________________\n")

text="Benvenuto nel programma di EXPLOIT\n"

for char in text:
	print(char, end='', flush=True)
	time.sleep(0.10)
	
print("_______________________________________")
print("_______________________________________\n")
time.sleep(1)

print("Operazioni possibili:")
print(" A-Scansione Porte\n","B-Scansione Metodi disponibili\n","C-Brute force PhpMyadmin\n","D-Brute force Dvwa\n")
r=input("Cosa vuoi fare ?")
r=r.upper()

match r:
	case "A":
		print ("Facciamo la scansione delle porte \n ")
		portscan()

	case "B":
		print ("Scansione Metodi disponibili \n ")
		metodi()

	case "C":
		print ("Brute force PhpMyadmin \n")
		myadminbrute()
	
	case "D":
		print ("Brute force Dvwa\n")
		dvwabrute()

	case _:
		print ("Nessuna operazione rilevata!")
