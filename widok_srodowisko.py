# -*- coding: utf-8 -*-
"""
Widok „Środowisko kursu” (w spec: environment_ui). Buduje go mentor.py przez zbuduj(app, parent).

Diagnoza i instalacja działają w wątkach roboczych; wyniki wracają do GUI kolejką odczytywaną przez app.after(...)
— główna pętla Tkinter nigdy nie czeka na procesy. Statusy w tabeli pochodzą z realnych uruchomień (srodowisko.diagnoza).
"""

import queue
import threading
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

import paczki
import srodowisko as S
from program import P, KATALOG_LOGOW, katalog_kursu, katalog_materialow, meta_kursu


def _M():
    import mentor
    return mentor


KOLORY = {S.GOTOWE: ("ziel_tlo", "ziel"), S.BRAK: ("czerw_tlo", "czerw"), S.ZLA_WERSJA: ("zolty", "pomar"), S.BLAD: ("czerw_tlo", "czerw"),
          S.OPCJONALNE: ("jasny", "szary"), S.SPRAWDZANIE: ("nieb_tlo", "nieb"), S.NIE_SPRAWDZONO: ("jasny", "szary"), S.POMINIETO: ("zolty", "pomar")}


def _stan(app):
    s = app.__dict__.setdefault("_srod", {})
    if s.get("kurs") != P.id:
        s.clear()
        s.update({"kurs": P.id, "diag": None, "w_toku": None, "log": [], "kolejka": None, "anuluj": None, "watek": None, "ostatnie_kroki": [], "blad": None})
    return s


def srodowisko_biezace():
    return S.srodowisko_programu(P)


def status_skrot():
    """(etykieta, kolory) do Panelu/przewodnika — z zapisanego stanu, bez uruchamiania procesów."""
    sr = srodowisko_biezace()
    if not sr.wymaga_srodowiska():
        return "nie wymaga środowiska", KOLORY[S.GOTOWE]
    st = sr.stan()
    if sr.gotowe():
        return "środowisko gotowe", KOLORY[S.GOTOWE]
    if st.get("diagnoza"):
        return "środowisko niepełne — zobacz zakładkę Środowisko", KOLORY[S.BRAK]
    return "środowisko nie sprawdzone — zobacz zakładkę Środowisko", KOLORY[S.NIE_SPRAWDZONO]


# ============================================================ widok
def zbuduj(app, parent):
    M = _M()
    K = M.K
    st = _stan(app)
    sr = srodowisko_biezace()
    st["sr"] = sr
    meta = meta_kursu(P.id)

    # --- nagłówek kursu
    z, k = M.karta(parent, tytul=f"{P.nazwa}")
    z.pack(fill="x", padx=28)
    wym = sr.wym
    opis = []
    if meta:
        opis.append(f"kurs z paczki · wersja {meta.get('wersja')} · zaimportowano {str(meta.get('data_importu', ''))[:16]}")
    else:
        opis.append("kurs wbudowany" + (f" · wersja {P.d.get('wersja')}" if P.d.get("wersja") else ""))
    if sr.wymaga_srodowiska():
        czesci = []
        if wym.get("python"):
            czesci.append(f"Python {wym['python']}")
        if sr.pakiety_wymagane():
            czesci.append("biblioteki: " + ", ".join(sr.pakiety_wymagane()))
        if wym.get("przegladarka"):
            czesci.append("przeglądarka: " + wym["przegladarka"])
        if wym.get("narzedzia_opcjonalne"):
            czesci.append("opcjonalnie: " + ", ".join(x["nazwa"] if isinstance(x, dict) else x for x in wym["narzedzia_opcjonalne"]))
        opis.append("wymagania (" + wym.get("zrodlo", "?") + "): " + "; ".join(czesci))
        opis.append(f"środowisko kursu: {sr.venv}  ·  log: {sr.log}")
    else:
        opis.append("Ten kurs nie wymaga Pythona ani innych programów — wszystko jest w Mentorze.")
    M.etykieta(k, "\n".join(opis), 10, wrap=860).pack(fill="x")
    for u in wym.get("uwagi", [])[:3]:
        M.etykieta(k, "ℹ " + u, 9, kolor=K["szary"], wrap=860).pack(fill="x")
    r = tk.Frame(k, bg=K["karta"])
    r.pack(fill="x", pady=(10, 0))
    st["przyciski"] = r
    _przyciski(app, r, sr)

    # --- lokalny serwer API kursu (gdy kurs go deklaruje)
    if sr.api_lokalne():
        _karta_api(app, parent, sr)

    # --- tabela statusów
    z, k = M.karta(parent, tytul="Składniki środowiska — statusy z realnych uruchomień, nie z PATH")
    z.pack(fill="x", padx=28, pady=(12, 0))
    if st.get("diag") is None and st.get("w_toku") != "diagnoza":
        zapisana = sr.stan().get("diagnoza")
        if zapisana and not st.get("odswiez"):
            st["diag"] = zapisana
            M.etykieta(k, f"Ostatnia diagnoza: {sr.stan().get('zapis', '')[:16]} — kliknij „Sprawdź ponownie”, żeby odświeżyć.", 9, kolor=K["szary"]).pack(fill="x", pady=(0, 6))
    wn = tk.Frame(k, bg=K["karta"])
    wn.pack(fill="x")
    st["tabela"] = wn
    if st.get("diag") is None and st.get("w_toku") != "diagnoza":
        _diagnozuj(app)
    _rysuj_tabele(app)

    # --- postęp / log
    z, k = M.karta(parent, tytul="Przebieg instalacji i testów")
    z.pack(fill="x", padx=28, pady=(12, 24))
    st["postep_karta"] = k
    st["krok_lbl"] = M.etykieta(k, st.get("krok_tekst") or ("Nic nie jest teraz wykonywane." if not st.get("w_toku") else "…"), 10, bold=True, wrap=860)
    st["krok_lbl"].pack(fill="x")
    st["pasek"] = ttk.Progressbar(k, maximum=100, value=st.get("pasek_wartosc", 0))
    st["pasek"].pack(fill="x", pady=(6, 6))
    txt = tk.Text(k, height=12, font=M.czc(9, mono=True), bg=K["jasny"], fg=K["tekst"], relief="flat", padx=10, pady=8, wrap="word", state="disabled")
    txt.pack(fill="x")
    st["log_txt"] = txt
    _ustaw_log(app)
    r = tk.Frame(k, bg=K["karta"])
    r.pack(fill="x", pady=(8, 0))
    M.przycisk(r, "Anuluj", lambda: _anuluj(app), "drugi").pack(side="left")
    M.przycisk(r, "Ponów", lambda: _ponow(app), "drugi").pack(side="left", padx=8)
    M.przycisk(r, "Pokaż szczegóły (pełny log)", lambda: _pokaz_log(app), "drugi").pack(side="left")
    if st.get("watek") and st["watek"].is_alive() and not st.get("poll"):
        _poll(app)


def _karta_api(app, parent, sr):
    """Lokalny serwer API z paczki: uruchamiany TYLKO przyciskiem, po weryfikacji sumy skryptu, na 127.0.0.1; Zatrzymaj; Sprawdź API (realne GET /health)."""
    M = _M()
    K = M.K
    st = _stan(app)
    api = sr.api_lokalne()
    z, k = M.karta(parent, tytul="Lokalny serwer API kursu")
    z.pack(fill="x", padx=28, pady=(12, 0))
    M.etykieta(k, f"Skrypt z paczki: {api['skrypt']} · adres: http://127.0.0.1:{api['port']} · tylko ten komputer (127.0.0.1), uruchamiany interpreterem kursu "
                  "po sprawdzeniu sumy SHA-256 z manifestu/INTEGRITY.json — nigdy automatycznie." + (f"\n{api['opis']}" if api.get("opis") else ""), 9, kolor=K["szary"], wrap=860).pack(fill="x")
    lbl = M.etykieta(k, "", 10, bold=True)
    lbl.pack(fill="x", pady=(6, 0))
    st["api_lbl"] = lbl

    def odswiez():
        s_ = sr.api_stan()
        if s_["dziala"]:
            lbl.configure(text=f"● DZIAŁA — {s_['url']} (PID {s_['pid']})", fg=K["ziel"])
        else:
            lbl.configure(text="○ nie uruchomiony", fg=K["szary"])

    def uruchom():
        if sr.api_stan()["dziala"]:
            odswiez()
            return
        try:
            sk, suma = sr.plik_paczki(api["skrypt"], api.get("sha256"))
        except RuntimeError as e:
            messagebox.showerror("Lokalne API", str(e), parent=app)
            return
        if not messagebox.askyesno("Uruchomić lokalne API kursu?",
                                   f"Mentor uruchomi skrypt z paczki kursu interpreterem kursu:\n{sk}\nSHA-256: {suma[:16]}… (zgodna z paczką)\n\n"
                                   f"Serwer będzie dostępny tylko lokalnie: http://127.0.0.1:{api['port']} — do ćwiczeń z HTTP/API. "
                                   "Zatrzymasz go przyciskiem „Zatrzymaj” (zatrzymuje się też przy zamknięciu Mentora).", parent=app):
            return
        ok, msg = sr.api_uruchom(log=lambda t: _dodaj_log(app, t))
        (messagebox.showinfo if ok else messagebox.showerror)("Lokalne API", msg, parent=app)
        odswiez()

    def zatrzymaj():
        ok, msg = sr.api_zatrzymaj()
        _dodaj_log(app, "API: " + msg)
        odswiez()

    def sprawdz():
        kod, tresc = sr.api_sprawdz()
        s_ = sr.api_stan()
        if kod is None:
            messagebox.showwarning("Sprawdź API", f"GET {s_['health']} nie odpowiada: {tresc}\n\nUruchom serwer przyciskiem „Uruchom”.", parent=app)
        else:
            messagebox.showinfo("Sprawdź API", f"GET {s_['health']}\nkod odpowiedzi: {kod}\ntreść: {tresc[:300]}", parent=app)
        _dodaj_log(app, f"API: GET {s_['health']} → {kod} {tresc[:80]}")
        odswiez()

    def w_przegladarce():
        import webbrowser
        webbrowser.open(sr.api_stan()["health"])
    r = tk.Frame(k, bg=K["karta"])
    r.pack(fill="x", pady=(8, 0))
    M.przycisk(r, "▶ Uruchom", uruchom, "glowny").pack(side="left")
    M.przycisk(r, "■ Zatrzymaj", zatrzymaj, "drugi").pack(side="left", padx=8)
    M.przycisk(r, "Sprawdź API (GET /health)", sprawdz, "drugi").pack(side="left")
    M.przycisk(r, "Otwórz w przeglądarce", w_przegladarce, "drugi").pack(side="left", padx=8)
    odswiez()


def _przyciski(app, r, sr):
    M = _M()
    for w in r.winfo_children():
        w.destroy()
    if sr.wymaga_srodowiska():
        M.przycisk(r, "🔍 Sprawdź ponownie", lambda: _diagnozuj(app, True), "drugi").pack(side="left")
        M.przycisk(r, "⬇ Zainstaluj brakujące", lambda: _instaluj(app), "glowny").pack(side="left", padx=8)
        M.przycisk(r, "✔ Sprawdź działanie", lambda: _testuj(app), "drugi").pack(side="left")
        M.przycisk(r, "🛠 Napraw środowisko", lambda: _napraw(app), "drugi").pack(side="left", padx=8)
        M.przycisk(r, "Usuń środowisko", lambda: _usun_srodowisko(app), "drugi").pack(side="left")
    r2 = tk.Frame(r.master, bg=M.K["karta"])
    r2.pack(fill="x", pady=(6, 0))
    if katalog_kursu(P.id) or katalog_materialow(P.id):
        M.przycisk(r2, "📂 Otwórz katalog kursu", lambda: app._otworz_folder(str(katalog_kursu(P.id) or katalog_materialow(P.id))), "drugi").pack(side="left")
    if katalog_kursu(P.id):
        M.przycisk(r2, "Usuń kurs…", lambda: _usun_kurs(app), "drugi").pack(side="left", padx=8)
    M.przycisk(r2, "▶ Rozpocznij lekcję", lambda: app.pokaz_lekcje(P.lekcje[0]["id"] if P.lekcje else None), "ciemny").pack(side="left", padx=8)


def _rysuj_tabele(app):
    M = _M()
    K = M.K
    st = _stan(app)
    k = st.get("tabela")
    if not k or not k.winfo_exists():
        return
    for w in k.winfo_children():
        w.destroy()
    diag = st.get("diag")
    if st.get("w_toku") == "diagnoza" and not diag:
        M.plakietka(k, S.SPRAWDZANIE, K["nieb_tlo"], K["nieb"]).pack(anchor="w")
        M.etykieta(k, "Uruchamiam interpretery i narzędzia, żeby sprawdzić, czy naprawdę działają…", 10, kolor=K["szary"]).pack(fill="x", pady=(4, 0))
        return
    if not diag:
        M.etykieta(k, "Brak diagnozy.", 10, kolor=K["szary"]).pack(fill="x")
        return
    wymagane_brak = [p for p in diag if p.get("wymagane") and p["status"] not in (S.GOTOWE, S.OPCJONALNE, S.POMINIETO)]
    sr = st["sr"]
    if not sr.wymaga_srodowiska():
        pod = "Kurs działa w samym Mentorze."
    elif not wymagane_brak:
        pod = "Wszystkie wymagane składniki działają — możesz zaczynać ćwiczenia."
    else:
        pod = f"Brakuje lub nie sprawdzono {len(wymagane_brak)} wymaganych składników. Lekcje (teoria) działają zawsze; ćwiczenia wymagające środowiska — po instalacji." + ("" if S.jest_internet(2) else "  Brak połączenia z internetem: instalacja poczeka, czytanie lekcji i ćwiczenia offline działają.")
    M.etykieta(k, pod, 10, bold=True, kolor=K["ziel"] if not wymagane_brak else K["pomar"], wrap=860).pack(fill="x", pady=(0, 8))
    for p in diag:
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x", pady=2)
        tlo, fg = KOLORY.get(p["status"], ("jasny", "szary"))
        M.plakietka(r, p["status"], K[tlo], K[fg]).pack(side="left")
        M.etykieta(r, "  " + p["nazwa"], 10, bold=p.get("wymagane", False)).pack(side="left")
        if p.get("szczegoly"):
            M.etykieta(k, "      " + p["szczegoly"], 9, kolor=K["szary"], wrap=840).pack(fill="x")


def _ustaw_log(app, ostatnie=40):
    st = _stan(app)
    t = st.get("log_txt")
    if not t or not t.winfo_exists():
        return
    t.configure(state="normal")
    t.delete("1.0", "end")
    t.insert("1.0", "\n".join(st["log"][-ostatnie:]) if st["log"] else "Log pojawi się tutaj (pełny zapis: " + str(st["sr"].log) + ")")
    t.see("end")
    t.configure(state="disabled")


def _dodaj_log(app, tekst):
    st = _stan(app)
    st["log"].append(tekst)
    _ustaw_log(app)


# ============================================================ diagnoza w tle
def _diagnozuj(app, odswiez=False):
    st = _stan(app)
    if st.get("w_toku"):
        return
    st["w_toku"] = "diagnoza"
    st["diag"] = None if odswiez else st.get("diag")
    st["odswiez"] = True
    sr = st["sr"]
    tydz = app.stan.biezacy_tydzien()
    wynik = {}

    def praca():
        try:
            wynik["diag"] = sr._odswiez_stan(tydz)     # diagnoza + zapis stanu (gotowe, tydzień, Python bazowy) w jednym miejscu
        except Exception as e:  # noqa: BLE001
            wynik["blad"] = f"{type(e).__name__}: {e}"

    t = threading.Thread(target=praca, daemon=True)
    t.start()
    _rysuj_tabele(app)

    def czekaj():
        if t.is_alive():
            app.after(200, czekaj)
            return
        st["w_toku"] = None
        if wynik.get("blad"):
            st["diag"] = [{"klucz": "blad", "nazwa": "Diagnoza", "status": S.BLAD, "szczegoly": wynik["blad"], "wymagane": True}]
        else:
            st["diag"] = wynik.get("diag", [])
        if app.aktywny == "srodowisko":
            _rysuj_tabele(app)
    app.after(200, czekaj)


# ============================================================ instalacja / testy w tle
def _potwierdz_plan(app, kroki, tytul):
    """Ekran potwierdzenia: lista zmian, źródła, rozmiary, internet, uprawnienia. Zwraca True po zgodzie."""
    M = _M()
    K = M.K
    okno = tk.Toplevel(app)
    okno.title(tytul)
    okno.configure(bg=K["tlo"])
    okno.transient(app)
    okno.grab_set()
    szer = min(900, app.winfo_width() - 60)
    tk.Label(okno, text=tytul, font=M.czc(13, "bold"), bg=K["tlo"], fg=K["tekst"]).pack(anchor="w", padx=18, pady=(14, 4))
    tk.Label(okno, text="Mentor wykona tylko poniższe kroki — nic z paczki kursu nie jest uruchamiane. Wszystko instaluje się w katalogu użytkownika, bez uprawnień administratora.",
             font=M.czc(9), bg=K["tlo"], fg=K["szary"], wraplength=szer, justify="left").pack(anchor="w", padx=18)
    ramka = tk.Frame(okno, bg=K["karta"], highlightbackground=K["ramka"], highlightthickness=1)
    ramka.pack(fill="both", expand=True, padx=18, pady=10)
    for i, kr in enumerate(kroki, 1):
        tk.Label(ramka, text=f"{i}. {kr['opis']}", font=M.czc(10, "bold"), bg=K["karta"], fg=K["tekst"], wraplength=szer - 40, justify="left", anchor="w").pack(fill="x", padx=12, pady=(8, 0))
        szcz = f"źródło: {kr['zrodlo']}   ·   rozmiar: {kr['rozmiar']}   ·   internet: {'tak' if kr['internet'] else 'nie'}   ·   uprawnienia: {kr['uprawnienia']}"
        if kr.get("sha256"):
            szcz += f"\nSHA-256 (przypięta w Mentorze, weryfikowana po pobraniu): {kr['sha256']}"
        tk.Label(ramka, text=szcz, font=M.czc(9), bg=K["karta"], fg=K["szary"], wraplength=szer - 40, justify="left", anchor="w").pack(fill="x", padx=24, pady=(0, 4))
    wynik = {"ok": False}
    r = tk.Frame(okno, bg=K["tlo"])
    r.pack(fill="x", padx=18, pady=(0, 14))

    def tak():
        wynik["ok"] = True
        okno.destroy()
    M.przycisk(r, "Zgadzam się — wykonaj", tak, "glowny").pack(side="left")
    M.przycisk(r, "Anuluj", okno.destroy, "drugi").pack(side="left", padx=8)
    okno.update_idletasks()
    okno.geometry(f"+{app.winfo_rootx() + 60}+{app.winfo_rooty() + 60}")
    app.wait_window(okno)
    return wynik["ok"]


def _start_worker(app, kroki_id, etykieta):
    st = _stan(app)
    sr = st["sr"]
    st["kolejka"] = queue.Queue()
    st["anuluj"] = threading.Event()
    st["w_toku"] = "instalacja"
    st["ostatnie_kroki"] = list(kroki_id)
    st["krok_tekst"] = etykieta
    st["pasek_wartosc"] = 0
    st["blad"] = None
    if st.get("krok_lbl") and st["krok_lbl"].winfo_exists():
        st["krok_lbl"].configure(text=etykieta)
    tydz = app.stan.biezacy_tydzien()
    st["watek"] = threading.Thread(target=sr.instaluj, args=(kroki_id, st["kolejka"], st["anuluj"], tydz), daemon=True)
    st["watek"].start()
    _poll(app)


def _poll(app):
    st = _stan(app)
    st["poll"] = True
    q = st.get("kolejka")
    koniec = False
    try:
        while q is not None:
            m = q.get_nowait()
            rodzaj = m[0]
            if rodzaj == "log":
                _dodaj_log(app, m[1])
            elif rodzaj == "krok":
                st["krok_tekst"] = f"{m[1]}: {m[2]}" + (f" — {m[3]}" if len(m) > 3 and m[3] else "")
                if st.get("krok_lbl") and st["krok_lbl"].winfo_exists():
                    st["krok_lbl"].configure(text=st["krok_tekst"])
            elif rodzaj == "postep":
                _, kid, ulamek, tekst = m
                st["krok_tekst"] = f"{kid}: {tekst}"
                if st.get("krok_lbl") and st["krok_lbl"].winfo_exists():
                    st["krok_lbl"].configure(text=st["krok_tekst"])
                if st.get("pasek") and st["pasek"].winfo_exists():
                    if ulamek is None:
                        st["pasek_wartosc"] = (st.get("pasek_wartosc", 0) + 3) % 100
                    else:
                        st["pasek_wartosc"] = int(ulamek * 100)
                    st["pasek"].configure(value=st["pasek_wartosc"])
            elif rodzaj == "test":
                _dodaj_log(app, f"TEST {m[1]}: {m[2]} — {m[3]}")
            elif rodzaj == "koniec":
                koniec = True
                wynik = m[1]
                st["w_toku"] = None
                st["blad"] = wynik["bledy"][0] if wynik["bledy"] else None
                st["pasek_wartosc"] = 100 if wynik["ok"] else st.get("pasek_wartosc", 0)
                st["krok_tekst"] = "Zakończono: " + ("wszystkie kroki wykonane." if wynik["ok"] else "przerwano z błędem — " + (st["blad"] or "")[:200] + "  (Ponów, gdy usuniesz przyczynę.)")
                if st.get("krok_lbl") and st["krok_lbl"].winfo_exists():
                    st["krok_lbl"].configure(text=st["krok_tekst"])
                if st.get("pasek") and st["pasek"].winfo_exists():
                    st["pasek"].configure(value=st["pasek_wartosc"])
                st["diag"] = st["sr"].stan().get("diagnoza") or st.get("diag")
                if app.aktywny == "srodowisko":
                    _rysuj_tabele(app)
    except queue.Empty:
        pass
    if koniec or not (st.get("watek") and st["watek"].is_alive()):
        st["poll"] = False
        if st.get("w_toku") == "instalacja":
            st["w_toku"] = None
        return
    app.after(150, lambda: _poll(app))


def _instaluj(app):
    st = _stan(app)
    if st.get("w_toku"):
        messagebox.showinfo("Środowisko", "Trwa inna operacja — poczekaj na jej zakończenie albo anuluj.", parent=app)
        return
    sr = st["sr"]
    diag = st.get("diag") or sr.diagnoza(app.stan.biezacy_tydzien())
    plan = sr.plan(diag)
    wykonywalne = [k for k in plan if not k["id"].startswith("info_") and k["id"] != "python_recznie"]
    if not wykonywalne:
        info = "\n".join("• " + k["opis"] for k in plan) or "Wszystko jest już zainstalowane."
        messagebox.showinfo("Środowisko", "Nie ma nic do zainstalowania automatycznie.\n\n" + info, parent=app)
        return
    if not _potwierdz_plan(app, plan, "Zainstaluj brakujące — co dokładnie się stanie"):
        return
    _start_worker(app, [k["id"] for k in wykonywalne], "Rozpoczynam instalację…")


def _testuj(app):
    st = _stan(app)
    if st.get("w_toku"):
        return
    sr = st["sr"]
    if not sr.python_venv():
        messagebox.showinfo("Sprawdź działanie", "Najpierw zainstaluj środowisko (przycisk „Zainstaluj brakujące”).", parent=app)
        return
    kroki = [{"id": "testy", "opis": "Testy końcowe: " + ", ".join(n for _, n in sr.lista_testow()), "zrodlo": "procesy lokalne w środowisku kursu; Selenium może pobrać sterownik przeglądarki (Selenium Manager)",
              "rozmiar": "—", "internet": any(t == "selenium" for t, _ in sr.lista_testow()), "uprawnienia": "brak"}]
    if not _potwierdz_plan(app, kroki, "Sprawdź działanie — uruchomię testy w środowisku kursu"):
        return
    _start_worker(app, ["testy"], "Uruchamiam testy…")


def _napraw(app):
    st = _stan(app)
    if st.get("w_toku"):
        return
    sr = st["sr"]
    if not messagebox.askyesno("Napraw środowisko", f"Usunę środowisko kursu:\n{sr.venv}\n\ni utworzę je od nowa (Python, biblioteki, testy). Twoje pliki w katalogu PRACA i postępy zostają bez zmian. Kontynuować?", parent=app):
        return
    sr.usun_srodowisko()
    st["diag"] = None
    diag = sr.diagnoza(app.stan.biezacy_tydzien())
    plan = [k for k in sr.plan(diag) if not k["id"].startswith("info_") and k["id"] != "python_recznie"]
    if not _potwierdz_plan(app, plan, "Napraw środowisko — co się stanie"):
        _diagnozuj(app, True)
        return
    _start_worker(app, [k["id"] for k in plan], "Naprawiam środowisko…")


def _usun_srodowisko(app):
    st = _stan(app)
    if st.get("w_toku"):
        return
    sr = st["sr"]
    if messagebox.askyesno("Usuń środowisko", f"Usunąć środowisko kursu (.venv i wyniki testów)?\n{sr.katalog}\n\nNIE usuwa plików ucznia (PRACA) ani postępów. Można je potem zainstalować ponownie.", parent=app):
        sr.usun_srodowisko()
        st["diag"] = None
        _diagnozuj(app, True)


def _usun_kurs(app):
    st = _stan(app)
    if st.get("w_toku"):
        return
    kid = P.id
    praca = paczki.katalog_pracy(kid)
    pyt = (f"Usunąć kurs „{P.nazwa}” ({kid}) z Mentora?\n\nUsunięte zostaną: pliki kursu z paczki i środowisko .venv.\n"
           f"ZOSTANĄ: Twoje pliki w {praca} oraz postępy (możesz zaimportować kurs ponownie).\n\nKontynuować?")
    if not messagebox.askyesno("Usuń kurs", pyt, parent=app):
        return
    usun_prace = messagebox.askyesno("Usuń kurs", f"Czy usunąć TAKŻE Twój katalog roboczy?\n{praca}\n\n„Nie” = pliki zostają (zalecane).", parent=app, default="no")
    paczki.usun_kurs(kid, usun_prace=usun_prace, usun_srodowisko=True)
    app._srod = {}
    from program import domyslna_sciezka
    sc = domyslna_sciezka()
    if sc:
        app.ustaw_program(sc)
    else:
        app.pokaz("ustawienia")


def _anuluj(app):
    st = _stan(app)
    if st.get("anuluj") and st.get("watek") and st["watek"].is_alive():
        st["anuluj"].set()
        _dodaj_log(app, "Anulowanie — czekam na zatrzymanie bieżącego kroku…")
    else:
        messagebox.showinfo("Anuluj", "Nic nie jest teraz wykonywane.", parent=app)


def _ponow(app):
    st = _stan(app)
    if st.get("w_toku"):
        return
    if not st.get("ostatnie_kroki"):
        _instaluj(app)
        return
    _start_worker(app, st["ostatnie_kroki"], "Ponawiam…")


def _pokaz_log(app):
    M = _M()
    K = M.K
    st = _stan(app)
    sr = st["sr"]
    okno = tk.Toplevel(app)
    okno.title("Szczegóły — log środowiska")
    okno.configure(bg=K["tlo"])
    okno.geometry("900x560")
    t = tk.Text(okno, font=M.czc(9, mono=True), bg=K["jasny"], fg=K["tekst"], relief="flat", padx=10, pady=8, wrap="none")
    sb = ttk.Scrollbar(okno, orient="vertical", command=t.yview)
    t.configure(yscrollcommand=sb.set)
    sb.pack(side="right", fill="y")
    t.pack(fill="both", expand=True)
    try:
        tekst = Path(sr.log).read_text(encoding="utf-8", errors="replace")
    except OSError:
        tekst = "(log jeszcze nie istnieje)"
    t.insert("1.0", tekst[-200_000:])
    t.see("end")
    t.configure(state="disabled")
    r = tk.Frame(okno, bg=K["tlo"])
    r.pack(fill="x")
    M.przycisk(r, "Otwórz folder logów", lambda: app._otworz_folder(str(KATALOG_LOGOW)), "drugi").pack(side="left", padx=10, pady=8)
    M.przycisk(r, "Zamknij", okno.destroy, "drugi").pack(side="left", pady=8)
