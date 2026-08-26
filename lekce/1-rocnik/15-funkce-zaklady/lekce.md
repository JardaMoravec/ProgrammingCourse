---
id: 15-funkce-zaklady
rocnik: 1
nazev: Funkce — definice, parametry, návratová hodnota
hodiny: 3
obtiznost: stredni
prerekvizity: [14-ridici-struktury-procviceni]
cile:
  - Definujete vlastní funkci pomocí def
  - Předáte parametry a vrátíte hodnotu return
  - Rozdělíte program na menší, znovupoužitelné části
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# Funkce — definice, parametry, návratová hodnota

## Cíle lekce

- Pochopíte, proč funkce zjednodušují kód
- Naučíte se `def`, parametry a `return`
- Zavoláte funkci a použijete její výsledek

## Proč funkce?

Bez funkcí se kód opakuje a hůře čte. Funkce **pojmenuje blok kódu** a lze ho volat opakovaně.

```python
def pozdrav(jmeno):
    print(f"Ahoj, {jmeno}!")

pozdrav("Anna")
pozdrav("Petr")
```

## Definice a volání

```python
def soucet(a, b):
    return a + b

vysledek = soucet(3, 5)
print(vysledek)  # 8
```

| Část | Význam |
|------|--------|
| `def` | začátek definice |
| `soucet` | název funkce |
| `a, b` | parametry |
| `return` | návratová hodnota (ukončí funkci) |

→ viz `priklady/funkce_zaklady.py`

## Parametry a návratová hodnota

```python
def je_sude(n):
    return n % 2 == 0

if je_sude(10):
    print("Sudé")
```

Funkce může vracet `True`/`False`, číslo, řetězec — cokoliv.

## Výchozí parametry

```python
def mocnina(zaklad, exponent=2):
    return zaklad ** exponent

print(mocnina(5))      # 25
print(mocnina(2, 10))  # 1024
```

## Docstring

```python
def obsah_obdelniku(a, b):
    """Vrátí obsah obdélníku se stranami a a b."""
    return a * b
```

Krátký popis pod `def` — dokumentace pro čtenáře kódu.

## Funkce vs. postupný kód

| Postupný kód | S funkcemi |
|--------------|------------|
| dlouhý soubor | menší, pojmenované bloky |
| kopírování | jedno volání |
| těžší testování | testujete jednu funkci |

## Shrnutí

| Pojem | Význam |
|-------|--------|
| `def f(x):` | definice funkce |
| `return` | vrátí hodnotu a skončí |
| parametr | vstup funkce |
| volání `f(5)` | spustí funkci s argumentem |

## Co dál

→ [Lekce 16: Seznamy](../16-seznamy/lekce.md)
