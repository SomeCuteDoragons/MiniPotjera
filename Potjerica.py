#Python 3.10 je izašao u 2021. godini. Ako nemaš već tu verziju instaliranu...
#import -> zašto ne from module import? zato što ovako znam da je neka komponenta iz modula dok ju pišem
#dobar dan 2.e da se zna da je ovo zapravo moj projekt
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
ploca=[3,3,3,3,3,3,3,0] #3 je prazno, 5 je igrač, 7 je lovac, 0 je nagrada (samo za boju)
pPit=0 #redni broj pitanja prve runde
lPit=0 #redni broj pitanja druge runde
ans=0 #odgovori za prvu rundu
bod=0 #bodovi za prvu rundu
ans2=0 #odgovori za drugu rundu
ansL=0 #lovčevi odgovori
kPozI=0 #pozicija kornjače igrača
kPozL=0 #pozicija kornjače lovca
odgZaEval=0 #odgovor za lovEval. Vidjeti ćeš u funkciji
lovEval=0 #evaluacija pitanja u drugoj rundi; 1 je kada su oboje krivo, 2 kada je igrač točan, 3 kada je lovac točan, 4 kada su oboje točni
bChange=0 #promjena boje na ploči po igraču ili lovcu
rezultat=0 #rezultat nakon druge runde, 1 lovac, 2 igrač, 0 nitko
tocOdg=0 #Točan odgovor u drugoj rundi

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
    print("Svakim točnim odgovorom Vi ili lovac ide za jedno mjesto unaprijed prema nagradi\n")
    print("Ako Vas lovac uhvati, izgubili ste igru!")
    print("Ako dođete do nagrade prije neg što Vas uhvati, pobijedili ste!")
    print("Ako nekako nitko ne dođe do nagrade nakon 20 pitanja, nitko ne pobjeđuje!\n")
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

def turtleInitKvadrat(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
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

def turtleChangeKvadrat(): #za TurtleChangeState
        turtle.pendown()
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

#Turtle ploča definirana po originalnoj ponudi
def initTurleBoard():
    global ploca
    for i in range(len(ploca)):
        if ploca[i]==3 or ploca[i]==0:
            turtle.fillcolor("black")
        elif ploca[i]==5:
            turtle.fillcolor("blue")
        elif ploca[i]==7:
            turtle.fillcolor("red")
        turtleInitKvadrat(-125, -300+(i*100)) #malo urednije ipak lolololok
    turtle.penup()


def turtleChangeState(): #mijenja boju na ploči
    global ploca, kPozI, kPozL, lovEval, bChange
    match lovEval:
        case 1:
            pass
        case 2:
            turtle.fillcolor("blue")
            turtleChangeKvadrat()
        case 3:
            turtle.fillcolor("red")
            turtleChangeKvadrat()
        case 4:
            if bChange==1:
                turtle.fillcolor("blue")
                turtleChangeKvadrat()
            elif bChange==2:
                turtle.fillcolor("red")
                turtleChangeKvadrat()
            else:
                print("huh")


def turtleMoveBoard(): #ovo je ipak bolji način?????? JOJ ŠTO JE SPORO
    global ploca, kPozI, kPozL, bChange
    
    # Osigura da se prijašnje mjesto vrati na crno
    for i in range(len(ploca)):
        turtle.penup()
        turtle.goto(-125, -300+(i*100))
        turtle.fillcolor("black")
        turtleChangeKvadrat()
    
    # Igrač
    kPozI = ploca.index(5)
    turtle.penup()
    turtle.goto(-125, -300+(kPozI*100))
    turtle.fillcolor("blue")
    turtleChangeKvadrat()
    
    # Lovac
    kPozL = ploca.index(7)
    turtle.penup()
    turtle.goto(-125, -300+(kPozL*100))
    turtle.fillcolor("red")
    turtleChangeKvadrat()


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
    global nagrada, izborPonuda, ploca
    print("Imam jednu ponudu za tebe, {0}".format(ime))
    print("Imaš tri opcije! Možeš ostati sa svojih {0} eura, ili si možeš povećati na {1}, ili možda smanjiti na {2}".format(nagrada, nagrada*2, nagrada*0.75))
    print("Na tebi je da odabereš. Unesi ostajem, povećavam ili smanjujem")
    izborPonuda=input()
    izborPonuda=izborPonuda.casefold() 
    if(izborPonuda=="ostajem"):
        print("Ostali ste sa {0} eura! Pametno.".format(nagrada))
        ploca=[7,3,5,3,3,3,3,0]
    elif(izborPonuda=="povećavam"):
        print("Povećali ste na {0} eura! Jako ste hrabri!".format(nagrada*2))
        nagrada=nagrada*2
        ploca=[7,5,3,3,3,3,3,0]
    elif(izborPonuda=="smanjujem"):
        print("Smanjili ste na {0} eura! Jeste li sigurni u sebe?".format(nagrada*0.75))
        nagrada=nagrada*0.75
        ploca=[7,3,3,5,3,3,3,0]
    else:
        print("Krivo ste upisali. Ponovno ću Vas pitati;")
        ponuda()

#E OVO JE DRUGA RUNDA UGH
def drugaRunda():
    global lPit, ans2, ansL, lovEval, kPozI, kPozL, ploca, rezultat, tocOdg #fakat ne znam što sve staviti u global iz prve dok ne počnem pisati funkciju pa nek sve ide (ponovno upućeno)
    match lPit: #staviti ću prava pitanja iz potjere možda hhhhhhhhhhhhhh ako budu pitanja iz potjere onda će biti pitanja iz potjere 10., 12. i 17. Svibnja 2025. ili koliko daleko mi hrti dopusti ići
        case 0:
            print("Koja je od navedenih pjesama pobjednica Dore nagrađena i Porinom za pjesmu godine?")
            tocOdg="a"
            print("A) Mama ŠČ!")
            print("B) Marija Magdalena")
            print("C) Ostani")
            ans2=input("Unesite A, B ili C: ")
            ans2 = ans2.casefold()
            if(ans2=="a" or ans2=="a)"):
                odgZaEval=2
            else:
                odgZaEval=1
            if(ansL=="a"):
                if odgZaEval==1:
                    lovEval=3
                else:
                    lovEval=4
            else:
                if odgZaEval==1:
                    lovEval=1
                else:
                    lovEval=2
        #da me ubije ova logika majke mi, samo zapamti od=2 else od=1 -> if od=1 lov=3 else lov=4 -> else if od=1 lov=1 else lov=2            
        case 1:
            print("Koliko su elegija u knjizi 'Corpus Tibullanium' zapravo Tibulove?")
            tocOdg="c"
            print("A) 32")
            print("B) 20")
            print("C) 16")
            ans2=input("Unesite A, B ili C: ")
            ans2 = ans2.casefold()
            if(ans2=="c" or ans2=="c)"):
                odgZaEval=2
            else:
                odgZaEval=1
            if(ansL=="c"):
                if odgZaEval==1:
                    lovEval=3
                else:
                    lovEval=4
            else:
                if odgZaEval==1:
                    lovEval=1
                else:
                    lovEval=2
        case 2:
            print("Na kojem poluotoku u Hrvatskoj se nalazi dolina Dingač, poznata po svojim vinogradima?")
            tocOdg="a"
            print("A) Pelješac")
            print("B) Istra")
            print("C) Klek")
            ans2=input("Unesite A, B ili C: ")
            ans2 = ans2.casefold()
            if(ans2=="a" or ans2=="a)"):
                odgZaEval=2
            else:
                odgZaEval=1
            if(ansL=="a"):
                if odgZaEval==1:
                    lovEval=3
                else:
                    lovEval=4
            else:
                if odgZaEval==1:
                    lovEval=1
                else:
                    lovEval=2
        case 3:
            print("Po čemu su bili nazvani raketoplani iz NASA-ina projekta Space Shuttle?")
            tocOdg="a"
            print("A) Po brodovima")
            print("B) Po generalima")
            print("C) Po saveznim državama")
            ans2=input("Unesite A, B ili C: ")
            ans2 = ans2.casefold()
            if(ans2=="a" or ans2=="a)"):
                odgZaEval=2
            else:
                odgZaEval=1
            if(ansL=="a"):
                if odgZaEval==1:
                    lovEval=3
                else:
                    lovEval=4
            else:
                if odgZaEval==1:
                    lovEval=1
                else:
                    lovEval=2
        case 4:
            print("Koje je ime pape koji je rezignirao 2013. godine?")
            tocOdg="c"
            print("A) Ivan Pavao II.")
            print("B) Inocent III.")
            print("C) Benedikt XVI.")
            ans2=input("Unesite A, B ili C: ")
            ans2=ans2.casefold()
            if(ans2=="c" or ans2=="c)"):
                odgZaEval=2
            else:
                odgZaEval=1
            if(ansL=="c"):
                if odgZaEval==1:
                    lovEval=3
                else:
                    lovEval=4
            else:
                if odgZaEval==1:
                    lovEval=1
                else:
                    lovEval=2
        case 5:
            print("Kojem je umjetničkom stilu ime dao talijanski slikar Giorgio Vasari koji ga je smatrao barbarskim?")
            tocOdg="c"
            print("A) Baroku")
            print("B) Romanici")
            print("C) Gotici")
            ans2=input("Unesite A, B ili C: ")
            ans2=ans2.casefold()
            if(ans2=="c" or ans2=="c)"):
                odgZaEval=2
            else:
                odgZaEval=1
            if(ansL=="c"):
                if odgZaEval==1:
                    lovEval=3
                else:
                    lovEval=4
            else:
                if odgZaEval==1:
                    lovEval=1
                else:
                    lovEval=2
        case 6:
            print("Dereze najbolje služe za hodanje po kojoj površini?")
            tocOdg="b"
            print("A) Po pijesku")
            print("B) Po ledu")
            print("C) Po blatu")
            ans2=input("Unesite A, B ili C: ")
            ans2=ans2.casefold()
            if(ans2=="b" or ans2=="b)"):
                odgZaEval=2
            else:
                odgZaEval=1
            if(ansL=="b"):
                if odgZaEval==1:
                    lovEval=3
                else:
                    lovEval=4
            else:
                if odgZaEval==1:
                    lovEval=1
                else:
                    lovEval=2
        case 7:
            print("Osnovni sastojci provalonskog namaza tapenade su: Kapare, inćuni i...")
            tocOdg="a" #tek mi je tu palo napamet. Zašto ne u prvoj rundi? Nije mi palo napamet i bilo je manje pitanja.
            print("A) Masline")
            print("B) Paradajz")
            print("C) Orasi")
            ans2=input("Unesite A, B ili C: ")
            ans2=ans2.casefold()
            if(ans2=="a" or ans2=="a)"):
                odgZaEval=2
            else:
                odgZaEval=1
            if(ansL=="a"):
                if odgZaEval==1:
                    lovEval=3
                else:
                    lovEval=4
            else:
                if odgZaEval==1:
                    lovEval=1
                else:
                    lovEval=2
        case 8:
            print("Koji je od ovih romana najprije objavljen?")
            tocOdg="b"
            print("A) Zločin i kazna")
            print("B) Ponos i predrasuda")
            print("C) Rat i Mir")
            ans2=input("Unesite A, B ili C: ")
            ans2=ans2.casefold()
            if(ans2=="b" or ans2=="b)"):
                odgZaEval=2
            else:
                odgZaEval=1
            if(ansL=="b"):
                if odgZaEval==1:
                    lovEval=3
                else:
                    lovEval=4
            else:
                if odgZaEval==1:
                    lovEval=1
                else:
                    lovEval=2
        case 9: #do ovih pitanja i nadalje se dolaze samo ako je lovac glup i igrač ništa ne zna :) (bez uvrede igraču)
            print("Vlada koje je države za 2027. raspisala referendum o pristupanju u Europsku Uniju?")
            tocOdg="c"
            print("A) Švicarske")
            print("B) Norveške")
            print("C) Islanda")
            ans2=input("Unesite A, B ili C: ")
            ans2=ans2.casefold()
            if(ans2=="c" or ans2=="c)"):
                odgZaEval=2
            else:
                odgZaEval=1
            if(ansL=="c"):
                if odgZaEval==1:
                    lovEval=3
                else:
                    lovEval=4
            else:
                if odgZaEval==1:
                    lovEval=1
                else:
                    lovEval=2
        case 10: #HRTi neda da idem daleko, ovo je već treći put kad su mi makli prvo 10.5. pa 12.5 a sad moram 17.5.
            print("Koliko je trajao mandat Angele Merkel na mjestu njemačke kancelarke?") #Obećajem da su ovo sve prava pitanja iz Potjere, stvarno ne lažem. Ok, osim one sa append na Pythonu :)
            tocOdg="b"
            print("A) 11 godina i 11 dana")
            print("B) 16 godina i 16 dana")
            print("C) 7 godina i 7 dana")
            ans2=input("Unesite A, B ili C: ")
            ans2=ans2.casefold()
            if(ans2=="b" or ans2=="b)"):
                odgZaEval=2
            else:
                odgZaEval=1
            if(ansL=="b"):
                if odgZaEval==1:
                    lovEval=3
                else:
                    lovEval=4
            else:
                if odgZaEval==1:
                    lovEval=1
                else:
                    lovEval=2
        case 11:
            print('"Jednakost" 2+2=5 našla se u nazivu ovogodišnjeg dokumentarca o kojem književniku?')
            tocOdg="c"
            print("A) O Hemingwayu")
            print("B) O Marquesu")
            print("C) O Orwelu")
            ans2=input("Unesite A, B ili C: ")
            ans2=ans2.casefold()
            if(ans2=="c" or ans2=="c)"):
                odgZaEval=2
            else:
                odgZaEval=1
            if(ansL=="c"):
                if odgZaEval==1:
                    lovEval=3
                else:
                    lovEval=4
            else:
                if odgZaEval==1:
                    lovEval=1
                else:
                    lovEval=2
        case 12:
            print("Jidiš, jezik ašenaskih Židova se razvio u srednjem vijeku na području srednjeg toka rijeke...")
            tocOdg="a"
            print("A) Rajne")
            print("B) Jordana")
            print("C) Dnjepra")
            ans2=input("Unesite A, B ili C: ")
            ans2=ans2.casefold()
            if(ans2=="a" or ans2=="a)"):
                odgZaEval=2
            else:
                odgZaEval=1
            if(ansL=="a"):
                if odgZaEval==1:
                    lovEval=3
                else:
                    lovEval=4
            else:
                if odgZaEval==1:
                    lovEval=1
                else:
                    lovEval=2
        case 13:
            print("Koja je NBA momčad dobila ime po seriji o Divljem zapadu s James Garnerom u glavnoj ulozi?")
            tocOdg="a"
            print("A) Dallas")
            print("B) Denver")
            print("C) Portland")
            ans2=input("Unesite A, B ili C: ")
            ans2=ans2.casefold()
            if(ans2=="a" or ans2=="a)"):
                odgZaEval=2
            else:
                odgZaEval=1
            if(ansL=="a"):
                if odgZaEval==1:
                    lovEval=3
                else:
                    lovEval=4
            else:
                if odgZaEval==1:
                    lovEval=1
                else:
                    lovEval=2
        case 14:

#napokon, pitanja sa lovcem nakon sto godina zabave sa kornjačom
def drugaRundaKostur(): #a ja misl ovo pianja a nije
    global lPit, ans2, ansL, lovEval, kPozI, kPozL, ploca, rezultat, tocOdg #fakat ne znam što sve staviti u global iz prve dok ne počnem pisati funkciju pa nek sve ide
    print("Započinjemo sa prvim pitanjem.")
    for i in range(20):
        print("\nPitanje {0} od {1}\n".format(i+1,20))
        ansL=random.choice("abc") #lovac nasumično odgovara, nadam se da random radi sa char
        drugaRunda()
        print("Lovac je odgovorio:",ansL)
        print("Točan odgovor je:",tocOdg)
        lPit+=1
        match lovEval:
            case 1:
                print("Oboje ste krivo odgovorili.")
            case 2:
                print("Točno ste odgovorili.")
                kPozI = ploca.index(5)
                ploca[kPozI+1]=5
                ploca[kPozI]=3
                turtleMoveBoard()
            case 3:
                print("Lovac je točno odgovorio, a Vi niste!")
                if(ploca.index(7)==(ploca.index(5)-1)):
                    rezultat=1
                else:
                    kPozL = ploca.index(7)
                    ploca[kPozL+1]=7
                    ploca[kPozL]=3
                    turtleMoveBoard()
            case 4:
                print("Oboje ste točno odgovorili!")
                kPozI = ploca.index(5)
                ploca[kPozI+1]=5
                ploca[kPozI]=3
                turtleMoveBoard()
                kPozL = ploca.index(7)
                ploca[kPozL+1]=7
                ploca[kPozL]=3
                turtleMoveBoard()
            case _:
                print("case default error, kako li se to uopće dogodilo?")
            
        if rezultat==1:
            break
        if ploca.index(5)==7:
            rezultat=2
            break



#Lovac igra
def loviti():
    global ploca, ansL, ans2, nagrada
    ponuda()
    initTurleBoard()
    print("No, dosta o tome sada! Vidjeti ćemo možeš li me uopće pobijediti! Ha!")
    drugaRundaKostur()
    

    
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
    
#Lovac igra 
print("\n\nSuper je prošla igra, ali vrijeme je za igru protiv lovca!")
print("Moje ime je Laki Topalović i biti ću Vaš lovac za ovu rundu")
loviti()
#provjera rezultata druge runde
if rezultat==1:
        print("Ah, uhvatio sam Vas! Tako ste izgubili igru! Baš šteta, haha!")
        print("Ništa od nagrade! Želim Vam sreće sljedeći put! Sreće da ponovno izgubite! >:)")
        print("No, možete me ispričati, idem se zabaviti sa svojih {0} eura! haha!".format(nagrada))
elif rezultat==2:
        print("Kako je to moguće! Ja sam mislio da sam najpametniji ovdje!")
        print("Teško mi je to povjerovati, pogotovo prihvatiti, ali ste pobijedili sasvim zasluženo...")
        print("Samo uzmi svojih {0} eura i bježi od mene!".format(nagrada))
elif rezultat==0:
        print("Stvarno? Nakon 20 pitanja da nitko nije pobijedio? Niti igrač, niti lovac!")
        print("Pa kakvi ste Vi to igrač, a da o ''pametnom'' lovcu da ne pričam!")
        print("Uzeti ću si ja svojih {0} eura, ionako ih niste zaslužili!".format(nagrada))
else:
        print("huh")

input("\n\n\nPritisnite enter za izlaz iz igre\n")
