from flask import Flask, flash, redirect, render_template, request, url_for

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
            flash(f"Zapsáno: {jmeno}")
            return redirect(url_for("index"))
    return render_template("index.html", chyba=chyba)
