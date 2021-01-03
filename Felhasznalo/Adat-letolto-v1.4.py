"""
Copyrighth
    Kertész Domokos
    kerteszdomokos@gmail.com

Projekt: Beléptető IoT
Verzió:v1.4
"""

import requests
import ast
import os

url='https://api.thingspeak.com/channels/1012388/feeds.json?api_key=[key]&results=2'
urlElsore='https://api.thingspeak.com/channels/1012388/feeds.json?api_key=[key]&results=100'

jelszo='j'

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
         14:"Arduino Error1",
         15:"Távvezérlés adatát sikeresen megkapta az arduino, és végre is hajtotta"
         
         }

def datum_alakit(d):
    f=d.replace("Z", " ")
    veg=f.replace("T", "  ")
    return veg


def szamval(): #Itt választja ki azt a számot, melyet értelmez
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
        except:
            print("\nERROR: Ismeretlen hiba!")
    except:
        print("\n","ERROR:  2. Nem értelmezhető üzenet!")
        print(badat)
    
    
def ElsoInd(): # Az Indítás után egyszer lefutó programrészlet
    print("         Dátum:                              Esemény:\n")
    v=e.json()
    v=str(v)
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
    print("\n...betöltés befejeződött. \nA program innentől valós időben keletkező adatokat mutat.\n\n")
    print("        Dátum:                         Esemény:\n")

#Program innen kezdi a futását!


be=input("Kérem a hozzáférési jelszót:  ")
if be!=jelszo:
    aw=0
    print("Hozzáférés megtagadva!\nAz erről szóló adatok feltöltése.....OK\n\n\n\n")
else:
    aw=1
    os.system('cls' if os.name == 'nt' else 'clear')
    print("OK")
if aw==1:
    print("Elindítás!\nA program 100 esetet (ha kevesebb esemény van mint 100, akkor az összeset) az előbbiekből betölt...\n\n")
    try:
        e=requests.get(urlElsore, timeout=5)
    except:
        print("ERROR: Valószínűsíthető hálózati hiba (1. ERR_TIMED_OUT)")
    ElsoInd()
    sz_arch=''
    while aw==1:# A folyamatos futás itt zajlik
        try:
            r=requests.get(url, timeout=5)
            sz=szamval()# sz változó a lényeg! list típusú!
            
            if sz[0]=='20':
                a=''
            else:
                if sz_arch != sz:
                    osztalyzas(sz[0], sz[1])
                    sz_arch=sz
                #else:#print("#", end='', flush=True)
        except:
            print("ERROR: Valószínűsíthető hálózati hiba (1. ERR_TIMED_OUT)")        
            
    
print("Program vége")
input("end")

