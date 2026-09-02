# Cvičení — Python a vývojové prostředí

## Cvičení 1 — Instalace (★☆☆)

Ověřte v terminálu:

```bash
python --version
pip --version
```

Výstup zkopírujte do `odpovedi.txt`.

@reseni
Příklad výstupu (verze se liší):

```
Python 3.12.4
pip 24.0 from ...
```

Pokud příkaz nefunguje, zkuste `python3` nebo ověřte, že je Python v PATH.
@end

---

## Cvičení 2 — První skript (★☆☆)

Vytvořte soubor `jmeno.py`, který vypíše:

```
Ahoj, [vaše jméno]! Učím se Python.
```

@reseni
```python
print("Ahoj, Karel! Učím se Python.")
```

Nebo s proměnnou:

```python
jmeno = "Karel"
print(f"Ahoj, {jmeno}! Učím se Python.")
```
@end

---

## Cvičení 3 — Konzole jako kalkulačka (★☆☆)

V konzoli Pythonu spočítejte bez kalkulačky:

- obvod čtverce se stranou 7,
- `(15 + 3) * 2`,
- `2 ** 10`.

@reseni
```python
>>> 4 * 7
28
>>> (15 + 3) * 2
36
>>> 2 ** 10
1024
```
@end

---

## Cvičení 4 — Zen of Python (★☆☆)

Spusťte `import this` a vyberte 2 věty, které vám dávají smysl. Vysvětlete vlastními slovy.

@reseni
Příklad:

- *„Beautiful is better than ugly.“* — Kód má být čitelný, ne jen funkční.
- *„Readability counts.“* — Kód čte člověk častěji, než ho počítač spouští.

V konzoli: `import this`
@end
