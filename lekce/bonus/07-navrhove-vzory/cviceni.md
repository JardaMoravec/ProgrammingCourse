# Cvičení — Návrhové vzory (základ)

Nic se neinstaluje. Cvičení jsou na papír. Do pololetního projektu vzory **nemusíte** jmenovat.

## Cvičení 1 — Který vzor? (★☆☆)

Ke každému nápadu napište **iterátor**, **strategie**, nebo **továrna**.

1. `for film in filmoteka:` vypíše názvy.
2. `udelej_jizdenku("student")` vrátí `StudentTarif()`.
3. V seznamu tarifů každý objekt odpoví na `cena()` jiným číslem.

@reseni
1. iterátor
2. továrna
3. strategie
@end

---

## Cvičení 2 — Kde smí být if (★★☆)

Proč je tohle v cyklu špatně, ale v továrně v pořádku?

```python
# A — v cyklu
for zvire in seznam:
    if type(zvire) is Pes:
        print("Haf!")
    else:
        print("Mnou!")

# B — při vzniku
def udelej_zvire(druh, jmeno):
    if druh == "pes":
        return Pes(jmeno)
    return Kocka(jmeno)
```

@reseni
**A** je obcházení strategie: další druh zvířete = další `if`. **B** rozhodne **jednou** při vzniku. Pak už `zvire.ozvi_se()` stačí. Továrna `if` smí, cyklus podle typu ne.
@end

---

## Cvičení 3 — Je to vzor? (★★☆)

Je `self.motor = Motor(90)` u auta návrhový vzor ze tří výše? Co to je?

@reseni
Není to iterátor, strategie ani továrna. Je to **složení** (auto motor **má**) z lekce 07 / 11. Vzor je pojmenovaný postup; ne každý vztah mezi třídami má v téhle lekci jméno.
@end
