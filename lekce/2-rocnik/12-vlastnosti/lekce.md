---
id: 12-vlastnosti
rocnik: 2
nazev: Vlastnosti a @property
hodiny: 5
obtiznost: stredni
prerekvizity: [11-moduly-a-soubory]
cile:
  - Vysvětlíte rozdíl mezi atributem a vlastností
  - Použijete @property pro odvozenou hodnotu
  - Ověříte hodnotu při zápisu pomocí setteru
migrovano_z: []
---

# Vlastnosti a `@property`

Lekce má **5 hodin**. Běžný atribut, například `self.jmeno`, je vhodný,
když jeho hodnotu není třeba počítat ani hlídat. Vlastnost použijte,
když chcete zachovat jednoduchý zápis `objekt.hodnota`, ale při čtení
nebo změně potřebujete spustit metodu.

## Cíle lekce

- Odlišíte běžný atribut od vlastnosti
- Vytvoříte vlastnost jen pro čtení
- Přiřadíte setter, který ověří novou hodnotu

## Vlastnost jen pro čtení

Vlastnost vytvoříte dekorátorem `@property`. Navenek se používá jako
atribut — bez závorek:

```python
class Objednavka:
    def __init__(self, cena, pocet):
        self.cena = cena
        self.pocet = pocet

    @property
    def celkem(self):
        return self.cena * self.pocet


objednavka = Objednavka(120, 3)
print(objednavka.celkem)  # 360
```

`celkem` se pokaždé vypočítá z aktuální ceny a počtu kusů. Není to
hodnota, kterou byste měli ukládat zvlášť — po změně ceny by mohla
zastaralá hodnota zůstat nesprávná. Bez setteru je `celkem` jen pro čtení.

## Setter a kontrola hodnoty

Setter se jmenuje stejně jako vlastnost a má dekorátor
`@nazev_vlastnosti.setter`. Skutečnou hodnotu ukládáme do atributu
`_vek`; podtržítko označuje, že je určený k použití uvnitř třídy.

```python
class Osoba:
    def __init__(self, vek):
        self.vek = vek

    @property
    def vek(self):
        return self._vek

    @vek.setter
    def vek(self, hodnota):
        if hodnota < 0:
            raise ValueError("Vek nesmi byt zaporny")
        self._vek = hodnota


osoba = Osoba(17)
osoba.vek = 18
print(osoba.vek)  # 18
```

Při `self.vek = vek` v konstruktoru Python zavolá setter. Stejná
kontrola tak platí při vytvoření objektu i při pozdější změně.
Vlastnost uvnitř setteru znovu nenastavujte: `self.vek = hodnota`
by setter zavolalo znovu a znovu. Ukládejte do `self._vek`.

Použijte `@property`, když máte jasný důvod — například výpočet nebo
validaci. U obyčejných dat je přímý atribut jednodušší a přehlednější.

## Časté chyby

| Chyba | Následek |
|-------|----------|
| `objekt.celkem()` | vlastnost se používá bez závorek |
| setter zapisuje `self.vek = hodnota` | nekonečné opakované volání setteru |
| kontrola je jen v konstruktoru | pozdější přiřazení ji obejde |
| každé pole automaticky obalíte property | zbytečný kód bez přínosu |
| vlastnost nazvete jinak než setter | dekorátor nepřiřadí setter ke správné vlastnosti |

## Shrnutí

| Zápis | Význam |
|-------|--------|
| `@property` | metoda se používá jako atribut při čtení |
| `@vek.setter` | metoda ověří a uloží nové `vek` |
| `self._vek` | vnitřní uložená hodnota |
| odvozená vlastnost | vypočítá se z jiných aktuálních atributů |

Příště použijete `dataclass` pro třídy, které hlavně uchovávají data.

## Co dál

→ [Lekce 13: Dataclasses](../13-dataclasses/lekce.md)
