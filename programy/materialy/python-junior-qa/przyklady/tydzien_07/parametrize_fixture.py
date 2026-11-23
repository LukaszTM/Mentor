# test_menedzer_demo.py — python -m pytest -v test_menedzer_demo.py
import json
import pytest


def kategoria_bmi(bmi):
    if bmi < 18.5:
        return "niedowaga"
    if bmi < 25:
        return "norma"
    if bmi < 30:
        return "nadwaga"
    return "otyłość"


@pytest.mark.parametrize("bmi, oczekiwana", [
    (18.4, "niedowaga"), (18.5, "norma"), (24.9, "norma"),
    (25, "nadwaga"), (29.9, "nadwaga"), (30, "otyłość"),
])
def test_kategoria_bmi(bmi, oczekiwana):
    assert kategoria_bmi(bmi) == oczekiwana


@pytest.fixture
def zadania():
    return [{"tytul": "Zamówić papier", "zrobione": False}, {"tytul": "Policzyć zeszyty", "zrobione": True}]


def test_otwarte(zadania):
    assert [z["tytul"] for z in zadania if not z["zrobione"]] == ["Zamówić papier"]


def test_zapis_i_odczyt(zadania, tmp_path):
    plik = tmp_path / "zadania.json"
    plik.write_text(json.dumps(zadania, ensure_ascii=False), encoding="utf-8")
    assert json.loads(plik.read_text(encoding="utf-8")) == zadania
