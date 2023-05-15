from operazioni import quadrato, cerchio, rettangolo
#from operazioni import cerchio
#from operazioni import rettangolo

print ("Perimetri calcolabili:\nA-Quadrato \nB-Cerchio \nC-Rettangolo")
r=input("Quale operazione vuoi eseguire ? ")
r=r.upper()

	match r:
		case "A":
		print ("Calcoliamo il quadrato! \n ")
		quadrato()

		case "B":
		print ("Calcoliamo il Cerchio! \n ")
		cerchio()

		case "C":
		print ("Calcoliamo il Rettangolo! \n")
		rettangolo()
	
	case _:
	print ("Nessuna operazione rilevata!")
