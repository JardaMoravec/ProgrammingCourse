# Cvičení — Routy a pohledové funkce

Soubory spouštějte v téže složce:

```bash
python -m flask --app NAZEV run --debug
```

(`NAZEV` = jméno souboru bez `.py`.)

---

## Cvičení 1 — Dvě adresy (★☆☆)

Soubor `dve_stranky.py`. Dvě routy, **prostý text** (ne HTML):

| Cesta | Odpověď |
|-------|---------|
| `/` | `Hlavní stránka` |
| `/info` | `Flask běží` |

Obě otevřete v prohlížeči (`/info` dopsat za `:5000`). Na `/neexistuje` ověřte **404**.

@reseni
```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hlavní stránka"


@app.route("/info")
def info():
    return "Flask běží"
```

Spustění: `python -m flask --app dve_stranky run --debug`
@end

---

## Cvičení 2 — Bufet (★★☆)

Soubor `bufet.py`. Dvě routy, odpověď je **krátké HTML** (ne prostý text):

| Cesta | Obsah |
|-------|--------|
| `/` | `<h1>` s názvem bufetu, `<p>` s dnešním jídlem, odkaz na `/alergeny` |
| `/alergeny` | `<h1>Alergeny</h1>`, jeden `<p>` (klidně vymyšlený seznam), odkaz zpět na `/` |

V prohlížeči klikněte na odkazy — nesmí skončit na 404.

@reseni
```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <h1>Školní bufet</h1>
    <p>Dnes: guláš s knedlíkem.</p>
    <p><a href="/alergeny">Alergeny</a></p>
    """


@app.route("/alergeny")
def alergeny():
    return """
    <h1>Alergeny</h1>
    <p>Lepek, mléko.</p>
    <p><a href="/">Zpět na bufet</a></p>
    """
```

Spustění: `python -m flask --app bufet run --debug`
@end

---

## Cvičení 3 — Nástěnka třídy (★★★)

Soubor `nastenka.py`. Tři routy, na každé **HTML** a odkazy na **obě ostatní** stránky:

| Cesta | Stránka |
|-------|---------|
| `/` | název třídy a krátké uvítání |
| `/rozvrh` | jeden údaj k rozvrhu (třeba „pondělí: matematika“) |
| `/sluzby` | kdo má tento týden službu |

Stačí `<h1>`, `<p>` a `<a href="…">`. Ověřte, že z každé stránky jdou otevřít zbylé dvě.

@reseni
```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <h1>3.A</h1>
    <p>Nástěnka třídy.</p>
    <p><a href="/rozvrh">Rozvrh</a> · <a href="/sluzby">Služby</a></p>
    """


@app.route("/rozvrh")
def rozvrh():
    return """
    <h1>Rozvrh</h1>
    <p>Pondělí: matematika.</p>
    <p><a href="/">Domů</a> · <a href="/sluzby">Služby</a></p>
    """


@app.route("/sluzby")
def sluzby():
    return """
    <h1>Služby</h1>
    <p>Tento týden: Novák, Dvořáková.</p>
    <p><a href="/">Domů</a> · <a href="/rozvrh">Rozvrh</a></p>
    """
```

Spustění: `python -m flask --app nastenka run --debug`
@end
