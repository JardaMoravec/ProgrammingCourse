# Cvičení — Statické soubory

Soubory spouštějte ze složky, kde leží `.py`, `templates/` i `static/`:

```bash
python -m flask --app NAZEV run --debug
```

---

## Úkol 1 — Barva nadpisu (★☆☆)

Soubor `oznameni.py`, šablona `templates/index.html` a `static/styly.css`.

Na `/` zobrazte `<h1>` a jeden `<p>`. CSS napojte z šablony (`url_for` nebo `/static/styly.css`) a nastavte nadpisu **barvu** (libovolnou).

V DevTools → Síť ověřte, že `/static/styly.css` vrací **200**.

@reseni
`oznameni.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
```

`templates/index.html`:

```html
<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <title>Oznámení</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='styly.css') }}">
</head>
<body>
  <h1>Ředitelské volno</h1>
  <p>V pátek výuka odpadá.</p>
</body>
</html>
```

`static/styly.css`:

```css
h1 {
  color: #2563eb;
}
```

Spustění: `python -m flask --app oznameni run --debug`
@end

---

## Úkol 2 — Logo v základu (★★☆)

Soubor `atelier.py`. Dědičnost z lekce 06 + statické soubory:

- `templates/zaklad.html` — menu (`/` a `/kontakt`), odkaz na CSS, v hlavičce `<img>` na `static/logo.svg`
- `templates/index.html` a `templates/kontakt.html` — `extends`, blok `obsah` s `<h1>` a `<p>`
- `static/styly.css` — aspoň jedna vlastnost (třeba mezera u menu)
- `static/logo.svg` — jednoduché SVG (klidně čtverec a písmeno)

Ověřte obě stránky: logo i styly jsou na obou.

@reseni
`atelier.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")
```

`templates/zaklad.html`:

```html
<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <title>Ateliér</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='styly.css') }}">
</head>
<body>
  <p><img src="{{ url_for('static', filename='logo.svg') }}" alt="Logo" width="48" height="48"></p>
  <nav>
    <a href="/">Domů</a>
    <a href="/kontakt">Kontakt</a>
  </nav>
  {% block obsah %}{% endblock %}
</body>
</html>
```

`templates/index.html`:

```html
{% extends "zaklad.html" %}
{% block obsah %}
  <h1>Ateliér keramiky</h1>
  <p>Točíme na kruhu v úterý.</p>
{% endblock %}
```

`templates/kontakt.html`:

```html
{% extends "zaklad.html" %}
{% block obsah %}
  <h1>Kontakt</h1>
  <p>atelier@skola.cz</p>
{% endblock %}
```

`static/styly.css`:

```css
nav a {
  margin-right: 0.75rem;
}
```

`static/logo.svg` — stačí malý soubor SVG (čtverec + písmeno), viz `priklady/static/logo.svg`.

Spustění: `python -m flask --app atelier run --debug`
@end
