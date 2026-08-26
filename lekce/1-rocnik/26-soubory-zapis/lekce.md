---
id: 26-soubory-zapis
rocnik: 1
nazev: IO operace — zápis do souboru
hodiny: 3
obtiznost: stredni
prerekvizity: [25-soubory-cteni]
cile:
  - Zapíšete text do souboru režimy w a a
  - Uložíte výstup programu do souboru
  - Zkopírujete soubor po řádcích
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# IO operace — zápis do souboru

## Cíle lekce

- Zapíšete data do textového souboru
- Rozlišíte přepsání (`w`) a doplnění (`a`)
- Spojíte čtení a zápis v jednom programu

## Zápis do souboru

```python
with open("vystup.txt", "w", encoding="utf-8") as f:
    f.write("První řádek\n")
    f.write("Druhý řádek\n")
```

Režim `"w"` **smaže** původní obsah!

→ viz `priklady/zapis_souboru.py`

## Doplnění na konec

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Nový záznam\n")
```

## Zápis ze seznamu

```python
radky = ["Anna", "Petr", "Eva"]
with open("jmena.txt", "w", encoding="utf-8") as f:
    for jmeno in radky:
        f.write(jmeno + "\n")
```

## Kopie souboru

```python
with open("zdroj.txt", "r", encoding="utf-8") as src:
    with open("kopie.txt", "w", encoding="utf-8") as dst:
        for radek in src:
            dst.write(radek)
```

## Bezpečnost

- `"w"` přepíše soubor — buďte opatrní
- Zálohujte důležitá data
- Používejte `encoding="utf-8"`

## Shrnutí

| Režim | Chování |
|-------|---------|
| `w` | nový / přepsání |
| `a` | doplnění |
| `r` | jen čtení |

## Co dál

→ [Lekce 27: Funkce — lokální a globální proměnné](../27-funkce-pokrocile/lekce.md)
