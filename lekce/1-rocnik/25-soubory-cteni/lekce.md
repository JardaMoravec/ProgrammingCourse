---
id: 25-soubory-cteni
rocnik: 1
nazev: IO operace — čtení ze souboru
hodiny: 3
obtiznost: stredni
prerekvizity: [24-retezce-metody]
cile:
  - Otevřete soubor pomocí with open
  - Přečtete celý soubor nebo po řádcích
  - Ošetříte chybějící soubor
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# IO operace — čtení ze souboru

## Cíle lekce

- Přečtete text ze souboru na disku
- Použijete bezpečný zápis `with open(...)`
- Zpracujete data po řádcích

## Otevření souboru

```python
with open("data.txt", "r", encoding="utf-8") as f:
    obsah = f.read()
    print(obsah)
```

`with` zajistí **automatické zavření** souboru.

→ viz `priklady/cteni_souboru.py`

## Čtení po řádcích

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for radek in f:
        print(radek.strip())
```

## readlines

```python
with open("data.txt", "r", encoding="utf-8") as f:
    radky = f.readlines()
print(f"Počet řádků: {len(radky)}")
```

## Ošetření chyby

```python
try:
    with open("neexistuje.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Soubor nenalezen.")
```

## Režimy otevření

| Režim | Význam |
|-------|--------|
| `"r"` | čtení (read) |
| `"w"` | zápis (write, smaže obsah) |
| `"a"` | doplnění na konec (append) |

## Shrnutí

Vždy specifikujte `encoding="utf-8"` pro českou diakritiku.

## Co dál

→ [Lekce 26: IO operace — zápis do souboru](../26-soubory-zapis/lekce.md)
