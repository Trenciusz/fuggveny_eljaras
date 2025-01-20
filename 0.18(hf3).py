"""Írj egy programot, amelyben van egy 'kerulet' nevű
függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is! 
Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét 
(0 tetszőleges paraméter: négyzet, 1 tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszőg, 
3 vagy több tetszőleges paraméter: sokszög)!
A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!"""

def kerulet(x, *args):
    if len(args) == 0:
        print("Négyzet", f"Kerület = {4*x}", sep = "\n")
    elif len(args) == 1:
        print("Téglalap", f"Kerület = {2*(x+sum(args))}", sep = "\n")
    elif len(args) == 2:
        print("Háromszög", f"Kerület = {x+ sum(args)}", sep = "\n")
    else:
        print("Sokszög", f"Kerület = {x+sum(args)}", sep = "\n")

kerulet(1)
kerulet(2,3)
kerulet(4,5,6)
kerulet(7,8,9,10,11,12,13)

"Azért telt el ilyen sok idő ez, és az előző commit közt mert közben elmentem enni"