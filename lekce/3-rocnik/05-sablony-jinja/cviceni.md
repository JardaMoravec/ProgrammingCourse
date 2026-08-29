# Cvičení — Šablony Jinja2

Soubory spouštějte **ze složky**, kde leží `.py` i `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

---

## Úkol 1 — První šablona (★☆☆)

Soubor `vitani.py` a `templates/index.html`. Na `/` použijte `render_template` — **ne** HTML v `return` řetězci.

Šablona má mít `<h1>` s textem `Vítej` a jeden `<p>` (libovolná věta).

@reseni
`vitani.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
```

`templates/index.html`:

```html
<h1>Vítej</h1>
<p>Toto je první šablona.</p>
```

Spustění: `python -m flask --app vitani run --debug`
@end

---

## Úkol 2 — Vizitka z proměnných (★★☆)

Soubor `vizitka.py` a `templates/index.html`. Do šablony předejte **jméno** a **obor** (klidně fiktivní).

Na `/` musí být:

- `<h1>` s jménem přes `{{ … }}`,
- `<p>` s oborem přes `{{ … }}`.

V Pythonu hodnoty uložte do proměnných a předejte je `render_template`.

@reseni
`vizitka.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)

jmeno = "Eva Nováková"
obor = "informační technologie"


@app.route("/")
def index():
    return render_template("index.html", jmeno=jmeno, obor=obor)
```

`templates/index.html`:

```html
<h1>{{ jmeno }}</h1>
<p>{{ obor }}</p>
```

Spustění: `python -m flask --app vizitka run --debug`
@end

---

## Úkol 3 — Jídelníček (★★★)

Soubor `jidelna.py` a dvě šablony. Dvě routy:

| Cesta | Šablona | Obsah |
|-------|---------|--------|
| `/` | `index.html` | `<h1>` název jídelny (z Pythonu), seznam **alespoň tří** jídel přes `{% for %}` jako `<ul>` / `<li>`, odkaz na `/oteviracka` |
| `/oteviracka` | `oteviracka.html` | `<h1>Otevírací doba</h1>`, jeden `<p>`, odkaz zpět na `/` |

Jídla držte v Pythonu jako seznam. V prohlížeči ověřte obě adresy i odkazy.

@reseni
`jidelna.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)

jidla = ["polévka", "řízek s bramborem", "kompot"]


@app.route("/")
def index():
    return render_template("index.html", nazev="Školní jídelna", jidla=jidla)


@app.route("/oteviracka")
def oteviracka():
    return render_template("oteviracka.html")
```

`templates/index.html`:

```html
<h1>{{ nazev }}</h1>
<ul>
  {% for jidlo in jidla %}
    <li>{{ jidlo }}</li>
  {% endfor %}
</ul>
<p><a href="/oteviracka">Otevírací doba</a></p>
```

`templates/oteviracka.html`:

```html
<h1>Otevírací doba</h1>
<p>Po–Pá 11:00–14:00</p>
<p><a href="/">Zpět na jídelníček</a></p>
```

Spustění: `python -m flask --app jidelna run --debug`
@end
