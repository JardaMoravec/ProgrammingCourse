# Cvičení — Metody řetězců

## Úkol 1 — Počet slov (★★☆)

Načtěte větu a vypište počet slov.

@reseni
```python
veta = input("Věta: ")
slova = veta.split()
print("Počet slov:", len(slova))
```
@end

---

## Úkol 2 — Email (★★☆)

Ověřte, zda řetězec obsahuje @ a tečku (zjednodušená kontrola).

@reseni
```python
email = input("Email: ")
if "@" in email and "." in email:
    print("Vypadá platně")
else:
    print("Neplatný formát")
```
@end

---

## Úkol 3 — Nahrazení (★★☆)

V textu nahraďte všechny mezery podtržítkem.

@reseni
```python
text = "hello world python"
print(text.replace(" ", "_"))
```
@end

---

## Úkol 4 — Obrácená věta (★★★)

Rozdělte větu na slova a vypište slova v opačném pořadí.

@reseni
```python
veta = input("Věta: ")
slova = veta.split()
slova.reverse()
print(" ".join(slova))
```
@end
