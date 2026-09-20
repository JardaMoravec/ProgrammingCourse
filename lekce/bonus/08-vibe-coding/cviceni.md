# Cvičení — Vibe coding

Nic se neinstaluje. Cvičení jsou na papír a na čtení krátkého kódu. Do chatu **nemusíte** nic posílat.

## Cvičení 1 — Asistent, nebo vibe coding? (★☆☆)

Ke každé situaci napište **asistent**, nebo **vibe coding**.

1. Napíšete přesné zadání, kód si přečtete, spustíte ho se vzorem ze zadání a jednu funkci přepíšete, protože jste `lambda` ještě neměli.
2. Vložíte celé AMOS zadání, zkopírujete první výstup, Evaluate je zelené, program vysvětlit neumíte.
3. Program spadne. Do chatu dáte traceback a ptáte se, co znamená `ZeroDivisionError`. Pak dělení ošetříte sami.
4. Pětkrát napíšete „oprav to“, soubor neotevřete.

@reseni
1. asistent
2. vibe coding (a u úkolu navíc podvod)
3. asistent
4. vibe coding
@end

---

## Cvičení 2 — Lepší zadání (★★☆)

Tenhle prompt je slabý:

`udělej python co sečte čísla`

Přepište ho tak, aby šel ověřit: jazyk, vstup, výstup, `input()` bez textu, jeden příklad.

@reseni
Například:

Python 3, bez importu. Načti dvě celá čísla, každé `int(input())` bez textu. Vypiš jeden řádek `Soucet: 30` (číslo je součet). Příklad: vstup `10` a `20`, výstup `Soucet: 30`.
@end

---

## Cvičení 3 — Co je špatně (★★☆)

Asistent navrhl:

```python
def prumer(cisla):
    soucet = 0
    for i in range(len(cisla) - 1):
        soucet += cisla[i]
    return soucet / len(cisla)
```

Pro `cisla = [2, 4, 6]` má vyjít `4.0`. Co program udělá a proč? Jak cyklus opravit **látkou z 1. ročníku** (bez nové knihovny)?

@reseni
Vypočte `(2 + 4) / 3` → `2.0`. `range(len(cisla) - 1)` nejde po poslední index.

Oprava třeba:

```python
def prumer(cisla):
    soucet = 0
    for cislo in cisla:
        soucet += cislo
    return soucet / len(cisla)
```

(Nebo `range(len(cisla))` bez `- 1`. Prázdný seznam pořád dělí nulou — to je další otázka, ne tahle chyba.)
@end

---

## Cvičení 4 — AMOS (★☆☆)

Úkol má automatický test. Smíte:

1. nechat si vysvětlit, proč `input()` v testu nesmí mít text?
2. vložit tajné známkované zadání do chatu a odevzdat první výstup?
3. použít návrh, který umíte řádek po řádku obhájit učiteli?

@reseni
1. ano — to je látka z 1. ročníku, ne opsaný program
2. ne — tajné zadání do chatu nepatří; odevzdání kódu bez porozumění je podvod
3. ano — asistent je nástroj, autor odevzdání jste vy
@end
