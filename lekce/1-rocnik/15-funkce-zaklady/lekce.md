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
  - Zavoláte funkci pozicně i pojmenovanými argumenty
  - Rozdělíte program na menší, znovupoužitelné části
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# Funkce — definice, parametry, návratová hodnota

## Cíle lekce

- Pochopíte, proč funkce zjednodušují kód
- Naučíte se `def`, parametry a `return`
- Zavoláte funkci **pozicně** i **pojmenovanými argumenty**

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

## Pojmenované argumenty

Při volání můžete u hodnoty uvést **jméno parametru**. Říká se tomu **pojmenovaný argument**.

```python
def obsah(a, b):
    return a * b


print(obsah(5, 3))        # podle pořadí
print(obsah(a=5, b=3))    # podle jména
print(obsah(b=3, a=5))    # pořadí u jmen nehraje roli
```

Hodí se, když má funkce víc parametrů a z `f(5, 3)` není hned jasné, co je co. Funguje to i s výchozí hodnotou: `mocnina(zaklad=2, exponent=10)`.

Pozicní argumenty (jen hodnota) musí být **před** pojmenovanými:

```python
obsah(5, b=3)    # ano
obsah(a=5, 3)    # ne — SyntaxError
```

Jméno musí sedět s parametrem v `def`. `obsah(sirka=5, b=3)` spadne na `TypeError`.

→ viz `priklady/funkce_zaklady.py`

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
| parametr | vstup funkce (v `def`) |
| argument | hodnota při volání |
| `f(5, 3)` | pozicní argumenty — rozhoduje pořadí |
| `f(a=5, b=3)` | pojmenované argumenty — rozhoduje jméno |

## Co dál

→ [Lekce 16: Seznamy](../16-seznamy/lekce.md)

Volitelně: [vibe coding (bonus)](../../bonus/08-vibe-coding/lekce.md) — asistent kódu pod kontrolou, mimo 81 hodin.
