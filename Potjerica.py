#Python 3.10 je izašao u 2021. godini. Ako nemaš već tu verziju instaliranu...
#import -> zašto ne from module import? zato što ovako znam da je neka komponenta iz modula dok ju pišem
import random
import turtle

#init varijabli -> stavljam si komentare uz svaku varijablu da sada ne bude neka višak koju zaboravim maknuti
ime=0 #baš se pitam za što ovo služi
pravilo=0 #da ne ispadne iz petlje bez ponavljanja pravila (nešto što mi se nije dalo implementirati u izboru ponude :3)
izborPravi=0 #izbor za pravila (zvuči zastrašujuće bez konteksta)
nagrada=100 #bilo bi glupo da je 0
izborPonuda=0 #izbor za ponudu
board=turtle.Screen() #turtle prozor
board.setup(width=400, height=900) #veličina prozora
ploca=[3,3,3,3,3,3,3] #3 je prazno, 5 je igrač, 7 je lovac
pPit=0 #redni broj pitanja pre runde
ans=0 #odgovori za prvu rundu
bod=0 #bodovi za prvu rundu
ans2=0 #odgovori za drugu rundu
ansL=0 #lovčevi odgovori
kPoz=0 #pozicija kornjače
#nema bodova za drugu rundu jer ona tako ne radi

#Turle da bude always on top
canvas = board.getcanvas()
root = canvas.winfo_toplevel()
root.attributes('-topmost', True)

#Inicijalizacija ploče u turtlu
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-125, -300)
turtle.pendown()
for i in range(8):
    #kPoz=turtle.position()
    #print("Pravokutnik {0} je na {1}".format(i+1, kPoz))
    #Pravokutnik 1 je na (-125.00,-300.00)
    #Pravokutnik 2 je na (-125.00,-200.00)
    #Pravokutnik 3 je na (-125.00,-100.00)
    #Pravokutnik 4 je na (-125.00,0.00)
    #Pravokutnik 5 je na (-125.00,100.00)
    #Pravokutnik 6 je na (-125.00,200.00)
    #Pravokutnik 7 je na (-125.00,300.00)
    #Nagrada je na (-125.00,400.00)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.forward(125)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(125)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-125, -200+(i*100))
    turtle.pendown()
turtle.penup()
turtle.goto(-125, -300)


#Pravila
def upute():
    print("\nMini Potjera radi vrlo slično kao normalna Potjera što vidite na televiziji, no ipak ima drukčija pravila\n")
    print("Igra je podijeljena u dva dijela: pojedinačna igra i igra protiv lovca\n")
    print("U prvom dijelu Vi sami odgovarate na pitanja i ovisno o broju Vaših točnih odgovora, toliko će biti završna nagrada u eurima!")
    print("(* nagradu u eurima nećete zapravo dobiti)\n")
    print("Zatim će Vam lovac ponuditi veći ili niži iznos")
    print("Ako odaberete niži iznos, biti ćete 3 koraka ispred lovca, a viši 1")
    print("Ako ostanete pri originalnom iznostu, biti ćete 2 koraka ispred lovca\n")
    print("U drugome dijelu igre ćete igrati protiv lovca")
    print("Bit će Vam prikazano Vaše mjesto i mjesto lovca iza Vas, te zadnje mjesto sa nagradom")
    print("Svakim točnim odgovorom Vi ili lovac ide za jedno mjesto unaprijed prema nagradi (nagrada je nakon zadnjeg polja)\n")
    print("Ako Vas lovac uhvati, izgubili ste igru!")
    print("Ako dođete do nagrade prije neg što Vas uhvati, pobijedili ste!")
    #Razlike od originala: ploča izgleda drukčije ja msm nagrada su totalno drukčije, lovac je random, nema treće runde, prva runda nije na time limitu i sve to

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
            ans = ans.casefold() 
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
            ans = ans.casefold() 
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
def initTurleBoard():
    turtle.penup()
    
    


#Pojedinačna igra
def pojedinac():
    print("Započinjemo sa prvim pitanjem!")
    global pPit, nagrada, bod
    for i in range(6):
        print("\nPitanje {0} od {1}\n".format(i+1,6))
        prvaRunda()
        pPit+=1
    if bod==0:
        print("Vaša nagrada, ako uopće dođete do nje, je 100 eura!")
    else:
        nagrada=100+(bod*150)
        print("Bravo! Samo tako nastavite i dobit ćete {0} eura!".format(nagrada))

#Iznos
def ponuda():
    global nagrada
    print("Imam jednu ponudu za tebe, {0}".format(ime))
    print("Imaš tri opcije! Možeš ostati sa svojih {0} eura, ili si možeš povećati na {1}, ili možda smanjiti na {2}".format(nagrada, nagrada*2, nagrada*0.75))
    print("Na tebi je da odabereš. Unesi ostajem, povećavam ili smanjujem")
    izborPonuda=input()
    izborPonuda=izborPonuda.casefold() 
    if(izborPonuda=="ostajem"):
        print("Ostali ste sa {0} eura! Pametno.".format(nagrada))
    elif(izborPonuda=="povećavam"):
        print("Povećali ste na {0} eura! Jako ste hrabri!".format(nagrada*2))
        nagrada=nagrada*2
    elif(izborPonuda=="smanjujem"):
        print("Smanjili ste na {0} eura! Jeste li sigurni u sebe?".format(nagrada*0.75))
        nagrada=nagrada*0.75
    else:
        print("Krivo ste upisali. Ponovno ću Vas pitati;")
        ponuda()

#Lovac igra
def loviti():
    ponuda()
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
loviti()
