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

- `cel` (zalecane) — jedno zdanie „po tej lekcji potrafisz…”; wyświetlane na górze lekcji.
- `czas_min` — orientacyjny czas lekcji; `w_praktyce` — lista kroków „jak to robisz naprawdę” (osobna karta).
- W `wyjasnienie` linia zaczynająca się od `## ` to nagłówek sekcji, od `- ` — punkt listy, od `|` — wiersz tabeli Markdown (`| a | b |`, wiersz `|---|---|` pomijany; w aplikacji renderowana jako siatka, w Asystencie offline jako lista); `\n` rozdziela akapity.
- Pierwsza lekcja na liście jest traktowana jako **wprowadzająca** (Panel → „Pierwsze kroki”, przewodnik „Jak zacząć”) — opisz w niej, jak uczyć się z programu.
- `slowa` — po nich Asystent Offline rozpoznaje temat w promptach („uczę się zmiennych”; odmiana słów jest tolerowana).
- `test` — 3–4 pytania zamknięte; używane w zakładce Lekcje („Sprawdź się”) i przy ręcznym wpisie czasu nauki
  (uczeń wybiera temat = lekcję i odpowiada na pytania z jej testu). `odp` to indeks poprawnej odpowiedzi od 0.

### Bloki standardu lekcji (`programy/STANDARD_KURSOW.md` §3) — zalecane, renderowane, gdy są

```json
{"po_co": "jedno zdanie — zastosowanie w prawdziwym projekcie",
 "wymagania": ["czego uczeń potrzebuje i gdzie są pliki"],
 "demonstracja": {"tytul": "…", "kroki": ["omówienie przykładu krok po kroku — co robi, dlaczego, co się zmieni"], "wynik": "oczekiwany wynik"},
 "jak_uruchomic": ["dokładna ścieżka/kliknięcia i oczekiwany wynik"],
 "cwiczenia": [
   {"rodzaj": "prowadzone", "tresc": "…", "wynik": "jak wygląda poprawny wynik", "plik": "cwiczenia/tydzien_04/id_1.md",
    "rozwiazanie_plik": "rozwiazania/tydzien_04/id_1.md",
    "wskazowki": ["1 pytanie naprowadzające", "2 gdzie szukać", "3 częściowy przykład"], "rozwiazanie": "pełne rozwiązanie (pokazywane na końcu)"},
   {"rodzaj": "samodzielne", "...": "jak wyżej — niewielka zmiana wymagająca decyzji"}],
 "typowe_bledy": [{"komunikat": "co widzi uczeń", "przyczyna": "…", "diagnoza": "jak sprawdzić", "poprawka": "…"}],
 "podsumowanie": "odpowiedź na pytanie „co potrafię teraz zrobić bez patrzenia na przykład?”"}
```

- Gdy lekcja ma `demonstracja` lub `cwiczenia`, Mentor renderuje ją w kolejności standardu: cel → po co → wymagania → 1 wyjaśnienie → 2 demonstracja
  (`przyklad` w ramce + `kroki` jako omówienie) → 3 jak uruchomić → 4/5 ćwiczenia z przyciskiem „Podpowiedź 1 z 3” → „Pokaż pełne rozwiązanie” →
  typowe błędy → pułapki → dodatkowe `zadania` → sprawdzenie (`pytania` + `podsumowanie`) → test. Bez tych bloków — układ klasyczny.
- Asystent Offline: komenda `podpowiedź` / `/podpowiedz [nr]` odkrywa kolejne `wskazowki` ćwiczenia z ostatnio otwartej lekcji, a na końcu `rozwiazanie`.
- Powtórka etapu to zwykła lekcja (np. `id: "powtorka_etap_2"`) dołączona do ostatniego tygodnia etapu, z tymi samymi blokami.

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
| `diagnoza` | lista pytań jak w `test` + `lekcja` (id) — zadanie diagnostyczne na start (Panel → Pierwsze kroki, Quiz, „Jak zacząć”); nie blokuje nauki, nie daje XP; wynik i lekcje do powtórki w `stan["diagnoza"]` |
| `pytania_dziennika` | lista pytań pomocniczych pokazywanych w zakładce Dziennik (domyślnie ogólne) |
| `materialy` | ścieżka (informacyjna) paczki materiałów; Mentor szuka jej w `programy/materialy/<id>/` i udostępnia „Skopiuj materiały kursu do katalogu projektu” (bez nadpisywania) |
| `quizy[...][i].lekcja` | id lekcji do powtórki po błędnej odpowiedzi — pokazywane na ekranie wyniku quizu |
| `poziom`, `system`, `wymagania_wstepne`, `umiejetnosci_koncowe` | metadane kursu dla START_TUTAJ.md i przewodnika (STANDARD §2) |
| `stan_prawny` / `firma` | dowolne metadane programu (np. „listopad 2026”, opis firmy ćwiczeniowej) |
| `narzedzia` | lista narzędzi Warsztatu do włączenia: `firma`, `place`, `zasilki`, `urlopy`, `czas`, `potracenia`, `zus`, `pit`, `przepisy` (zakładka Warsztat pojawia się tylko, gdy lista nie jest pusta) |
| `parametry` | parametry roku dla kalkulatorów (`minimalne`, `wypadkowa`, `prog`, `kwota_zmn`, `wspolczynnik`…; brakujące — z `kadry.DOMYSLNE`) |
| `firma_osoby` / `firma_regulaminy` | osoby firmy ćwiczeniowej (`imie, nazwisko, pesel, rodzaj, kod, od, do, etat, zasadnicze, ppk, kup, pit2, student, mlody…`) i założenia regulaminów — dla narzędzi Firma, Lista płac, eZUS |
| `przepisy` | biblioteka offline: `[{akt, art, tytul, tresc, slowa, lekcja, isap}]` |
| `checklista` | `[{po: "Po etapie 1", punkty: ["..."]}]` |
| `sciaga` | `[{tytul, pozycje: [["komenda", "co robi"]]}]` |
| `linki` | `[["nazwa", "https://..."]]` |
| `wskazowki`, `motywacja_powrot` | teksty na Panel |
| `pojecia` | `{"terminal": "definicja"}` — dla Asystenta Offline („co to jest…”) |
| `bledy` | `{"TypeError": {co, pytanie}}` — tłumaczenie błędów; brak = wbudowany słownik błędów Pythona |
| `pytania_rekrutacyjne` | `[["kategoria", "pytanie", "wzorzec"]]` — dla `/rekrutacja` |

Walidacja: program z brakującym polem obowiązkowym, powtórzonym `id` zadania, lekcją bez `id`/`nazwa`/`wyjasnienie`
lub pytaniem z błędnym `odp` nie zostanie wczytany — Mentor wypisze, co poprawić.
