# -*- coding: utf-8 -*-
"""Kontrola weryfikatorów kursu: każdy test z WERYFIKATORY musi PRZECHODZIĆ na rozwiązaniach wzorcowych (wzorce/)
i NIE przechodzić na pustym katalogu oraz na plikach startowych (startowe/) i zapisach agenta z błędem (odpowiedzi_agenta/).

Uruchom:  python sprawdz_weryfikatory.py      (używane też przez testy/test_kurs_python.py)
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TU = Path(__file__).resolve().parent
WER = TU / "weryfikatory"


def zloz_test(nazwa):
    """Treść pliku testu z paczki: wspólny początek + właściwe testy (test działa jako jeden plik).
    Linia „# wzorce: a.py, b.py” na początku testu wkleja słownik WZORZEC {nazwa: kod} z rozwiązań wzorcowych — do testów mutacyjnych."""
    t = (WER / nazwa).read_text(encoding="utf-8")
    wstawka = ""
    pierwsza = t.splitlines()[0] if t else ""
    if pierwsza.startswith("# wzorce:"):
        pliki = [x.strip() for x in pierwsza.split(":", 1)[1].split(",") if x.strip()]
        wstawka = "WZORZEC = " + repr({f: (TU / "wzorce" / f).read_text(encoding="utf-8") for f in pliki}) + "\n\n"
    return (WER / "_wspolne.py").read_text(encoding="utf-8") + "\n\n" + wstawka + t


def testy():
    return sorted(p.name for p in WER.glob("test_t*.py"))


def _git(ws, *a):
    env = dict(os.environ, GIT_AUTHOR_NAME="Kursant", GIT_AUTHOR_EMAIL="kursant@example.com", GIT_COMMITTER_NAME="Kursant", GIT_COMMITTER_EMAIL="kursant@example.com")
    subprocess.run(["git", "-C", str(ws), *a], check=True, capture_output=True, env=env)


def przygotuj_wzorzec(cel):
    """Kopia wzorców jako repozytorium Git z historią jak u kursanta: commity z opisami, scalona gałąź feature/tydzien4, origin na GitHubie."""
    cel = Path(cel)
    shutil.copytree(TU / "wzorce", cel, dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__"))
    _git(cel, "init", "-q", "-b", "main")
    _git(cel, "add", ".gitignore", "hello.py", "README.md"); _git(cel, "commit", "-q", "-m", "Dodaj hello.py i README")
    nowe = subprocess.run(["git", "-C", str(cel), "ls-files", "--others", "--exclude-standard"], capture_output=True, text=True, check=True).stdout.split()
    pozostale = sorted(x for x in nowe if x != "TYDZIEN4.md")
    for i in range(0, len(pozostale), 5):
        _git(cel, "add", *pozostale[i:i + 5]); _git(cel, "commit", "-q", "-m", f"Dodaj programy z kursu (część {i // 5 + 1})")
    _git(cel, "switch", "-q", "-c", "feature/tydzien4")
    _git(cel, "add", "TYDZIEN4.md"); _git(cel, "commit", "-q", "-m", "Dodaj podsumowanie tygodnia 4")
    _git(cel, "switch", "-q", "main")
    _git(cel, "merge", "-q", "--no-ff", "feature/tydzien4", "-m", "Merge pull request #1 from kursant/feature/tydzien4")
    shas = subprocess.run(["git", "-C", str(cel), "log", "--format=%h", "-n", "3"], capture_output=True, text=True, check=True).stdout.split()
    (cel / "RECENZJA.md").write_text("# Recenzja projektu jak senior tester\n\n" + "".join(
        f"## Uwaga {i}: {u}\nDecyzja: wdrażam — commit {sha}.\n\n" for i, (u, sha) in enumerate(zip(
            ["hasło w kodzie konfiguracji", "brak testu wydania całego stanu", "time.sleep w testach E2E"], shas), 1)), encoding="utf-8")
    _git(cel, "add", "RECENZJA.md"); _git(cel, "commit", "-q", "-m", "Dodaj RECENZJA.md z decyzjami po przeglądzie")
    _git(cel, "remote", "add", "origin", "https://github.com/kursant/nauka-python.git")
    _git(cel, "update-ref", "refs/remotes/origin/main", "HEAD")
    return cel


def uruchom(test, ws, wybor=None, python=sys.executable):
    """(kod, wyjście) uruchomienia testu z paczki tak, jak robi to Mentor (kopia w osobnym katalogu, MENTOR_WORKSPACE)."""
    with tempfile.TemporaryDirectory(prefix="wer_") as td:
        (Path(td) / test).write_text(zloz_test(test), encoding="utf-8")
        args = [python, "-X", "utf8", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--rootdir", td, "-o", "addopts=", test]
        if wybor:
            args += ["-k", wybor]
        env = dict(os.environ, MENTOR_WORKSPACE=str(ws), PYTHONDONTWRITEBYTECODE="1")
        p = subprocess.run(args, cwd=td, capture_output=True, text=True, env=env, timeout=300)
        return p.returncode, p.stdout + p.stderr


def wybory_zadan():
    """[(id_zadania, plik_testu, wybor)] ze wszystkich zadań kursu."""
    sys.path.insert(0, str(TU))
    import zadania_wszystkie
    out = []
    for z in zadania_wszystkie.ZADANIA:
        spr = (z.get("cwiczenie") or {}).get("sprawdzenie") or {}
        if spr.get("rodzaj") == "test_zewnetrzny":
            out.append((z["id"], spr["plik_testu"].split("/")[-1], spr.get("wybor")))
    return out


def kod_z_md(md):
    m = re.search(r"```python\n(.*?)```", md, re.S)
    return m.group(1) if m else None


def kontrola(log=print, python=sys.executable):
    bledy = []
    with tempfile.TemporaryDirectory(prefix="wzorzec_") as td, tempfile.TemporaryDirectory(prefix="pusty_") as pusty:
        ws = przygotuj_wzorzec(Path(td) / "PRACA")
        for zid, test, wyb in wybory_zadan():
            k, out = uruchom(test, ws, wyb, python=python)
            if k != 0 or "passed" not in out:
                bledy.append(f"{zid}: {test} -k {wyb} NIE przechodzi na wzorcu:\n{out[-1500:]}")
            k, out = uruchom(test, pusty, wyb, python=python)
            if k == 0:
                bledy.append(f"{zid}: {test} -k {wyb} przechodzi na PUSTYM katalogu")
            if "deselected" in out and "passed" not in out and "failed" not in out and "error" not in out:
                bledy.append(f"{zid}: {test} -k {wyb} nie wybiera żadnego testu")
        # pliki startowe z błędami i zapisy agenta z celowym błędem — test musi je złapać
        for zid, test, wyb, plik_ucznia, kod in zapisy_z_bledem():
            with tempfile.TemporaryDirectory(prefix="blad_") as tb:
                shutil.copytree(ws, tb, dirs_exist_ok=True)
                (Path(tb) / plik_ucznia).write_text(kod, encoding="utf-8")
                k, out = uruchom(test, tb, wyb, python=python)
                if k == 0:
                    bledy.append(f"{zid}: plik z celowym błędem ({plik_ucznia}) PRZECHODZI test {test} -k {wyb}")
    for b in bledy:
        log("BŁĄD " + b)
    return bledy


def zapisy_z_bledem():
    """Pliki startowe (startowe/*.py) i zapisy agenta (odpowiedzi_agenta/*.md) — każdy zawiera błąd, który test musi wykryć."""
    zad = {z[0]: z for z in wybory_zadan()}
    sys.path.insert(0, str(TU))
    import zadania_wszystkie
    plik_zad = {z["id"]: z["cwiczenie"]["plik"] for z in zadania_wszystkie.ZADANIA if z.get("cwiczenie")}
    out = []
    for p in sorted((TU / "startowe").glob("*.py")):
        for zid, pl in plik_zad.items():
            if pl == p.name and zid in zad:
                out.append((zid, zad[zid][1], zad[zid][2], pl, p.read_text(encoding="utf-8")))
    for p in sorted((TU / "odpowiedzi_agenta").glob("*.md")) if (TU / "odpowiedzi_agenta").exists() else []:
        zid = p.stem
        kod = kod_z_md(p.read_text(encoding="utf-8"))
        assert kod and zid in zad, f"odpowiedzi_agenta/{p.name}: brak bloku ```python albo zadania {zid} z testem"
        out.append((zid, zad[zid][1], zad[zid][2], plik_zad[zid], kod))
    return out


if __name__ == "__main__":
    b = kontrola()
    print("OK — wszystkie weryfikatory spójne" if not b else f"{len(b)} błędów")
    sys.exit(1 if b else 0)
