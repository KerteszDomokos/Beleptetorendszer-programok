"""
Copyrighth
    Kertész Domokos
    kerteszdomokos@gmail.com

Projekt: Értelmező Beléptető
Verzió:v3.1
Élesben teszt!
"""
import sqlite3
    
def osztalyzas (sorok, ssz):
    q=0
    datesemenykod={}
    esem={}
    dat=sorok[1]
    riaszt_t=[]
    riaszt_e=[]
    while q<ssz:
        if q%2==0:
            dat=sorok[q]
            print(sorok[q].strip())
            
        else:    
            vizsg=sorok[q]
            datesemenykod[dat] = vizsg
            #print(vizsg)
            if vizsg=='bk 1\n':
                es ='Kertész Domokos belépett'
                esem[dat]="Kertész Domokos belépett"
                es="Kertész Domokos belépett"
                print("Kertész Domokos belépett")
                ez=[dat, es]
                curs.execute("INSERT INTO Belépések VALUES(?, ?)", ez)
            
            
            if vizsg=='bk 2\n':
                es ='[szemely1] belépett'
                esem[dat]='[szemely1] belépett'
                es='[szemely1] belépett'
                print('[szemely1] belépett')
                ez=[dat, es]
                curs.execute("INSERT INTO Belépések VALUES(?, ?)", ez)
            
            
            if vizsg=='bk 3\n':
                es ='[szemely2] belépett'
                esem[dat]='[szemely2]'
                es ='[szemely2]'
                print('[szemely2]')
                ez=[dat, es]
                curs.execute("INSERT INTO Belépések VALUES(?, ?)", ez)
            
            
            if vizsg=='bk 4\n':
                es ='[szemely3] belépett'
                esem[dat]='[szemely3]'
                es ='[szemely3]'
                print('[szemely3]')
                ez=[dat, es]
                curs.execute("INSERT INTO Riasztások VALUES(?, ?)", ez)
            
            
            if vizsg=='bk 5\n':
                es ='[szemely4] belépett'
                esem[dat]='[szemely4]'
                es ='[szemely4]'
                print('[szemely4]')
                ez=[dat, es]
                curs.execute("INSERT INTO Riasztások VALUES(?, ?)", ez)
            
            
            if vizsg=='bk 6\n':
                es ='[szemely5] belépett'
                esem[dat]='[szemely5]'
                es ='[szemely5]'
                print('[szemely5]')
                ez=[dat, es]
                curs.execute("INSERT INTO Riasztások VALUES(?, ?)", ez)
            
            
            if vizsg=='bk 7\n':
                es ='[szemely6] belépett'
                esem[dat]='[szemely6]'
                es ='[szemely6]'
                print('[szemely6]')
                ez=[dat, es]
                curs.execute("INSERT INTO Riasztások VALUES(?, ?)", ez)
            
            
            if vizsg=='bk 8\n':
                es ='Elrontott jelszó!'
                esem[dat]='Elrontott jelszó!'
                es ='Elrontott jelszó!'
                print('Elrontott jelszó!')
                ez=[dat, es]
                curs.execute("INSERT INTO Riasztások VALUES(?, ?)", ez)
            
            
            if vizsg=='bl\n':
                es ='Belépés érzékelve'
                esem[dat]='Belépés érzékelve'
                es ='Belépés érzékelve'
                print('Belépés érzékelve')
                ez=[dat, es]
                curs.execute("INSERT INTO Riasztások VALUES(?, ?)", ez)
            
            
            if vizsg=='r 1\n':                              #Riasztások külön műveletei
                riaszt_t.append(dat)
                riaszt_e.append(vizsg)
                ez=[dat,'Riszt! Belépés érzékelő']
                curs.execute("INSERT INTO Riasztások VALUES(?, ?)", ez)
                print('A riasztások táblába insertálva.')
                esem[dat]='Riszt! Belépés érzékelő'
                es ='Riszt! Belépés érzékelő'
                print('Riszt! Belépés érzékelő')
            
            
            if vizsg=='r 2\n':
                riaszt_t.append(dat)
                riaszt_e.append(vizsg)
                ez=[dat,'Riaszt! Mozgás érzékelő']
                curs.execute("INSERT INTO Riasztások VALUES(?, ?)", ez)
                print('A riasztások táblába insertálva.')
                esem[dat]='Riaszt! Mozgás érzékelő'
                es ='Riaszt! Mozgás érzékelő'
                print('Riaszt! Mozgás érzékelő')
            
            
            if vizsg=='r 3\n':
                riaszt_t.append(dat)
                riaszt_e.append(vizsg)
                ez=[dat,'Riszt!Széf kinyitás']
                curs.execute("INSERT INTO Riasztások VALUES(?, ?)", ez)
                print('A riasztások táblába insertálva.')
                esem[dat]='Riszt!Széf kinyitás'
                es ='Riszt!Széf kinyitás'
                print('Riszt!Széf kinyitás')
            
            
            if vizsg=='r 4\n':                              #Riasztások külön műveletek vége
                riaszt_t.append(dat)
                riaszt_e.append(vizsg)
                ez=[dat,'Riaszt! Áramtalanítás']
                curs.execute("INSERT INTO Riasztások VALUES(?, ?)", ez)
                print('A riasztások táblába insertálva.')
                esem[dat]='Riaszt! Áramtalanítás'
                es ='Riaszt! Áramtalanítás'
                print('Riaszt! Áramtalanítás')
            
            
            if vizsg=='o\n':
                es ='Széf nyitva'
                esem[dat]='Széf nyitva'
                es ='Széf nyitva'
                print('Széf nyitva')
            
            
            if vizsg=='ki 2\n':
                es ='Kilépés felhesználó kérésére'
                esem[dat]='Kilépés felhesználó kérésére'
                es ='Kilépés felhesználó kérésére'
                print('Kilépés felhesználó kérésére')
            
            
            if vizsg=='ki 1\n': 
                es ='Kilépés inaktivitás miatt'
                esem[dat]='Kilépés inaktivitás miatt'
                es ='Kilépés inaktivitás miatt'
                print('Kilépés inaktivitás miatt')
            
            
            if vizsg=='pir 1\n':
                es ='Mozgásérzékelés 1. szektor'
                esem[dat]='Mozgásérzékelés 1. szektor'
                es ='Mozgásérzékelés 1. szektor'
                print('Mozgásérzékelés 1. szektor')
            
            
            if vizsg=='pir 2\n':
                es ='Mozgásérzékelés 2. szektor'
                esem[dat]='Mozgásérzékelés 2. szektor'
                es ='Mozgásérzékelés 2. szektor'
                print('Mozgásérzékelés 2. szektor')
            
            
            if vizsg=='rst\n':
                es ='Újraindítás'
                esem[dat]='Újraindítás'
                es ='Újraindítás'
                print('Újraindítás')
                
                
            ad=[dat, es]
            curs.execute("INSERT INTO Események VALUES(?, ?)", ad)
            

            
            
            
        q=q+1
    #print(datesemenykod['03.09.2019 19:26:36 \n'])
    #print("Könyvtárból:",esem['03.09.2019 19:22:33 \n'])
    #print(esem)
    



def main():
    sor=file.readlines()
    f=0
    hossz=len(sor)
    while f<hossz:
        f=f+1
        osztalyzas(sor, hossz)
    file.close()
    conn.commit()
    conn.close()
    
#előre meghatározott kódokkal egyenlővé tett eseményeket tartalmazó fájl elérési útja
eleres='D:/kodolt.txt'

file = open (eleres, 'r', encoding='utf8')

conn = sqlite3.connect('[database source]')
curs = conn.cursor()
curs.execute("CREATE TABLE IF NOT EXISTS Események (Datum TEXT, Esemeny TEXT)")
curs.execute("CREATE TABLE IF NOT EXISTS Riasztások (Dátum TEXT, Riasztás_oka TEXT)")
curs.execute("CREATE TABLE IF NOT EXISTS Belépések (Dátum TEXT, Belépő személy TEXT)")

main()
print("Program vége")
input("end")

