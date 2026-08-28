# Cvičení — Přetypování, vstup a výstup

## Úkol 1 — Výpočet let do důchodu (★★☆)

> Zdroj: `zdroje/Úkoly 1/úkol 1 - výpočet let do důchodu.docx`

Vytvořte konzolovou aplikaci:

- načte věk uživatele,
- vypočítá roky do důchodu (předpoklad: důchod ve 65 letech),
- vypíše srozumitelnou zprávu.

@reseni
```python
DUODUCHOD = 65

vek = int(input("Zadejte věk: "))
let = DUODUCHOD - vek

if let > 0:
    print(f"Do důchodu jdete za {let} let.")
elif let == 0:
    print("Do důchodu jdete letos.")
else:
    print("Už jste v důchodovém věku.")
```
@end

---

## Úkol 2 — Obvod trojúhelníku (★★☆)

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

## Úkol 3 — Převod minut (★★☆)

Načtěte počet minut a vypište kolik to je hodin a minut (např. 135 → 2 h 15 min).

@reseni
```python
minut = int(input("Počet minut: "))
hodiny = minut // 60
zbytek = minut % 60
print(f"{minut} min = {hodiny} h {zbytek} min")
```
@end
