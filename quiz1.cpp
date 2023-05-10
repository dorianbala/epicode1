#include <stdio.h>

int main() {

char g; /* per giocare oppure no */
char r; /* r per risposta */
int p ; /* p per punteggio dell'utente */

printf("Benvenuto! Il gioco è un quiz con 3 domande, ciascuna con tre risposte, alla fine ti verrà dato un punteggio. \n");
printf("Vuoi giocare al quiz? a-si, b-no "); /* chiediamo per la prima volta all'utente se vuole giocare*/
scanf(" %c", &g); /* inserisco la risposta dell utente nella variabile g */

if(g == 'a') { /*verifico se g è uguale a s quindi faccio partire il gioco*/
do {  /* inizio del ciclo do while */
p = 0; /* inizializzo p a 0*/

 /*prima domanda con a seguito le possibilità di risposta */
printf("Domanda 1: In quale giorno dell'anno si festeggia la liberazione italiana? \n");
printf("a- 21 gennaio \n");
printf("b- 25 aprile \n");
printf("c- 30 settembre\n");
scanf(" %c", &r);  /*inserisco la risposta nella variabile r*/
if(r == 'b') { /*se la risposta è giusta aggiungo un punto*/
p++;
}

printf("Domanda 2: Qual è la canzone più ascoltata al mondo? \n");
printf("a- Shape of You, Ed Sheeran \n");
printf("b- Blinding Lights, The Weeknd \n"); 
printf("c- Dance Monkey, Tones and I\n");
scanf(" %c", &r);
if(r == 'a') {
p++;
}

printf("Domanda 3: Qual è il linguaggio di programmazione più difficile mai inventato?\n");
printf("a- Crimer\n");
printf("b- Python\n");
printf("c- Malbolge\n");
scanf(" %c", &r);
if (r == 'c') {
p++;
}
printf("Hai risposto bene a %d domande su 3\n", p); /*stampiamo in output il totale delle doamnde esatte*/

printf("Vuoi giocare di nuovo? s-si, n-no\n"); /*propongo all'utente di rigiocare*/
scanf(" %c", &g); 

} while (g == 'a');
}
return 0;
}
