# Cvičení — Vlastní výjimky a iterace

Cvičení jsou na hodinu. Úkoly do AMOS mají jiná zadání. Výjimka musí dědit z `Exception`. Cyklus `for` jde přes **objekt**, ne přes vnitřní seznam.

## Cvičení 1 — Mimo rozsah (★☆☆)

Třída `MimoRozsah(Exception)`. Je-li číslo `15` větší než `10`, vyvolejte `MimoRozsah` a v `except` vypište `mimo`.

Ověření: výstup je `mimo`.

@reseni
```python
class MimoRozsah(Exception):
    pass


n = 15
try:
    if n > 10:
        raise MimoRozsah()
    print(n)
except MimoRozsah:
    print("mimo")
```
@end

---

## Cvičení 2 — Teplota (★★☆)

Třída `MocChladno(Exception)`. Třída `Teplota` má metodu `nastav(self, t)`. Když je `t` menší než `-273`, vyvolejte `MocChladno`. Zkuste nastavit `-300`, v `except` vypište `chladno`. Pak nastavte `20` a vypište `t.hodnota`.

Ověření: dva řádky `chladno` a `20`.

@reseni
```python
class MocChladno(Exception):
    pass


class Teplota:
    def __init__(self):
        self.hodnota = 0

    def nastav(self, t):
        if t < -273:
            raise MocChladno()
        self.hodnota = t


t = Teplota()
try:
    t.nastav(-300)
except MocChladno:
    print("chladno")
t.nastav(20)
print(t.hodnota)
```
@end

---

## Cvičení 3 — Nejde for (★☆☆)

Proč spadne cyklus? Doplňte `__iter__` tak, aby vypsal `A` a `B`.

```python
class Skupina:
    def __init__(self):
        self.jmena = ["A", "B"]


for jmeno in Skupina():
    print(jmeno)
```

@reseni
Objekt nemá `__iter__`, proto `TypeError`. Půjčte iterátor ze seznamu:

```python
class Skupina:
    def __init__(self):
        self.jmena = ["A", "B"]

    def __iter__(self):
        return iter(self.jmena)


for jmeno in Skupina():
    print(jmeno)
```
@end

---

## Cvičení 4 — Playlist (★★☆)

Třída `Playlist` drží seznam `skladby`. Metoda `pridej(self, nazev)` skladbu přidá. `__iter__` vrátí `iter(self.skladby)`. Přidejte `Ahoj` a `Doma` a cyklem vypište názvy.

Ověření: dva řádky `Ahoj` a `Doma`. V cyklu `for skladba in playlist`, ne `for skladba in playlist.skladby`.

@reseni
```python
class Playlist:
    def __init__(self):
        self.skladby = []

    def pridej(self, nazev):
        self.skladby.append(nazev)

    def __iter__(self):
        return iter(self.skladby)


p = Playlist()
p.pridej("Ahoj")
p.pridej("Doma")
for skladba in p:
    print(skladba)
```
@end
