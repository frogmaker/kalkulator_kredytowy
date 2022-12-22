# kalkulator_kredytowy

Dla zadanych wartości oprocentowania, okresu kredytowania i kapitału kredytu,
program wylicza ratę kredytu z podziałem na kapitał i odsetki,
w wariancie dla raty stałej oraz malejącej.

Przykładowy wynik działania programu:

#############################################################

   Parametry kredytu:  300000.0 5.0 360.0

#############################################################

   Dla kredytu o ratach stałych:

   Miesięczna rata:  1610.46
   w tym:
   kapitał:  357.9
   odsetki:  1252.57

#############################################################

   Dla kredytu o ratach malejących:

   Rata kapitałowa (stała):  833.0
   Pierwsza rata:  2083 w tym odsetki:  1250
   Ostatnia rata:  836 w tym odsetki:  3

#############################################################

   Porównanie:

   Miesiąc w którym raty obu rodzajów kredytów się wyrównają: 136 ( 11 lat 4 m-c )

   Koszty kredytu (odsetki):
   raty stałe:  279767.35 vs. raty malejące:  225625.0

2083

    ''''''''......
    
                  ''''''''......
                  
*********************************************************************** 1610    raty stałe

                                 '''''......
                                 
                                             '''''''.......
                                             
                                                            '''''''....  836    raty malejące
                                                            

.............................................................................................

1 ..............................136....................................  360    miesiące
