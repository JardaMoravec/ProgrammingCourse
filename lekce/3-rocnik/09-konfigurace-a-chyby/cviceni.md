# Cvičení — Konfigurace a chybové stránky

Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

---

## Úkol 1 — Vlastní 404 (★☆☆)

Soubor `chyba.py`. Jedna routa `/` se šablonou (stačí `<h1>`).

Přidejte `@app.errorhandler(404)` a šablonu `templates/404.html` s `<h1>Stránka neexistuje</h1>` a odkazem na `/` (`url_for`).

Handler musí vracet **`, 404`**. Ověřte v Síti: `/neexistuje` má stav 404 a vaši stránku, ne anglické Not Found.

@reseni
`chyba.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def nenalezeno(chyba):
    return render_template("404.html"), 404
```

`templates/index.html`:

```html
<h1>Domů</h1>
```

`templates/404.html`:

```html
<h1>Stránka neexistuje</h1>
<p><a href="{{ url_for('index') }}">Zpět na hlavní stránku</a></p>
```

Spustění: `python -m flask --app chyba run --debug`
@end

---

## Úkol 2 — Učebna, která není (★★☆)

Soubor `ucebny.py`. Slovník aspoň dvou učeben (klíče třeba `A12`, `B03`).

| Cesta | Chování |
|-------|---------|
| `/` | seznam odkazů přes `url_for` |
| `/ucebna/<kod>` | existuje → `<h1>` s kódem a `<p>` s popisem |
| `/ucebna/<kod>` | není ve slovníku → `abort(404)` |
| jakákoli jiná cesta | stejná `404.html` jako v úkolu 1 |

Ověřte `/ucebna/A12` (200) i `/ucebna/Z99` (404).

@reseni
`ucebny.py`:

```python
from flask import Flask, abort, render_template

app = Flask(__name__)

UCEBNY = {
    "A12": "počítačová učebna",
    "B03": "laboratoř",
}


@app.route("/")
def index():
    return render_template("index.html", ucebny=UCEBNY)


@app.route("/ucebna/<kod>")
def ucebna(kod):
    if kod not in UCEBNY:
        abort(404)
    return render_template("ucebna.html", kod=kod, popis=UCEBNY[kod])


@app.errorhandler(404)
def nenalezeno(chyba):
    return render_template("404.html"), 404
```

`templates/index.html`:

```html
<h1>Učebny</h1>
<ul>
  {% for kod in ucebny %}
    <li><a href="{{ url_for('ucebna', kod=kod) }}">{{ kod }}</a></li>
  {% endfor %}
</ul>
```

`templates/ucebna.html`:

```html
<h1>{{ kod }}</h1>
<p>{{ popis }}</p>
<p><a href="{{ url_for('index') }}">Zpět</a></p>
```

`templates/404.html`:

```html
<h1>Stránka neexistuje</h1>
<p><a href="{{ url_for('index') }}">Zpět</a></p>
```

Spustění: `python -m flask --app ucebny run --debug`
@end
