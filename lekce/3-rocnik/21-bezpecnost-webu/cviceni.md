# Cvičení — Bezpečnost (XSS, SQL injection)

Dnes dvě malé aplikace — každá na **jeden** problém. Formulář z [lekce 11](../11-formulare-a-request/lekce.md), šablona z [lekce 05](../05-sablony-jinja/lekce.md).

Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

---

## Cvičení 1 — Pozdrav (★☆☆)

Soubor `pozdrav.py`. **Bez databáze.**

Na `/` formulář **GET** s polem `name="jmeno"`. Hodnotu čtěte `request.args.get("jmeno", "")`.
Když není prázdná, na stránce **`Ahoj, `** a jméno ze šablony.

Do pole napište `<b>Eva</b>` a zkuste **obě** varianty v šabloně (Python neměňte):

| Zápis v šabloně | Co uvidíte |
|-----------------|------------|
| `jmeno` s filtrem `safe` | **tučné** Eva — prohlížeč značku spustí |
| `{{ jmeno }}` | znaky `&lt;b&gt;`, ne tučné písmo |

Nechte tam **`{{ jmeno }}`** bez `|safe`.

@reseni
`pozdrav.py` je u obou stejný:

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    jmeno = request.args.get("jmeno", "")
    return render_template("index.html", jmeno=jmeno)
```

`templates/index.html` — nejdřív bez kontroly (`|safe`):

```html
<h1>Pozdrav</h1>
<form action="{{ url_for('index') }}" method="get">
  <label>Jméno <input name="jmeno" value="{{ jmeno }}"></label>
  <button type="submit">Pozdravit</button>
</form>
{% if jmeno %}
  <p>Ahoj, {{ jmeno|safe }}</p>
{% endif %}
```

Pak `|safe` smažte:

```html
  <p>Ahoj, {{ jmeno }}</p>
```

Spustění: `python -m flask --app pozdrav run --debug`
@end

---

## Cvičení 2 — Hledání města (★★☆)

Soubor `mesta.py`. Zkopírujte `data/mesta.db` vedle něj (uvnitř **Praha** a **Brno**).

Na `/` formulář **GET** s polem `name="q"`. Tabulka `mesta`, sloupec `nazev`.

- prázdné `q`: vypište **obě** města (`SELECT nazev`, `fetchall`),
- neprázdné: `WHERE nazev = ?` a hodnotu v tuple — **přesný** název.

SQL neskládejte f-řetězcem. `g` nepotřebujete. Spojení otevřete, přečtěte, zavřete.

Vyzkoušejte `Praha` (jen jeden řádek). Pak do pole napište uvozovku — **nesmí** se objevit obě města najednou.

@reseni
`mesta.py`:

```python
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    q = request.args.get("q", "").strip()
    conn = sqlite3.connect("mesta.db")
    conn.row_factory = sqlite3.Row
    if q:
        radky = conn.execute(
            "SELECT nazev FROM mesta WHERE nazev = ?",
            (q,),
        ).fetchall()
    else:
        radky = conn.execute("SELECT nazev FROM mesta").fetchall()
    conn.close()
    return render_template("index.html", radky=radky, q=q)
```

`templates/index.html`:

```html
<h1>Města</h1>
<form action="{{ url_for('index') }}" method="get">
  <label>Název <input name="q" value="{{ q }}"></label>
  <button type="submit">Hledat</button>
</form>
<ul>
  {% for radek in radky %}
    <li>{{ radek.nazev }}</li>
  {% endfor %}
</ul>
```

Spustění: `python -m flask --app mesta run --debug`
@end
