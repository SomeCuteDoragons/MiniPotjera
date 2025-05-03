#import
import random
import turtle

#init varijabli 
ime=0
pravilo=0
izborPravi=0
nagrada=100
ponuda=3
board=turtle.Screen()
board.screensize(310,540)
pPit=0
ans=0
bod=0

#Pravila
def upute():
    print("\nMini Potjera radi vrlo slično kao normalna Potjera što vidite na televiziji\n")
    print("Igra je podijeljena u dva dijela: pojedinačna igra i igra protiv lovca\n")
    print("U prvom dijelu Vi sami odgovarate na pitanja i ovisno o broju Vaših točnih odgovora, toliko će biti završna nagrada u eurima!")
    print("(* nagradu u eurima nećete zapravo dobiti)\n")
    print("Zatim će Vam lovac ponuditi veći ili niži iznos")
    print("Ako odaberete niži iznos, biti ćete 4 koraka ispred lovca, a viši 2")
    print("Ako ostanete pri originalnom iznostu, biti ćete 3 koraka ispred lovca\n")
    print("U drugome dijelu igre ćete igrati protiv lovca")
    print("Bit će Vam prikazano Vaše mjesto i mjesto lovca iza Vas, te zadnje mjesto sa nagradom")
    print("Svakim točnim odgovorom Vi ili lovac ide za jedno mjesto unaprijed prema nagradi\n")
    print("Ako Vas lovac uhvati, izgubili ste igru!")
    print("Ako dođete do nagrade prije neg što Vas uhvati, pobijedili ste!")

#Pitanja za prvu rundu
def prvaRunda():
    global bod
    match pPit:
        case 0:
            print("Što radi append metoda u Pythonu?")
            print("A) Dodaje element na kraj liste")
            print("B) Dodaje element na početak liste")
            print("C) Dodaje element na željeno mjesto u listi")
            ans=input("Unesite A, B ili C: ")
            ans = ans.casefold() #Nikad ne možeš računati da je end user pametan
            if(ans=="a" or ans=="a)"):
                print("Točno!")
                bod+=1
            else:
                print("Nažalost, krivo!")
                print("Točan odgovor je A) Dodaje element na kraj liste")
        case 1:
            print("Koji je glavni grad Maroka?")
            print("A) Casablanca")
            print("B) Havana")
            print("C) Rabat")
            ans=input("Unesite A, B ili C: ")
            ans = ans.casefold() #Mora da bude malo slovo
            if(ans=="c" or ans=="c)"):
                print("Točno!")
                bod+=1
            else:
                print("Nažalost, krivo!")
                print("Točan odgovor je C) Rabat")
        case 2:
            print("Koji je najduži tunel u Europi?")
            print("A) Tunnel De Frejus")
            print("B) Zhongnanshan Tunnel")
            print("C) Lærdalstunnelen")
            ans=input("Unesite A, B ili C: ")
            ans = ans.casefold() 
            if(ans=="c" or ans=="c)"):
                print("Točno!")
                bod+=1
            else:
                print("Nažalost, krivo!")
                print("Točan odgovor je C) Lærdalstunnelen")
        case 3:
            print("Kada se otvorila III. Gimnazija, Osijek?")
            print("A) 1991.")
            print("B) 1890.")
            print("C) 1795.")
            ans=input("Unesite A, B ili C: ")
            ans = ans.casefold()
            if(ans=="b" or ans=="b)"):
                print("Točno!")
                bod+=1
            else:
                print("Nažalost, krivo!")
                print("Točan odgovor je B) 1890.")
        case 4:
            print("Iz koje Kranjčevićeve pjesme dolazi stih 'Kud li se trgom vucare trome, prostačke psine, podvita repa, kičme ko britva'")
            print("A) Eli! Eli! Iama azavtani!?")
            print("B) Mojsije")
            print("C) Gospodskomu Kastoru")
            ans=input("Unesite A, B ili C: ")
            ans = ans.casefold()
            if(ans=="c" or ans=="c)"):
                print("Točno!")
                bod+=1
            else:
                print("Nažalost, krivo!")
                print("Točan odgovor je C) Gospodskomu Kastoru")
        case 5:
            print("Koje je novo ime uvedeno za odmorište Križ na autocesti A3?")
            print("A) Novoselec")
            print("B) Bosutsko")
            print("C) Marija")
            ans=input("Unesite A, B ili C: ")
            ans = ans.casefold()
            if(ans=="a" or ans=="a)"):
                print("Točno!")
                bod+=1
            else:
                print("Nažalost, krivo!")
                print("Točan odgovor je A) Novoselec")
        case _:
            print("case default error, kako li se to uopće dogodilo?")



#Turtle ploča
def slikovitiPrikaz():
    print("lorem ipsum")
    
#Iznos
def ponuda():
    print("lorem ipsum")
#Pojedinačna igra
def pojedinac():
    print("Započinjemo sa prvim pitanjem!")
    for i in range(6):
        global pPit
        print("\nPitanje {0} od {1}\n".format(i+1,6))
        prvaRunda()
        pPit+=1
    if bod==0:
        print("Vaša nagrada, ako uopće dođete do nje, je 100 eura!")
    else:
        nagrada=100+(bod*150)
        print("Bravo! Samo tako nastavite i dobit ćete {0} eura!".format(nagrada))
#Lovac igra
def loviti():
    print("lorem ipsum")
#Ime i uvod
print("Dobro došli u Mini Potjeru!")
print("Mini Potjera je minijaturna, malo jednostavnija verzija Potjere na Vašem računalu")
print("Mogu li Vas pitati, koje je Vaše ime?")
ime=input()
print("Dobar Vam dan,",ime)
print("Želite li čuti pravila? Ako da, unesite da, inače unesite ne")
while(pravilo==0): #Izbor za prikaz uputa, ne smije biti broj ili python krešti
    izborPravi=input()
    izborPravi=izborPravi.casefold() #Nikad ne možeš računati da je end user pametan
    if(izborPravi=="da"):
        upute()
        pravilo=1
    elif(izborPravi=="ne"):
        pravilo=1
    else:
        print("Upisali ste nešto krivo!")

#Pojedinačna igra uvod
print("\n\n\nDobra Večer, {0}, ja sam Ilija Čvorović, voditelj današnje Potjere!".format(ime))
print("U početku ću Vas ja pitati nekoliko pitanja da odredimo iznos Vaše nagrade!")
print("Započeti ćemo sa 100 eura\n")
pojedinac()
    
#Lovac igra uvod
print("\n\nSuper je prošla igra, ali vrijeme je za igru protiv lovca!")
print("Moje ime je Laki Topalović i biti ću Vaš lovac za ovu rundu")
