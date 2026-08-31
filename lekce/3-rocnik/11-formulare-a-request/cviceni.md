# Cvičení — Formuláře a objekt request

Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

---

## Úkol 1 — Hledání (★☆☆)

Soubor `hledani.py`. Na `/` formulář **GET** s polem `name="q"`.

Po odeslání se v adrese objeví `?q=…`. Hodnotu přečtěte `request.args.get("q", "")` a vypište ji na stránce (třeba `Hledáte: pes`).

Ověřte v adresním řádku i v Síti, že jde o **GET**.

@reseni
`hledani.py`:

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    dotaz = request.args.get("q", "")
    return render_template("index.html", dotaz=dotaz)
```

`templates/index.html`:

```html
<h1>Hledání</h1>
<form action="{{ url_for('index') }}" method="get">
  <label>Hledat <input name="q"></label>
  <button type="submit">Hledat</button>
</form>
{% if dotaz %}
  <p>Hledáte: {{ dotaz }}</p>
{% endif %}
```

Spustění: `python -m flask --app hledani run --debug`
@end

---

## Úkol 2 — Otázka třídnímu (★★☆)

Soubor `dotaz.py`. Na `/` formulář **POST** s polem `name="otazka"`.

Routa musí přijímat GET i POST (`methods=["GET", "POST"]`). Text přečtěte
`request.form.get("otazka", "")` a po odeslání ho vypište na stránce.

Ověřte v Síti: odeslání je **POST**, stav 200, v adrese **není** `?otazka=`.

@reseni
`dotaz.py`:

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    if request.method == "POST":
        text = request.form.get("otazka", "")
    return render_template("index.html", text=text)
```

`templates/index.html`:

```html
<h1>Schránka otázek</h1>
{% if text %}
  <p>Otázka: {{ text }}</p>
{% endif %}
<form action="{{ url_for('index') }}" method="post">
  <label>Otázka <input name="otazka"></label>
  <button type="submit">Odeslat</button>
</form>
```

Spustění: `python -m flask --app dotaz run --debug`
@end
