from flask import Flask, abort, render_template

app = Flask(__name__)
app.config["NAZEV"] = "Půjčovna kol"

KOLA = {
    "treking": "Trekingové kolo na delší výlety.",
    "mesto": "Městské kolo do provozu.",
    "elektrokolo": "Elektrokolo s dojezdem 80 km.",
}


@app.route("/")
def index():
    return render_template("index.html", kola=KOLA)


@app.route("/kolo/<slug>")
def kolo(slug):
    if slug not in KOLA:
        abort(404)
    return render_template("kolo.html", slug=slug, popis=KOLA[slug])


@app.errorhandler(404)
def nenalezeno(chyba):
    return render_template("404.html"), 404
