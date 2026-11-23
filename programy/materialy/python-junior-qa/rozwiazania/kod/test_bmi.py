import pytest

from bmi import kategoria, oblicz_bmi


@pytest.mark.parametrize("bmi, oczekiwana", [
    (18.4, "niedowaga"), (18.5, "norma"), (24.9, "norma"),
    (25, "nadwaga"), (29.9, "nadwaga"), (30, "otyłość"),
])
def test_kategoria_granice(bmi, oczekiwana):
    assert kategoria(bmi) == oczekiwana


@pytest.mark.parametrize("waga, wzrost", [(0, 1.7), (70, 0), (80, 180)])
def test_oblicz_bmi_zle_dane(waga, wzrost):
    with pytest.raises(ValueError):
        oblicz_bmi(waga, wzrost)
