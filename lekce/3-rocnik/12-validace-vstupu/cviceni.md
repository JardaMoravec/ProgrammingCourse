# Cvičení — Validace dat na serveru

Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

---

## Úkol 1 — Rezervace hřiště (★☆☆)

Soubor `rezervace.py`. Formulář POST, pole `name="jmeno"`.

Po odeslání:

- prázdné jméno nebo samé mezery → na stránce **`Vyplňte jméno`** (formulář zůstane),
- neprázdné → vypište jméno (třeba `Rezervováno: Eva`).

Použijte `.strip()`. Ověřte odeslání bez vyplnění i se jménem.

@reseni
`rezervace.py`:

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    chyba = ""
    jmeno = ""
    if request.method == "POST":
        jmeno = request.form.get("jmeno", "").strip()
        if not jmeno:
            chyba = "Vyplňte jméno"
    return render_template("index.html", chyba=chyba, jmeno=jmeno)
```

`templates/index.html`:

```html
<h1>Rezervace hřiště</h1>
{% if chyba %}
  <p>{{ chyba }}</p>
{% endif %}
{% if jmeno and not chyba %}
  <p>Rezervováno: {{ jmeno }}</p>
{% endif %}
<form action="{{ url_for('index') }}" method="post">
  <label>Jméno <input name="jmeno" value="{{ jmeno }}"></label>
  <button type="submit">Rezervovat</button>
</form>
```

Spustění: `python -m flask --app rezervace run --debug`
@end

---

## Úkol 2 — Věk do dotazníku (★★☆)

Soubor `vek.py`. Formulář POST, pole `name="vek"`.

Po odeslání:

- nejde převést na `int` (`abc`, prázdné, `3.5`) → **`Zadejte celé číslo`**,
- celé číslo → vypište ho (třeba `Věk: 15`).

Použijte `try` / `except ValueError`. Prázdné pole můžete nejdřív odchytit `.strip()` jako v úkolu 1, nebo nechat spadnout do `ValueError` — obojí je dnes v pořádku.

@reseni
`vek.py`:

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    chyba = ""
    zprava = ""
    raw = ""
    if request.method == "POST":
        raw = request.form.get("vek", "").strip()
        try:
            vek = int(raw)
        except ValueError:
            chyba = "Zadejte celé číslo"
        else:
            zprava = f"Věk: {vek}"
    return render_template("index.html", chyba=chyba, zprava=zprava, raw=raw)
```

`templates/index.html`:

```html
<h1>Dotazník</h1>
{% if chyba %}
  <p>{{ chyba }}</p>
{% endif %}
{% if zprava %}
  <p>{{ zprava }}</p>
{% endif %}
<form action="{{ url_for('index') }}" method="post">
  <label>Věk <input name="vek" value="{{ raw }}"></label>
  <button type="submit">Odeslat</button>
</form>
```

Spustění: `python -m flask --app vek run --debug`
@end
