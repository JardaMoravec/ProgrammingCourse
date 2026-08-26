# Cvičení — Řetězce (základy)

## Úkol 1 — Iniciály (★☆☆)

Jméno a příjmení — vypište iniciály (první písmena).

@reseni
```python
jmeno = input("Jméno: ")
prijmeni = input("Příjmení: ")
print(jmeno[0].upper() + "." + prijmeni[0].upper() + ".")
```
@end

---

## Úkol 2 — Palindrom (★★☆)

Zadejte slovo — je palindrom? (stejné zepředu i zezadu)

@reseni
```python
slovo = input("Slovo: ").lower()
print("Ano" if slovo == slovo[::-1] else "Ne")
```
@end

---

## Úkol 3 — Věta z částí (★★☆)

Spojte seznam slov do věty (mezery mezi slovy).

@reseni
```python
slova = ["Python", "je", "skvělý"]
veta = " ".join(slova)
print(veta)
```
@end

---

## Úkol 4 — Rámeček (★★☆)

Vypište text uprostřed rámečku z hvězdiček.

@reseni
```python
text = "Ahoj"
sirka = len(text) + 4
print("*" * sirka)
print("* " + text + " *")
print("*" * sirka)
```
@end
