import os

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "skola"

SLOZKA = os.path.join("static", "uploads")


@app.route("/", methods=["GET", "POST"])
def index():
    chyba = ""
    if request.method == "POST":
        soubor = request.files.get("soubor")
        if soubor is None or soubor.filename == "":
            chyba = "Vyberte soubor."
        else:
            jmeno = secure_filename(soubor.filename)
            if not jmeno:
                chyba = "Vyberte soubor."
            else:
                os.makedirs(SLOZKA, exist_ok=True)
                soubor.save(os.path.join(SLOZKA, jmeno))
                flash("Uloženo: " + jmeno)
                return redirect(url_for("index"))
    obrazky = []
    if os.path.isdir(SLOZKA):
        obrazky = os.listdir(SLOZKA)
    return render_template("index.html", chyba=chyba, obrazky=obrazky)
