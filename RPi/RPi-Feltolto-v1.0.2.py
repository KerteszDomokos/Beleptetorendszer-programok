"""
Copyrighth
    Kertész Domokos 2020
    kerteszdomokos@gmail.com

Projekt: RasberryPi teljes csomag része
Verzió:v1.0.1
"""

import requests
import ast
import os


def fileread():
    with open('./buffer.txt', 'r', encoding='utf-8') as file: #az elérési útvonal csak RP-n működik, különben, RP: ./buffer.txt
        elsosor=file.readline()
        
        if elsosor=="":
            return 111
        else:
            print("Aktuális sor értéke: ",elsosor)
            with open('G:/buffer.txt', 'r', encoding='utf-8') as filedel:
                sorok=[]
                for sor in filedel:
                    sorok.append(sor)
            print(sorok[0])
            elsosor=sorok[0]
            with open('G:/buffer.txt', 'w', encoding='utf-8') as filedel:
                i=1
                while i<len(sorok):
                    filedel.write(sorok[i])
                    i=i+1
            #print(sorok)   
            return int(elsosor)



ert=0
urla='https://api.thingspeak.com/update?api_key=[key]&field1='
ki=''
ert=fileread()


while True:
    
    url=urla+str(ert)
    #print(ert)
    if ert!=111:
        try:
            e=requests.get(url, timeout=5)
            print("Üzenet küldése, érték: ", ert, " ...")
            while int(e.json())==0:
                e=requests.get(url, timeout=5)
                print("#",end='', flush=True)

            print(" 100%\nElküldve\n")
        except:
            print("ERROR: Valószínűsíthető hálózati hiba")
        

        print(" ")
        ert=fileread()
    else:
        a=0
        print("File üres. Várakozás a tartalomra...")
        while a==0:
            mv=fileread()
            if mv!=111:
                print("...tartalom érkzett!")
                a=1
                ert=mv
    

