---
id: 06-vstup-a-vystup
rocnik: 1
nazev: Vstup a výstup (input, print)
hodiny: 3
obtiznost: zacatecnik
prerekvizity: [05-aritmeticke-operatory]
cile:
  - Načtete vstup od uživatele pomocí input()
  - Vypíšete výstup pomocí print() a f-stringu
  - Převedete text z input() na číslo pomocí int() a float()
migrovano_z:
  - "zdroje/Programování 1.docx"
---

# Vstup a výstup (input, print)

## Cíle lekce

- Vytvoříte **interaktivní** konzolový program
- Pochopíte, že `input()` vrací vždy text
- Použijete **f-string** pro přehledný výstup (proměnné, výrazy, zaokrouhlení)

> Od této lekce **úkoly v Moodle (VPL)** očekávají program se vstupem a výstupem — stejně jako v zadání.

## Výstup — print()

Funkce `print()` zobrazí text (nebo jiné hodnoty) v konzoli:

```python
print("Ahoj")                    # jeden text
print("Ahoj", jmeno, "!")        # více hodnot — mezi nimi mezera
print(f"Věk: {vek} let")         # f-string (doporučeno)
```

| Způsob | Příklad | Kdy použít |
|--------|---------|------------|
| jeden text | `print("Ahoj")` | pevná zpráva |
| více hodnot | `print("Součet:", soucet)` | rychlý výpis, mezery mezi hodnotami |
| **f-string** | `print(f"Součet: {soucet}")` | srozumitelná věta s proměnnými — **nejčastěji** |

## f-string — formátovaný řetězec

**f-string** (anglicky *formatted string literal*) je řetězec s prefixem **`f`** před uvozovkami. Uvnitř složených závorek `{…}` vložíte **proměnnou** nebo **výraz** — Python ho tam při běhu **dosadí** jako text.

```python
jmeno = "Anna"
vek = 16
print(f"Ahoj, {jmeno}!")           # Ahoj, Anna!
print(f"{jmeno} je {vek} let.")    # Anna je 16 let.
```

### Proč f-string?

Bez f-stringu musíte text **skládat** — spojovat řetězce operátorem `+` nebo posílat více argumentů do `print()`. F-string je **přehlednější**, když chcete jednu souvislou větu:

```python
a = 10
b = 3

# méně přehledné — spojování +
print("Výsledek: " + str(a) + " + " + str(b) + " = " + str(a + b))

# přehledné — f-string
print(f"Výsledek: {a} + {b} = {a + b}")
```

V `{…}` nemusí být jen proměnná — můžete tam napsat **libovolný výraz**:

```python
vek = int(input())   # uživatel zadá např. 16
print(f"Za 5 let vám bude {vek + 5} let.")
print(f"Obvod: {2 * (5 + 3)}")    # výraz přímo v závorkách
```

### Uvozovky uvnitř f-stringu

Řetězec může být v **jednoduchých** nebo **dvojitých** uvozovkách. Když uvnitř potřebujete uvozovky, zvolte opačný typ:

```python
jmeno = "Anna"
print(f'Řekla: "{jmeno}"')         # Řekla: "Anna"
print(f"Jmenuji se {jmeno}.")      # běžná věta
```

### Desetinná čísla — zaokrouhlení ve výpisu

Po `float(input())` často dostanete hodně desetinných míst (např. `3.3333333333`). Ve f-stringu lze výpis **omezit** pomocí `:.2f` (2 desetinná místa):

```python
a = 10
b = 3
podil = a / b
print(f"Podíl: {podil}")           # Podíl: 3.3333333333333335
print(f"Podíl: {podil:.2f}")       # Podíl: 3.33
```

| Zápis | Význam |
|-------|--------|
| `{x}` | hodnota proměnné `x` |
| `{x + y}` | výsledek výrazu |
| `{x:.2f}` | desetinné číslo se 2 místy za tečkou |

### Časté chyby

```python
jmeno = "Anna"

print("Ahoj, {jmeno}!")    # ❌ vypíše doslova: Ahoj, {jmeno}!
print(f"Ahoj, {jmeno}!")   # ✅ vypíše: Ahoj, Anna!
```

Chybí prefix **`f`** — Python pak `{jmeno}` nevyhodnotí.

```python
print(f"Řekl: "Ahoj"")     # ❌ syntaktická chyba — stejné uvozovky
print(f'Řekl: "Ahoj"')     # ✅ vnější ' ', uvnitř " "
```

→ viz `priklady/vstup_vystup.py` a `priklady/pretipovani.py`

## Vstup — input()

`input()` načte řádek od uživatele a vrací **vždy řetězec** (`str`):

```python
jmeno = input("Zadejte své jméno: ")
print("Ahoj", jmeno, "!")
```

Text v uvozovkách u `input()` je **výzva** pro uživatele — v testech VPL se posílá jen samotná data (bez výzev).

## Vstup jako číslo

Pro výpočty musíte text převést na číslo:

```python
vek = int(input("Zadejte věk: "))
print("Za 5 let vám bude", vek + 5)
```

Desetinné číslo: `float(input())`.

Podrobněji o typech a přetypování v [lekci 07](../07-datove-typy/lekce.md).

## Kompletní příklad

```python
a = float(input("První číslo: "))
b = float(input("Druhé číslo: "))
print(f"Součet: {a + b}")
```

## Shrnutí

| Funkce | Účel |
|--------|------|
| `input()` | Načtení textu od uživatele |
| `print()` | Výpis na obrazovku |
| `int(...)` | Text → celé číslo |
| `float(...)` | Text → desetinné číslo |
| `f"{x}"` | f-string — řetězec s dosazenými hodnotami v `{…}` |
| `{x:.2f}` | f-string — desetinné číslo se 2 desetinnými místy |

## Co dál

→ [Lekce 07: Datové typy](../07-datove-typy/lekce.md)
