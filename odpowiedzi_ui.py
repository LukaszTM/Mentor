# -*- coding: utf-8 -*-
"""
Panel „Sprawdź odpowiedzi” (tkinter) — wspólny dla ćwiczeń w lekcjach i formularzy w Warsztacie.
Logika porównań: odpowiedzi.py. Stan (wpisy, liczba prób, wynik) zapisuje się w mentor_dane.json pod programem: stan.d["odpowiedzi"][klucz].
"""

import datetime as dt
import tkinter as tk
from tkinter import ttk

import odpowiedzi as O

XP_KOMPLET = 2          # punkty za komplet poprawnych odpowiedzi bez podglądania klucza (raz na ćwiczenie/formularz)
PROBY_DO_KLUCZA = 2     # po tylu próbach wolno pokazać poprawne wartości
DLUGA_OPCJA = 30        # lista wyboru z dłuższą opcją dostaje własny wiersz na całą szerokość panelu (obok etykiety byłaby ucięta)


def _M():
    import mentor
    return mentor


def zapis(app, klucz):
    """Zapisany stan panelu albo pusty słownik."""
    return app.stan.d.setdefault("odpowiedzi", {}).get(klucz) or {}


def wynik_tekst(z):
    """Krótki opis zapisanego wyniku do plakietek („4/5 · 2 próby”)."""
    if not z or not z.get("max"):
        return ""
    return f"{z.get('ok', 0)}/{z['max']} · {z.get('proby', 0)} {'próba' if z.get('proby') == 1 else 'próby' if 2 <= z.get('proby', 0) <= 4 else 'prób'}"


def panel(app, parent, pola, klucz, W=600, bg=None, po_sprawdzeniu=None, po_pokazaniu=None, naglowek=True):
    """Buduje formularz odpowiedzi w „parent”. Zwraca ramkę. po_sprawdzeniu(wynik) — po każdym „Sprawdź”; po_pokazaniu() — po odsłonięciu klucza."""
    M = _M()
    K = M.K
    bg = bg or K["karta"]
    zap = dict(zapis(app, klucz))
    wpisy0 = zap.get("wpisy") or {}
    ramka = tk.Frame(parent, bg=bg)
    ramka.pack(fill="x", pady=(6, 0))
    if naglowek:
        M.etykieta(ramka, "✍ Twoje odpowiedzi — wpisz i kliknij „Sprawdź”; Mentor oceni każde pole osobno i nie zdradzi wyniku", 9, kolor=K["szary"], bg=bg, wrap=W).pack(fill="x", pady=(0, 4))
    siatka = tk.Frame(ramka, bg=bg)
    siatka.pack(fill="x")
    siatka.columnconfigure(0, weight=1)
    szer_pola = 190                                   # miejsce na pole wpisu (px); etykieta zawija się w reszcie szerokości
    zmienne, statusy = {}, {}
    zawijane = []                                     # (etykieta, widżet obok albo None) — szerokość zawijania dopasowuje się do faktycznej szerokości panelu
    wiersz, sekcja = 0, None
    for p in pola:
        if p.get("sekcja") and p["sekcja"] != sekcja:          # nagłówek bloku formularza (np. „III.B. Zestawienie należnych składek…”)
            sekcja = p["sekcja"]
            ns = tk.Label(siatka, text=sekcja, font=M.czc(10, "bold"), bg=bg, fg=K["akcent"], anchor="w", justify="left", wraplength=max(W - 20, 220))
            ns.grid(row=wiersz, column=0, columnspan=2, sticky="w", pady=(8, 0))
            zawijane.append((ns, None))
            wiersz += 1
        opcje = [str(o) for o in (p.get("opcje") or [])]
        dlugie = p.get("typ") == "wybor" and max((len(o) for o in opcje), default=0) > DLUGA_OPCJA     # nie zmieści się obok etykiety → własny wiersz
        et = tk.Label(siatka, text=p.get("etykieta", ""), font=M.czc(10), bg=bg, fg=K["tekst"], anchor="w", justify="left",
                      wraplength=max(W - 20, 220) if dlugie else max(W - szer_pola - 20, 200))
        et.grid(row=wiersz, column=0, columnspan=2 if dlugie else 1, sticky="w", pady=(3, 0))
        var = tk.StringVar(value=str(wpisy0.get(p["id"], "")))
        if p.get("typ") == "wybor":
            w = ttk.Combobox(siatka, textvariable=var, values=opcje, width=max(12, min(DLUGA_OPCJA, max((len(o) for o in opcje), default=12))), state="readonly")
        else:
            w = tk.Entry(siatka, textvariable=var, font=M.czc(10), width=18, relief="flat", bg=K["jasny"], fg=K["tekst"], insertbackground=K["tekst"])
            w.bind("<Return>", lambda e: sprawdz())
        if dlugie:
            wiersz += 1
            w.grid(row=wiersz, column=0, columnspan=2, sticky="we", padx=(14, 0), pady=(2, 0), ipady=3)
        else:
            w.grid(row=wiersz, column=1, sticky="e", padx=(8, 0), pady=(3, 0), ipady=3)
        zawijane.append((et, None if dlugie else w))
        st = tk.Label(siatka, text="", font=M.czc(9), bg=bg, fg=K["szary"], anchor="w", justify="left", wraplength=max(W - 30, 220))
        st.grid(row=wiersz + 1, column=0, columnspan=2, sticky="w", padx=(14, 0))
        wiersz += 2
        st.grid_remove()                              # wiersz statusu pojawia się dopiero po sprawdzeniu
        zawijane.append((st, None))
        zmienne[p["id"]], statusy[p["id"]] = var, st

    def _dopasuj(_e=None):
        """Etykiety zawijają się w faktycznej szerokości panelu (karta lekcji bywa węższa niż założone W) — nic nie chowa się pod polem wpisu."""
        szer = siatka.winfo_width()
        if szer <= 40:
            return
        for lab, obok in zawijane:
            cel = max(szer - 30, 140) if obok is None else max(szer - obok.winfo_reqwidth() - 34, 140)
            if int(lab.cget("wraplength")) != cel:
                lab.configure(wraplength=cel)

    siatka.bind("<Configure>", _dopasuj)
    r = tk.Frame(ramka, bg=bg)
    r.pack(fill="x", pady=(6, 0))
    podsum = tk.Label(ramka, text="", font=M.czc(10, "bold"), bg=bg, fg=K["szary"], anchor="w", justify="left", wraplength=max(W - 20, 220))

    def _zapisz(**zmiany):
        zap.update(zmiany)
        zap["wpisy"] = {k: v.get() for k, v in zmienne.items()}
        app.stan.d.setdefault("odpowiedzi", {})[klucz] = dict(zap)
        app.stan.zapisz()

    def _pokaz_wynik(w, proby):
        for x in w["wyniki"]:
            st = statusy[x["id"]]
            if x["ok"] is True:
                st.configure(text="✔ dobrze", fg=K["ziel"])
            elif x["ok"] is None:
                st.configure(text="— puste", fg=K["szary"])
            else:
                st.configure(text="✘ " + x["info"], fg=K["czerw"])
            st.grid()
        if w["komplet"]:
            podsum.configure(text=f"✔ Komplet: {w['ok']}/{w['max']}" + (" — bez podglądania klucza" if not zap.get("pokazane") else ""), fg=K["ziel"])
        else:
            podsum.configure(text=f"{w['ok']}/{w['max']} poprawnie · próba {proby}" + (" — popraw pola oznaczone ✘" if w["ok"] < w["max"] else ""), fg=K["pomar"])
        b_klucz.configure(state="normal" if (proby >= PROBY_DO_KLUCZA and not w["komplet"]) else "disabled")

    def sprawdz():
        w = O.sprawdz(pola, {k: v.get() for k, v in zmienne.items()})
        if w["puste"] == w["max"]:
            podsum.configure(text="Wpisz przynajmniej jedną odpowiedź.", fg=K["szary"])
            return
        proby = int(zap.get("proby", 0)) + 1
        pierwszy_komplet = w["komplet"] and not zap.get("komplet")
        if pierwszy_komplet and not zap.get("pokazane"):
            app.stan.d["xp"] = app.stan.d.get("xp", 0) + XP_KOMPLET
        _zapisz(proby=proby, ok=w["ok"], max=w["max"], komplet=bool(zap.get("komplet") or w["komplet"]), data=str(dt.date.today()))
        _pokaz_wynik(w, proby)
        if po_sprawdzeniu:
            po_sprawdzeniu(w)

    def pokaz_klucz():
        w = O.sprawdz(pola, {k: v.get() for k, v in zmienne.items()})
        for p, x in zip(pola, w["wyniki"]):
            if x["ok"] is not True:
                statusy[p["id"]].configure(text="→ poprawnie: " + O.poprawna(p), fg=K["nieb"])
                statusy[p["id"]].grid()
        _zapisz(pokazane=True)
        b_klucz.configure(state="disabled")
        podsum.configure(text="Klucz pokazany — przelicz jeszcze raz sam i wyjaśnij różnicę w dzienniku.", fg=K["nieb"])
        if po_pokazaniu:
            po_pokazaniu()

    M.przycisk(r, "Sprawdź odpowiedzi", sprawdz).pack(side="left")
    b_klucz = M.przycisk(r, f"Pokaż klucz (po {PROBY_DO_KLUCZA} próbach)", pokaz_klucz, "drugi")
    b_klucz.pack(side="left", padx=8)
    b_klucz.configure(state="disabled")
    podsum.pack(fill="x", pady=(4, 0))
    if zap.get("proby"):
        _pokaz_wynik(O.sprawdz(pola, wpisy0), int(zap["proby"]))
    ramka.sprawdz, ramka.pokaz_klucz, ramka.zmienne = sprawdz, pokaz_klucz, zmienne     # uchwyty dla testów GUI
    return ramka
