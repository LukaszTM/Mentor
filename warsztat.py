# -*- coding: utf-8 -*-
"""
Warsztat — narzędzia wewnętrzne Mentora: kalkulatory kadrowo-płacowe, symulator eZUS/Płatnika, symulator e-Urzędu (PIT),
biblioteka przepisów offline. Zero kont zewnętrznych, zero instalacji: wszystko liczy kadry.py, wyniki zapisują się
do katalogu projektu ucznia. Widok buduje mentor.py (widok_warsztat) przez zbuduj(app, parent, narzedzie).
"""

import csv
import datetime as dt
import io
import json
import random
import tkinter as tk
from pathlib import Path
from tkinter import ttk

import kadry
from program import P

NARZEDZIA = [
    ("firma", "🏭", "Firma ćwiczeniowa"), ("place", "💰", "Lista płac"), ("zasilki", "🩺", "Zasiłki i chorobowe"),
    ("urlopy", "🏖", "Urlopy i ekwiwalent"), ("czas", "⏰", "Czas pracy"), ("potracenia", "⚖", "Potrącenia"),
    ("delegacje", "🚚", "Delegacje i diety"), ("zus", "📨", "eZUS / Płatnik"), ("pit", "🧾", "e-Urząd: PIT"), ("przepisy", "📚", "Przepisy"),
]
NAZWY = {k: n for k, _, n in NARZEDZIA}
MIESIACE = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]


# ============================================================ stan i pomocnicze
def _M():
    import mentor
    return mentor


def stan(app):
    """Dane Warsztatu bieżącego programu (zapisywane w mentor_dane.json pod programem)."""
    w = app.stan.d.setdefault("warsztat", {})
    if not w.get("osoby"):
        w["osoby"] = json.loads(json.dumps(P.firma_osoby))
        for o in w["osoby"]:
            o.setdefault("dokumenty", [])
    for k in ("kartoteka", "rsa", "komplety", "wyslane", "pit_wyslane"):
        w.setdefault(k, [])
    if "ezla" not in w:
        w["ezla"] = _seed_ezla(w["osoby"])
    return w


def _seed_ezla(osoby):
    """Fikcyjne e-ZLA w skrzynce płatnika (jak w eZUS) — dla osób z firmy ćwiczeniowej."""
    rok = kadry.DOMYSLNE["rok"]
    wz = [(0, (3, 10), (3, 19), "A", "choroba"), (1, (6, 2), (6, 25), "", "choroba"), (4, (11, 3), (11, 9), "", "opieka nad dzieckiem (PESEL dziecka)"),
          (6, (9, 14), (10, 2), "", "choroba — pobyt w szpitalu 14–20.09"), (2, (11, 16), (11, 27), "", "choroba"), (7, (5, 1), (5, 14), "", "wypadek w drodze do pracy")]
    out = []
    for i, (idx, od, do, kod, opis) in enumerate(wz, 1):
        if idx >= len(osoby):
            continue
        o = osoby[idx]
        out.append({"nr": f"ZLA{rok}{i:04d}", "pesel": o["pesel"], "osoba": f"{o['imie']} {o['nazwisko']}", "od": f"{rok}-{od[0]:02d}-{od[1]:02d}",
                    "do": f"{rok}-{do[0]:02d}-{do[1]:02d}", "kod": kod, "opis": opis, "pobrane": False})
    return out


def _osoba_etykieta(o):
    return f"{o['imie']} {o['nazwisko']} — {o.get('stanowisko', '')} ({o.get('rodzaj', '')})"


def _data(s):
    s = (s or "").strip()
    for f in ("%Y-%m-%d", "%d.%m.%Y", "%d-%m-%Y"):
        try:
            return dt.datetime.strptime(s, f).date()
        except ValueError:
            pass
    return None


def _liczba(s, dom=0.0):
    try:
        return float(str(s).replace(",", ".").replace(" ", "") or dom)
    except ValueError:
        return dom


def zapisz_do_projektu(app, podkatalog, nazwa, tresc, status=None):
    proj = app.stan.d.get("projekt")
    if not proj:
        if status:
            status.configure(text="Najpierw wskaż katalog projektu (Mój projekt).", fg=_M().K["czerw"])
        return None
    cel = Path(proj) / podkatalog
    cel.mkdir(parents=True, exist_ok=True)
    p = cel / nazwa
    p.write_text(tresc, encoding="utf-8")
    if status:
        status.configure(text=f"✔ zapisano {podkatalog}/{nazwa}", fg=_M().K["ziel"])
    app._pliki_cache.clear()
    return p


def _formatuj_kroki(tytul, kroki, szer=78, zawijaj=False):
    """Kroki obliczeń: opis ...... wartość. zawijaj=True — długi opis łamie się na kilka linii (szerokość szer), wartość na końcu."""
    import textwrap
    linie = [tytul, "=" * len(tytul)]
    for opis, wartosc in kroki:
        w = kadry.fmt(wartosc) if isinstance(wartosc, (int, float)) else str(wartosc)
        if len(opis) + len(w) + 3 > szer:
            if zawijaj:
                cz = textwrap.wrap(opis, szer - 4) or [""]
                linie.extend(cz[:-1])
                ost = cz[-1]
                if len(ost) + len(w) + 3 > szer:
                    linie.append(ost)
                    linie.append(" " * (szer - len(w)) + w)
                else:
                    linie.append(ost + " " + "." * (szer - len(ost) - len(w) - 2) + " " + w)
            else:
                linie.append(opis)
                linie.append(" " * (szer - len(w)) + w)
        else:
            linie.append(opis + " " + "." * (szer - len(opis) - len(w) - 2) + " " + w)
    return "\n".join(linie)


class Formularz:
    """Pomocnik: etykieta + pole w siatce; .get(nazwa) zwraca tekst, .liczba(nazwa) float."""

    def __init__(self, parent, kolumny=2):
        M = _M()
        self.K = M.K
        self.ramka = tk.Frame(parent, bg=M.K["karta"])
        self.ramka.pack(fill="x")
        self.pola = {}
        self.kolumny = kolumny
        self.n = 0
        self.M = M

    def pole(self, nazwa, etykieta, wartosc="", szer=14, opcje=None, check=False, podpowiedz=None):
        M = self.M
        r, c = divmod(self.n, self.kolumny)
        self.n += 1
        kom = tk.Frame(self.ramka, bg=M.K["karta"])
        kom.grid(row=r, column=c, sticky="w", padx=(0, 18), pady=3)
        if check:
            var = tk.BooleanVar(value=bool(wartosc))
            tk.Checkbutton(kom, text=etykieta, variable=var, bg=M.K["karta"], fg=M.K["tekst"], selectcolor=M.K["jasny"],
                           activebackground=M.K["karta"], font=M.czc(10)).pack(side="left")
            self.pola[nazwa] = var
            return var
        tk.Label(kom, text=etykieta, font=M.czc(10), bg=M.K["karta"], fg=M.K["tekst"], anchor="w").pack(side="left")
        var = tk.StringVar(value=str(wartosc))
        if opcje is not None:
            w = ttk.Combobox(kom, textvariable=var, values=list(opcje), width=szer, state="readonly" if podpowiedz == "readonly" else "normal")
        else:
            w = tk.Entry(kom, textvariable=var, font=M.czc(10), width=szer, relief="flat", bg=M.K["jasny"], fg=M.K["tekst"], insertbackground=M.K["tekst"])
        w.pack(side="left", padx=(6, 0), ipady=3)
        self.pola[nazwa] = var
        return var

    def nowy_wiersz(self):
        self.n = (self.n + self.kolumny - 1) // self.kolumny * self.kolumny

    def get(self, nazwa):
        v = self.pola[nazwa].get()
        return v if not isinstance(v, bool) else v

    def liczba(self, nazwa, dom=0.0):
        return _liczba(self.pola[nazwa].get(), dom)

    def bool(self, nazwa):
        return bool(self.pola[nazwa].get())


def _wynik(parent, wysokosc=16):
    """Pole wyniku (monospace) z poziomym paskiem przewijania — tabele nie są obcinane."""
    M = _M()
    ramka = tk.Frame(parent, bg=M.K["karta"])
    t = tk.Text(ramka, font=M.czc(9, mono=True), bg=M.K["jasny"], fg=M.K["tekst"], relief="flat", padx=12, pady=10, height=wysokosc, wrap="none")
    xs = ttk.Scrollbar(ramka, orient="horizontal", command=t.xview)
    t.configure(xscrollcommand=xs.set)
    t.pack(fill="both", expand=True)
    xs.pack(fill="x")
    ramka.pack(fill="both", expand=True, pady=(8, 0))
    t.ramka = ramka
    t.pack_forget = ramka.pack_forget          # wywołania txt.pack_forget()/txt.pack() w narzędziach dotyczą całej ramki
    t.pack = lambda **k: ramka.pack(**k)
    return t


def _ustaw(t, tekst):
    t.configure(state="normal")
    t.delete("1.0", "end")
    t.insert("1.0", tekst)


def _status(parent):
    M = _M()
    s = tk.Label(parent, text="", font=M.czc(9), bg=M.K["karta"], fg=M.K["szary"], anchor="w")
    s.pack(fill="x", pady=(4, 0))
    return s


# ============================================================ wejście
def zbuduj(app, parent, narzedzie):
    globals()["BUDUJ_" + narzedzie](app, parent)


def _karta(parent, tytul=None):
    M = _M()
    z, k = M.karta(parent, tytul=tytul)
    z.pack(fill="x", pady=(0, 10))
    return k


# ============================================================ FIRMA
def BUDUJ_firma(app, parent):
    M = _M()
    w = stan(app)
    k = _karta(parent, "Firma ćwiczeniowa — Twoje dane na cały kurs")
    M.etykieta(k, P.firma or "Program nie opisuje firmy.", 10, wrap=820).pack(fill="x")
    k = _karta(parent, f"Pracownicy i współpracownicy ({len(w['osoby'])})")
    t = _wynik(k, 18)
    linie = [f"{'Lp':<3}{'Imię i nazwisko':<22}{'Stanowisko':<26}{'Rodzaj':<11}{'Umowa / od':<22}{'Etat':<6}{'Zasadn.':>9}  {'PESEL':<12}{'Ur.':<11}{'Uwagi'}"]
    for i, o in enumerate(w["osoby"], 1):
        linie.append(f"{i:<3}{o['imie'] + ' ' + o['nazwisko']:<22}{o.get('stanowisko', ''):<26}{o.get('rodzaj', ''):<11}{(o.get('umowa', '') + ' od ' + o.get('od', '')):<22}"
                     f"{o.get('etat', 1):<6}{kadry.fmt(o.get('zasadnicze', 0)):>9}  {o['pesel']:<12}{o.get('ur', ''):<11}{o.get('uwagi', '')}")
    _ustaw(t, "\n".join(linie))
    r = tk.Frame(k, bg=M.K["karta"])
    r.pack(fill="x", pady=(8, 0))
    st = _status(k)

    def zapisz():
        md = [f"# {P.nazwa} — FIRMA.md", "", P.firma, "", "## Pracownicy i współpracownicy", "",
              "| Lp | Imię i nazwisko | Stanowisko | Rodzaj | Umowa | Od | Do | Etat | Zasadnicze | Data ur. | PESEL (fikcyjny) | PPK | KUP | PIT-2 | Uwagi |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for i, o in enumerate(w["osoby"], 1):
            md.append(f"| {i} | {o['imie']} {o['nazwisko']} | {o.get('stanowisko', '')} | {o.get('rodzaj', '')} | {o.get('umowa', '')} | {o.get('od', '')} | {o.get('do', '') or '—'} | "
                      f"{o.get('etat', 1)} | {kadry.fmt(o.get('zasadnicze', 0))} | {o.get('ur', '')} | {o['pesel']} | {'tak' if o.get('ppk') else 'nie'} | {o.get('kup', 250)} | {o.get('pit2', 300)} | {o.get('uwagi', '')} |")
        md += ["", "## Regulaminy (założenia)", ""] + [f"- {x}" for x in P.firma_regulaminy]
        zapisz_do_projektu(app, "", "FIRMA.md", "\n".join(md) + "\n", st)

    M.przycisk(r, "Zapisz FIRMA.md do projektu", zapisz).pack(side="left")
    M.przycisk(r, "Przywróć dane firmy z programu", lambda: (w.update(osoby=[]), stan(app), app.pokaz("warsztat")), "drugi").pack(side="left", padx=8)
    if P.firma_regulaminy:
        k = _karta(parent, "Regulaminy — założenia firmy")
        for x in P.firma_regulaminy:
            M.etykieta(k, "• " + x, 10, wrap=820).pack(fill="x", pady=(0, 2))


# ============================================================ LISTA PŁAC
def BUDUJ_place(app, parent):
    M = _M()
    w = stan(app)
    par = P.parametry or {}
    k = _karta(parent, "Lista płac: brutto → netto → koszt pracodawcy")
    M.etykieta(k, "Wybierz osobę z firmy (pola wypełnią się same) albo wpisz własne dane. „Tryb ćwiczenia”: najpierw wpisz swoje netto, potem sprawdź.", 9, kolor=M.K["szary"], wrap=820).pack(fill="x", pady=(0, 6))
    f = Formularz(k, 2)
    osoby = ["— własne dane —"] + [_osoba_etykieta(o) for o in w["osoby"]]
    f.pole("osoba", "Osoba", osoby[0], 30, opcje=osoby, podpowiedz="readonly")
    rok = par.get("rok", kadry.DOMYSLNE["rok"])
    f.pole("miesiac", "Miesiąc", f"{rok}-{min(dt.date.today().month, 12):02d}", 8)
    f.nowy_wiersz()
    f.pole("zasadnicze", "Zasadnicze", "6000", 10)
    f.pole("zmienne", "Nadgodziny/premie/nocne", "0", 10)
    f.pole("natura", "Świadczenia w naturze", "0", 10)
    f.pole("wyn_chorobowe", "Wynagrodzenie chorobowe", "0", 10)
    f.pole("zasilek", "Zasiłek (płatnik wypłaca)", "0", 10)
    f.pole("potracenia", "Potrącenia", "0", 10)
    f.pole("kup", "KUP", "250", 6, opcje=["0", "250", "300"])
    f.pole("pit2", "PIT-2 (kwota zmn.)", "300", 6, opcje=["0", "300", "150", "100"])
    f.pole("ppk_prac", "PPK pracownik %", str(par.get("ppk_prac", 2.0)), 6)
    f.pole("ppk_pracod", "PPK pracodawca %", str(par.get("ppk_pracod", 1.5)), 6)
    f.pole("dochod", "Dochód narastająco", "0", 10)
    f.pole("er_narast", "Podst. emer.-rent. narast.", "0", 10)
    f.pole("ulga", "ulga dla młodych (do 26 lat)", False, check=True)
    f.pole("fp_zw", "zwolnienie z FP/FGŚP (55+/60+)", False, check=True)
    f.pole("umowna", "Pensja wg umowy (pełny mies., do FP)", "0", 10)

    def wypelnij(*_):
        i = osoby.index(f.get("osoba")) - 1
        if i < 0:
            return
        o = w["osoby"][i]
        f.pola["zasadnicze"].set(str(o.get("zasadnicze", 0)))
        f.pola["umowna"].set(str(o.get("zasadnicze", 0)))
        f.pola["kup"].set(str(o.get("kup", 250)))
        f.pola["pit2"].set(str(o.get("pit2", 300)))
        f.pola["ppk_prac"].set(str(par.get("ppk_prac", 2.0)) if o.get("ppk") else "0")
        f.pola["ppk_pracod"].set(str(par.get("ppk_pracod", 1.5)) if o.get("ppk") else "0")
        f.pola["ulga"].set(bool(o.get("mlody")))
        f.pola["fp_zw"].set(bool(o.get("fp_zwolnienie")))

    f.pola["osoba"].trace_add("write", wypelnij)
    r = tk.Frame(k, bg=M.K["karta"])
    r.pack(fill="x", pady=(8, 0))
    txt = _wynik(k, 20)
    st = _status(k)
    ostatni = {}

    def policz(pokaz=True):
        wyn = kadry.lista_plac(zasadnicze=f.liczba("zasadnicze"), zmienne=f.liczba("zmienne"), natura=f.liczba("natura"), wyn_chorobowe=f.liczba("wyn_chorobowe"),
                               zasilek=f.liczba("zasilek"), kup=f.liczba("kup"), pit2=f.liczba("pit2"), ppk_prac=f.liczba("ppk_prac"), ppk_pracod=f.liczba("ppk_pracod"),
                               ulga_mlodych=f.bool("ulga"), dochod_narast=f.liczba("dochod"), podstawa_er_narast=f.liczba("er_narast"), fp_zwolnienie=f.bool("fp_zw"),
                               potracenia=f.liczba("potracenia"), par=par, pensja_umowna=f.liczba("umowna"))
        ostatni.clear()
        ostatni.update(wyn)
        if pokaz:
            _ustaw(txt, _formatuj_kroki(f"Lista płac — {f.get('osoba')} — {f.get('miesiac')}", wyn["kroki"]) +
                   f"\n\nNETTO: {kadry.fmt(wyn['netto'])} zł   ·   koszt pracodawcy: {kadry.fmt(wyn['koszt'])} zł   ·   dochód narastająco po: {kadry.fmt(wyn['dochod_narast_po'])}")
        return wyn

    def sprawdz():
        moje = _liczba(f.get("moje"))
        wyn = policz(False)
        if abs(moje - wyn["netto"]) < 0.005:
            _ustaw(txt, f"✔ Zgadza się: {kadry.fmt(moje)} zł. Oto pełne kroki:\n\n" + _formatuj_kroki("Lista płac", wyn["kroki"]))
        else:
            kand = []
            for opis, wart in wyn["kroki"]:
                if isinstance(wart, (int, float)) and abs(abs(moje - wyn["netto"]) - abs(wart)) < 0.02:
                    kand.append(opis)
            pod = ("Różnica równa się kwocie: " + "; ".join(kand)) if kand else "Policz jeszcze raz w kolejności: składki osobno → zdrowotna od (brutto − składki) → podstawa PIT zaokrąglona → zaliczka − PIT-2 → PPK."
            _ustaw(txt, f"✘ Twoje netto {kadry.fmt(moje)} ≠ {kadry.fmt(wyn['netto'])} (różnica {kadry.fmt(moje - wyn['netto'])}).\n{pod}\n\nNie pokazuję kroków — popraw i sprawdź ponownie (albo kliknij „Policz”).")

    def dodaj():
        wyn = policz(False)
        i = osoby.index(f.get("osoba")) - 1
        o = w["osoby"][i] if i >= 0 else None
        wiersz = {"miesiac": f.get("miesiac").strip(), "pesel": o["pesel"] if o else "", "osoba": f"{o['imie']} {o['nazwisko']}" if o else "własne dane",
                  "kod": o.get("kod", "0110") if o else "0110",
                  **{kk: wyn[kk] for kk in ("przychod_oskl", "podstawa_er", "emer", "rent", "chor", "podstawa_zdr", "zdrowotna", "ppk_prac", "ppk_pracod", "przychod_pracy",
                                            "zwolnione", "kup", "podstawa_pit", "zaliczka", "zasilek", "wyn_chorobowe", "netto", "emer_p", "rent_p", "wyp", "fp", "fgsp", "koszt")}}
        w["kartoteka"] = [x for x in w["kartoteka"] if not (x["miesiac"] == wiersz["miesiac"] and x["osoba"] == wiersz["osoba"])] + [wiersz]
        app.stan.zapisz()
        st.configure(text=f"✔ dodano do listy płac {wiersz['miesiac']}: {wiersz['osoba']} (wierszy w miesiącu: {sum(1 for x in w['kartoteka'] if x['miesiac'] == wiersz['miesiac'])})", fg=M.K["ziel"])

    def lista():
        m = f.get("miesiac").strip()
        wiersze = [x for x in w["kartoteka"] if x["miesiac"] == m]
        if not wiersze:
            _ustaw(txt, f"Brak wierszy dla miesiąca {m}. Policz pracownika i kliknij „Dodaj do listy miesiąca”.")
            return
        _ustaw(txt, _tabela_listy(m, wiersze))

    def zapisz():
        m = f.get("miesiac").strip()
        wiersze = [x for x in w["kartoteka"] if x["miesiac"] == m]
        if not wiersze:
            st.configure(text="Lista miesiąca jest pusta.", fg=M.K["czerw"])
            return
        zapisz_do_projektu(app, "04-place", f"lista_plac_{m}.md", "```\n" + _tabela_listy(m, wiersze) + "\n```\n", st)
        buf = io.StringIO()
        pola = ["miesiac", "osoba", "przychod_oskl", "emer", "rent", "chor", "zdrowotna", "kup", "ppk_pracod", "podstawa_pit", "zaliczka", "ppk_prac", "wyn_chorobowe", "zasilek", "netto", "emer_p", "rent_p", "wyp", "fp", "fgsp", "koszt"]
        wr = csv.DictWriter(buf, fieldnames=pola, delimiter=";", extrasaction="ignore")
        wr.writeheader()
        for x in wiersze:
            wr.writerow({kk: (str(v).replace(".", ",") if isinstance(v, float) else v) for kk, v in x.items() if kk in pola})
        zapisz_do_projektu(app, "04-place", f"lista_plac_{m}.csv", buf.getvalue(), st)
        st.configure(text=f"✔ zapisano 04-place/lista_plac_{m}.md i .csv", fg=M.K["ziel"])

    def usun():
        m = f.get("miesiac").strip()
        w["kartoteka"] = [x for x in w["kartoteka"] if x["miesiac"] != m]
        app.stan.zapisz()
        st.configure(text=f"Usunięto listę {m}.", fg=M.K["szary"])

    M.przycisk(r, "Policz", policz).pack(side="left")
    tk.Label(r, text="  Tryb ćwiczenia — moje netto:", font=M.czc(10), bg=M.K["karta"], fg=M.K["tekst"]).pack(side="left", padx=(12, 0))
    f.pola["moje"] = tk.StringVar()
    tk.Entry(r, textvariable=f.pola["moje"], font=M.czc(10), width=10, relief="flat", bg=M.K["jasny"], fg=M.K["tekst"], insertbackground=M.K["tekst"]).pack(side="left", padx=6, ipady=3)
    M.przycisk(r, "Sprawdź", sprawdz, "drugi").pack(side="left")
    r2 = tk.Frame(k, bg=M.K["karta"])
    r2.pack(fill="x", pady=(6, 0))
    M.przycisk(r2, "Dodaj do listy miesiąca", dodaj, "drugi").pack(side="left")
    M.przycisk(r2, "Pokaż listę miesiąca", lista, "drugi").pack(side="left", padx=8)
    M.przycisk(r2, "Zapisz listę (MD + CSV)", zapisz, "drugi").pack(side="left")
    r3 = tk.Frame(k, bg=M.K["karta"])
    r3.pack(fill="x", pady=(6, 0))
    M.przycisk(r3, "Wyczyść listę miesiąca", usun, "drugi").pack(side="left")
    txt.pack_forget()
    txt.pack(fill="both", expand=True, pady=(8, 0))
    st.pack_forget()
    st.pack(fill="x", pady=(4, 0))


def _tabela_listy(m, wiersze):
    naglowek = f"{'Osoba':<22}{'Brutto':>10}{'Społ.':>9}{'Zdrow.':>9}{'Zaliczka':>9}{'PPK pr.':>8}{'Chorob.':>9}{'Zasiłek':>9}{'NETTO':>10}{'Koszt':>11}"
    linie = [f"Lista płac {m}", naglowek, "-" * len(naglowek)]
    s = {kk: 0.0 for kk in ("przychod_oskl", "spol", "zdrowotna", "zaliczka", "ppk_prac", "wyn_chorobowe", "zasilek", "netto", "koszt")}
    for x in wiersze:
        spol = x["emer"] + x["rent"] + x["chor"]
        linie.append(f"{x['osoba'][:21]:<22}{kadry.fmt(x['przychod_oskl']):>10}{kadry.fmt(spol):>9}{kadry.fmt(x['zdrowotna']):>9}{kadry.fmt(x['zaliczka']):>9}"
                     f"{kadry.fmt(x['ppk_prac']):>8}{kadry.fmt(x['wyn_chorobowe']):>9}{kadry.fmt(x['zasilek']):>9}{kadry.fmt(x['netto']):>10}{kadry.fmt(x['koszt']):>11}")
        for kk in s:
            s[kk] += spol if kk == "spol" else x[kk]
    linie.append("-" * len(naglowek))
    linie.append(f"{'RAZEM':<22}{kadry.fmt(s['przychod_oskl']):>10}{kadry.fmt(s['spol']):>9}{kadry.fmt(s['zdrowotna']):>9}{kadry.fmt(s['zaliczka']):>9}"
                 f"{kadry.fmt(s['ppk_prac']):>8}{kadry.fmt(s['wyn_chorobowe']):>9}{kadry.fmt(s['zasilek']):>9}{kadry.fmt(s['netto']):>10}{kadry.fmt(s['koszt']):>11}")
    linie.append(f"\nZaliczka PIT do US (do 20. następnego mies.): {kadry.fmt(s['zaliczka'])}   ·   bilans: brutto = netto + obciążenia pracownika")
    return "\n".join(linie)


# ============================================================ ZASIŁKI
def BUDUJ_zasilki(app, parent):
    M = _M()
    par = P.parametry or {}
    k = _karta(parent, "A · Podstawa wymiaru zasiłku z 12 miesięcy")
    M.etykieta(k, "Wpisz 12 miesięcy przed miesiącem niezdolności: składniki STAŁE (kwota umowna), ZMIENNE faktycznie wypłacone, dni obowiązujące i przepracowane "
               "(urlop = przepracowane). Kalkulator wyłączy miesiące < 50% i uzupełni pozostałe.", 9, kolor=M.K["szary"], wrap=820).pack(fill="x", pady=(0, 6))
    g = tk.Frame(k, bg=M.K["karta"])
    g.pack(fill="x")
    for c, h in enumerate(("Miesiąc", "Stałe", "Zmienne", "Dni obow.", "Dni przepr.")):
        tk.Label(g, text=h, font=M.czc(9, "bold"), bg=M.K["karta"], fg=M.K["szary"]).grid(row=0, column=c, padx=4)
    rok = par.get("rok", kadry.DOMYSLNE["rok"])
    wiersze = []
    for i in range(12):
        m = (dt.date.today().month - 12 + i - 1) % 12 + 1
        vals = [tk.StringVar(value=f"{MIESIACE[m - 1]} {rok - 1 if m > dt.date.today().month - 1 else rok}"), tk.StringVar(value="6000"), tk.StringVar(value="0"),
                tk.StringVar(value=str(kadry.wymiar(rok, m)["dni_pracy"])), tk.StringVar(value=str(kadry.wymiar(rok, m)["dni_pracy"]))]
        for c, v in enumerate(vals):
            tk.Entry(g, textvariable=v, font=M.czc(9), width=16 if c == 0 else 9, relief="flat", bg=M.K["jasny"], fg=M.K["tekst"], insertbackground=M.K["tekst"]).grid(row=i + 1, column=c, padx=4, pady=1)
        wiersze.append(vals)
    f = Formularz(k, 3)
    f.pole("etat", "Etat", "1", 5)
    f.pole("dni", "Dni niezdolności", "10", 5)
    f.pole("proc", "% zasiłku", "80", 5, opcje=["80", "100", "70", "75", "90", "81,5"])
    txt = _wynik(k, 14)
    st = _status(k)

    def policz():
        mies = [{"nazwa": v[0].get(), "stale": _liczba(v[1].get()), "zmienne": _liczba(v[2].get()), "dni_obow": int(_liczba(v[3].get())), "dni_przepr": int(_liczba(v[4].get()))} for v in wiersze]
        wyn = kadry.podstawa_zasilku(mies, etat=f.liczba("etat", 1.0), par=par)
        dz_proc = kadry.zl(wyn["dzienna"] * f.liczba("proc") / 100)
        kw = kadry.zl(dz_proc * f.liczba("dni"))
        _ustaw(txt, _formatuj_kroki("Podstawa wymiaru zasiłku", wyn["kroki"]) +
               f"\n\nStawka dzienna × {f.get('proc')}% = {kadry.fmt(dz_proc)} zł (zaokrąglona do grosza) → za {f.get('dni')} dni: {kadry.fmt(kw)} zł")
        return wyn, kw

    r = tk.Frame(k, bg=M.K["karta"])
    r.pack(fill="x", pady=(6, 0))
    M.przycisk(r, "Policz podstawę", policz).pack(side="left")
    M.przycisk(r, "Zapisz do projektu", lambda: zapisz_do_projektu(app, "04-place", "podstawa_zasilku.md", "```\n" + txt.get("1.0", "end") + "```\n", st), "drugi").pack(side="left", padx=8)
    txt.pack_forget(); txt.pack(fill="both", expand=True, pady=(8, 0)); st.pack_forget(); st.pack(fill="x")

    k2 = _karta(parent, "B · Pula 33/14 dni i okres zasiłkowy 182/270")
    M.etykieta(k2, "Dodaj nieobecności z roku (daty RRRR-MM-DD). Rodzaj: choroba / opieka / wypadek_praca / wypadek_droga / ciaza.", 9, kolor=M.K["szary"], wrap=820).pack(fill="x", pady=(0, 6))
    f2 = Formularz(k2, 3)
    f2.pole("od", "Od", f"{rok}-03-10", 11)
    f2.pole("do", "Do", f"{rok}-03-19", 11)
    f2.pole("rodzaj", "Rodzaj", "choroba", 13, opcje=["choroba", "opieka", "wypadek_praca", "wypadek_droga", "ciaza"], podpowiedz="readonly")
    f2.pole("w50", "pracownik 50+ (14 dni)", False, check=True)
    f2.pole("dzienna", "Stawka dzienna (z A)", "0", 9)
    lista = []
    txt2 = _wynik(k2, 10)
    st2 = _status(k2)

    def dodaj_nb():
        od, do = _data(f2.get("od")), _data(f2.get("do"))
        if not od or not do or do < od:
            st2.configure(text="Popraw daty (RRRR-MM-DD, „do” ≥ „od”).", fg=M.K["czerw"])
            return
        lista.append({"od": od, "do": do, "rodzaj": f2.get("rodzaj")})
        rozlicz()

    def rozlicz():
        wyn = kadry.pula_chorobowa(lista, wiek_50_plus=f2.bool("w50"), rok=rok)
        dz = f2.liczba("dzienna")
        linie = [f"Pula wynagrodzenia chorobowego: {wyn['limit']} dni, wykorzystano {wyn['uzyte']}", ""]
        for x in wyn["pozycje"]:
            dzp = kadry.zl(dz * x['proc'] / 100)
            kw = f"   kwota ({kadry.fmt(dzp)}/dzień): chorobowe {kadry.fmt(kadry.zl(dzp * x['chorobowe']))} + zasiłek {kadry.fmt(kadry.zl(dzp * x['zasilek']))}" if dz else ""
            linie.append(f"{x['od']} – {x['do']}  {x['rodzaj']:<14}{x['dni']:>3} dni  {x['proc']}%  → {x['uwaga']}{kw}")
        _ustaw(txt2, "\n".join(linie) if lista else "Brak nieobecności.")

    r = tk.Frame(k2, bg=M.K["karta"])
    r.pack(fill="x", pady=(6, 0))
    M.przycisk(r, "Dodaj nieobecność", dodaj_nb).pack(side="left")
    M.przycisk(r, "Wyczyść", lambda: (lista.clear(), rozlicz()), "drugi").pack(side="left", padx=8)
    M.przycisk(r, "Zapisz do projektu", lambda: zapisz_do_projektu(app, "04-place", "pula_chorobowa.md", "```\n" + txt2.get("1.0", "end") + "```\n", st2), "drugi").pack(side="left")
    txt2.pack_forget(); txt2.pack(fill="both", expand=True, pady=(8, 0)); st2.pack_forget(); st2.pack(fill="x")


# ============================================================ URLOPY
def BUDUJ_urlopy(app, parent):
    M = _M()
    par = P.parametry or {}
    rok = par.get("rok", kadry.DOMYSLNE["rok"])
    k = _karta(parent, "Wymiar urlopu (art. 153–155¹ KP)")
    f = Formularz(k, 2)
    f.pole("staz", "Staż pracy (lata)", "4", 5)
    f.pole("etat", "Etat", "1", 5)
    f.pole("mies", "Miesięcy w roku", "12", 5)
    f.pole("pierwsza", "pierwsza praca w życiu", False, check=True)
    txt = _wynik(k, 6)
    M.przycisk(k, "Policz wymiar", lambda: _ustaw(txt, _formatuj_kroki("Wymiar urlopu", kadry.wymiar_urlopu(f.liczba("staz"), f.liczba("etat", 1), f.bool("pierwsza"), int(f.liczba("mies", 12)))["kroki"]) +
                                                 f"\n\nUrlop: {kadry.wymiar_urlopu(f.liczba('staz'), f.liczba('etat', 1), f.bool('pierwsza'), int(f.liczba('mies', 12)))['dni']} dni = "
                                                 f"{kadry.wymiar_urlopu(f.liczba('staz'), f.liczba('etat', 1), f.bool('pierwsza'), int(f.liczba('mies', 12)))['godziny']} h (w tym 4 dni na żądanie)")).pack(anchor="w", pady=(6, 0))
    txt.pack_forget(); txt.pack(fill="both", expand=True, pady=(8, 0))

    k = _karta(parent, f"Ekwiwalent za urlop (współczynnik {kadry.wspolczynnik_ekwiwalentu(rok)} w {rok})")
    f2 = Formularz(k, 3)
    f2.pole("stale", "Stałe (mies.)", "6000", 9)
    f2.pole("zm3", "Zmienne — suma 3 mies.", "0", 9)
    f2.pole("r12", "Roczne — suma 12 mies.", "0", 9)
    f2.pole("godz", "Godziny urlopu", "56", 6)
    f2.pole("etat", "Etat", "1", 5)
    f2.pole("norma", "Norma dobowa", "8", 4, opcje=["8", "7"])
    f2.pole("rok", "Rok", str(rok), 6)
    txt2 = _wynik(k, 7)
    M.przycisk(k, "Policz ekwiwalent", lambda: _ustaw(txt2, _formatuj_kroki("Ekwiwalent", kadry.ekwiwalent(f2.liczba("stale"), f2.liczba("zm3"), f2.liczba("r12"), f2.liczba("godz"), int(f2.liczba("rok", rok)), f2.liczba("etat", 1), int(f2.liczba("norma", 8)))["kroki"]))).pack(anchor="w", pady=(6, 0))
    txt2.pack_forget(); txt2.pack(fill="both", expand=True, pady=(8, 0))

    k = _karta(parent, "Urlopowe ze zmiennych i pomniejszenie za nieobecności")
    f3 = Formularz(k, 3)
    f3.pole("zm3", "Zmienne z 3 mies.", "1200", 9)
    f3.pole("g3", "Godziny przepr. 3 mies.", "500", 6)
    f3.pole("gu", "Godziny urlopu", "40", 6)
    f3.pole("pensja", "Pensja stała", "6000", 9)
    f3.pole("dch", "Dni choroby", "0", 5)
    f3.pole("ginne", "Godz. innych nieobecności", "0", 5)
    f3.pole("wym", "Wymiar miesiąca (h)", str(kadry.wymiar(rok, dt.date.today().month)["godziny"]), 5)
    txt3 = _wynik(k, 8)

    def policz3():
        a = kadry.wynagrodzenie_urlopowe(f3.liczba("zm3"), f3.liczba("g3"), f3.liczba("gu"))
        b = kadry.pomniejszenie(f3.liczba("pensja"), int(f3.liczba("dch")), f3.liczba("ginne"), int(f3.liczba("wym", 160)))
        _ustaw(txt3, _formatuj_kroki("Wynagrodzenie urlopowe (część zmienna)", a["kroki"]) + "\n\n" + _formatuj_kroki("Pomniejszenie pensji stałej", b["kroki"]))

    M.przycisk(k, "Policz", policz3).pack(anchor="w", pady=(6, 0))
    txt3.pack_forget(); txt3.pack(fill="both", expand=True, pady=(8, 0))


# ============================================================ CZAS PRACY
def BUDUJ_czas(app, parent):
    M = _M()
    par = P.parametry or {}
    rok = par.get("rok", kadry.DOMYSLNE["rok"])
    k = _karta(parent, "Wymiar czasu pracy (art. 130 KP) i dodatek nocny")
    f = Formularz(k, 3)
    f.pole("rok", "Rok", str(rok), 6)
    f.pole("mies", "Miesiąc", str(dt.date.today().month), 4)
    f.pole("nocne", "Godziny nocne", "0", 5)
    txt = _wynik(k, 16)

    def policz():
        r, m = int(f.liczba("rok", rok)), int(f.liczba("mies", 1))
        w = kadry.wymiar(r, m)
        linie = [_formatuj_kroki(f"Wymiar {MIESIACE[m - 1]} {r}", w["kroki"]), f"dni pracy: {w['dni_pracy']}; święta obniżające wymiar: {', '.join(str(d) for d in w['swieta_obnizajace']) or 'brak'}"
                 + (f"; święto w sobotę ({', '.join(str(d) for d in w['soboty_swiateczne'])}) → wyznacz inny dzień wolny" if w["soboty_swiateczne"] else ""), ""]
        if f.liczba("nocne"):
            n = kadry.dodatek_nocny(r, m, f.liczba("nocne"), par)
            linie += [_formatuj_kroki("Dodatek nocny", n["kroki"]), ""]
        linie.append(f"{'Miesiąc':<14}{'Wymiar':>7}{'Dni':>5}   {'Miesiąc':<14}{'Wymiar':>7}{'Dni':>5}")
        for i in range(6):
            a, b = kadry.wymiar(r, i + 1), kadry.wymiar(r, i + 7)
            linie.append(f"{MIESIACE[i]:<14}{a['godziny']:>5} h{a['dni_pracy']:>5}   {MIESIACE[i + 6]:<14}{b['godziny']:>5} h{b['dni_pracy']:>5}")
        linie.append(f"Rok {r}: {kadry.wymiar_roczny(r)} h, {kadry.wymiar_roczny(r) // 8} dni roboczych → współczynnik ekwiwalentu {kadry.wspolczynnik_ekwiwalentu(r)}")
        _ustaw(txt, "\n".join(linie))

    M.przycisk(k, "Policz", policz).pack(anchor="w", pady=(6, 0))
    txt.pack_forget(); txt.pack(fill="both", expand=True, pady=(8, 0))

    k = _karta(parent, "Nadgodziny (art. 151¹ KP)")
    f2 = Formularz(k, 2)
    f2.pole("zas", "Zasadnicze + stałe dodatki", "6000", 9)
    f2.pole("wym", "Wymiar miesiąca (h)", "168", 5)
    f2.pole("h50", "Nadgodziny 50% (dobowe, dzień roboczy)", "0", 5)
    f2.pole("h100", "Nadgodziny 100% (noc, nd/święto, średniotyg.)", "0", 5)
    txt2 = _wynik(k, 7)
    M.przycisk(k, "Policz", lambda: _ustaw(txt2, _formatuj_kroki("Nadgodziny", kadry.nadgodziny(f2.liczba("zas"), f2.liczba("wym", 160), f2.liczba("h50"), f2.liczba("h100"))["kroki"]))).pack(anchor="w", pady=(6, 0))
    txt2.pack_forget(); txt2.pack(fill="both", expand=True, pady=(8, 0))

    k = _karta(parent, "Okres wypowiedzenia i data rozwiązania")
    f3 = Formularz(k, 2)
    f3.pole("rodzaj", "Rodzaj umowy", "nieokreslona", 13, opcje=["nieokreslona", "okreslona", "probna"], podpowiedz="readonly")
    f3.pole("staz", "Staż u pracodawcy (mies.)", "40", 5)
    f3.pole("probna", "Długość próbnej (dni)", "90", 5)
    f3.pole("data", "Data doręczenia", str(dt.date.today()), 11)
    txt3 = _wynik(k, 4)

    def policz3():
        okres, opis = kadry.okres_wypowiedzenia(int(f3.liczba("staz")), f3.get("rodzaj"), int(f3.liczba("probna")))
        d = _data(f3.get("data"))
        if not d:
            _ustaw(txt3, "Podaj datę RRRR-MM-DD.")
            return
        _ustaw(txt3, f"Okres: {opis}\nDoręczono {d} ({['pn', 'wt', 'śr', 'cz', 'pt', 'sb', 'nd'][d.weekday()]}) → umowa rozwiąże się {kadry.koniec_wypowiedzenia(d, okres)}\n"
                     "Tygodniowy kończy się w sobotę, miesięczny — ostatniego dnia miesiąca, dni robocze — bez sobót, niedziel i świąt.")

    M.przycisk(k, "Policz", policz3).pack(anchor="w", pady=(6, 0))
    txt3.pack_forget(); txt3.pack(fill="both", expand=True, pady=(8, 0))


# ============================================================ POTRĄCENIA
def BUDUJ_potracenia(app, parent):
    M = _M()
    par = P.parametry or {}
    k = _karta(parent, "Potrącenia z wynagrodzenia — granice i kwoty wolne")
    f = Formularz(k, 2)
    f.pole("netto", "Netto pracownika", "4300", 9)
    f.pole("rodzaj", "Rodzaj", "inne", 18, opcje=["alimenty", "inne", "zaliczka", "kara", "zgoda_inne", "zgoda_pracodawca"], podpowiedz="readonly")
    f.pole("zaj", "Kwota zajęcia (0 = bez limitu)", "0", 9)
    f.pole("kup", "KUP pracownika", "250", 5, opcje=["0", "250", "300"])
    f.pole("pit2", "PIT-2", "300", 5, opcje=["0", "300", "150", "100"])
    f.pole("ppk", "PPK pracownika %", "0", 5)
    f.pole("etat", "Etat", "1", 5)
    txt = _wynik(k, 9)
    st = _status(k)

    def policz():
        zaj = f.liczba("zaj") or None
        w = kadry.potracenia(f.liczba("netto"), f.get("rodzaj"), zaj, f.liczba("kup"), f.liczba("pit2"), f.liczba("ppk"), f.liczba("etat", 1), par)
        _ustaw(txt, _formatuj_kroki("Potrącenie", w["kroki"]) + f"\n\nPotrącasz: {kadry.fmt(w['max'])} zł · pracownik otrzymuje: {kadry.fmt(w['zostaje'])} zł")

    r = tk.Frame(k, bg=M.K["karta"])
    r.pack(fill="x", pady=(6, 0))
    M.przycisk(r, "Policz", policz).pack(side="left")
    M.przycisk(r, "Zapisz do projektu", lambda: zapisz_do_projektu(app, "04-place", "potracenie.md", "```\n" + txt.get("1.0", "end") + "```\n", st), "drugi").pack(side="left", padx=8)
    txt.pack_forget(); txt.pack(fill="both", expand=True, pady=(8, 0)); st.pack_forget(); st.pack(fill="x")


# ============================================================ DELEGACJE I DIETY
def _dt_z_pol(d, g):
    """Data (RRRR-MM-DD / DD.MM.RRRR) + godzina (HH:MM) → datetime albo None."""
    data = _data(d)
    if not data:
        return None
    try:
        h, m = (g or "0:00").strip().split(":")
        return dt.datetime(data.year, data.month, data.day, int(h), int(m))
    except ValueError:
        return None


def BUDUJ_delegacje(app, parent):
    M = _M()
    par = P.parametry or {}
    D = kadry.DELEGACJE
    k = _karta(parent, f"Podróż krajowa — dieta {kadry.fmt(D['dieta_krajowa'])} zł (rozporządzenie z 29.01.2013)")
    M.etykieta(k, "Podaj wyjazd i powrót z godzinami — kalkulator liczy doby jak rozporządzenie (do 8 h / 8–12 h / ponad 12 h), pomniejsza diety za "
                  "zapewnione posiłki (25/50/25% pełnej diety), dolicza ryczałty i kilometrówkę. Projekt diety 60 zł (od 1.01.2027) to nadal projekt — nie licz nim.", 9, wrap=820).pack(fill="x", pady=(0, 6))
    f = Formularz(k, 2)
    f.pole("d1", "Wyjazd (data)", "2026-11-16", 11)
    f.pole("g1", "godz.", "06:00", 6)
    f.pole("d2", "Powrót (data)", "2026-11-17", 11)
    f.pole("g2", "godz.", "18:30", 6)
    f.pole("sn", "Śniadania zapewnione", "0", 4)
    f.pole("ob", "Obiady", "0", 4)
    f.pole("ko", "Kolacje", "0", 4)
    f.pole("nr", "Noclegi bez rachunku", "0", 4)
    f.pole("nk", "Noclegi z rachunku (zł)", "0", 8)
    f.pole("nn", "— liczba", "0", 4)
    f.pole("doj", "Doby z ryczałtem na dojazdy", "", 4)
    f.pole("km", "Km autem prywatnym", "0", 6)
    f.pole("poj", "Pojazd", "osobowy powyżej 900 cm³", 22, opcje=list(D["km"]), podpowiedz="readonly")
    f.pole("bil", "Bilety (zł)", "0", 8)
    f.pole("inne", "Inne wydatki (zł)", "0", 8)
    f.pole("zal", "Zaliczka (zł)", "0", 8)
    f.pole("dfirm", "Dieta wg regulaminu (gdy wyższa)", "", 6)
    M.etykieta(k, "Doby z ryczałtem na dojazdy: puste = wszystkie rozpoczęte doby, 0 = brak (auto prywatne lub służbowe). Noclegi bez rachunku = ryczałt 150% diety.", 9, kolor=M.K["szary"], wrap=820).pack(fill="x", pady=(4, 0))
    txt = _wynik(k, 20)
    st = _status(k)
    ostatni = {}

    def policz():
        a, b = _dt_z_pol(f.get("d1"), f.get("g1")), _dt_z_pol(f.get("d2"), f.get("g2"))
        if not a or not b:
            _ustaw(txt, "Podaj daty RRRR-MM-DD i godziny HH:MM.")
            return
        doj = f.get("doj").strip()
        w = kadry.delegacja_krajowa(a, b, int(f.liczba("sn")), int(f.liczba("ob")), int(f.liczba("ko")), int(f.liczba("nr")), f.liczba("nk"), int(f.liczba("nn")),
                                    int(_liczba(doj)) if doj != "" else None, f.liczba("km"), f.get("poj"), f.liczba("bil"), f.liczba("inne"), f.liczba("zal"),
                                    f.liczba("dfirm") or None, par)
        linie = [_formatuj_kroki("Rozliczenie krajowej podróży służbowej", w["kroki"], 76, zawijaj=True)]
        if w["ostrzezenia"]:
            linie += ["", "UWAGA: " + "; ".join(w["ostrzezenia"])]
        linie += ["", f"Zwolnione z PIT i składek do limitów z rozporządzenia (art. 21 ust. 1 pkt 16 lit. a PIT; § 2 ust. 1 pkt 15 rozp. składkowego)"
                      + (f"; NADWYŻKA {kadry.fmt(w['nadwyzka'])} zł → lista płac" if w["nadwyzka"] else "")]
        ostatni["tekst"] = "\n".join(linie)
        _ustaw(txt, ostatni["tekst"])

    r = tk.Frame(k, bg=M.K["karta"])
    r.pack(fill="x", pady=(6, 0))
    M.przycisk(r, "Policz", policz).pack(side="left")
    M.przycisk(r, "Zapisz do projektu", lambda: zapisz_do_projektu(app, "04-place", "delegacja_krajowa.md", "```\n" + ostatni.get("tekst", txt.get("1.0", "end")) + "\n```\n", st), "drugi").pack(side="left", padx=8)
    txt.pack_forget(); txt.pack(fill="both", expand=True, pady=(8, 0)); st.pack_forget(); st.pack(fill="x")

    k = _karta(parent, "Podróż zagraniczna — dieta i limit noclegu wg załącznika (§ 13–21)")
    M.etykieta(k, "Czas za granicą liczysz od przekroczenia granicy (lądowa: w drodze za granicę; lot: od startu z ostatniego lotniska w kraju). "
                  "Niepełna doba: do 8 h = 1/3, ponad 8 do 12 h = 1/2, ponad 12 h = cała dieta. Część krajowa (do granicy / z lotniska) — jak podróż krajowa.", 9, wrap=820).pack(fill="x", pady=(0, 6))
    f2 = Formularz(k, 2)
    f2.pole("kraj", "Kraj", "Niemcy", 16, opcje=list(D["zagraniczne"]), podpowiedz="readonly")
    f2.pole("h", "Godziny za granicą", "30", 6)
    f2.pole("hk", "Godziny części krajowej", "0", 6)
    f2.pole("kurs", "Kurs NBP z dnia zaliczki", "4,30", 7)
    f2.pole("sn", "Śniadania", "0", 4)
    f2.pole("ob", "Obiady", "0", 4)
    f2.pole("ko", "Kolacje", "0", 4)
    f2.pole("pw", "całodzienne wyżywienie", False, check=True)
    f2.pole("nr", "Noclegi bez rachunku", "0", 4)
    f2.pole("nk", "Noclegi z rachunku (waluta)", "0", 8)
    f2.pole("nn", "— liczba", "0", 4)
    f2.pole("dw", "Dojazdy dworzec/lotnisko (0–2)", "2", 4, opcje=["0", "1", "2"], podpowiedz="readonly")
    f2.pole("dk", "Doby z ryczałtem na komunikację", "", 4)
    f2.pole("zal", "Zaliczka (waluta)", "0", 8)
    M.etykieta(k, "Dojazdy dworzec/lotnisko: 2 = w obie strony (1 dieta), 1 = w jedną (50% diety), 0 = brak. Doby z ryczałtem na komunikację: puste = wszystkie rozpoczęte. Noclegi bez rachunku = ryczałt 25% limitu.", 9, kolor=M.K["szary"], wrap=820).pack(fill="x", pady=(4, 0))
    txt2 = _wynik(k, 20)
    st2 = _status(k)
    ostatni2 = {}

    def policz2():
        dk = f2.get("dk").strip()
        w = kadry.delegacja_zagraniczna(f2.get("kraj"), f2.liczba("h"), int(f2.liczba("sn")), int(f2.liczba("ob")), int(f2.liczba("ko")), f2.bool("pw"), int(f2.liczba("nr")),
                                        f2.liczba("nk"), int(f2.liczba("nn")), int(f2.liczba("dw", 2)), int(_liczba(dk)) if dk != "" else None, f2.liczba("kurs", 1.0),
                                        f2.liczba("zal"), f2.liczba("hk"), par)
        linie = [_formatuj_kroki(f"Rozliczenie zagranicznej podróży służbowej — {f2.get('kraj')} ({w['waluta']})", w["kroki"], 76, zawijaj=True)]
        if w["ostrzezenia"]:
            linie += ["", "UWAGA: " + "; ".join(w["ostrzezenia"])]
        linie += ["", "Zwolnione z PIT i składek do limitów z rozporządzenia; kwota w PLN po średnim kursie NBP z dnia wypłaty zaliczki (§ 20 ust. 3)."]
        ostatni2["tekst"] = "\n".join(linie)
        _ustaw(txt2, ostatni2["tekst"])

    r2 = tk.Frame(k, bg=M.K["karta"])
    r2.pack(fill="x", pady=(6, 0))
    M.przycisk(r2, "Policz", policz2).pack(side="left")
    M.przycisk(r2, "Zapisz do projektu", lambda: zapisz_do_projektu(app, "04-place", "delegacja_zagraniczna.md", "```\n" + ostatni2.get("tekst", txt2.get("1.0", "end")) + "\n```\n", st2), "drugi").pack(side="left", padx=8)
    txt2.pack_forget(); txt2.pack(fill="both", expand=True, pady=(8, 0)); st2.pack_forget(); st2.pack(fill="x")

    k = _karta(parent, "Stawki i limity — stan prawny XI 2026")
    tab = [f"{'Krajowa':<38}{'kwota':>10}   podstawa", f"{'dieta za dobę':<38}{kadry.fmt(D['dieta_krajowa']):>10}   § 7 ust. 1 (od 1.01.2023); projekt 60 zł od 1.01.2027 — NIE obowiązuje",
           f"{'ryczałt za nocleg (150% diety)':<38}{kadry.fmt(1.5 * D['dieta_krajowa']):>10}   § 8 ust. 3", f"{'limit noclegu z rachunku (20 diet)':<38}{kadry.fmt(20 * D['dieta_krajowa']):>10}   § 8 ust. 1",
           f"{'ryczałt na dojazdy (20% diety / doba)':<38}{kadry.fmt(0.2 * D['dieta_krajowa']):>10}   § 9", ""]
    tab += [f"{'Kilometrówka (max, od 17.01.2023)':<38}{'zł/km':>10}   rozp. MI z 25.03.2002, Dz.U. 2023 poz. 5"] + [f"{n:<38}{s:>10.2f}" for n, s in D["km"].items()] + [""]
    tab += [f"{'Zagraniczna':<20}{'waluta':<8}{'dieta':>8}{'limit noclegu':>15}"] + [f"{kr:<20}{w:<8}{d:>8g}{l:>15g}" for kr, (w, d, l) in D["zagraniczne"].items()]
    tab += ["", "Zagraniczna: nocleg ryczałt 25% limitu; dojazd z/do dworca 1 dieta (50% w jedną stronę); komunikacja miejscowa 10% diety/doba; posiłki −15/−30/−30%; całodzienne wyżywienie → 25% diety.",
            "Pełny załącznik (wszystkie państwa): Warsztat → Przepisy → „podróże służbowe”."]
    t3 = _wynik(k, 24)
    _ustaw(t3, "\n".join(tab))
    t3.configure(state="disabled")


# ============================================================ eZUS / PŁATNIK
def BUDUJ_zus(app, parent):
    M = _M()
    w = stan(app)
    par = P.parametry or {}
    rok = par.get("rok", kadry.DOMYSLNE["rok"])
    nb = ttk.Notebook(parent)
    nb.pack(fill="both", expand=True)
    strony = {}
    for nazwa in ("Ubezpieczeni", "Dokument zgłoszeniowy", "Rozliczenie DRA/RCA/RSA", "e-ZLA", "Rejestr wysłanych"):
        fr = tk.Frame(nb, bg=M.K["tlo"])
        nb.add(fr, text=nazwa)
        strony[nazwa] = fr

    # --- Ubezpieczeni
    k = _karta(strony["Ubezpieczeni"], "Rejestr ubezpieczonych płatnika (jak w eZUS)")
    t = _wynik(k, 16)

    def odswiez_ub():
        linie = [f"{'Osoba':<24}{'PESEL':<13}{'Rodzaj':<11}{'Kod':<8}{'Status zgłoszenia':<38}{'Dokumenty'}"]
        for o in w["osoby"]:
            zg = [d for d in o.get("dokumenty", []) if d.get("status") == "przyjęty"]
            zua = [d for d in zg if d["typ"] in ("ZUA", "ZZA")]
            zwua = [d for d in zg if d["typ"] == "ZWUA"]
            if o.get("student"):
                status = "nie podlega (student do 26 lat)"
            elif o.get("rodzaj") == "dzieło":
                status = "nie podlega (dzieło) — RUD"
            elif len(zua) > len(zwua):
                status = f"zgłoszony od {zua[-1]['data']} ({zua[-1]['typ']})"
            elif zwua:
                status = f"wyrejestrowany {zwua[-1]['data']}"
            else:
                status = "NIEZGŁOSZONY"
            linie.append(f"{o['imie'] + ' ' + o['nazwisko']:<24}{o['pesel']:<13}{o.get('rodzaj', ''):<11}{o.get('kod', ''):<8}{status:<38}{', '.join(d['typ'] + ('✔' if d.get('status') == 'przyjęty' else '✘') for d in o.get('dokumenty', []))}")
        _ustaw(t, "\n".join(linie))

    odswiez_ub()
    M.etykieta(k, "Statusy wynikają wyłącznie z dokumentów, które wysłałeś w zakładce „Dokument zgłoszeniowy” — jak w prawdziwym ZUS.", 9, kolor=M.K["szary"]).pack(fill="x", pady=(6, 0))
    rr = tk.Frame(k, bg=M.K["karta"])
    rr.pack(fill="x", pady=(6, 0))
    M.przycisk(rr, "Odśwież", odswiez_ub, "drugi").pack(side="left")

    def reset():
        for o in w["osoby"]:
            o["dokumenty"] = []
        w["wyslane"] = []
        w["komplety"] = []
        app.stan.zapisz()
        odswiez_ub()

    M.przycisk(rr, "Wyczyść wszystkie zgłoszenia (zacznij od nowa)", reset, "drugi").pack(side="left", padx=8)

    # --- Dokument zgłoszeniowy
    k = _karta(strony["Dokument zgłoszeniowy"], "Dokument zgłoszeniowy: wypełnij → weryfikuj → wyślij")
    f = Formularz(k, 2)
    osoby = [_osoba_etykieta(o) for o in w["osoby"]]
    f.pole("osoba", "Osoba", osoby[0], 34, opcje=osoby, podpowiedz="readonly")
    f.pole("typ", "Typ", "ZUA", 7, opcje=["ZUA", "ZZA", "ZWUA", "ZCNA", "ZIUA"], podpowiedz="readonly")
    f.pole("kod", "Kod tytułu (np. 011000)", "011000", 9)
    f.pole("data", "Data powstania/ustania", f"{rok}-01-01", 11)
    f.pole("chorobowe", "dobrowolne chorobowe (zlecenie)", False, check=True)
    f.pole("kod_wyrej", "ZWUA: kod przyczyny", "100", 6, opcje=list(kadry.KODY_WYREJ))
    f.pole("tryb", "ZWUA: tryb rozwiązania", "", 3, opcje=[""] + list(kadry.TRYBY_ROZW))
    f.pole("czlonek_pesel", "ZCNA: PESEL członka", "", 12)
    f.pole("stopien", "ZCNA: pokrewieństwo", "11", 4, opcje=["01", "11", "21", "30", "31", "32"])
    f.pole("czlonek", "ZCNA: imię i nazwisko", "", 20)
    M.etykieta(k, "Kody tytułu: " + " · ".join(f"{kk[:2]} {kk[2:]} {v}" for kk, v in kadry.KODY_TYTULU.items()) + "\n5. znak: 0 brak / 1 emerytura / 2 renta; 6. znak: niepełnosprawność 0–3. "
               "Kody przyczyny ZWUA: 100 ustanie tytułu, 500 zgon, 600 inna. Tryby rozwiązania: " + " · ".join(f"{kk} {v}" for kk, v in kadry.TRYBY_ROZW.items()), 9, kolor=M.K["szary"], wrap=820).pack(fill="x", pady=(6, 0))
    txt = _wynik(k, 9)
    st = _status(k)
    ostatnia = {}

    def dok_z_form():
        return {"typ": f.get("typ"), "kod": f.get("kod").strip(), "data": _data(f.get("data")), "chorobowe": f.bool("chorobowe"), "kod_wyrej": f.get("kod_wyrej"),
                "tryb": f.get("tryb"), "czlonek_pesel": f.get("czlonek_pesel").strip(), "stopien": f.get("stopien"), "czlonek": f.get("czlonek").strip()}

    def weryfikuj():
        o = w["osoby"][osoby.index(f.get("osoba"))]
        dok = dok_z_form()
        osoba = dict(o, data_zatrudnienia=_data(o.get("od")), data_ustania=_data(o.get("do")))
        bledy, ostrz = kadry.sprawdz_zgloszenie(dok, osoba, w["osoby"], dzis=dt.date(rok, 12, 31) if dt.date.today().year > rok else None)
        ostatnia.clear()
        ostatnia.update(dok=dok, osoba=o, bledy=bledy)
        linie = [f"Weryfikacja {dok['typ']} — {o['imie']} {o['nazwisko']}:"]
        linie += [f"  ✘ BŁĄD KRYTYCZNY: {b}" for b in bledy]
        linie += [f"  ⚠ ostrzeżenie: {x}" for x in ostrz]
        if not bledy and not ostrz:
            linie.append("  ✔ dokument poprawny — możesz wysłać")
        elif not bledy:
            linie.append("  ✔ brak błędów krytycznych — ostrzeżenia przeczytaj, wysyłka możliwa")
        _ustaw(txt, "\n".join(linie))
        return not bledy

    def wyslij():
        if not ostatnia or ostatnia.get("dok") != dok_z_form():
            if not weryfikuj():
                st.configure(text="Dokument ma błędy krytyczne — ZUS go odrzuci. Popraw i zweryfikuj.", fg=M.K["czerw"])
                return
        elif ostatnia["bledy"]:
            st.configure(text="Dokument ma błędy krytyczne — ZUS go odrzuci. Popraw i zweryfikuj.", fg=M.K["czerw"])
            return
        o = ostatnia["osoba"]
        dok = ostatnia["dok"]
        upp = f"UPP-{rok}{random.randint(100000, 999999)}"
        wpis = {"typ": dok["typ"], "kod": dok["kod"], "data": str(dok["data"]), "status": "przyjęty", "upp": upp, "wyslano": str(dt.date.today()),
                "kod_wyrej": dok["kod_wyrej"] if dok["typ"] == "ZWUA" else "", "tryb": dok["tryb"] if dok["typ"] == "ZWUA" else "", "czlonek": dok.get("czlonek", "") if dok["typ"] == "ZCNA" else ""}
        o.setdefault("dokumenty", []).append(wpis)
        w["wyslane"].append({"osoba": f"{o['imie']} {o['nazwisko']}", **wpis})
        app.stan.zapisz()
        st.configure(text=f"✔ wysłano {dok['typ']} dla {o['imie']} {o['nazwisko']} — Urzędowe Poświadczenie Przedłożenia {upp}", fg=M.K["ziel"])
        ostatnia.clear()
        odswiez_ub()

    r = tk.Frame(k, bg=M.K["karta"])
    r.pack(fill="x", pady=(6, 0))
    M.przycisk(r, "Weryfikuj (jak Płatnik)", weryfikuj).pack(side="left")
    M.przycisk(r, "Wyślij do ZUS (symulacja)", wyslij, "drugi").pack(side="left", padx=8)
    txt.pack_forget(); txt.pack(fill="both", expand=True, pady=(8, 0)); st.pack_forget(); st.pack(fill="x")

    # --- Rozliczenie
    k = _karta(strony["Rozliczenie DRA/RCA/RSA"], "Komplet DRA / RCA / RSA za miesiąc")
    f2 = Formularz(k, 2)
    f2.pole("miesiac", "Miesiąc (RRRR-MM)", f"{rok}-{dt.date.today().month:02d}", 8)
    f2.pole("ident", "Identyfikator", "01", 4, opcje=["01", "02", "03", "04"])
    M.etykieta(k, "RCA powstaje z wierszy listy płac tego miesiąca (narzędzie „Lista płac” → „Dodaj do listy miesiąca”). RSA dodajesz tutaj lub pobierasz z e-ZLA.", 9, kolor=M.K["szary"], wrap=820).pack(fill="x", pady=(4, 6))
    f3 = Formularz(k, 3)
    f3.pole("osoba", "RSA: osoba", osoby[0], 30, opcje=osoby, podpowiedz="readonly")
    f3.pole("kod", "kod przerwy", "313", 5, opcje=list(kadry.KODY_PRZERW))
    f3.pole("od", "od", f"{rok}-{dt.date.today().month:02d}-01", 11)
    f3.pole("do", "do", f"{rok}-{dt.date.today().month:02d}-05", 11)
    f3.pole("kwota", "kwota (zasiłek)", "0", 8)
    M.etykieta(k, "Kody przerw: " + " · ".join(f"{kk} {v}" for kk, v in kadry.KODY_PRZERW.items()), 9, kolor=M.K["szary"], wrap=820).pack(fill="x", pady=(2, 0))
    txt2 = _wynik(k, 16)
    st2 = _status(k)

    def rsa_miesiaca():
        m = f2.get("miesiac").strip()
        return [x for x in w["rsa"] if x.get("od", "").startswith(m)]

    def rca_miesiaca():
        m = f2.get("miesiac").strip()
        return [x for x in w["kartoteka"] if x["miesiac"] == m and x.get("pesel")]

    def dodaj_rsa():
        o = w["osoby"][osoby.index(f3.get("osoba"))]
        od, do = _data(f3.get("od")), _data(f3.get("do"))
        if not od or not do:
            st2.configure(text="Popraw daty RSA.", fg=M.K["czerw"])
            return
        w["rsa"].append({"pesel": o["pesel"], "osoba": f"{o['imie']} {o['nazwisko']}", "kod_przerwy": f3.get("kod"), "od": str(od), "do": str(do), "kwota": f3.liczba("kwota")})
        app.stan.zapisz()
        pokaz_komplet()

    def rca_wiersze():
        out = []
        for x in rca_miesiaca():
            out.append({"pesel": x["pesel"], "osoba": x["osoba"], "kod": x.get("kod", "0110"), "podstawa_er": x["podstawa_er"], "podstawa_ch": x["przychod_oskl"], "podstawa_zdr": x["podstawa_zdr"],
                        "emer": x["emer"], "rent": x["rent"], "chor": x["chor"], "wyp": x["wyp"], "zdr": x["zdrowotna"], "emer_p": x["emer_p"], "rent_p": x["rent_p"], "fp": x["fp"], "fgsp": x["fgsp"]})
        return out

    def rsa_wiersze():
        return [dict(x, od=_data(x["od"]), do=_data(x["do"])) for x in rsa_miesiaca()]

    def pokaz_komplet(wynik_weryfikacji=None):
        m = f2.get("miesiac").strip()
        rca, rsa = rca_wiersze(), rsa_wiersze()
        s = kadry.dra_sumy(rca, rsa, par)
        linie = [f"KOMPLET {f2.get('ident')} {m[5:7]} {m[:4]} — płatnik AGRO-MLEKO sp. z o.o. (termin: 15. dnia następnego miesiąca)", "",
                 "ZUS RCA (imienne raporty składkowe):", f"{'Osoba':<22}{'Kod':<7}{'Podst. ER':>10}{'Podst. CH':>10}{'Emer.':>9}{'Rent.':>8}{'Chor.':>8}{'Wyp.':>8}{'Zdrow.':>9}"]
        for x in rca:
            linie.append(f"{x['osoba'][:21]:<22}{x['kod']:<7}{kadry.fmt(x['podstawa_er']):>10}{kadry.fmt(x['podstawa_ch']):>10}{kadry.fmt(x['emer'] + x['emer_p']):>9}{kadry.fmt(x['rent'] + x['rent_p']):>8}{kadry.fmt(x['chor']):>8}{kadry.fmt(x['wyp']):>8}{kadry.fmt(x['zdr']):>9}")
        if not rca:
            linie.append("  (brak — dodaj osoby w „Lista płac” → „Dodaj do listy miesiąca”)")
        linie += ["", "ZUS RSA (przerwy i świadczenia):"]
        for x in rsa:
            linie.append(f"  {x['osoba']:<22}{x['kod_przerwy']} {kadry.KODY_PRZERW.get(x['kod_przerwy'], '?')[:40]:<42}{x['od']} – {x['do']}  {kadry.fmt(x.get('kwota', 0))}")
        if not rsa:
            linie.append("  (brak)")
        linie += ["", "ZUS DRA (deklaracja zbiorcza):",
                  f"  liczba ubezpieczonych: {s['liczba']}", f"  składki emerytalne: {kadry.fmt(s['emer'])}   rentowe: {kadry.fmt(s['rent'])}   chorobowe: {kadry.fmt(s['chor'])}   wypadkowe: {kadry.fmt(s['wyp'])}",
                  f"  społeczne razem: {kadry.fmt(s['spoleczne'])}   zdrowotne: {kadry.fmt(s['zdr'])}   FP: {kadry.fmt(s['fp'])}   FGŚP: {kadry.fmt(s['fgsp'])}",
                  f"  wypłacone zasiłki (do odliczenia): {kadry.fmt(s['zasilki'])}", f"  DO ZAPŁATY na NRS: {kadry.fmt(s['do_zaplaty'])}"]
        if wynik_weryfikacji is not None:
            bledy, ostrz = wynik_weryfikacji
            linie += ["", "WERYFIKACJA:"] + [f"  ✘ BŁĄD: {b}" for b in bledy] + [f"  ⚠ {x}" for x in ostrz] + (["  ✔ komplet poprawny"] if not bledy and not ostrz else [])
        _ustaw(txt2, "\n".join(linie))
        return rca, rsa, s

    def weryfikuj2():
        m = f2.get("miesiac").strip()
        try:
            r_, m_ = int(m[:4]), int(m[5:7])
        except ValueError:
            st2.configure(text="Miesiąc w formacie RRRR-MM.", fg=M.K["czerw"])
            return None
        rca, rsa = rca_wiersze(), rsa_wiersze()
        wcz = [x["ident"] for x in w["komplety"] if x["miesiac"] == m]
        bledy, ostrz = kadry.sprawdz_komplet(rca, rsa, w["osoby"], m_, r_, f2.get("ident"), wcz)
        if not rca:
            bledy.append("Komplet bez żadnego RCA.")
        pokaz_komplet((bledy, ostrz))
        return bledy

    def wyslij2():
        bledy = weryfikuj2()
        if bledy is None or bledy:
            st2.configure(text="Komplet ma błędy krytyczne — popraw.", fg=M.K["czerw"])
            return
        m = f2.get("miesiac").strip()
        rca, rsa, s = pokaz_komplet()
        upp = f"UPP-{rok}{random.randint(100000, 999999)}"
        w["komplety"].append({"miesiac": m, "ident": f2.get("ident"), "upp": upp, "do_zaplaty": s["do_zaplaty"], "liczba": s["liczba"], "wyslano": str(dt.date.today())})
        w["wyslane"].append({"osoba": "— komplet —", "typ": f"DRA/RCA/RSA {f2.get('ident')} {m}", "kod": "", "data": m, "status": "przyjęty", "upp": upp, "wyslano": str(dt.date.today())})
        app.stan.zapisz()
        st2.configure(text=f"✔ komplet {f2.get('ident')} {m} przyjęty — {upp}; przelew {kadry.fmt(s['do_zaplaty'])} zł na NRS do 15. dnia następnego miesiąca", fg=M.K["ziel"])

    def zapisz2():
        m = f2.get("miesiac").strip()
        zapisz_do_projektu(app, "05-zus-us", f"zus_{m}.md", "```\n" + txt2.get("1.0", "end") + "```\n", st2)

    r = tk.Frame(k, bg=M.K["karta"])
    r.pack(fill="x", pady=(6, 0))
    M.przycisk(r, "Dodaj RSA", dodaj_rsa, "drugi").pack(side="left")
    M.przycisk(r, "Usuń RSA miesiąca", lambda: (w.update(rsa=[x for x in w["rsa"] if not x.get("od", "").startswith(f2.get("miesiac").strip())]), app.stan.zapisz(), pokaz_komplet()), "drugi").pack(side="left", padx=8)
    M.przycisk(r, "Pokaż komplet", pokaz_komplet, "drugi").pack(side="left")
    M.przycisk(r, "Weryfikuj", weryfikuj2).pack(side="left", padx=8)
    M.przycisk(r, "Wyślij (symulacja)", wyslij2, "drugi").pack(side="left")
    M.przycisk(r, "Zapisz do projektu", zapisz2, "drugi").pack(side="left", padx=8)
    txt2.pack_forget(); txt2.pack(fill="both", expand=True, pady=(8, 0)); st2.pack_forget(); st2.pack(fill="x")

    # --- e-ZLA
    k = _karta(strony["e-ZLA"], "Skrzynka e-ZLA płatnika (jak w eZUS)")
    txt3 = _wynik(k, 10)
    st3 = _status(k)

    def pokaz_ezla():
        linie = [f"{'Nr':<12}{'Osoba':<24}{'Od':<12}{'Do':<12}{'Dni':>4}  {'Kod':<4}{'Opis':<40}{'Pobrane'}"]
        for z in w["ezla"]:
            dni = (_data(z["do"]) - _data(z["od"])).days + 1
            linie.append(f"{z['nr']:<12}{z['osoba']:<24}{z['od']:<12}{z['do']:<12}{dni:>4}  {z['kod'] or '—':<4}{z['opis']:<40}{'✔' if z['pobrane'] else ''}")
        linie.append("\nKody: A — ta sama choroba po przerwie < 60 dni, B — ciąża, C — alkohol (5 dni bez zasiłku), D — gruźlica, E — po ustaniu tytułu.")
        _ustaw(txt3, "\n".join(linie))

    pokaz_ezla()
    f4 = Formularz(k, 3)
    f4.pole("nr", "e-ZLA", w["ezla"][0]["nr"] if w["ezla"] else "", 12, opcje=[z["nr"] for z in w["ezla"]], podpowiedz="readonly")
    f4.pole("kod_rsa", "Kod przerwy do RSA", "331", 5, opcje=["331", "313", "312", "314"])
    f4.pole("kwota", "Kwota świadczenia", "0", 9)

    def pobierz():
        z = next((x for x in w["ezla"] if x["nr"] == f4.get("nr")), None)
        if not z:
            return
        z["pobrane"] = True
        w["rsa"].append({"pesel": z["pesel"], "osoba": z["osoba"], "kod_przerwy": f4.get("kod_rsa"), "od": z["od"], "do": z["do"], "kwota": f4.liczba("kwota")})
        app.stan.zapisz()
        pokaz_ezla()
        st3.configure(text=f"✔ {z['nr']} dodano do RSA jako {f4.get('kod_rsa')} ({z['od']} – {z['do']})", fg=M.K["ziel"])

    r = tk.Frame(k, bg=M.K["karta"])
    r.pack(fill="x", pady=(6, 0))
    M.przycisk(r, "Pobierz do RSA", pobierz).pack(side="left")
    M.przycisk(r, "Zapisz skrzynkę do projektu", lambda: zapisz_do_projektu(app, "05-zus-us", "ezla.md", "```\n" + txt3.get("1.0", "end") + "```\n", st3), "drugi").pack(side="left", padx=8)
    txt3.pack_forget(); txt3.pack(fill="both", expand=True, pady=(8, 0)); st3.pack_forget(); st3.pack(fill="x")

    # --- Rejestr
    k = _karta(strony["Rejestr wysłanych"], "Rejestr dokumentów wysłanych do ZUS (UPP)")
    txt4 = _wynik(k, 16)
    linie = [f"{'Wysłano':<12}{'Osoba':<24}{'Dokument':<24}{'Kod':<8}{'Data':<12}{'Status':<10}{'UPP'}"]
    for x in w["wyslane"]:
        linie.append(f"{x.get('wyslano', ''):<12}{x.get('osoba', ''):<24}{x['typ']:<24}{x.get('kod', ''):<8}{x.get('data', ''):<12}{x.get('status', ''):<10}{x.get('upp', '')}")
    _ustaw(txt4, "\n".join(linie) if w["wyslane"] else "Jeszcze nic nie wysłano.")
    st4 = _status(k)
    M.przycisk(k, "Zapisz rejestr do projektu", lambda: zapisz_do_projektu(app, "05-zus-us", "rejestr_zus.md", "```\n" + txt4.get("1.0", "end") + "```\n", st4), "drugi").pack(anchor="w", pady=(6, 0))


# ============================================================ e-URZĄD: PIT
def BUDUJ_pit(app, parent):
    M = _M()
    w = stan(app)
    par = P.parametry or {}
    rok = par.get("rok", kadry.DOMYSLNE["rok"])
    k = _karta(parent, "e-Urząd Skarbowy (symulacja): PIT-11 i PIT-4R")
    M.etykieta(k, "Kartoteka to wiersze dodane w „Lista płac” → „Dodaj do listy miesiąca”. PIT-11 sumuje wypłaty pracownika w roku (zasada kasowa), PIT-4R — zaliczki miesięczne płatnika.", 9, kolor=M.K["szary"], wrap=820).pack(fill="x", pady=(0, 6))
    f = Formularz(k, 2)
    f.pole("rok", "Rok podatkowy", str(rok), 6)
    osoby = sorted({x["osoba"] for x in w["kartoteka"]}) or ["— brak wierszy w kartotece —"]
    f.pole("osoba", "Podatnik (PIT-11)", osoby[0], 30, opcje=osoby, podpowiedz="readonly")
    txt = _wynik(k, 22)
    st = _status(k)

    def wiersze_roku():
        r = f.get("rok").strip()
        return [x for x in w["kartoteka"] if x["miesiac"].startswith(r)]

    def pit11():
        os_ = f.get("osoba")
        ww = [x for x in wiersze_roku() if x["osoba"] == os_]
        if not ww:
            _ustaw(txt, "Brak wypłat tej osoby w kartotece za ten rok.")
            return
        o = next((x for x in w["osoby"] if f"{x['imie']} {x['nazwisko']}" == os_), {})
        s = lambda kk: kadry.zl(sum(x.get(kk, 0) for x in ww))
        przych = s("przychod_pracy")
        zwol = s("zwolnione")
        skl = s("emer") + s("rent") + s("chor")
        linie = [f"PIT-11 za {f.get('rok')} — INFORMACJA O PRZYCHODACH Z INNYCH ŹRÓDEŁ ORAZ O DOCHODACH I POBRANYCH ZALICZKACH (wersja ćwiczeniowa)",
                 f"Płatnik: AGRO-MLEKO sp. z o.o.      Podatnik: {os_}   PESEL {o.get('pesel', '')}", f"Miesięcy z wypłatą: {len(ww)}  ({', '.join(x['miesiac'] for x in ww)})", "",
                 "E. DOCHODY PODATNIKA, POBRANE ZALICZKI ORAZ SKŁADKI",
                 f"  Należności ze stosunku pracy — przychód: {kadry.fmt(kadry.zl(przych - zwol)):>12}   KUP: {kadry.fmt(s('kup')):>10}   dochód: {kadry.fmt(kadry.zl(przych - zwol - s('kup'))):>12}",
                 f"  Zasiłki pieniężne z ubezpieczenia społecznego (inne źródła): {kadry.fmt(s('zasilek')):>12}",
                 f"  Pobrane zaliczki razem: {kadry.fmt(s('zaliczka')):>12}", f"  Składki na ubezpieczenia społeczne podlegające odliczeniu: {kadry.fmt(kadry.zl(skl)):>12}",
                 f"  Składka zdrowotna: {kadry.fmt(s('zdrowotna'))} (od 2022 nie podlega odliczeniu — pole informacyjne tylko w tej symulacji)", ""]
        if zwol:
            linie += ["G. PRZYCHODY ZWOLNIONE OD PODATKU", f"  Ulga dla młodych — przychody ze stosunku pracy: {kadry.fmt(zwol)}", ""]
        linie.append("Terminy: do urzędu skarbowego — do 31 stycznia (elektronicznie, UPL-1); podatnikowi — do końca lutego.")
        _ustaw(txt, "\n".join(linie))

    def pit4r():
        ww = wiersze_roku()
        if not ww:
            _ustaw(txt, "Brak wierszy w kartotece za ten rok.")
            return
        linie = [f"PIT-4R za {f.get('rok')} — DEKLARACJA ROCZNA O ZALICZKACH NA PODATEK DOCHODOWY (wersja ćwiczeniowa)", "Płatnik: AGRO-MLEKO sp. z o.o.", "",
                 f"{'Miesiąc':<12}{'Liczba podatników':>18}{'Zaliczka należna':>18}{'Termin wpłaty':>16}"]
        razem = 0.0
        for m in sorted({x["miesiac"] for x in ww}):
            mm = [x for x in ww if x["miesiac"] == m]
            z = kadry.zl(sum(x["zaliczka"] for x in mm))
            razem += z
            r_, m_ = int(m[:4]), int(m[5:7])
            nm = dt.date(r_ + (m_ == 12), m_ % 12 + 1, 20)
            linie.append(f"{m:<12}{len(mm):>18}{kadry.fmt(z):>18}{str(nm):>16}")
        linie += ["", f"RAZEM zaliczki: {kadry.fmt(kadry.zl(razem))}   (musi się zgadzać z wpłatami na mikrorachunek i z sumą PIT-11)", "Termin złożenia: do 31 stycznia następnego roku."]
        _ustaw(txt, "\n".join(linie))

    def wyslij():
        tresc = txt.get("1.0", "end").strip()
        if not tresc.startswith("PIT-"):
            st.configure(text="Najpierw wygeneruj PIT-11 albo PIT-4R.", fg=M.K["czerw"])
            return
        upo = f"UPO-{rok}{random.randint(100000, 999999)}"
        w["pit_wyslane"].append({"co": tresc.split(" — ")[0], "upo": upo, "data": str(dt.date.today())})
        app.stan.zapisz()
        st.configure(text=f"✔ {tresc.split(' — ')[0]} przyjęty przez e-Urząd (symulacja) — Urzędowe Poświadczenie Odbioru {upo}", fg=M.K["ziel"])

    r = tk.Frame(k, bg=M.K["karta"])
    r.pack(fill="x", pady=(6, 0))
    M.przycisk(r, "Generuj PIT-11", pit11).pack(side="left")
    M.przycisk(r, "Generuj PIT-4R", pit4r, "drugi").pack(side="left", padx=8)
    M.przycisk(r, "Wyślij (symulacja, UPO)", wyslij, "drugi").pack(side="left")
    r2 = tk.Frame(k, bg=M.K["karta"])
    r2.pack(fill="x", pady=(6, 0))
    M.przycisk(r2, "Zapisz do projektu", lambda: zapisz_do_projektu(app, "05-zus-us", f"pit_{f.get('osoba').split()[0].lower() if txt.get('1.0', '1.6') == 'PIT-11' else '4r'}_{f.get('rok')}.md", "```\n" + txt.get("1.0", "end") + "```\n", st), "drugi").pack(side="left")
    txt.pack_forget(); txt.pack(fill="both", expand=True, pady=(8, 0)); st.pack_forget(); st.pack(fill="x")
    if w["pit_wyslane"]:
        M.etykieta(k, "Wysłane: " + "; ".join(f"{x['co']} ({x['upo']}, {x['data']})" for x in w["pit_wyslane"][-6:]), 9, kolor=M.K["szary"], wrap=820).pack(fill="x", pady=(6, 0))


# ============================================================ PRZEPISY
def BUDUJ_przepisy(app, parent):
    M = _M()
    k = _karta(parent, f"Biblioteka przepisów (offline) — {len(P.przepisy)} regulacji")
    M.etykieta(k, "To streszczenia na potrzeby nauki (stan prawny z programu). Pełne teksty aktów są publiczne i bez logowania w ISAP — link pod każdym wpisem, jeśli masz internet.", 9, kolor=M.K["szary"], wrap=820).pack(fill="x", pady=(0, 6))
    r = tk.Frame(k, bg=M.K["karta"])
    r.pack(fill="x")
    tk.Label(r, text="Szukaj:", font=M.czc(10), bg=M.K["karta"], fg=M.K["tekst"]).pack(side="left")
    szukaj = tk.StringVar()
    tk.Entry(r, textvariable=szukaj, font=M.czc(10), width=36, relief="flat", bg=M.K["jasny"], fg=M.K["tekst"], insertbackground=M.K["tekst"]).pack(side="left", padx=6, ipady=3)
    cialo = tk.Frame(k, bg=M.K["karta"])
    cialo.pack(fill="both", expand=True, pady=(8, 0))
    lb = tk.Listbox(cialo, font=M.czc(10), bg=M.K["jasny"], fg=M.K["tekst"], relief="flat", selectbackground=M.K["akcent"], selectforeground=M.K["btn_tekst"], activestyle="none", width=46, height=22)
    lb.pack(side="left", fill="y")
    txt = tk.Text(cialo, font=M.czc(10), bg=M.K["jasny"], fg=M.K["tekst"], relief="flat", padx=12, pady=10, wrap="word", height=22)
    txt.pack(side="left", fill="both", expand=True, padx=(10, 0))
    widoczne = []

    def filtruj(*_):
        q = szukaj.get().lower().strip()
        lb.delete(0, "end")
        widoczne.clear()
        for p in P.przepisy:
            blob = " ".join(str(p.get(x, "")) for x in ("akt", "art", "tytul", "tresc", "slowa")).lower()
            if not q or all(s in blob for s in q.split()):
                widoczne.append(p)
                lb.insert("end", f" {p['art']} — {p['tytul']}")

    def pokaz(_=None):
        i = lb.curselection()
        if not i:
            return
        p = widoczne[i[0]]
        txt.configure(state="normal")
        txt.delete("1.0", "end")
        txt.insert("end", f"{p['akt']}\n{p['art']} — {p['tytul']}\n\n{p['tresc']}\n")
        if p.get("lekcja"):
            txt.insert("end", f"\nLekcja: {P.lekcja(p['lekcja'])['nazwa'] if P.lekcja(p['lekcja']) else p['lekcja']}")
        if p.get("isap"):
            txt.insert("end", f"\n\nŹródło (opcjonalnie, bez logowania): {p['isap']}")

    szukaj.trace_add("write", filtruj)
    lb.bind("<<ListboxSelect>>", pokaz)
    filtruj()
    if widoczne:
        lb.selection_set(0)
        pokaz()
