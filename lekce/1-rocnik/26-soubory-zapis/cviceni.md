# Cvičení — Zápis do souboru

## Cvičení 1 — Deník (★★☆)

Načtěte větu od uživatele a **doplňte** ji do souboru denik.txt.

@reseni
```python
zaznam = input("Záznam: ")
with open("denik.txt", "a", encoding="utf-8") as f:
    f.write(zaznam + "\n")
```
@end

---

## Cvičení 2 — Seznam jmen (★★☆)

Uložte seznam 5 jmen do souboru (jedno jméno na řádek).

@reseni
```python
jmena = ["Anna", "Petr", "Eva", "Tom", "Lucie"]
with open("jmena.txt", "w", encoding="utf-8") as f:
    for j in jmena:
        f.write(j + "\n")
```
@end

---

## Cvičení 3 — Kopie (★★☆)

Zkopírujte obsah souboru a.txt do b.txt.

@reseni
```python
with open("a.txt", "r", encoding="utf-8") as src:
    obsah = src.read()
with open("b.txt", "w", encoding="utf-8") as dst:
    dst.write(obsah)
```
@end

---

## Cvičení 4 — Výsledky programu (★★★)

Program spočítá součet 1–100 a výsledek uloží do souboru.

@reseni
```python
soucet = sum(range(1, 101))
with open("vysledek.txt", "w", encoding="utf-8") as f:
    f.write(f"Součet 1-100: {soucet}\n")
```
@end
