# -*- coding: utf-8 -*-
"""Przykładowy test pytest uruchamiany w środowisku kursu — sprawdza, że pytest naprawdę działa (zbiera i wykonuje testy)."""


def dodaj(a, b):
    return a + b


def test_dodawanie():
    assert dodaj(2, 3) == 5


def test_napisy():
    assert "Mentor".lower() == "mentor"
