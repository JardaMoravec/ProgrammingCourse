---
id: 04-promenne-a-pamet
rocnik: 1
nazev: Proměnné, paměť a pojmenování
hodiny: 3
obtiznost: zacatecnik
prerekvizity: [03-bloky-kodu]
cile:
  - Vytvoříte a použijete proměnné
  - Pochopíte dynamické typování
  - Dodržíte pravidla pojmenování
migrovano_z:
  - "zdroje/Programování 1.docx"
---

# Proměnné, paměť a pojmenování

## Cíle lekce

- Víte, co je proměnná a k čemu slouží
- Umíte proměnným přiřazovat a měnit hodnoty
- Znáte pravidla pro názvy proměnných

## Co je proměnná?

**Proměnná** je pojmenované místo v paměti pro uložení hodnoty. V Pythonu jsou proměnné **odkazy na objekty** — název ukazuje na data v paměti.

```python
x = 5
```

Vytvořili jsme proměnnou `x` s hodnotou `5`.

## Dynamické typování

V Pythonu **nemusíte deklarovat typ** proměnné. Typ se určí automaticky podle přiřazené hodnoty:

```python
a = 10        # int
a = "text"    # nyní str — typ se změnil
```

Výhoda: rychlejší psaní kódů. Nevýhoda: typ není na první pohled vidět — později použijeme type hints.

## Case-sensitivity

Python **rozlišuje velikost písmen**:

```python
test = 10
Test = 5
TEST = 3
# Tři různé proměnné!
```

## Pravidla pojmenování

| Povoleno | Zakázáno |
|----------|----------|
| písmena, číslice, `_` | mezery, `-`, `.`, `@` |
| začít písmenem nebo `_` | klíčová slova (`if`, `for`, …) |

**Doporučené styly:**

```python
nazev_dlouhe_promenne = 1   # snake_case (preferováno v Pythonu)
nazevDlouhePromenne = 1     # camelCase
```

## Práce s proměnnými

```python
a = 10
b = a              # b je 10
b = a - 3          # b je 7
c = b - a          # c je -3
```

### Operace s textem

```python
ovoce = "jablko"
ovoce = ovoce + " a banán"   # zřetězení
print((ovoce + ", ") * 3)    # opakování řetězce
```

→ viz `priklady/promenne.py`

## Mutable a immutable

**Mutable** = objekt lze **měnit za běhu** (doplnit prvek, změnit obsah). **Immutable** = objekt **nelze změnit** — každá „úprava“ vytvoří **nový** objekt.

| Mutable (měnitelné) | Immutable (neměnitelné) |
|---------------------|-------------------------|
| `list`, `dict`, `set` | `int`, `float`, `bool`, `str`, `tuple` |

```python
seznam = [1, 2, 3]
seznam.append(4)      # OK — seznam je mutable

text = "Ahoj"
# text[0] = "X"     # chyba — řetězec je immutable
text = text + "!"     # vytvoří se nový řetězec
```

V Pythonu **nejde nastavit proměnnou jako immutable** (neexistuje `const` jako v jiných jazycích). Jméno `x` vždy jen ukazuje na objekt — klidně na jiný:

```python
x = 10
x = 20   # dovoleno — přesměrování jména
```

> **Poznámka:** Neměnnost je u Pythonu věcí **typu objektu** a **kultury jazyka** (standardní knihovna, zvyklosti programátorů) — ne příkazu, kterým byste proměnnou „uzamkli“. Konstanty proto píšeme konvencí `MAX_HODNOT = 100`; interpret to sice nevynucuje, ale **dodržuje se to jako pravidlo týmu / komunity** kolem Pythonu. Detailněji o typech v [lekci 07](../07-datove-typy/lekce.md).

## Deklarace, definice, inicializace

| Pojem | V Pythonu |
|-------|-----------|
| Deklarace | Nepoužívá se samostatně |
| Inicializace | První přiřazení hodnoty (`=`) |
| Definice | Přiřazení = vytvoření proměnné |

V Pythonu inicializace a definice proběhnou **v jednom kroku** pomocí `=`.

## Shrnutí

| Pojem | Význam |
|-------|--------|
| Proměnná | Pojmenovaný odkaz na hodnotu |
| Dynamický typ | Typ se nemusí deklarovat |
| Přiřazení | `=` uloží hodnotu do proměnné |
| Mutable | objekt lze měnit (např. `list`) |
| Immutable | objekt nelze měnit (např. `str`, `int`) |

## Co dál

→ [Lekce 05: Aritmetické operátory](../05-aritmeticke-operatory/lekce.md)
