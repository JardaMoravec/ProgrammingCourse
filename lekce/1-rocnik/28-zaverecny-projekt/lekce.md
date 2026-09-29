---
id: 28-zaverecny-projekt
rocnik: 1
nazev: Závěrečný projekt
hodiny: 12
obtiznost: pokrocily
prerekvizity: [27-funkce-pokrocile]
cile:
  - Složíte jednu konzolovou aplikaci z lekcí 04–27
  - Téma schválíte dřív, než začnete kód
  - Odevzdáte známkovaný závěrečný projekt
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# Závěrečný projekt

Lekce má **12 hodin**. Nová syntaxe **nepřibývá**. Celá lekce je **závěrečný projekt** — známkovaný, práce v hodině i doma.

## Cíle lekce

- Navrhnete, co program dělá, **než** napíšete kód
- Složíte jednu konzolovou aplikaci z lekcí 04–27
- Načtete data ze souboru a výsledek zapíšete do jiného souboru

## Rozvrh 12 hodin

| Hodiny | Co dělat |
|--------|----------|
| 1 | návrh: co program dělá, jaký soubor, jaké funkce; téma schválí učitel |
| 2–10 | kód, zkoušení, opravy |
| 11 | zkouška na jiném vstupním souboru |
| 12 | odevzdání do AMOS, krátká ukázka učiteli |

Bez schváleného tématu v první hodině kód nepište.

## Mapa lekcí 04–27

| Lekce | V projektu musíte ukázat |
|-------|--------------------------|
| [06](../06-vstup-a-vystup/lekce.md) | aspoň jeden `input()` a srozumitelný `print` |
| [09](../09-vetveni-podminek/lekce.md) | podmínka `if` |
| [12](../12-cyklus-while/lekce.md), [13](../13-cyklus-for/lekce.md) | cyklus nad načtenými daty |
| [15](../15-funkce-zaklady/lekce.md) | aspoň dvě vlastní funkce s parametrem a `return` |
| [16](../16-seznamy/lekce.md) nebo [19](../19-slovniky/lekce.md) | seznam nebo slovník |
| [24](../24-retezce-metody/lekce.md) | metoda řetězce (`strip`, `split`, `lower`, …) |
| [25](../25-soubory-cteni/lekce.md), [26](../26-soubory-zapis/lekce.md) | čtení textového souboru a zápis výsledku do jiného |

`global` nepoužívejte. Data mezi funkcemi posílejte parametrem a návratovou hodnotou.

## Téma projektu

Téma je **vaše**, učitel ho schválí v první hodině. Musí dávat smysl a splnit seznam v záložce **Úkoly**.

Nesmí to být kopie cvičení nebo úkolu z hodin (součet, čtverec, pozdrav, věk, nákup, odpočet, průměr známek, počet řádků).

Obsah podle školního řádu: slušné, bez urážek, násilí, erotiky, drog, zbraní a nenávisti. V datech nejsou známky spolužáků ani citlivé údaje o konkrétních lidech.

Nápady, které nemusíte použít: seznam knih a hledání podle autora, inventura skladu, docházka, výsledky závodu, jídelníček na týden.

## Časté chyby

| Chyba | Následek |
|-------|----------|
| hned kód bez návrhu | program neumí vysvětlit, co dělá |
| všechno v jedné funkci | chybí `return` a parametry |
| `global` místo parametru | porušení lekce 27 |
| data natvrdo v kódu | chybí čtení souboru |
| výsledek jen na obrazovku | chybí zápis do souboru |
| vstupní soubor s jedním řádkem | cyklus nad daty není vidět |

## Shrnutí

| Pojem | Význam |
|-------|--------|
| návrh | co program dělá a jaké má funkce **před** kódem |
| závěrečný projekt | jedna konzolová aplikace z lekcí 04–27, známka |

Známku určuje **učitel** (téma, návrh, splnění seznamu, že kód umíte vysvětlit). Automatický test výstup nekontroluje.

## Co dál

Ve 2. ročníku navážete objektovým programováním a SQL.

Volitelně: [Konzole](../../bonus/01-konzole/lekce.md), [Git a GitHub](../../bonus/02-git-a-github/lekce.md), [Docker](../../bonus/03-docker/lekce.md). Po souborech také [CSV, JSON a XML](../../bonus/05-csv-json-xml/lekce.md). Nejsou v 81 hodinách, lze je přeskočit.
