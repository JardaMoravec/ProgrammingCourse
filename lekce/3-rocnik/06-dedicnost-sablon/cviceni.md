# Cvičení — Dědičnost šablon

Soubory spouštějte ze složky, kde leží `.py` i `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

---

## Úkol 1 — Základ a jedna stránka (★☆☆)

Soubor `klub.py`. Šablony `templates/zaklad.html` a `templates/index.html`.

- V základu kostra stránky a blok `obsah`.
- `index.html` základ **rozšíří** (`extends`) a v bloku dá `<h1>` s názvem kroužku a jeden `<p>`.
- Na `/` renderujte **potomka**, ne základ.

@reseni
`klub.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
```

`templates/zaklad.html`:

```html
<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <title>Kroužek</title>
</head>
<body>
  {% block obsah %}{% endblock %}
</body>
</html>
```

`templates/index.html`:

```html
{% extends "zaklad.html" %}
{% block obsah %}
  <h1>Foto kroužek</h1>
  <p>Fotíme ve středu odpoledne.</p>
{% endblock %}
```

Spustění: `python -m flask --app klub run --debug`
@end

---

## Úkol 2 — Společné menu (★★☆)

Soubor `muzeum.py`. Tři šablony: `zaklad.html`, `index.html`, `sbirka.html`.

V **základu** menu s odkazy na `/` a `/sbirka`. Dvě routy, obě přes `extends`:

| Cesta | Šablona | V bloku `obsah` |
|-------|---------|------------------|
| `/` | `index.html` | `<h1>` název muzea, jeden `<p>` |
| `/sbirka` | `sbirka.html` | `<h1>Sbírka</h1>`, jeden `<p>` |

Menu nekopírujte do potomků. V prohlížeči ověřte, že je vidět na **obou** stránkách.

@reseni
`muzeum.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sbirka")
def sbirka():
    return render_template("sbirka.html")
```

`templates/zaklad.html`:

```html
<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <title>Muzeum</title>
</head>
<body>
  <nav>
    <a href="/">Domů</a>
    <a href="/sbirka">Sbírka</a>
  </nav>
  {% block obsah %}{% endblock %}
</body>
</html>
```

`templates/index.html`:

```html
{% extends "zaklad.html" %}
{% block obsah %}
  <h1>Městské muzeum</h1>
  <p>Expozice dějin města.</p>
{% endblock %}
```

`templates/sbirka.html`:

```html
{% extends "zaklad.html" %}
{% block obsah %}
  <h1>Sbírka</h1>
  <p>Pravěké nálezy z okolí.</p>
{% endblock %}
```

Spustění: `python -m flask --app muzeum run --debug`
@end
