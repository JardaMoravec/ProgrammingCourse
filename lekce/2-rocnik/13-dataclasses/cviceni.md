# Cvičení — Dataclasses

## Cvičení 1 — Účastník soutěže (★☆☆)

Vytvořte dataclass `Ucastnik` s atributy `jmeno` a `cislo`. Načtěte
jméno a číslo, vytvořte dva účastníky se stejnými údaji a vypište
prvního a výsledek porovnání pomocí `==`.

@reseni
```python
from dataclasses import dataclass


@dataclass
class Ucastnik:
    jmeno: str
    cislo: int


prvni = Ucastnik(input(), int(input()))
druhy = Ucastnik(prvni.jmeno, prvni.cislo)
print(prvni)
print(prvni == druhy)
```
@end

---

## Cvičení 2 — Sklad s vlastní evidencí (★★☆)

Vytvořte dataclass `Sklad` s názvem a slovníkem `stavy`, který má
výchozí hodnotu vytvořenou pomocí `field(default_factory=dict)`.
Založte dva sklady, přidejte zboží pouze do prvního slovníku a ověřte,
že evidence druhého zůstane prázdná.

@reseni
```python
from dataclasses import dataclass, field


@dataclass
class Sklad:
    nazev: str
    stavy: dict = field(default_factory=dict)


prvni = Sklad("Potraviny")
druhy = Sklad("Naradi")
prvni.stavy["Mouka"] = 4
print(prvni.stavy)
print(druhy.stavy)
```
@end
