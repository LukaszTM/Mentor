import pytest

from system import create_app


@pytest.fixture
def k():
    return create_app(":memory:").test_client()


def r(**z):
    d = {"gosc": "Anna", "email": "anna@pod-lipa.pl", "pokoj": "Lipowy", "od": "2026-12-20", "do": "2026-12-23"}
    d.update(z)
    return d


def test_strona(k):
    assert "Pod Lipą" in k.get("/").get_data(as_text=True)


def test_zapis(k):
    assert k.post("/api/rezerwacje", json=r()).status_code == 201


def test_koszt_grudzien(k):
    assert k.post("/api/rezerwacje", json=r()).get_json()["koszt"] == 540


def test_koszt_przelom_miesiaca(k):
    assert k.post("/api/rezerwacje", json=r(od="2026-11-30", do="2026-12-02")).get_json()["koszt"] == 320


def test_zly_email(k):
    assert k.post("/api/rezerwacje", json=r(email="anna@")).status_code == 400


def test_zly_pokoj(k):
    assert k.post("/api/rezerwacje", json=r(pokoj="Brzozowy")).status_code == 400


def test_zle_daty(k):
    assert k.post("/api/rezerwacje", json=r(od="2026-12-23", do="2026-12-20")).status_code == 400


def test_kolizja(k):
    k.post("/api/rezerwacje", json=r())
    assert k.post("/api/rezerwacje", json=r(od="2026-12-21", do="2026-12-22")).status_code == 409


def test_wyjazd_przyjazd(k):
    k.post("/api/rezerwacje", json=r())
    assert k.post("/api/rezerwacje", json=r(od="2026-12-23", do="2026-12-25")).status_code == 201


def test_lista_bez_email(k):
    k.post("/api/rezerwacje", json=r())
    assert all("email" not in x for x in k.get("/api/rezerwacje").get_json())


def test_usuwanie(k):
    i = k.post("/api/rezerwacje", json=r()).get_json()["id"]
    assert k.delete(f"/api/rezerwacje/{i}").status_code == 204
    assert k.delete(f"/api/rezerwacje/{i}").status_code == 404


def test_wolne(k):
    k.post("/api/rezerwacje", json=r())
    assert k.get("/api/wolne?od=2026-12-21&do=2026-12-22").get_json()["wolne"] == ["Dębowy", "Klonowy"]
