# Cvičení — Anatomie programu a bloky kódu

## Úkol 1 — Oprava odsazení (★★☆)

Opravte tento kód tak, aby běžel bez chyby:

```python
print("Start")
if True:
print("Uvnitř bloku")
    print("Špatně")
print("Konec")
```

@reseni
```python
print("Start")
if True:
    print("Uvnitř bloku")
    print("Správně odsazeno")
print("Konec")
```
@end

---

## Úkol 2 — Vlastní struktura (★☆☆)

Napište program `struktura.py`, který vypíše alespoň 4 řádky s vnořeným blokem `if True:`.

@reseni
```python
print("Řádek 1 — hlavní blok")
print("Řádek 2 — hlavní blok")

if True:
    print("Řádek 3 — vnořený blok")
    print("Řádek 4 — vnořený blok")

print("Řádek 5 — zpět v hlavním bloku")
```
@end

---

## Úkol 3 — Komentáře (★☆☆)

Do programu z úkolu 2 doplňte komentáře vysvětlující, co jednotlivé části dělají.

@reseni
```python
# Program demonstruje hlavní a vnořený blok
print("Start programu")

if True:
    # Tento blok se vždy provede (podmínka je True)
    print("Uvnitř podmínky")

print("Konec programu")
```
@end
