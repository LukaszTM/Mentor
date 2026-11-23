# Sklep testowy „Papierowy Kot”

Lokalna aplikacja do ćwiczeń z kursu „Python od zera → Junior QA”: API (tydzień 5), Selenium i Page Object Model (tydzień 8), przypadki testowe i raporty błędów (tydzień 9).

## Jak uruchomić
```
python app.py
```
Adres: http://127.0.0.1:5001 · login `tester`, hasło `Test123!` · API: `/api/produkty`, `/api/produkty?kategoria=biuro`, `/api/produkty/3`.

## Strony i lokatory
| strona | elementy (id / data-test) |
|---|---|
| /logowanie | `#login`, `#haslo`, `[data-test=zaloguj]`, `[data-test=blad]` |
| /produkty | `[data-test=powitanie]`, `#promocja` (pojawia się po ok. 1,5 s), `#szukaj`, `#szukaj-btn`, `#produkty .produkt`, `#ilosc-<id>`, `#dodaj-<id>`, `[data-test=liczba-wynikow]` |
| /koszyk | `#koszyk tr.pozycja`, `[data-test=suma]`, `#kod`, `#zastosuj`, `#do-zamowienia` |
| /zamowienie | `#imie`, `#email`, `#kod_pocztowy`, `[data-test=zamawiam]`, `[data-test=komunikat]`, `[data-test=blad]` |

## Wymagania (specyfikacja sklepu)
- Login nie zależy od wielkości liter; hasło — zależy.
- Wyszukiwarka nie zależy od wielkości liter.
- Suma koszyka = Σ cena × ilość; kod KOT10 daje jednorazowo −10%.
- Do koszyka nie można dodać produktu, którego nie ma na stanie, ani więcej sztuk, niż jest na stanie.
- Kod pocztowy w formacie NN-NNN (z myślnikiem).

Sklep ma **celowo wprowadzone defekty** — znajdź je, porównując działanie ze specyfikacją powyżej.
