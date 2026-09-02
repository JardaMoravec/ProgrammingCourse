# Cvičení — Chyby a výjimky

## Cvičení 1 — Procvičení výjimek (★★★)

> Zdroj: `úkol 12 - procvičení výjimek.docx`

Postupně ověřte vstup uživatele s konkrétní chybovou hláškou.

@reseni
Ukázka pro celé číslo v intervalu (bod 3):

```python
while True:
    try:
        x = int(input("Celé číslo od -100 do 100: "))
        if -100 <= x <= 100:
            print(f"Číslo je {x}.")
            break
        raise ValueError("mimo interval")
    except ValueError:
        print("Chyba: zadejte celé číslo v rozsahu -100 až 100.")
```

Obdobně pro desetinné číslo (`float`), sudé číslo (`x % 2 != 0`), dělení nulou (`ZeroDivisionError`).
@end

---

## Cvičení 2 — Bezpečný input (★★☆)

Načtěte kladné celé číslo — dokud nedostane platný vstup.

@reseni
```python
while True:
    try:
        n = int(input("Zadejte kladné celé číslo: "))
        if n <= 0:
            raise ValueError("není kladné")
        break
    except ValueError:
        print("Neplatný vstup. Zkuste znovu.")

print("Děkuji, zadali jste:", n)
```
@end

---

## Cvičení 3 — Co spadne? (★★☆)

Predikujte výjimku, pak ověřte.

@reseni
| Kód | Výjimka |
|-----|---------|
| `int("12.5")` | `ValueError` |
| `10 / 0` | `ZeroDivisionError` |
| `"text" + 5` | `TypeError` |
@end
