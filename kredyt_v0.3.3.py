# -*- coding: UTF-8 -*-
import locale

# Set to users preferred locale:
locale.setlocale(locale.LC_ALL, '')
# Or a specific locale:
#locale.setlocale(locale.LC_NUMERIC, "en_PL.UTF-8")
import math
c = 2
print("#############################################################")
print("#   Kalkulator rat kredytu by frogmaker")
print("#   Kontakt z autorem: gg:5043515 ; serwis@hupla.pl ")
print("#############################################################")
while c == 2:


    print("")
    k = float(input("Wprowadź kwotę kredytu: ")) #kwota kredytu
    pp = input("wprowadź stawkę oprocentowania (np: 3.63): ") #stawka oprocentowania
    p = float(pp.replace(',', '.'))
    oo = float(input("wprowadź okres kredytowania w latach: ")) #okres kredytowania
    o = float(oo*12)

    kbak = k
    print("#############################################################")
    print("#")
    print("#   Parametry kredytu: ", k, p, o)
    print("#")
    print("#############################################################")
    def obliczrate(k, p, o):
        return float((k*((1 + (p/100/12))**o)*(p/100/12)/(((1+(p/100/12))**o)-1)))
    def obliczodsetki(k, p, o):
        return float(k*(p/100)*(30.5/365.25))
    rata = obliczrate(k, p, o)
    odsetki = obliczodsetki(k, p, o)
    def malejaca(k, p, o):
        return float(k/o)
    def miesiacwyrownania(k, p, o):
        return float((o/k)*(k-((1200/p)*(rata-(k/o)))))
    t = miesiacwyrownania(k, p, o)
    print("#")
    print("#   Dla kredytu o ratach stałych:")
    print("#")
    print("#   Miesięczna rata: ", round(rata, 2))
    print("#   w tym:")
    print("#   kapitał: ", round(rata - odsetki, 2))
    print("#   odsetki: ", round(odsetki, 2))
    print("#")
    print("#############################################################")
    print("#")
    print("#   Dla kredytu o ratach malejących: ")
    print("#")
    print("#   Rata kapitałowa (stała): ", round(malejaca(k, p, o), 0))
    PR = float(malejaca(k, p, o)+(k*p/1200))
    ODSmal1 = float(k*p/1200)
    print("#   Pierwsza rata: ", math.floor(PR), "w tym odsetki: ", math.floor(ODSmal1))
    OR = float(malejaca(k, p, o)+(malejaca(k, p, o)*p/1200))
    ODSmal0 = float(malejaca(k, p, o)*p/1200)
    print("#   Ostatnia rata: ", math.floor(OR), "w tym odsetki: ", math.floor(ODSmal0))
    print("#")
    print("#############################################################")
    print("#")
    print("#   Porównanie:")
    print("#")

    print("#   Miesiąc w którym raty obu rodzajów kredytów się wyrównają:", math.floor(t), "(", math.floor(t/12), "lat", math.floor(t)-math.floor(t/12)*12,  "m-c )")
    print("#")
    print("#   Koszty kredytu (odsetki):")
    print("#   raty stałe: ", round(rata*o-k, 2), "vs.", "raty malejące: ", round((ODSmal1+ODSmal0)/2*o, 2))
    print("#")
    print("")
    print("#")
    print("#", math.floor(PR))
    print("#", "     '''''''......")
    print("#", "                  '''''''......")
    print("#", "***********************************************************************", math.floor(rata), "   raty stałe")
    print("#", "                              '''''''......")
    print("#", "                                            '''''''......")
    print("#", "                                                          '''''''......", math.floor(OR), "    raty malejące")
    print("#")
    print("__________________________________________________________________________")
    print("1", "...........................", math.floor(t), ".......................................", math.floor(o), "     [miesiące]")
    print("")
    print("")
    c = float(1)
    input("Press ENTER to contiune...")
    while c == 1:
        print("wybierz symulację raty kredytu:")
        print("1 - powtórz symulację")
        print("2 - zmiana stopy procentowej (rata stała)")
        print("3 - zmień parametry kredytu (rata stała)")
        print("4 - nadpłata (rata stała)")
        print("5 - wesprzyj autora")
        print("6 - zakończ")
        z = input()

        if z == "4":
            print("wprowadź kwotę nadpłaty:")
            n = float(input())
            k = kbak - n
            rata = obliczrate(k, p, o)
            odsetki = obliczodsetki(k, p, o)
            print("Nowa rata po nadpłacie:", round(rata, 2), "w tym kapitał:", round(rata - odsetki, 2), "odsetki:",  round(odsetki, 2))
            k = kbak
            input("Press ENTER to contiune...")
    
        elif z == "2":
            print("wprowadź marzę banku w % (np: 1.80):")
            marzap = (input())
            marza = float(marzap.replace(',', '.'))
            print("wprowadź stawkę WIBOR6M w % (np: 1.83):")
            wiborp = (input())
            wibor = float(wiborp.replace(',', '.'))
            pbak = p
            p = marza + wibor
            print("Nowa stawka oprocentowania:" , p,"%")
            input("Press ENTER to contiune...")
            rata = obliczrate(k, p, o)
            odsetki = obliczodsetki(k, p, o)
            print("Nowa rata po zmianie oprocentowania:", round(rata, 2), "w tym kapitał:", round(rata - odsetki, 2), "odsetki:",  round(odsetki, 2))
            p = float(pbak)
            input("Press ENTER to contiune...")
        
        elif z == "3":
            print("wprowadź nowe oprocentowanie:")
            pp = (input())
            p = float(pp.replace(',', '.'))
            print("wprowadź nową kwotę kredytu:")
            k = float(input())
            print("wprowadź nowy okres kredytowania:")
            o = float(input())
            print("Parametry kredytu: ", k, p, o)
            rata = obliczrate(k, p, o)
            odsetki = obliczodsetki(k, p, o)
            print("Miesięczna rata:", round(rata, 2))
            print("w tym:")
            print("kapitał:", round(rata - odsetki, 2))
            print("odsetki:", round(odsetki, 2))
            input("Press ENTER to contiune...")

        elif z == "5":
            print("Bitcoin (BTC): 17dgi8g3XyT2JcuHp76R4He8Yp28iJvbyB")
            print("Bitcoin Cash (BCC): qp92jhsqa6dqt0enffsmjmrh953gff3rxufe2c2vyw")
            print("Litecoin (LTC): LcUr5bWoTDwUsFfTdME62zSMJYcCQpCV3H")
            print("Iridium (ird): ir47aGcna4jaUn8tk9s8tBFT9uuFncDG8T8SZn78nd4kN4eUhYtzeFMFdSXT8G43AsELZf48PzFwoUGKQGRWjZK414NSu1PCq")
            print("Scala (xla): SvjvQckKCqic8qhHgREnY5ScSgigqAt5o2cEDrPcCPn72idRsooW2HJdMYUJqJSULuLAFHfKbhKFCC9xgU2Fkqg71BpmuANbe")
            input("Press ENTER to contiune...")
        elif z == "1":
            c = float(2)
        else:
            c = 0, input("Press ENTER to exit")