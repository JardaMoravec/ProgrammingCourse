"""Autor má seznam knih — atribut může být objekt i seznam."""


class Kniha:
    pass


class Autor:
    pass


k = Kniha()
k.nazev = "Válka s Mloky"
k.zanr = "román"
k.pocet_stran = 280

a = Autor()
a.jmeno = "Karel"
a.prijmeni = "Čapek"
a.knihy = []
a.knihy.append(k)

print(a.jmeno, a.prijmeni)
print(len(a.knihy))
print(a.knihy[0].nazev)
