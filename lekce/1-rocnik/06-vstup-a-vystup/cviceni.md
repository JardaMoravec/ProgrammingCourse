# Cvičení — Přetypování, vstup a výstup

## Cvičení 1 — Výpočet let do důchodu (★★☆)

> Zdroj: `zdroje/Úkoly 1/úkol 1 - výpočet let do důchodu.docx`

Vytvořte konzolovou aplikaci. Věk je menší než 65:

- načte věk uživatele,
- vypočítá roky do důchodu (důchod ve 65 letech),
- vypíše zprávu, např. `Do důchodu jdete za 40 let.`

@reseni
```python
vek = int(input("Zadejte věk: "))
let = 65 - vek
print(f"Do důchodu jdete za {let} let.")
```
@end

---

## Cvičení 2 — Obvod trojúhelníku (★★☆)

Načtěte délky tří stran (float) a vypište obvod.

@reseni
```python
a = float(input("Strana a: "))
b = float(input("Strana b: "))
c = float(input("Strana c: "))
obvod = a + b + c
print(f"Obvod trojúhelníku: {obvod}")
```
@end

---

## Cvičení 3 — Převod minut (★★☆)

Načtěte počet minut a vypište kolik to je hodin a minut (např. 135 → 2 h 15 min).

@reseni
```python
minut = int(input("Počet minut: "))
hodiny = minut // 60
zbytek = minut % 60
print(f"{minut} min = {hodiny} h {zbytek} min")
```
@end
