# Cvičení — Čtení ze souboru

## Cvičení 1 — Počet řádků (★★☆)

Přečtěte soubor a vypište počet řádků.

@reseni
```python
with open("data.txt", "r", encoding="utf-8") as f:
    radky = f.readlines()
print("Řádků:", len(radky))
```
@end

---

## Cvičení 2 — Součet ze souboru (★★☆)

Soubor obsahuje jedno číslo na řádek — sečtěte je.

@reseni
```python
soucet = 0
with open("cisla.txt", "r", encoding="utf-8") as f:
    for radek in f:
        soucet += float(radek.strip())
print("Součet:", soucet)
```
@end

---

## Cvičení 3 — Nejdelší řádek (★★★)

Najděte nejdelší řádek v souboru.

@reseni
```python
nej = ""
with open("data.txt", "r", encoding="utf-8") as f:
    for radek in f:
        r = radek.rstrip()
        if len(r) > len(nej):
            nej = r
print(nej)
```
@end

---

## Cvičení 4 — Výpis s čísly (★★☆)

Vypište soubor s prefixem čísla řádku: `1: text`.

@reseni
```python
with open("data.txt", "r", encoding="utf-8") as f:
    for i, radek in enumerate(f, 1):
        print(f"{i}: {radek.rstrip()}")
```
@end
