# Cvičení — CSV, JSON a XML

Soubory ze složky `priklady/` si zkopírujte vedle skriptu. Spouštějte ze stejné složky.

---

## Cvičení 1 — CSV (★☆☆)

Ze souboru `zaci.csv` vypište jména žáků starších 16 let (věk jako číslo), každé na vlastní řádek.

@reseni
```python
import csv

with open("zaci.csv", "r", encoding="utf-8", newline="") as f:
    for radek in csv.DictReader(f):
        if int(radek["vek"]) > 16:
            print(radek["jmeno"])
```

U ukázkových dat: `Petr`.
@end

---

## Cvičení 2 — JSON (★★☆)

Ze souboru `zaci.json` vypište **počet** žáků a pod tím všechna jména v původním pořadí.

@reseni
```python
import json

with open("zaci.json", "r", encoding="utf-8") as f:
    zaci = json.load(f)

print(len(zaci))
for zak in zaci:
    print(zak["jmeno"])
```

U ukázkových dat:

```
2
Anna
Petr
```
@end

---

## Cvičení 3 — XML (★★☆)

Ze souboru `zaci.xml` vypište jména ve formátu `Jméno (věk)`.

@reseni
```python
import xml.etree.ElementTree as ET

koren = ET.parse("zaci.xml").getroot()
for zak in koren.findall("zak"):
    jmeno = zak.find("jmeno").text
    vek = zak.find("vek").text
    print(f"{jmeno} ({vek})")
```

```
Anna (16)
Petr (17)
```
@end

---

## Cvičení 4 — Který formát? (★☆☆)

Ke každé situaci napište **CSV**, **JSON**, nebo **XML** a jednu větu proč.

1. Export známek do Excelu (jeden žák = jeden řádek, stejné sloupce).
2. Seznam knih, u každé vnořený objekt autora (jméno + rok narození).
3. Starší školní systém posílá rozvrh ve značkách `<hodina>`.

@reseni
1. **CSV** — plochá tabulka, Excel ho otevře.
2. **JSON** — vnořený objekt; v CSV byste autora „spláceli“ do sloupců.
3. **XML** — značky; dnes by to spíš bylo JSON, ale zadání je XML.
@end
