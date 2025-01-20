"""Írj eljárást, amely paraméterül kapott 2 számot összehasonlít, 
és a képernyőre kiírja, melyik a nagyobb szám! 
Kezeld azt az esetet is, ha a két szám egyenlő!"""

def osszehasonlitas(szam1, szam2):
    if szam1>szam2:
        print("Az első szám nagyobb")
    elif szam2>szam1:
        print("A második szám nagyobb")
    else:
        print("A két szám egyenlő")
osszehasonlitas(3,0)