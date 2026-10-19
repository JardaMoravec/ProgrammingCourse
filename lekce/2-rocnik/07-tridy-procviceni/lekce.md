---
id: 07-tridy-procviceni
rocnik: 2
nazev: Třídy — souhrn a procvičení
hodiny: 5
obtiznost: stredni
prerekvizity: [06-specialni-metody]
cile:
  - Zopakujete třídu, konstruktor a metodu
  - Složíte __str__, __eq__ a __len__ do jednoho programu
  - Podle zadání vyberete, co z lekcí 03–06 úloha potřebuje
migrovano_z: []
---

# Třídy — souhrn a procvičení

Lekce má **5 hodin** (jeden týden). Nová syntaxe **nepřibývá**. Složíte [třídy](../03-tridy-a-objekty/lekce.md), [konstruktor](../04-konstruktor/lekce.md), [metody](../05-metody/lekce.md) a [speciální metody](../06-specialni-metody/lekce.md).

Dědičnost je až příští lekce. Tady cvičení v hodině nejsou — procvičení jsou **úkoly**.

## Cíle lekce

- Z objektu, konstruktoru a metody složíte jeden program
- `print(objekt)` řeší `__str__`, `==` řeší `__eq__`, `len(objekt)` řeší `__len__`
- V úkolech dodržíte přesný výstup

## Co kam patří

| Potřebuji… | Lekce | Zápis |
|------------|-------|--------|
| třídu a její údaje | [03](../03-tridy-a-objekty/lekce.md) | `class`, objekt, tečka |
| údaje hned při vzniku | [04](../04-konstruktor/lekce.md) | `__init__(self, ...)` |
| spočítat nebo změnit stav | [05](../05-metody/lekce.md) | metoda se `self` |
| čitelný výpis, rovnost, délku | [06](../06-specialni-metody/lekce.md) | `__str__`, `__eq__`, `__len__` |

Speciální metodu nevoláte tečkou. `print(k)`, `a == b` a `len(p)` ji spustí samy.

## Všechno najednou

Kniha umí text a rovnost. Polička umí přidat knihu a říct, kolik jich je:

```python
class Kniha:
    def __init__(self, nazev):
        self.nazev = nazev

    def __eq__(self, jina):
        return self.nazev == jina.nazev

    def __str__(self):
        return self.nazev


class Policka:
    def __init__(self):
        self.knihy = []

    def pridej(self, kniha):
        self.knihy.append(kniha)

    def __len__(self):
        return len(self.knihy)


a = Kniha("R.U.R.")
b = Kniha("R.U.R.")
p = Policka()
p.pridej(a)
p.pridej(Kniha("Krakatit"))
print(a)       # R.U.R.
print(a == b)  # True
print(len(p))  # 2
```

→ viz `priklady/kniha_a_policka.py`

`pridej` je obyčejná metoda. `__str__`, `__eq__` a `__len__` jsou speciální.

## Časté chyby

| Chyba | Následek |
|-------|----------|
| atribut až za `Kniha(...)` | konstruktor ho nenastaví, snadno chybí |
| `print` uvnitř `__str__` | `print(k)` vypíše `None` |
| `__eq__` bez `return` | `==` vyjde `False` |
| `len(self.knihy)` v hlavním programu | zadání chce `len` na vašem objektu |

## Shrnutí

| Pojem | Kde |
|-------|-----|
| třída, objekt, atribut | lekce 03 |
| `__init__` | lekce 04 |
| metoda, `self` | lekce 05 |
| `__str__`, `__eq__`, `__len__` | lekce 06 |

Příště dědičnost — společný kód dvou tříd přesunete do rodiče.

Automatický test v AMOS kontroluje **výstup** pěti úkolů.

Lekce končí **známkovaným úkolem** s tajným zadáním — dostanete ho od učitele. Hodnotí učitel.

## Co dál

→ [Lekce 08: Dědičnost](../08-dedicnost/lekce.md)
