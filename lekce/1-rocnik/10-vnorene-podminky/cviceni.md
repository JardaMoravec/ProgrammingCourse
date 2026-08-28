# Cvičení — Vnořené podmínky

## Úkol 1 — Refaktoring (★★☆)

Přepište vnořený kód na `and` nebo řetězení porovnání — výstup zůstane stejný:

```python
vek = int(input("Věk: "))
if vek >= 18:
    if vek < 65:
        print("Jste v produktivním věku.")
    else:
        print("Jste v důchodovém věku.")
else:
    print("Nejste plnoletí.")
```

@reseni
```python
vek = int(input("Věk: "))

if 18 <= vek < 65:
    print("Jste v produktivním věku.")
elif vek >= 65:
    print("Jste v důchodovém věku.")
else:
    print("Nejste plnoletí.")
```
@end

---

## Úkol 2 — Dopravné podle hmotnosti (★★★)

Načtěte hmotnost zásilky v kg. Při **neplatné** hodnotě (≤ 0) vypište `Neplatná hmotnost.`
Jinak určete cenu dopravy:

| Hmotnost | Cena |
|----------|------|
| do 5 kg včetně | `Dopravné: 49 Kč` |
| do 20 kg včetně | `Dopravné: 99 Kč` |
| do 50 kg včetně | `Dopravné: 149 Kč` |
| nad 50 kg | `Dopravné: 249 Kč` |

@reseni
```python
hmotnost = float(input("Hmotnost (kg): "))

if hmotnost <= 0:
    print("Neplatná hmotnost.")
elif hmotnost <= 5:
    print("Dopravné: 49 Kč")
elif hmotnost <= 20:
    print("Dopravné: 99 Kč")
elif hmotnost <= 50:
    print("Dopravné: 149 Kč")
else:
    print("Dopravné: 249 Kč")
```
@end

---

## Úkol 3 — Čtverec nebo obdélník (★★☆)

Načtěte délky stran `a` a `b`. Pokud je některá **≤ 0**, vypište `Chyba: strany musí být kladné.`
Jinak rozhodněte:

- strany stejné → `Je to čtverec.`
- strany různé → `Je to obdélník.`

@reseni
```python
a = float(input("Strana a: "))
b = float(input("Strana b: "))

if a <= 0 or b <= 0:
    print("Chyba: strany musí být kladné.")
elif a == b:
    print("Je to čtverec.")
else:
    print("Je to obdélník.")
```
@end

---

## Úkol 4 — Přihlášení (★★★)

Načtěte **jméno** a **heslo**. Platný účet je jen `admin` s heslem `tajne`.
Vypište jednu zprávu:

- neznámé jméno → `Neznámé jméno.`
- správné jméno, špatné heslo → `Špatné heslo.`
- obojí správně → `Přihlášení úspěšné.`

*(Ukázka situace, kdy vnoření dává smysl — heslo kontrolujete až po ověření jména.)*

@reseni
```python
jmeno = input("Jméno: ")
heslo = input("Heslo: ")

if jmeno == "admin":
    if heslo == "tajne":
        print("Přihlášení úspěšné.")
    else:
        print("Špatné heslo.")
else:
    print("Neznámé jméno.")
```
@end
