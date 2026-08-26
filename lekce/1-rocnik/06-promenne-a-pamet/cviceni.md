# Cvičení — Proměnné

## Úkol 1 — Výměna hodnot (★★☆)

Máte `a = 5` a `b = 10`. Vyměňte jejich hodnoty **bez** třetí proměnné (nápověda: sčítání/odčítání) nebo **s** proměnnou `temp`.

@reseni
**S pomocnou proměnnou:**

```python
a = 5
b = 10
temp = a
a = b
b = temp
print(a, b)  # 10 5
```

**Bez třetí proměnné (Python trik):**

```python
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5
```
@end

---

## Úkol 2 — Pojmenování (★☆☆)

Které názvy jsou platné? Vysvětlete proč ne u špatných.

`2jmeno`, `moje_promenna`, `moje-promenna`, `_skryta`, `for`

@reseni
| Název | Platný? | Důvod |
|-------|---------|-------|
| `2jmeno` | ne | začíná číslicí |
| `moje_promenna` | ano | snake_case |
| `moje-promenna` | ne | pomlčka není povolena |
| `_skryta` | ano | podtržítko je OK |
| `for` | ne | klíčové slovo jazyka |
@end

---

## Úkol 3 — Výpočet zisku — příprava (★☆☆)

> Plná verze v lekci 09 s podmínkami.

```python
nakupni = 50
prodejni = 100
rozdil = prodejni - nakupni
print("Rozdíl:", rozdil, "Kč")
```

Rozšiřte o vlastní hodnoty a vyzkoušejte záporný rozdíl.

@reseni
```python
nakupni = 120
prodejni = 80
rozdil = prodejni - nakupni
print("Rozdíl:", rozdil, "Kč")  # -40 Kč (ztráta)
```
@end
