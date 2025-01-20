"""Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű 
függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható 
szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!"""
import random

lista = [random.randint(0,20) for _ in range(10)]

def harommal_oszthatok(lista):
    hany_harommal_oszthato = 0
    for szam in lista:
        if szam % 3 == 0:
            hany_harommal_oszthato += 1
    return hany_harommal_oszthato

print(f"{harommal_oszthatok(lista)} hárommal osztható szám volt a listában")