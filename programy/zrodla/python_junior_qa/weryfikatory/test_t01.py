# Weryfikator tygodnia 1 — kalkulator.py, wiek.py, rabat.py, bmi.py (program uruchamiany z danymi dla input()).
import datetime as _dt


def test_kalkulator():
    for dane, ocz in (("8\n+\n2\n", "10"), ("7\n/\n2\n", "3.5"), ("6\n*\n2.5\n", "15"), ("3\n-\n10\n", "-7")):
        kod, out = uruchom("kalkulator.py", dane)
        bez_bledu(kod, out, dane)
        zawiera(out, ocz, dane=dane)
    kod, out = uruchom("kalkulator.py", "5\n/\n0\n")
    bez_bledu(kod, out, "5 / 0")
    zawiera(out, "zero", dane="5 / 0 (komunikat o dzieleniu przez zero)")
    kod, out = uruchom("kalkulator.py", "5\n%\n2\n")
    bez_bledu(kod, out, "5 % 2")
    zawiera(out, "nieznane", dane="5 % 2 (komunikat „Nieznane działanie”)")


def test_wiek():
    rok = _dt.date.today().year
    for ur, wiek, kat in ((rok - 30, 30, "pełnoletni"), (rok - 18, 18, "pełnoletni"), (rok - 17, 17, "niepełnoletni"), (rok - 5, 5, "niepełnoletni")):
        kod, out = uruchom("wiek.py", f"{ur}\n")
        bez_bledu(kod, out, ur)
        zawiera(out, str(wiek), kat, dane=ur)
        if kat == "pełnoletni":
            assert "niepelnoletn" not in norm(out), f"dla roku {ur} (wiek {wiek}) program wypisał „niepełnoletni” — sprawdź warunek >= 18"
    kod, out = uruchom("wiek.py", f"{rok + 1}\n")
    bez_bledu(kod, out, rok + 1)
    zawiera(out, "przyszłości", dane=f"{rok + 1} (rok z przyszłości)")


def test_rabat():
    for kwota, proc, zaplata in (("99.99", "0%", "99.99"), ("100", "5%", "95.00"), ("299.99", "5%", "284.99"), ("300", "10%", "270.00"), ("1000", "10%", "900.00")):
        kod, out = uruchom("rabat.py", kwota + "\n")
        bez_bledu(kod, out, kwota)
        zawiera(out, proc, zaplata, dane=kwota)
    kod, out = uruchom("rabat.py", "-5\n")
    bez_bledu(kod, out, "-5")
    zawiera(out, "ujemna", dane="-5 (komunikat: kwota nie może być ujemna)")


def test_bmi():
    for dane, bmi, kat in (("1.80\n81\n", "25.0", "nadwaga"), ("1.70\n50\n", "17.3", "niedowaga"), ("1.75\n70\n", "22.9", "norma"), ("1.60\n80\n", "31.2", "otyłość"),
                           ("2.00\n74\n", "18.5", "norma")):
        kod, out = uruchom("bmi.py", dane)
        bez_bledu(kod, out, dane)
        zawiera(out, bmi, kat, dane=dane)
    kod, out = uruchom("bmi.py", "0\n70\n")
    bez_bledu(kod, out, "0 i 70")
    zawiera(out, "większe od zera", dane="wzrost 0")
    kod, out = uruchom("bmi.py", "180\n80\n")
    bez_bledu(kod, out, "180 i 80")
    zawiera(out, "metrach", dane="wzrost 180 (w centymetrach)")
