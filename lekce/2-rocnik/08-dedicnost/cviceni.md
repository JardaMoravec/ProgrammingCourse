# Cvičení — Dědičnost

Cvičení jsou na hodinu. Úkoly do AMOS mají jiná zadání. Vztah musí být **„je“** (kočka je zvíře), ne „má“.

## Cvičení 1 — Kočka (★☆☆)

Třída `Zvire` (`jmeno`) s metodou `predstavit(self)`, která vrátí jméno. Třída `Kocka(Zvire)` s metodou `zamnoukej(self)`, která vrátí `Mnou!`. Vypište představení a mňouknutí.

Ověření: pro `Kocka("Micka")` je výstup `Micka` a na dalším řádku `Mnou!`.

@reseni
```python
class Zvire:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def predstavit(self):
        return self.jmeno


class Kocka(Zvire):
    def zamnoukej(self):
        return "Mnou!"


k = Kocka("Micka")
print(k.predstavit())
print(k.zamnoukej())
```
@end

---

## Cvičení 2 — Žák je osoba (★★☆)

Třída `Osoba` (`jmeno`, `prijmeni`) s metodou `cele_jmeno(self)`. Třída `Zak(Osoba)` má v konstruktoru navíc `rocnik`. Použijte `super()`. Vypište `Eva Novak, rocnik 2`.

Ověření: `z.jmeno` je `Eva`, `z.rocnik` je `2`.

@reseni
```python
class Osoba:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

    def cele_jmeno(self):
        return self.jmeno + " " + self.prijmeni


class Zak(Osoba):
    def __init__(self, jmeno, prijmeni, rocnik):
        super().__init__(jmeno, prijmeni)
        self.rocnik = rocnik


z = Zak("Eva", "Novak", 2)
print(z.cele_jmeno() + ", rocnik " + str(z.rocnik))
```
@end

---

## Cvičení 3 — Chybí super (★☆☆)

Proč spadne poslední `print`? Opravte konstruktor tak, aby vypsal `Azor`.

```python
class Zvire:
    def __init__(self, jmeno):
        self.jmeno = jmeno


class Pes(Zvire):
    def __init__(self, jmeno, plemeno):
        self.plemeno = plemeno


p = Pes("Azor", "labrador")
print(p.jmeno)
```

@reseni
`Pes` má vlastní `__init__`, takže se konstruktor zvířete **nespustí**. Jméno nastaví `super()`:

```python
class Zvire:
    def __init__(self, jmeno):
        self.jmeno = jmeno


class Pes(Zvire):
    def __init__(self, jmeno, plemeno):
        super().__init__(jmeno)
        self.plemeno = plemeno


p = Pes("Azor", "labrador")
print(p.jmeno)  # Azor
```
@end

---

## Cvičení 4 — Jízdní kolo (★★☆)

Třída `Vozidlo` (`znacka`) s `__str__`, které vrátí značku. Třída `JizdniKolo(Vozidlo)` má navíc `prevody` (celé číslo). `__str__` kola vrátí `znacka, 21 prevodu`. Vypište objekt kola.

Ověření: `print(JizdniKolo("Author", 21))` je `Author, 21 prevodu`.

@reseni
```python
class Vozidlo:
    def __init__(self, znacka):
        self.znacka = znacka

    def __str__(self):
        return self.znacka


class JizdniKolo(Vozidlo):
    def __init__(self, znacka, prevody):
        super().__init__(znacka)
        self.prevody = prevody

    def __str__(self):
        return self.znacka + ", " + str(self.prevody) + " prevodu"


print(JizdniKolo("Author", 21))
```
@end
