from flask import Flask, abort, render_template

app = Flask(__name__)
app.config["NAZEV"] = "Školní nástěnka"

CLANKY = {
    1: "Zápis do kroužků začíná v pondělí.",
    2: "V pátek je ředitelské volno.",
}


@app.route("/")
def index():
    return render_template("index.html", clanky=CLANKY)


@app.route("/clanek/<int:cislo>")
def clanek(cislo):
    if cislo not in CLANKY:
        abort(404)
    return render_template("clanek.html", cislo=cislo, text=CLANKY[cislo])


@app.errorhandler(404)
def nenalezeno(chyba):
    return render_template("404.html"), 404
