"""Készítsen függvényt random_gyumik néven, ami egy 30 elemű listát ad vissza. 
A lista elemei véletlenszerűen jönnek létre az alábbi szavak közül válogatva:
"alma" ; "körte"; "szilva"; "barack"; "málna"; "füge"; "eper" <--- itt legyen egy commit, ha kész!
*) Módosítsa a függvényt úgy, hogy legyen egy paramétere, ami meghatározza hogy a lista hány elemmel jöjjön létre!
(a korábbi 30 helyett) <--- itt is legyen egy commit!"""
import random
lista = ["alma", "körte", "szilva", "barack", "málna", "füge", "eper"]

def random_gyumik():
    random_lista = [random.choice(lista) for _ in range(30)]
    return random_lista
print(random_gyumik())