"""
Copyrighth
    Kertész Domokos
    kerteszdomokos@gmail.com

Projekt: Távvezérlés parancssora
Verzió:v1.3
"""

import requests
import ast
import os
import sys
if "G:\\Privát adatok\\Arduino\\Projektek\\Belepteto_fenti_szoba\\RasberryPi" not in sys.path:
    sys.path.append("G:\\Privát adatok\\Arduino\\Projektek\\Belepteto_fenti_szoba\\RasberryPi")
    print("Hozzáadva")



def bej():
    j=input("Kérem a jelszót!\nJelszó:")
    os.system('cls' if os.name == 'nt' else 'clear')
    if j==jelszo:
        return 1
    else:
        return 0

def betolt(be):
    print("Beléptetőrendszer adatainak betöltése...\nA kért mennyiségű adatot betöltöm...\n")
    
    ElsoInd(be)
    return "Betöltés sikeres"
def datum_alakit(d):
    f=d.replace("Z", " ")
    veg=f.replace("T", "  ")
    return veg
    
def beep(*ert):
    try:
        serw('2')
        print("Sípolás bekapcsolva!")
    except:
        print("ERROR: serw() függvény sikertelen meghívás")
    
    
def beepoff(*a):
    serw('3')
    print("Sípolás kikapcsolva!")
    
    
def szamval(r): #Itt választja ki azt a számot, melyet értelmez
    v=r.json()
    v=str(v)
    dic=ast.literal_eval(v)
    ert=''
    ert=dic['feeds']
    dic2=ast.literal_eval(str(ert))
    i=0
    dic3={}
    dic3=ast.literal_eval(str(dic2[1]))
    szam=dic3['field1']
    dat=dic3['created_at']
    datv=datum_alakit(dat)
    return szam, datv
    
    
def osztalyzas(badat, datu): # Osztályozza, és kiírja az adatokat
    try:
        feld=int (badat)
        try:
            es=kod[feld]
            if feld!=20:
                print("\n", datu,"   -----------  ",  es,"\n")
        except KeyError:
            print("\nERROR:  01, Key error in dictionary")
            errs=errs+1
        except:
            print("\nERROR: Ismeretlen hiba!")
            errs=errs+1
    except:
        print("\n","ERROR:  2. Nem értelmezhető üzenet!")
        print(badat)
        errs=errs+1
    
def ElsoInd(be): # Az Indítás után egyszer lefutó programrészlet
    print("         Dátum:                              Esemény:\n")
    urlElsor='https://api.thingspeak.com/channels/1012388/feeds.json?api_key=[key]'
    urlElsore=urlElsor+str(be)
    try:
        e=requests.get(urlElsore, timeout=5)
        v=e.json()
        v=str(v)
        try:
            dic=ast.literal_eval(v)
            ert=''
            ert=dic['feeds']
            dic2=ast.literal_eval(str(ert))
            i=0
            dic3={}
            while  len(dic2)>i:
                dic3=ast.literal_eval(str(dic2[i]))
                szam=dic3['field1']
                dat=dic3['created_at']
                datv=datum_alakit(dat)
                osztalyzas(szam, datv)
                i=i+1
            print("\n...betöltés befejeződött. ")
        except:
            print("ERROR: Egyéb hiba")
        
    except:
        print("ERROR: Internetkapcsolati hiba!")
def command(ert):
    print("Teszt OK",ert)


def serw(dat):
    datas="2"+dat
    send(datas)
    

def help(ert):
    print("Segítség: ")
    print(helptext)

def send (uz):
    url=urla+uz
    try:
        e=requests.get(url, timeout=5)
        print("Eredmény: e.json() =",e.json())
        while int(e.json())==0:
            e=requests.get(url, timeout=5)
            print(e.json(), " ",end='', flush=True)
        print()
    except:
        print("ERROR: Hálózati hiba")
def sp(text):
    send(text)
    
def akt(*args):
    serw('1')
    print("A rendszert aktivizáltam! Ellenőrizze a távoli felügyelettel! (inf parancs)")
    
def cl(v):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("                 ©Kertész Domokos 2020\nBeléptetőrendszer távoli vezérlés parancssora. Internetkapcsolat szükséges!\nInformációk: kerteszdomokos@gmail.com\nMinden jog fenntertva! Terjeszteni tilos!\nSegítséghez írja be a help, vagy a h parancsot!")
    
def live(ert):
    ert=input("Ebből a parancsból  nem tud a továbbiakban kilépni.\nFolytatja? [i/n]")
    if ert!="i":
        print("Végrehajtás megszakítva! Kilépés... OK")
        return
    
    else:
        print("\n...betöltés befejeződött. \nA program innentől valós időben keletkező adatokat mutat.\n\n")
        print("        Dátum:                         Esemény:\n")
        while True:# A folyamatos futás itt zajlik
            r=requests.get(urlread, timeout=5)
            sz=szamval(r)# sz változó a lényeg! list típusú!
            
            if sz[0]=='20':
                a=''
            else:
                if sz_arch != sz:
                    osztalyzas(sz[0], sz[1])
                    sz_arch=sz
                else:
                    print("#", end='', flush=True)
                    
def err(val):
    print(errortxt)

def parancs(parancsokk, args):
    try:
        return parancsokk(args)
    except:
        print("Parancs végrehajtása sikertelen! Err: függvényhiba0")
        errs=errs+1
    
parancsok={ "comm":command, 
            "help":help,
            "h":help,
            "send":send, 
            "sp":sp,
            "inf":betolt,
            "serw":serw,
            "aakt":akt,
            "del":cl,
            "cls":cl,
            "beepon":beep,
            "beepoff":beepoff,
            "live":live,
            "err":err,
            "akt":akt
            }


urla='https://api.thingspeak.com/update?api_key=[key]&field1='
urlread='https://api.thingspeak.com/channels/1012388/feeds.json?api_key=[key]&results=2'

kod=    {   # A kódolás értelmezésére létrehozott szótár
         0: "ERR.:KeyIs0",
         1: "Kertész Domokos belépett",
         2: "[szemely1] belépett",
         3: "[szemely2] belépett",
         4: "[szemely3] belépett",
         5: "[szemely4] belépett",
         6: "[szemely5] belépett",
         7: "[szemely6] belépett",
         8: "Jelszó elrontva a külső panelen",
         9: "Belépés érzékelővel",
         10:"Széf nyitás",
         11:"Kilépés",
         12:"Mozgásérzékelve",
         13:"RESET - A rendszer újraindult",
         14:"Arduino Error1"
         }

helptext= """
Parancsok:
			comm: 
			teszt parancs
			argumentumok:nincs
            
			help:
			segítség kinyeréséhez
			argumentumok:nincs
            
			h:
			segítség kinyeréséhez
			argumentumok:nincs
            
			send:
			adat feltöltés közvetlenül a ThingSpeak szerverére
			argumentumok:feltöltendő adat
            
			sp:
			beszéd átküldése a Rasberry Pire
			argumentumok: kimondandó szöveg
            
			inf:
			Kiírja az adat letöltő program kódját használva az információkat
                További info: Ez azt jelenti, hogy láthatjuk a beléptetőrendszer adatait, de nem élőben! 
                    Gyakran találkozhatunk hibákkal!
                    Az adatbetöltés számának irányítása is gyakran hibába ütközik!
                    Ez a parancs fejlesztés alatt áll!
			argumentumok:ahány darab eseményt szeretnénk lekérdezni
            
			serw:
			Az arduino sofrwarére küldendő adat
			argumentumok:kód
            
			aakt:			
			A rendszer aktivizálása. Arduino-nak küldi, soros porton
			argumentumok:nincs
			
            
			del:
			Törli a konzolt
			argumentumok:nincs
            
			cls:
			Törli a konzolt	
			argumentumok:nincs
            
			beep:
			Bekapcsolja a hangszórót
			argumentumok:nincs
            
			beepoff:
			Kikapcsolja a hangszórót
			argumentumok:nincs
            
            exit:
			Kilépés a futásból. Lezáró adatok megtekintése. Amennyiben nem kíváncsi az adatokra, csak zárja be az ablakot!
			argumentumok:nincs
            
            err:
			Kiírja az összes a csomaghoz tartozó program hibaüzeneteit, és magyarázatát
			argumentumok:nincs
            
Ha nincs argumentum, akkor csak nyomjon enter-t ha kérdezi a program!

"""
errortxt="""

											Hibák leírása

Adat letöltő: (ugyanígy a távvezérlő hasonló részei)
Arduino Error1:
    -SD kártya nem elérhető
    
ERROR:  01, kulcs hiba a szótárban:
	-Nem értelmezhető az üzenet, amely kódolva érkezett. A szótárban nem található a keresett kulcs
	
ERROR: Ismeretlen hiba!:
	-Sikertelen osztályzás. A hiba ismeretlen, de nem KeyError (lásd: előző)
	
ERROR:  2. Nem értelmezhető üzenet! (a nem értelmezhető üzenet):
	-A kódolt üzenet sikertelen értelmezése. Leggyakabban a konvertálással szokott gond lenni
	
ERROR: Valószínűsíthető hálózati hiba (1. ERR_TIMED_OUT):
	-Nem tudja végrehajtani a HTTP GET kérést. Általában az internetkapcsolat hiányát jelenti

Feltöltő:
ERROR: Valószínűsíthető hálózati hiba (1. ERR_TIMED_OUT):
	-Nem tudja végrehajtani a HTTP GET kérést. Általában az internetkapcsolat hiányát jelenti

File-iro:
ERROR: Serial connection - Próbálja csatlakoztatni az eszközt, illetve beállítani a portot
	-Sikertelen csatlakozás a megadott porthoz. Oka lehet a platformok közti különbség

Error: olvasásás sikertelen
	-A soros porton érkező adatok olvasása sikertelen. Ha az ERROR: Serial connection megjelent ez is meg fog jelenni
	
ERROR: Hozzáfűzés siekrtelen
	- A filehoz csatolás sikertelen. Ok nem ismert
	
ERROR: Nullérték
	-Az érkező érték nulla, ezt figyelmen kívül hagyja. Oka általában jelzavar a kommunikációban


Távvezérlő:
ERROR: Egyéb hiba
    -A konvertálásnál, ill értelmezésnél adódó esetleges hibák

ERROR: Internetkapcsolati hiba!
    -Ha nem egyéb hiba, a .json(), illetve a GET kérésnél adódó hibák

"""

jelszo="j"
e=bej()
ps=0
errs=0
if e==1:
    print("                 ©Kertész Domokos 2021\nBeléptetőrendszer távoli vezérlés parancssora. Internetkapcsolat szükséges!\nInformációk: kerteszdomokos@gmail.com\nMinden jog fenntertva! Terjeszteni tilos!\nSegítséghez írja be a help, vagy a h parancsot!")
    while True:
        
        command = input("\n>>>>")
        if command=="exit":
            break
        try:
            parancsok[command]
            bemenetek=input("argument >>>>")
            parancs(parancsok[command],bemenetek)
        except:
            print("Parancs nem felismerhető")
            errs=errs+1
        ps=ps+1
     

    print("Összegző adatok:")
    print("Kiadott parancsok száma ",ps+1)
    print("Hibák száma: ",errs)

else:
    print("Sikerelen bejelentkezés! Adat mentése...OK")





print("Program vége")
input()

