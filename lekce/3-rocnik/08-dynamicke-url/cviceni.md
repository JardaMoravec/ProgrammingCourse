# Cvičení — Dynamické URL a url_for

Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

---

## Úkol 1 — Jméno v adrese (★☆☆)

Soubor `profil.py`. Jedna dynamická routa:

`/profil/<jmeno>`

Hodnotu z cesty předejte do šablony a vypište v `<h1>` (např. `Profil: Eva`).

Ověřte **dopsáním do adresy** v prohlížeči: `/profil/Eva` a `/profil/Petr`. Odkazy `url_for` ještě nepište — to je úkol 2.

@reseni
`profil.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/profil/<jmeno>")
def profil(jmeno):
    return render_template("profil.html", jmeno=jmeno)
```

`templates/profil.html`:

```html
<h1>Profil: {{ jmeno }}</h1>
```

Spustění: `python -m flask --app profil run --debug`
@end

---

## Úkol 2 — Pozdrav z URL (★★☆)

Soubor `pozdrav.py`. Routa `/ahoj/<jmeno>`: hodnotu z cesty vypište v `<h1>` (přes šablonu a `{{ jmeno }}`).

Na `/` dejte dva odkazy vytvořené `url_for('ahoj', jmeno='…')` — třeba Eva a Petr.

Ověřte `/ahoj/Eva` i kliknutí z hlavní stránky.

@reseni
`pozdrav.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ahoj/<jmeno>")
def ahoj(jmeno):
    return render_template("ahoj.html", jmeno=jmeno)
```

`templates/index.html`:

```html
<h1>Pozdravy</h1>
<p><a href="{{ url_for('ahoj', jmeno='Eva') }}">Eva</a></p>
<p><a href="{{ url_for('ahoj', jmeno='Petr') }}">Petr</a></p>
```

`templates/ahoj.html`:

```html
<h1>Ahoj, {{ jmeno }}</h1>
<p><a href="{{ url_for('index') }}">Zpět</a></p>
```

Spustění: `python -m flask --app pozdrav run --debug`
@end
