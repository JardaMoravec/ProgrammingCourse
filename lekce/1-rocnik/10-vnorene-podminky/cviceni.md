# Cvičení — Vnořené podmínky

## Úkol 1 — Refaktoring (★★☆)

Přepište vnořený kód na `and` nebo řetězení:

```python
if a > 0:
    if a < 10:
        print("OK")
```

@reseni
```python
a = 5

if a > 0 and a < 10:
    print("OK")

# nebo
if 0 < a < 10:
    print("OK")
```
@end

---

## Úkol 2 — Kino (★★★)

Načtěte věk. Ceny: dítě (< 12) 100 Kč, student (12–26) 150 Kč, dospělý (27–64) 200 Kč, senior (65+) 120 Kč.

@reseni
```python
vek = int(input("Váš věk: "))

if vek < 0 or vek > 120:
    print("Neplatný věk.")
elif vek < 12:
    print("Cena vstupenky: 100 Kč")
elif vek <= 26:
    print("Cena vstupenky: 150 Kč")
elif vek <= 64:
    print("Cena vstupenky: 200 Kč")
else:
    print("Cena vstupenky: 120 Kč")
```
@end

---

## Úkol 3 — Trojúhelník (★★★)

Načtěte délky stran a, b, c. Ověřte platnost trojúhelníku.

@reseni
```python
a = float(input("Strana a: "))
b = float(input("Strana b: "))
c = float(input("Strana c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Chyba: strany musí být kladné.")
elif a + b > c and a + c > b and b + c > a:
    print("Trojúhelník existuje.")
else:
    print("Trojúhelník neexistuje.")
```
@end
