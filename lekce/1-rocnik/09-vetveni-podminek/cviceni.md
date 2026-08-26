# Cvičení — Větvení programu

## Úkol 1 — Výpočet zisku (★★☆)

> Zdroj: `úkol 3 - výpočet zisku.docx`

Kompletní program se vstupem od uživatele a větvením pro zisk/ztrátu.

@reseni
```python
nakupni = float(input("Nákupní cena (Kč): "))
prodejni = float(input("Prodejní cena (Kč): "))
rozdil = prodejni - nakupni

if rozdil >= 0:
    print(f"Vydělali jste: {rozdil} Kč")
else:
    print(f"Prodělali jste: {-rozdil} Kč")
```
@end

---

## Úkol 2 — Vlastnosti čísla (★★★)

> Zdroj: `úkol 6 - zjištění vlastností čísla.docx`

Načtěte celé číslo od -1000 do 1000. Pokud je mimo rozsah, chybová hláška. Jinak vypište vlastnosti.

@reseni
```python
cislo = int(input("Zadejte číslo (-1000 až 1000): "))

if cislo < -1000 or cislo > 1000:
    print("Chyba: číslo mimo povolený rozsah.")
else:
    if cislo > 0:
        print("Číslo je kladné.")
    elif cislo < 0:
        print("Číslo je záporné.")
    else:
        print("Číslo je nula.")

    if cislo % 2 == 0:
        print("Číslo je sudé.")
    else:
        print("Číslo je liché.")

    if cislo % 10 == 0:
        print("Je násobkem deseti.")
    else:
        print("Není násobkem deseti.")

    if cislo % 5 == 0:
        print("Je násobkem pěti.")
    else:
        print("Není násobkem pěti.")
```
@end

---

## Úkol 3 — BMI (★★★)

> Zdroj: `úkol 9 - výpočet BMI indexu.docx`

Načtěte váhu (kg) a výšku (m). Vypočítejte BMI a vypište kategorii.

@reseni
```python
vaha = float(input("Váha (kg): "))
vyska = float(input("Výška (m): "))
bmi = vaha / (vyska ** 2)
print(f"BMI je {bmi:.2f}.")

if bmi < 16.5:
    print("Podvýživa.")
elif bmi < 18.5:
    print("Podváha.")
elif bmi < 25:
    print("Ideální váha.")
elif bmi < 30:
    print("Nadváha.")
elif bmi < 35:
    print("Mírná obezita.")
else:
    print("Obezita.")
```
@end

---

## Úkol 4 — Krychle (★★☆)

> Zdroj: `úkol 4a - výpočet objemu a povrchu krychle`

Načtěte stranu `a`. Pokud je záporná, chyba. Jinak objem a povrch.

@reseni
```python
a = float(input("Strana krychle a: "))

if a < 0:
    print("Chyba: strana nemůže být záporná.")
else:
    objem = a ** 3
    povrch = 6 * a ** 2
    print(f"Objem: {objem}")
    print(f"Povrch: {povrch}")
```
@end
