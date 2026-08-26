---
id: 19-slovniky
rocnik: 1
nazev: Slovníky (asociativní pole)
hodiny: 3
obtiznost: stredni
prerekvizity: [18-tuples-a-range]
cile:
  - Vytvoříte slovník a přistoupíte k hodnotám podle klíče
  - Přidáte, změníte a smažete páry klíč–hodnota
  - Projdete slovník cyklem
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# Slovníky (asociativní pole)

## Cíle lekce

- Pochopíte slovník jako mapu **klíč → hodnota**
- Uložíte a vyhledáte data podle jména (např. telefonní seznam)
- Ovládnete základní operace se slovníky

## Vytvoření slovníku

```python
student = {
    "jmeno": "Anna",
    "rocnik": 1,
    "email": "anna@skola.cz",
}

print(student["jmeno"])
print(student.get("telefon", "neuvedeno"))
```

→ viz `priklady/slovniky.py`

## Přidání a změna

```python
student["telefon"] = "123456789"
student["rocnik"] = 2
del student["email"]
```

## Procházení

```python
for klic in student:
    print(klic, student[klic])

for klic, hodnota in student.items():
    print(f"{klic}: {hodnota}")
```

## Slovník vs. seznam

| Seznam | Slovník |
|--------|---------|
| index 0, 1, 2… | klíč (řetězec, číslo…) |
| pořadí | páry klíč–hodnota |
| `[1, 2, 3]` | `{"a": 1, "b": 2}` |

## Časté metody

| Metoda | Význam |
|--------|--------|
| `d.keys()` | všechny klíče |
| `d.values()` | všechny hodnoty |
| `d.items()` | páry |
| `"x" in d` | test klíče |

## Shrnutí

Slovník = rychlé vyhledání podle **jména**, ne podle pozice.

## Co dál

→ [Lekce 20: Cykly nad seznamy a slovníky](../20-cykly-nad-kolekcemi/lekce.md)
