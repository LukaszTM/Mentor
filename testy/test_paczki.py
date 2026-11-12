# -*- coding: utf-8 -*-
"""Import paczek ZIP: bezpieczeństwo (zip-slip, ścieżki bezwzględne, limity), stare paczki v1.1, manifest, aktualizacja z kopią."""

import json
import os
import stat
import tempfile
import zipfile
from pathlib import Path

import pytest

import paczki
import program
from program import KATALOG_KURSOW


def _zip_z_wpisami(cel, wpisy, kurs=True):
    with zipfile.ZipFile(cel, "w") as z:
        if kurs:
            z.writestr("kurs_mentor.json", json.dumps({"format": "mentor-program/1", "id": "wrogi", "nazwa": "Wrogi", "tygodnie": [], "lekcje": []}))
        for nazwa, tresc in wpisy:
            z.writestr(nazwa, tresc)
    return cel


@pytest.mark.parametrize("nazwa", ["../../evil.txt", "a/../../evil.txt", "/etc/passwd", "C:\\Windows\\evil.txt", "..\\evil.txt", "ok/\x00zero.txt"])
def test_wroga_sciezka_odrzucona(tmp_path, nazwa):
    zly = _zip_z_wpisami(tmp_path / "zly.zip", [(nazwa, "x")])
    with pytest.raises(paczki.BladPaczki):
        paczki.przejrzyj_zip(zly)
    assert not (tmp_path.parent / "evil.txt").exists()


def test_symlink_w_archiwum_odrzucony(tmp_path):
    cel = tmp_path / "sym.zip"
    with zipfile.ZipFile(cel, "w") as z:
        z.writestr("kurs_mentor.json", json.dumps({"format": "mentor-program/1", "id": "sym", "nazwa": "Sym", "tygodnie": [], "lekcje": []}))
        info = zipfile.ZipInfo("link.txt")
        info.external_attr = (stat.S_IFLNK | 0o777) << 16
        z.writestr(info, "/etc/passwd")
    with pytest.raises(paczki.BladPaczki):
        paczki.przejrzyj_zip(cel)


def test_za_duzo_plikow(tmp_path, monkeypatch):
    monkeypatch.setattr(paczki, "LIMIT_LICZBY_PLIKOW", 5)
    cel = _zip_z_wpisami(tmp_path / "duzo.zip", [(f"p{i}.txt", "x") for i in range(10)])
    with pytest.raises(paczki.BladPaczki, match="Za dużo plików"):
        paczki.przejrzyj_zip(cel)


def test_bomba_kompresji(tmp_path, monkeypatch):
    monkeypatch.setattr(paczki, "LIMIT_ROZMIARU", 1024 * 1024)
    cel = _zip_z_wpisami(tmp_path / "bomba.zip", [])
    with zipfile.ZipFile(cel, "a", zipfile.ZIP_DEFLATED) as z:
        z.writestr("zera.bin", b"\0" * (3 * 1024 * 1024))
    with pytest.raises(paczki.BladPaczki):
        paczki.przejrzyj_zip(cel)


def test_nie_zip(tmp_path):
    p = tmp_path / "nie.zip"
    p.write_text("to nie jest zip")
    with pytest.raises(paczki.BladPaczki):
        paczki.przejrzyj_zip(p)


def test_brak_pliku_kursu(tmp_path):
    cel = _zip_z_wpisami(tmp_path / "pusty.zip", [("README.md", "x")], kurs=False)
    with pytest.raises(paczki.BladPaczki, match="nie ma pliku kursu"):
        paczki.przejrzyj_zip(cel)


def test_podglad_starej_paczki_v11(zip_kursu):
    """Paczka v1.1: JSON w korzeniu + requirements.txt + .bat/.ps1 — podgląd widzi skrypty i ostrzega; wymagania z pola srodowisko/requirements."""
    z = zip_kursu("ai-dev-lab", "1.1", skrypty=True, requirements="pytest==9.2.0\nrequests\nselenium\n")
    pg = paczki.przejrzyj_zip(z)
    assert pg["id"] == "ai-dev-lab" and pg["wersja"] == "1.1"
    assert set(pg["skrypty"]) == {"install.bat", "setup.ps1"}
    assert pg["ostrzezenia"] and "NIE uruchamia" in pg["ostrzezenia"][0]
    assert pg["manifest"] is None
    assert {p["nazwa"] for p in pg["wymagania"]["pakiety"]} >= {"pytest", "requests", "selenium"}
    opis = paczki.opis_podgladu(pg)
    for fragment in ("Identyfikator", "wersja 1.1", "Wymagania", "Internet", "Uprawnienia", "skrypty"):
        assert fragment.lower() in opis.lower(), fragment


def test_import_v11_nie_uruchamia_skryptow(zip_kursu, tmp_path):
    znacznik = Path(tempfile.gettempdir()) / "mentor_test_bat.txt"
    znacznik.unlink(missing_ok=True)
    z = zip_kursu("ai-dev-lab", "1.1", skrypty=True)
    w = paczki.importuj_zip(z)
    assert w["kurs_json"].exists() and w["katalog"] == KATALOG_KURSOW / "ai-dev-lab"
    assert (w["katalog"] / "paczka" / "install.bat").exists(), "skrypt zostaje w paczce, ale nie jest wykonywany"
    assert not znacznik.exists()
    meta = json.loads((w["katalog"] / "meta.json").read_text(encoding="utf-8"))
    assert meta["skrypty_niewykonywane"] == ["install.bat", "setup.ps1"]
    assert w["praca"] and w["praca"].is_dir() and w["praca"].name == "PRACA"
    assert str(w["praca"]).startswith(os.environ["MENTOR_PRACA"])
    # katalog PRACA poza katalogiem kursu i środowiska
    assert KATALOG_KURSOW not in w["praca"].parents
    # program czyta kurs z paczki przez lista_programow
    sciezki = [sc for sc, *_ in program.lista_programow()]
    assert w["kurs_json"] in sciezki
    assert program.katalog_materialow("ai-dev-lab") == w["katalog"] / "paczka"
    paczki.usun_kurs("ai-dev-lab")
    assert not w["katalog"].exists() and w["praca"].exists(), "Usuń kurs domyślnie zostawia PRACA"


def test_import_z_manifestem(zip_kursu):
    man = {"schema": "mentor-course/1", "course_id": "kurs-man", "version": "2.0", "entrypoint": "kurs_mentor.json",
           "requirements": {"python": ">=3.11,<3.14", "python_packages_lock": "requirements.lock", "required_tools": [], "optional_tools": [{"name": "git", "from_week": 4}],
                            "browser": "edge", "browser_from_week": 8},
           "checks": [{"kind": "python_import", "module": "pytest"}]}
    z = zip_kursu("kurs-man", "2.0", manifest=man, dodatkowe={"requirements.lock": "pytest==9.2.0 \\\n    --hash=sha256:" + "a" * 64 + "\n"})
    pg = paczki.przejrzyj_zip(z)
    assert pg["manifest"]["schema"] == "mentor-course/1"
    w = pg["wymagania"]
    assert w["zrodlo"] == "manifest" and w["python"] == ">=3.11,<3.14" and w["przegladarka"] == "edge" and w["przegladarka_od_tygodnia"] == 8
    assert w["narzedzia_opcjonalne"] == [{"nazwa": "git", "od_tygodnia": 4}]
    assert [p["nazwa"] for p in w["pakiety"]] == ["pytest"], "pakiety z locka paczki"
    wyn = paczki.importuj_zip(z)
    meta = json.loads((wyn["katalog"] / "meta.json").read_text(encoding="utf-8"))
    assert meta["wersja"] == "2.0" and meta["wymagania"]["zrodlo"] == "manifest"
    paczki.usun_kurs("kurs-man")


def test_manifest_sprzeczny_z_kursem(zip_kursu):
    man = {"schema": "mentor-course/1", "course_id": "inny-id", "version": "2.0", "entrypoint": "kurs_mentor.json"}
    z = zip_kursu("kurs-x", "2.0", manifest=man)
    with pytest.raises(paczki.BladPaczki, match="Sprzeczne"):
        paczki.przejrzyj_zip(z)


def test_aktualizacja_z_kopia_i_stabilne_id(zip_kursu):
    z1 = zip_kursu("kurs-upd", "1.0")
    w1 = paczki.importuj_zip(z1)
    (w1["praca"] / "moj_plik.py").write_text("print(1)\n", encoding="utf-8")
    z2 = zip_kursu("kurs-upd", "1.1")
    with pytest.raises(paczki.BladPaczki) as e:
        paczki.importuj_zip(z2)
    assert getattr(e.value, "konflikt", None) and e.value.konflikt["istniejacy"]["wersja"] == "1.0"
    w2 = paczki.importuj_zip(z2, nadpisz=True)
    assert w2["kopia"] and w2["kopia"].is_dir() and (w2["kopia"] / "kurs.json").exists()
    meta = json.loads((w2["katalog"] / "meta.json").read_text(encoding="utf-8"))
    assert meta["wersja"] == "1.1"
    d = json.loads(w2["kurs_json"].read_text(encoding="utf-8"))
    assert d["id"] == "kurs-upd"
    assert [z["id"] for t in d["tygodnie"] for z in t["zadania"]][:3] == ["t0z1", "t0z2", "t0z3"], "identyfikatory zadań stabilne między wersjami"
    assert (w2["praca"] / "moj_plik.py").exists(), "pliki ucznia w PRACA zostają"
    paczki.usun_kurs("kurs-upd")


def test_wymagania_heurystyczne_bez_manifestu():
    d = {"format": "mentor-program/1", "id": "x", "nazwa": "X", "tygodnie": [], "lekcje": [{"id": "a", "nazwa": "pytest i selenium"}]}
    w = paczki.wymagania_kursu(d)
    assert w["zrodlo"] == "heurystyka" and {p["nazwa"] for p in w["pakiety"]} == {"pytest", "selenium"} and w["przegladarka"] == "edge"
    assert paczki.czy_wymaga_srodowiska(w)
    d2 = {"format": "mentor-program/1", "id": "y", "nazwa": "Y", "tygodnie": [], "lekcje": [{"id": "a", "nazwa": "Prawo pracy"}]}
    w2 = paczki.wymagania_kursu(d2)
    assert w2["zrodlo"] == "brak" and not paczki.czy_wymaga_srodowiska(w2)


def test_requirements_bez_pola_srodowisko(tmp_path):
    """Program bez pola „srodowisko” + requirements.txt: pakiety z requirements; spoza zaufanej listy → nieobslugiwane (bez auto-instalacji)."""
    d = {"format": "mentor-program/1", "id": "kurs-req", "nazwa": "Req", "tygodnie": [], "lekcje": []}
    w = paczki.wymagania_kursu(d, requirements_txt="pytest==9.2.0\nnumpy==2.0.0\n")
    assert w["zrodlo"] == "requirements"
    assert [p["nazwa"] for p in w["pakiety"]] == ["pytest", "numpy"]
    assert w["nieobslugiwane"] == ["numpy"]
    assert any("zaufanej listy" in u for u in w["uwagi"])
