from flask import Flask, redirect, render_template_string, request, url_for

app = Flask(__name__)
PRODUKTY = [{"nazwa": "Zeszyt A5", "cena": 4.5}]
STRONA = """<h1>Magazyn</h1>
{% if blad %}<p data-test="blad">{{ blad }}</p>{% endif %}
<ul>{% for p in produkty %}<li class="produkt">{{ p.nazwa }} — {{ '%.2f'|format(p.cena) }} zł</li>{% endfor %}</ul>
<form method="post"><input name="nazwa" value="{{ nazwa }}"><input name="cena"><button data-test="zapisz">Zapisz</button></form>"""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nazwa = request.form.get("nazwa", "").strip()
        try:
            cena = float(request.form.get("cena", "").replace(",", "."))
        except ValueError:
            cena = None
        if not nazwa:
            blad = "Podaj nazwę produktu"
        elif cena is None or cena < 0:
            blad = "Cena musi być liczbą nieujemną"
        else:
            PRODUKTY.append({"nazwa": nazwa, "cena": cena})
            return redirect(url_for("index"))
        return render_template_string(STRONA, produkty=PRODUKTY, blad=blad, nazwa=nazwa), 400
    return render_template_string(STRONA, produkty=PRODUKTY, blad=None, nazwa="")


klient = app.test_client()
print(klient.get("/").status_code)
odp = klient.post("/", data={"nazwa": "Klej", "cena": "3,40"})
print(odp.status_code, odp.headers["Location"])
odp = klient.post("/", data={"nazwa": "", "cena": "5"})
print(odp.status_code, "Podaj nazwę produktu" in odp.get_data(as_text=True))
odp = klient.post("/", data={"nazwa": "<b>X</b>", "cena": "-1"})
print(odp.status_code, "&lt;b&gt;X&lt;/b&gt;" in odp.get_data(as_text=True))
print([p["nazwa"] for p in PRODUKTY])
