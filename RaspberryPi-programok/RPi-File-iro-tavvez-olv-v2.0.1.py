"""
Copyrighth
    Kertész Domokos
    kerteszdomokos@gmail.com

Projekt: RasberryPi file-író program, távvezérlés olvasóval együtt
Verzió:v2.0.1
"""

import serial
import requests
import ast
from gtts import gTTS
from playsound import playsound
import os

url='https://api.thingspeak.com/channels/1038345/feeds.json?api_key=[key]&results=2'

def beszed(szoveg):
    """try:
        tts = gTTS(text=szoveg, lang='hu')
        tts.save("G:\impro.mp3")
        playsound("G:\impro.mp3")
        playsound("G:\lezar.wav")
        os.remove("G:\impro.mp3")
        """
        #Linux:
    try:
        tts = gTTS(text=szoveg, lang='hu')
        tts.save("./impro.mp3")
        playsound("./impro.mp3")
        playsound("./lezar.wav")
        os.remove("./impro.mp3")
    
    except AssertionError:
        print("ERROR: Nincs kimondandó szöveg!")
    except:
        #print("ERROR: Egyéb hiba")#windows
        print("ERROR: OPrendszer egyedi lejátszás hiba")#raspbian
    
def serkuld(data):

    print("Serkuld() fügvényben")
    #print(bytes(data))
    try:
        
        ser.write(data.encode())
        print(data.encode())
        print("Sikeres küldés!")
    except:
        print("Sikertelen csatlakozás a soros porthoz")
        
    return 1

def command(ert):
    print("OK",ert)


def vegrehajt(func,arg):
    return func(arg)


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
    return szam, dat


parancsok={ '0':command,
            '1':beszed,
            '2':serkuld
            }
sz_arch=[]

def hozzf(szoveg):
    with open('./buffer.txt', 'a', encoding='utf-8') as file: #az elérési útvonal csak RP-n működik, különben, RP elérési: ./buffer.txt
        file.write(szoveg+'\n')
        print("Sikeres file-írás!", szoveg)

try:
    ser=serial.Serial(timeout=.1, port='com8', baudrate='9600')
    
except:
    print("ERROR: Serial connection\nPróbálja csatlakoztatni az eszközt, illetve beállítani a portot")



while True:
    try:
        r=requests.get(url, timeout=5)
    except:
        print("Error: Internet hiba")
    
    sz=szamval()# sz változó a lényeg! list típusú!
    #print(sz)
    if sz_arch != sz:
        print("\n",sz[0])
        kulcs=str(sz[0])
        if sz[0]in parancsok.keys():
            v=vegrehajt(parancsok[kulcs])
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
    try:
        dat=ser.readline()
        #print(dat)
        try:
            kod=int(dat)
            try:
                if kod!=0:
                    hozzf(str(kod))
                else:
                    print("ERROR: Nullérték")

            except:
                print("ERROR: Hozzáfűzés siekrtelen")
                
                
        except:
            pass
    except:
        print("Error: olvasásás sikertelen")
        break
