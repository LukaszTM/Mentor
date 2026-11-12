# Format programu nauczania (`mentor-program/1`)

Program to jeden plik `.json` w folderze `programy/`. Mentor wczytuje go przy starcie (Ustawienia → Program nauczania →
Przełącz / Wgraj program z pliku…). Postępy każdego programu są zapisywane osobno.

Najszybszy start: Ustawienia → „Zapisz pusty szablon programu” → otwórz `moj-program.json` w PyCharm → wypełnij → „Wgraj program z pliku…”.
Wolisz Python zamiast JSON? Skopiuj `programy/zrodla/python_junior_qa/`, zmień treści, uruchom `zbuduj.py`.

## Pola obowiązkowe

| Pole | Co to |
|---|---|
| `nazwa` | Nazwa programu (pasek boczny, Panel, eksport) |
| `etapy` | Lista `{nr, nazwa, tygodnie: [numery], cel}` — etapy grupują tygodnie; każdy ukończony etap = odznaka |
| `tygodnie` | Lista tygodni (poniżej) |
| `lekcje` | Lista lekcji (poniżej) |

## Tydzień

```json
{"tydzien": 1, "etap": 0, "tytul": "Zmienne, typy, warunki",
 "tematy": "jedno zdanie z listą tematów",
 "rola_asystenta": "co asystent AI może robić w tym tygodniu",
 "lekcje": ["zmienne", "warunki"],
 "zadania": [ ...zadania... ]}
```

Zadania 1–4 Mentor pokazuje jako pon–czw, ostatnie jako „zadanie tygodnia” (piątek). Może być inna liczba zadań.

## Zadanie

```json
{"id": "t1z1", "tytul": "zmienne.py — 5 zmiennych różnych typów",
 "opis": "jedno zdanie: co ma powstać",
 "kroki": ["Krok 1 — konkretnie: co kliknąć, co wpisać, jaką komendę.", "Krok 2…"],
 "sprawdz": "jak uczeń sam sprawdza, że gotowe",
 "problemy": ["typowy problem → co zrobić"],
 "pliki": ["zmienne.py"],
 "xp": 10, "czas_min": 60}
```

- `kroki` — pełna instrukcja; linie zaczynające się od `git `, `python`, `pip `, `cd `, `print(` itd. są wyświetlane jako kod.
- `pliki` — nazwy plików, których istnienie w katalogu projektu Mentor wykrywa (podpowiedź, nie zaliczenie).
- `id` musi być unikalne w całym programie (to klucz postępów).

## Lekcja

```json
{"id": "zmienne", "tydzien": 1, "nazwa": "Zmienne i typy danych",
 "slowa": ["zmienn", "typ", "int", "float"],
 "wyjasnienie": "2–4 akapity (\\n rozdziela akapity)",
 "przyklad": "kod lub przykład krok po kroku",
 "zadania": ["łatwe", "średnie", "trudniejsze"],
 "pytania": [["pytanie otwarte?", "wzorcowa odpowiedź"]],
 "pulapki": ["na co uważać"],
 "test": [{"p": "pytanie?", "o": ["A", "B", "C", "D"], "odp": 1, "w": "wyjaśnienie"}]}
```

- `slowa` — po nich Asystent Offline rozpoznaje temat w promptach („uczę się zmiennych”).
- `test` — 3–4 pytania zamknięte; używane w zakładce Lekcje („Sprawdź się”) i przy ręcznym wpisie czasu nauki
  (uczeń wybiera temat = lekcję i odpowiada na pytania z jej testu). `odp` to indeks poprawnej odpowiedzi od 0.

## Pola opcjonalne (z wartościami domyślnymi)

| Pole | Co to |
|---|---|
| `podtytul`, `opis`, `autor`, `wersja` | metadane |
| `katalog_projektu` | sugerowana nazwa katalogu projektu |
| `czas_dziennie_min` | orientacyjny czas dzienny |
| `zasady` | lista zasad nauki (tekst) |
| `quizy` | `{"0": [pytania jak w test], "1": [...]}` — quiz tygodnia (klucz = numer tygodnia jako tekst) |
| `rytm_dnia` | fazy sesji `{nazwa, minuty, ikona, opis, prompt}` — domyślnie 20/50/15/5 |
| `prompty` | szablony `{nazwa, kiedy, tresc}` do Asystenta |
| `claude_md` | treść pliku CLAUDE.md tworzonego w projekcie |
| `szablony` | `{"klucz": "tekst"}` albo `{"klucz": {"nazwa", "kiedy", "tresc"}}` — każdy pokazuje się w zakładce Prompty |
| `stanowisko` | nazwa roli docelowej (np. „Junior QA”) — nagłówek próbnej rozmowy rekrutacyjnej w Asystencie |
| `stan_prawny` / `firma` | dowolne metadane programu (np. „listopad 2026”, opis firmy ćwiczeniowej) |
| `checklista` | `[{po: "Po etapie 1", punkty: ["..."]}]` |
| `sciaga` | `[{tytul, pozycje: [["komenda", "co robi"]]}]` |
| `linki` | `[["nazwa", "https://..."]]` |
| `wskazowki`, `motywacja_powrot` | teksty na Panel |
| `pojecia` | `{"terminal": "definicja"}` — dla Asystenta Offline („co to jest…”) |
| `bledy` | `{"TypeError": {co, pytanie}}` — tłumaczenie błędów; brak = wbudowany słownik błędów Pythona |
| `pytania_rekrutacyjne` | `[["kategoria", "pytanie", "wzorzec"]]` — dla `/rekrutacja` |

Walidacja: program z brakującym polem obowiązkowym, powtórzonym `id` zadania, lekcją bez `id`/`nazwa`/`wyjasnienie`
lub pytaniem z błędnym `odp` nie zostanie wczytany — Mentor wypisze, co poprawić.
