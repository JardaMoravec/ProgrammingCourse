---
id: 14-nahravani-souboru
rocnik: 3
nazev: Nahrávání souborů a obrázků
hodiny: 2
obtiznost: zacatecnik
prerekvizity: [13-presmerovani-a-flash]
cile:
  - Napíše formulář s enctype multipart a input type file
  - Přečte nahrávku z request.files a uloží ji na disk
  - Zobrazí nahraný obrázek ze static/uploads
---

# Nahrávání souborů a obrázků

## Cíle lekce

- Do formuláře přidáte **soubor** (`input type="file"`)
- Soubor z požadavku uložíte na disk
- Obrázek ukážete ze složky `static/` — jako v [lekci 07](../07-staticke-soubory/lekce.md)

Text z formuláře je v `request.form` ([lekce 11](../11-formulare-a-request/lekce.md)). **Soubor tam není.** Přijde zvlášť, v `request.files`.

Zápis `open(…)` z 1. ročníku je pro text, který program sám vytvoří. Nahrávku z prohlížeče ukládá Flask metodou `.save()`.

## Formulář musí poslat soubor

Bez dvou věcí prohlížeč soubor **nepošle**:

```html
<form action="{{ url_for('index') }}" method="post" enctype="multipart/form-data">
  <label>Soubor <input type="file" name="soubor"></label>
  <button type="submit">Nahrát</button>
</form>
```

| Atribut | Proč |
|---------|------|
| `method="post"` | soubor patří do těla požadavku, ne do URL |
| `enctype="multipart/form-data"` | jinak Flask v `request.files` nic nemá |
| `type="file"` | v prohlížeči tlačítko *Procházet* |
| `name="soubor"` | stejný klíč v Pythonu: `request.files.get("soubor")` |

V Síti uvidíte POST se typem `multipart/form-data`, ne obyčejný formulář.

## request.files a uložení

```python
from werkzeug.utils import secure_filename
import os

soubor = request.files.get("soubor")
if soubor is None or soubor.filename == "":
    chyba = "Vyberte soubor."
else:
    jmeno = secure_filename(soubor.filename)
    os.makedirs("static/uploads", exist_ok=True)
    soubor.save(os.path.join("static", "uploads", jmeno))
```

`soubor.filename` je název z **klientského** počítače. `secure_filename` z něj udělá bezpečnou variantu (`../tajne.txt` se neuloží mimo složku). Balíček `werkzeug` máte s Flaskem, `pip` navíc nepotřebujete.

`os.makedirs(…, exist_ok=True)` složku `static/uploads` vytvoří, pokud ještě není. Bez ní `.save()` spadne.

Prázdný výběr poznáte podle `filename == ""`. `if not soubor` nestačí — objekt často existuje i bez souboru.

Úspěch: `flash` a `redirect` jako v [lekci 13](../13-presmerovani-a-flash/lekce.md). Chyba: stav **200**, `{{ chyba }}`, bez přesměrování.

## Obrázek na stránce

Soubor ve `static/uploads/foto.png` Flask naservíruje na `/static/uploads/foto.png`. V šabloně:

```html
<img src="{{ url_for('static', filename='uploads/foto.png') }}" alt="Nahraná fotka">
```

Prohlížeč ho stáhne **dalším GET** — stejný princip jako CSS v lekci 07.

Když ukládáte vždy pod stejným názvem (`foto.png`), další nahrání předchozí soubor přepíše. Jména v databázi jsou až později.

V ukázce se na GET vypíšou **všechny** soubory ze složky (`os.listdir`) — jednoduchá nástěnka.

![Schéma: POST soubor, uložení, GET obrázku ze static](diagramy/nahrani-souboru.svg)

→ kompletní příklad: `priklady/app.py` a `priklady/templates/index.html`

## Časté chyby

- chybí `enctype="multipart/form-data"` — `request.files` je prázdné,
- čtete `request.form` místo `request.files`,
- `input` bez `name`,
- ukládáte mimo `static/` a v `img` čekáte `/static/…`,
- chybí `os.makedirs` — složka `uploads` neexistuje,
- berete `filename` bez `secure_filename`.

## Shrnutí

| Pojem | Význam |
|-------|--------|
| `enctype="multipart/form-data"` | formulář umí poslat soubor |
| `request.files` | nahrané soubory (ne `request.form`) |
| `secure_filename` | bezpečný název souboru |
| `.save(cesta)` | zápis na disk |
| `static/uploads/` | místo, odkud jde obrázek znovu stáhnout |

## Co dál

→ [Lekce 15: Relace (session)](../15-relace/lekce.md)
