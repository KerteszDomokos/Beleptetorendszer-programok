"""
Copyrighth
    Kertész Domokos
    kerteszdomokos@gmail.com

Projekt: Távvezérlés
Verzió:v1.1
"""
import requests
import ast
from gtts import gTTS
from playsound import playsound
import os
import serial

url='https://api.thingspeak.com/channels/1038345/feeds.json?api_key=[key]&results=2'

def beszed(szoveg):
    try:
        #platform: Windows
        tts = gTTS(text=szoveg, lang='hu')
        tts.save("G:\impro.mp3")
        playsound("G:\impro.mp3")
        playsound("G:\lezar.wav")
        os.remove("G:\impro.mp3")
        """
        # platform: Linux:
        try:
            tts = gTTS(text=szoveg, lang='hu')
            tts.save("./impro.mp3")
            playsound("./impro.mp3")
            playsound("./lezar.wav")
            os.remove("./impro.mp3")
        except:
            print("ERROR: OPrendszer egyedi lejátszás hiba")
        """
    except AssertionError:
        print("ERROR: Nincs kimondandó szöveg!")
    except:
        print("ERROR: Egyéb hiba")
    
def serkuld(data):

    print("Serkuld() fügvényben")
    #print(bytes(data))
    try:
        
        ser.write(data.encode())
        print(data.encode())
        print("Sikeres küldés!")
    except:
        print("Sikertelen küldés a serporton")
        
    return 1

def command(ert):
    print("OK",ert)


def vegrehajt(func,arg):
    return func(arg)


def szamval(): # értelmezendő karakter kiválasztása
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
    return szam, dat


parancsok={ '0':command,
            '1':beszed,
            '2':serkuld
            }
sz_arch=[]
try:
    ser=serial.Serial(timeout=2, port='com8', baudrate='9600', write_timeout=.5)#platform: Windows
    print("Soros kommunikáió konfigurálása sikeres")
    
except:
    print("ERROR: Serial connection\nPróbálja csatlakoztatni az eszközt, illetve beállítani a portot")
    

while True:# A folyamatos futás itt zajlik
        r=requests.get(url, timeout=5)
        sz=szamval()        
        if sz_arch != sz:
            print("\n",sz[0])
            kulcs=str(sz[0])
            if sz[0]in parancsok.keys():
                v=vegrehajt(parancsok[kulcs],0)
            else:
                kl=list(kulcs)
                if len(kl)<5:
                    print(kl[0],kl[1])
                    v=vegrehajt(parancsok[kl[0]],kl[1])
                else:
                    beszed(kulcs)
            sz_arch=sz
        else:
            print("#", end='', flush=True)




print("Program vége")
input("end")

