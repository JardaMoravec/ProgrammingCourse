# Cvičení — Aritmetické operátory

> Původní úkoly: `zdroje/Úkoly 1/úkol 4a`, `4b`, `5` (geometrie — plná verze až s podmínkami v lekci 09)

## Cvičení 1 — Kalkulačka (★☆☆)

V konzoli spočítejte objem krychle se stranou `a = 5`. Vzorec: V = a³.

@reseni
```python
a = 5
objem = a ** 3
print("Objem krychle:", objem)  # 125
```
@end

---

## Cvičení 2 — Dělení se zbytkem (★★☆)

Kolik je `17 // 5` a `17 % 5`? Vysvětlete, co každý výsledek znamená.

@reseni
```python
print(17 // 5)  # 3 — kolikrát se 5 vejde do 17 (celá část)
print(17 % 5)   # 2 — zbytek po dělení
```

`//` vrací celočíselný podíl, `%` zbytek. Ověření: `3 * 5 + 2 = 17`.
@end

---

## Cvičení 3 — Teplota (★★☆)

Převeďte 25 °C na Fahrenheit: `F = C * 9/5 + 32`. Napište jako jeden výraz v Pythonu.

@reseni
```python
c = 25
f = c * 9 / 5 + 32
print(f"{c} °C = {f} °F")  # 77.0 °F
```
@end

---

## Cvičení 4 — Zkrácené operátory (★★☆)

```python
x = 10
x += 5
x *= 2
x -= 3
```

Jaká je finální hodnota `x`? Ověřte v Pythonu.

@reseni
Postup: `10 → 15 → 30 → 27`

```python
x = 10
x += 5   # 15
x *= 2   # 30
x -= 3   # 27
print(x)  # 27
```
@end
