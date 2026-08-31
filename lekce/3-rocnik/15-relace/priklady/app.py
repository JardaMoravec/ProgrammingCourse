from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "skola"


@app.route("/", methods=["GET", "POST"])
def index():
    chyba = ""
    if request.method == "POST":
        jmeno = request.form.get("jmeno", "").strip()
        if not jmeno:
            chyba = "Vyplňte jméno."
        else:
            session["jmeno"] = jmeno
            return redirect(url_for("index"))
    return render_template(
        "index.html",
        chyba=chyba,
        jmeno=session.get("jmeno", ""),
    )


@app.route("/odhlasit", methods=["POST"])
def odhlasit():
    session.clear()
    return redirect(url_for("index"))
