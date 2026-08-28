---
id: 03-bloky-kodu
rocnik: 1
nazev: Anatomie programu a bloky kódu
hodiny: 3
obtiznost: zacatecnik
prerekvizity: [02-python-a-prostredi]
cile:
  - Popíšete strukturu jednoduchého Python programu
  - Pochopíte roli odsazení místo složených závorek
  - Naučíte se vnořovat bloky kódu
migrovano_z:
  - "zdroje/Programování 1.docx (kap. Bloky kodu)"
---

# Anatomie programu a bloky kódu

## Cíle lekce

- Víte, z čeho se skládá běžný program
- Rozumíte odsazování v Pythonu
- Umíte číst vnořenou strukturu kódu

## Anatomie programu

Typický konzolový program v Pythonu:

1. **Komentáře** — vysvětlení pro člověka (interpret je ignoruje)
2. **Příkazy** — instrukce prováděné shora dolů
3. **Výstup** — `print()` zobrazí výsledek uživateli

```python
# Toto je komentář — interpret ho přeskočí
print("Program startuje")
print("Program končí")
```

## Blok kódu

**Blok** je souvislá část kódu, která tvoří logický celek (podmínka, cyklus, funkce).

V Pythonu se bloky **neoddělují složenými závorkami** `{ }` jako v C nebo JavaScriptu, ale **odsazením**.

### Pravidla odsazování

- používejte **4 mezery** na úroveň (doporučeno),
- **nemíchejte** tabulátory a mezery v jednom souboru,
- všechny příkazy ve stejném bloku musí mít **stejné odsazení**.

```python
# Hlavní blok (úroveň 0)
print("začátek")

    # Toto by byla CHYBA — neočekávané odsazení
```

Správně vnořený blok uvidíte u podmínek a cyklů v dalších lekcích. Zde ukázka struktury:

```python
print("hlavní blok")

if True:
    print("vnořený blok")
    print("stále ve vnořeném bloku")

print("zpět v hlavním bloku")
```

→ viz `priklady/bloky.py`

## Vnořování bloků

Bloky lze vnořovat téměř libovolně hluboko — každá úroveň = +4 mezery:

```python
if True:
    if True:
        print("druhá úroveň vnoření")
```

Později u cyklů a podmínek to využijete často.

## Spuštění programu

1. Uložte soubor s příponou `.py`
2. V terminálu: `python nazev_souboru.py`
3. Interpret provede příkazy **sekvenčně** shora dolů

## Časté chyby

| Chyba | Příčina |
|-------|---------|
| `IndentationError` | Špatné odsazení |
| `SyntaxError` | Překlep, chybějící dvojtečka u bloku |
| `NameError` | Použití neexistující proměnné |

## Shrnutí

| Pojem | Význam |
|-------|--------|
| Blok | Logická skupina příkazů |
| Odsazení | Struktura bloku v Pythonu |
| Komentář | Řádek začínající `#` |
| Sekvenční běh | Příkazy se provádějí po pořadí |

## Co dál

→ [Lekce 04: Proměnné a paměť](../04-promenne-a-pamet/lekce.md)
