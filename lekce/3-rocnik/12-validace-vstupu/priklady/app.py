from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    chyba = ""
    zprava = ""
    raw = ""
    if request.method == "POST":
        raw = request.form.get("pocet", "").strip()
        if not raw:
            chyba = "Zadejte počet."
        else:
            try:
                pocet = int(raw)
            except ValueError:
                chyba = "Zadejte celé číslo."
            else:
                zprava = f"Objednáno sešitů: {pocet}"
    return render_template("index.html", chyba=chyba, zprava=zprava, pocet=raw)
