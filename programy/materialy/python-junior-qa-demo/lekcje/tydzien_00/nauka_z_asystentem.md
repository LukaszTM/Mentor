# Jak uczyć się z asystentem AI, żeby to Ty umiał programować
Tydzień 0 · lekcja 5 z 16 · ≈ 40 min

**Po tej lekcji potrafisz:** piszesz prompty, które uczą (wskazówka zamiast rozwiązania), wybierasz tryb asystenta w Mentorze (Offline, API, Claude Code), sprawdzasz odpowiedzi AI i chronisz swoje dane.

**Po co mi to?** AI przyspiesza naukę albo ją zastępuje — zależy od pytania. Na rozmowie rekrutacyjnej i w pracy liczy się to, co umiesz wyjaśnić bez AI.

## Czego potrzebujesz
- Mentor → zakładka Asystent.
- Katalog PRACA (Mój projekt → Utwórz katalog roboczy).

## 1 · Wyjaśnienie od podstaw
### Trzy tryby asystenta w Mentorze
| tryb | koszt | co potrafi |
|---|---|---|
| Offline | 0 zł, bez internetu | słowniczek kursu, wyjaśnienia błędów Pythona, podpowiedzi do zadań |
| API | płatność za użycie (klucz z console.anthropic.com) | prawdziwa rozmowa z modelem, pliki przez @nazwa.py |
| Claude Code | plan Pro lub wyższy | agent w terminalu w katalogu PRACA |
Kurs przejdziesz w trybie Offline. Klucz API wpisujesz wyłącznie w Mentorze (zapis lokalny) — nigdy do pliku w repozytorium.
### Prompt, który uczy
ŹLE: „Napisz mi program kalkulator”. Dostajesz gotowy kod i niczego się nie uczysz.
DOBRZE: „Uczę się if/elif. Mój kalkulator źle dzieli przez zero — oto kod i komunikat błędu. **Nie podawaj rozwiązania**, zadaj mi pytanie naprowadzające.”
Schemat: **kontekst** (czego się uczę) + **co zrobiłem** (kod, błąd) + **czego chcę** (wskazówka / wyjaśnienie linii / przegląd) + **ograniczenie** (bez gotowca).
### Drabina pomocy
1 pytanie naprowadzające → 2 wskazanie fragmentu („zobacz linię 7”) → 3 częściowy przykład → 4 pełne rozwiązanie z omówieniem — dopiero gdy 1–3 nie pomogły.
### AI się myli
Model potrafi z pewnością podać nieistniejącą funkcję albo bibliotekę (tzw. halucynacja). Zasada: każdą nazwę funkcji sprawdzasz w dokumentacji Pythona, a każdy kod **uruchamiasz i testujesz**.
### Prywatność
Nie wklejaj do AI haseł, kluczy API, danych osobowych (PESEL, adresy) ani kodu firmy bez zgody. W kursie dane są fikcyjne.
### CLAUDE.md — zasady na stałe
Plik CLAUDE.md w katalogu projektu czyta Claude Code na początku każdej sesji. Mentor tworzy go przyciskiem (Mój projekt → „Utwórz CLAUDE.md z zasadami”). Wpisz tam np.: „Uczę się Pythona. Nie podawaj gotowych rozwiązań zadań. Tłumacz po polsku.”

## 2 · Demonstracja — krok po kroku
**Jedna pomoc — cztery poziomy**

```
Prompt (dobry):
Uczę się pętli while w Pythonie (tydzień 2 kursu).
Mój program suma.py ma liczyć sumę liczb do wpisania 0, ale kręci się bez końca.
Kod:
    suma = 0
    x = int(input("Liczba: "))
    while x != 0:
        suma = suma + x
    print(suma)
Nie podawaj poprawionego kodu. Zadaj mi jedno pytanie, które pomoże znaleźć błąd.

Odpowiedź asystenta (wskazówka):
Co zmienia wartość zmiennej x wewnątrz pętli? Kiedy warunek x != 0 może stać się fałszywy?
```

1. Kontekst: „Uczę się pętli while (tydzień 2)” — asystent dopasuje poziom wyjaśnienia.
2. Co zrobiłem: kod i opis objawu („kręci się bez końca”). Bez kodu asystent zgaduje.
3. Ograniczenie: „Nie podawaj poprawionego kodu” — chronisz swoją naukę.
4. Odpowiedź to pytanie naprowadzające: x nie zmienia się w pętli, więc warunek zawsze jest prawdziwy. Sam(a) dopisujesz `x = int(input("Liczba: "))` w środku pętli.
5. Gdyby to nie pomogło: poziom 2 — „wskaż linię”, poziom 3 — „pokaż fragment”, poziom 4 — „pełne rozwiązanie z wyjaśnieniem każdej linii”.
6. Na koniec: uruchom poprawiony program i przetestuj: 5, 3, 0 → suma 8.

✔ **Oczekiwany wynik:** Błąd znaleziony przez Ciebie, a w notatki.md zapisana reguła: „w pętli while coś musi zmieniać warunek”.

## 3 · Jak to uruchomić
1. Mentor → Asystent → tryb Offline → wpisz pytanie, np. „co to jest pętla”.
2. Mentor → Prompty: gotowe szablony promptów do skopiowania (Nowy temat, Błąd, Przegląd kodu).

## W praktyce
- Każda rozmowa z AI kończy się Twoim uruchomieniem kodu i jednym zdaniem w notatki.md.
- Raz w tygodniu poproś asystenta o pytania sprawdzające z tematu tygodnia.

## 4 · Ćwiczenie prowadzone
Oceń 3 prompty (dobry / zły): (1) „Zrób zadanie t1z2”; (2) „Uczę się if/elif. Oto mój kod i błąd ZeroDivisionError. Nie dawaj rozwiązania — wskaż, gdzie szukać”; (3) „Wyjaśnij linia po linii, co robi ten kod: …” Czas: 10 minut.

📄 `cwiczenia/tydzien_00/nauka_z_asystentem_1.md` · rozwiązanie: `rozwiazania/tydzien_00/nauka_z_asystentem_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Asystent napisał: „Użyj funkcji `lista.sum()`, żeby dodać elementy listy”. Uruchamiasz `[1, 2, 3].sum()` i widzisz `AttributeError: 'list' object has no attribute 'sum'`. (1) Czy asystent miał rację? (2) Jak poprawnie dodać elementy listy (wpisz wywołanie dla listy [1, 2, 3])? Czas: 10 minut.

📄 `cwiczenia/tydzien_00/nauka_z_asystentem_2.md` · rozwiązanie: `rozwiazania/tydzien_00/nauka_z_asystentem_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Kod od AI działa, ale nie wiesz dlaczego.**
  - Przyczyna: Poziom 4 drabiny od razu.
  - Jak sprawdzić: Spróbuj wyjaśnić 3 linie na głos.
  - Poprawka: Poproś: „wyjaśnij linia po linii” i przepisz ręcznie.
- ✘ **AttributeError / ModuleNotFoundError w kodzie od AI.**
  - Przyczyna: Halucynacja: nieistniejąca metoda lub biblioteka.
  - Jak sprawdzić: Dokumentacja Pythona albo `help(obiekt)`.
  - Poprawka: Zapytaj AI: „czy ta funkcja na pewno istnieje? podaj link do dokumentacji” i sprawdź sam.

## Pułapki
- Wklejanie kodu z kluczem API do czatu — klucz trzeba potem unieważnić.
- Wiara w pewny ton AI — pewność to nie dowód; dowodem jest uruchomiony test.

## Dodatkowe zadania
1. Utwórz CLAUDE.md przyciskiem w Mój projekt i dopisz 3 własne zasady.
2. Zadaj Asystentowi Offline pytanie o zmienną, funkcję i pętlę.
3. Zapisz w notatki.md swój szablon dobrego promptu.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jakie 4 elementy ma prompt, który uczy?**
  - Kontekst, co zrobiłem (kod/błąd), czego chcę, ograniczenie.
- **Czym jest halucynacja AI?**
  - Pewnie podana nieprawda, np. nieistniejąca funkcja.
- **Czego nie wklejasz do AI?**
  - Haseł, kluczy, danych osobowych, cudzego kodu bez zgody.

## Co potrafię teraz bez patrzenia na przykład?
Prosisz o wskazówki zamiast gotowców, idziesz po drabinie pomocy, sprawdzasz każdą odpowiedź AI uruchomieniem i nie wysyłasz danych prywatnych.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Claude Code — Best practices (dostęp 23.11.2026) — <https://code.claude.com/docs/en/best-practices>
- Claude Code — How Claude remembers your project (CLAUDE.md) (dostęp 23.11.2026) — <https://code.claude.com/docs/en/memory>
- Python — Poradnik (oficjalna dokumentacja, wersja polska) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Najlepsza pierwsza prośba przy błędzie:
  - A) napisz poprawny kod
  - B) zadaj mi pytanie naprowadzające
  - C) usuń błąd
  - D) przepisz cały program
- AI podało nieistniejącą funkcję. To:
  - A) halucynacja
  - B) nowa wersja Pythona
  - C) błąd Windows
  - D) funkcja ukryta
- Gdzie wpisujesz klucz API?
  - A) do CLAUDE.md
  - B) do kodu w repozytorium
  - C) tylko w Mentorze (zapis lokalny)
  - D) w README
- Tryb asystenta bez internetu i opłat:
  - A) API
  - B) Claude Code
  - C) Offline
  - D) żaden

Odpowiedzi: B, A, C, C
