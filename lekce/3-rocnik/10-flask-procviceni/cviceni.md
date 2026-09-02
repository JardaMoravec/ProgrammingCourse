# Cvičení — Flask základy (souhrn)

Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

---

## Cvičení 1 — Botanická zahrada (★★☆)

Soubor `zahrada.py`. Slovník aspoň dvou rostlin (klíče třeba `dub`, `kapradina`).

| Cesta | Chování |
|-------|---------|
| `/` | seznam odkazů přes `url_for` |
| `/rostlina/<slug>` | `<h1>` se slugem, `<p>` s popisem |

Dědičnost: menu jen v `templates/zaklad.html`, potomci `extends`.
Odkaz zpět na `/` také `url_for`. Dnes **neřešte** 404 — otevřete jen rostliny ze seznamu.

@reseni
`zahrada.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)

ROSTLINY = {
    "dub": "listnatý strom",
    "kapradina": "stínomilná rostlina",
}


@app.route("/")
def index():
    return render_template("index.html", rostliny=ROSTLINY)


@app.route("/rostlina/<slug>")
def rostlina(slug):
    return render_template("rostlina.html", slug=slug, popis=ROSTLINY[slug])
```

`templates/zaklad.html`:

```html
<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}Zahrada{% endblock %}</title>
</head>
<body>
  <nav>
    <a href="{{ url_for('index') }}">Domů</a>
  </nav>
  {% block obsah %}{% endblock %}
</body>
</html>
```

`templates/index.html`:

```html
{% extends "zaklad.html" %}
{% block title %}Rostliny{% endblock %}
{% block obsah %}
  <h1>Rostliny</h1>
  <ul>
    {% for slug in rostliny %}
      <li><a href="{{ url_for('rostlina', slug=slug) }}">{{ slug }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
```

`templates/rostlina.html`:

```html
{% extends "zaklad.html" %}
{% block title %}{{ slug }}{% endblock %}
{% block obsah %}
  <h1>{{ slug }}</h1>
  <p>{{ popis }}</p>
{% endblock %}
```

Spustění: `python -m flask --app zahrada run --debug`
@end

---

## Cvičení 2 — Planetárium (★★★)

Soubor `planety.py`. Stejná kostra jako ve cvičení 1 (dědičnost, `url_for`).

Do `app.config["NAZEV"]` uložte název webu a vypište ho na hlavní stránce
přes `{{ config.NAZEV }}`.

Dynamická cesta `/planeta/<slug>`. Slovník aspoň dvou planet.

| Situace | Stav |
|---------|------|
| slug ve slovníku | **200**, `<h1>` se slugem |
| slug chybí (třeba `/planeta/xyz`) | **`abort(404)`** |
| cesta bez routy (`/neexistuje`) | stejná `404.html` |

Handler: `return render_template("404.html"), 404`.
Na 404 stránce `<h1>Stránka neexistuje</h1>` a odkaz na `/` přes `url_for`.

Ověřte v Síti: existující planeta 200, `/planeta/xyz` i `/neexistuje` obojí 404.

@reseni
`planety.py`:

```python
from flask import Flask, abort, render_template

app = Flask(__name__)
app.config["NAZEV"] = "Školní planetárium"

PLANETY = {
    "mars": "červená planeta",
    "saturn": "planeta s prstenci",
}


@app.route("/")
def index():
    return render_template("index.html", planety=PLANETY)


@app.route("/planeta/<slug>")
def planeta(slug):
    if slug not in PLANETY:
        abort(404)
    return render_template("planeta.html", slug=slug, popis=PLANETY[slug])


@app.errorhandler(404)
def nenalezeno(chyba):
    return render_template("404.html"), 404
```

`templates/zaklad.html`:

```html
<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}{{ config.NAZEV }}{% endblock %}</title>
</head>
<body>
  <nav>
    <a href="{{ url_for('index') }}">Domů</a>
  </nav>
  {% block obsah %}{% endblock %}
</body>
</html>
```

`templates/index.html`:

```html
{% extends "zaklad.html" %}
{% block title %}Planety{% endblock %}
{% block obsah %}
  <h1>{{ config.NAZEV }}</h1>
  <ul>
    {% for slug in planety %}
      <li><a href="{{ url_for('planeta', slug=slug) }}">{{ slug }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
```

`templates/planeta.html`:

```html
{% extends "zaklad.html" %}
{% block title %}{{ slug }}{% endblock %}
{% block obsah %}
  <h1>{{ slug }}</h1>
  <p>{{ popis }}</p>
{% endblock %}
```

`templates/404.html`:

```html
{% extends "zaklad.html" %}
{% block title %}Nenalezeno{% endblock %}
{% block obsah %}
  <h1>Stránka neexistuje</h1>
  <p><a href="{{ url_for('index') }}">Zpět</a></p>
{% endblock %}
```

Spustění: `python -m flask --app planety run --debug`
@end
