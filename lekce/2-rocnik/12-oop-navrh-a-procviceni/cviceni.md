# Cvičení — OOP návrh

Cvičení jsou na **první hodinu** (návrh na papír). Zbytek 9 hodin je pololetní projekt — zadání v Úkolech, řešení tu není.

## Cvičení 1 — Je, nebo má? (★☆☆)

U každé dvojice napište **je** (dědičnost) nebo **má** (složení):

1. tramvaj — vozidlo
2. tramvaj — řidič
3. polévka — jídlo
4. objednávka — položky

@reseni
1. je — `class Tramvaj(Vozidlo)`
2. má — `self.ridic = Ridic(...)`
3. je — `class Polevka(Jidlo)`
4. má — seznam položek v objednávce (`self.polozky = ...`)
@end

---

## Cvičení 2 — Půjčovna (★★☆)

Zadání jednou větou: *Půjčovna půjčuje kola i koloběžky. Každé má značku a cenu za hodinu. Kolo má převody, koloběžka má brzdu. Výpůjčka má zákazníka a seznam půjčených věcí.*

Napište seznam tříd a u každé, zda **je** nebo **má** jinou. Ještě nepište kód.

@reseni
| Třída | Vztah |
|-------|--------|
| `Vozitko` | rodič (značka, cena za hodinu) |
| `Kolo` | **je** vozítko, navíc převody |
| `Kolobezka` | **je** vozítko, navíc brzda |
| `Zakaznik` | jméno |
| `Vypujcka` | **má** zákazníka a seznam vozítek |

Společné (`znacka`, cena, třeba `cena_za(hodiny)`) patří `Vozitko`. Cyklus přes výpůjčku využije přepis u kola a koloběžky.
@end

---

## Cvičení 3 — Co je špatně (★★☆)

Návrh: `class Motor(Auto)` protože „motor je v autě“. Proč to nesedí? Jak to opravit?

@reseni
„Je v autě“ znamená **má**, ne **je**. Motor není auto. Správně: `class Auto` má `self.motor = Motor(...)`. Dědí se jen když potomek **je** rodič (auto je vozidlo).
@end
