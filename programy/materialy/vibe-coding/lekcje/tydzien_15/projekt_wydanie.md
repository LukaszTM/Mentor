# Wydanie wersji 1.0: CHANGELOG, tag, release i przekazanie
Tydzień 15 · lekcja 47 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** wydajesz wersję 1.0.0 projektu: lista kontrolna przed wydaniem, CHANGELOG, tag Git i release na GitHubie, a dla klienta — przekazanie z instrukcją i planem utrzymania.

**Po co mi to?** „Skończone” w zawodzie znaczy: wydane, opisane i możliwe do utrzymania. Wydanie z tagiem to też dowód dla rekrutera, że doprowadzasz projekty do końca.

## Czego potrzebujesz
- Projekt końcowy z kamieniami 1–4.
- Lekcje „README” i „CI”.

## 1 · Wyjaśnienie od podstaw
### Wersjonowanie semantyczne (SemVer)
Numer GŁÓWNA.MNIEJSZA.POPRAWKA: 1.0.0 — pierwsza stabilna; 1.1.0 — nowa funkcja zgodna wstecz; 1.1.1 — poprawka błędu; 2.0.0 — zmiana łamiąca zgodność (np. inny format API).
### Lista kontrolna przed wydaniem
| obszar | sprawdzenie |
|---|---|
| testy | wszystkie zielone lokalnie i w CI |
| bezpieczeństwo | tabela 6 dziur, brak sekretów w repo (wyszukiwanie), debug wyłączony, SECRET_KEY ze zmiennej |
| dane | brak prawdziwych danych osobowych, *.db w .gitignore |
| dokumentacja | README (test obcej osoby), CHANGELOG, LICENSE |
| zależności | requirements.txt z wersjami, każda paczka zweryfikowana |
| instrukcje agenta | AGENTS.md aktualny |
### CHANGELOG.md (zasady „Keep a Changelog”)
```
# Changelog

### [1.0.0] - 2027-03-10
### Dodano
- API rezerwacji z walidacją (201/400/409)
- Lista rezerwacji bez danych kontaktowych
### Bezpieczeństwo
- Zapytania SQL wyłącznie z parametrami
```
Sekcje: Dodano, Zmieniono, Naprawiono, Usunięto, Bezpieczeństwo. Najnowsza wersja na górze. Piszesz dla ludzi, nie wklejasz listy commitów.
### Tag i release
- `git tag -a v1.0.0 -m "Wersja 1.0.0"` → `git push origin v1.0.0`.
- GitHub → Releases → Draft a new release → wybierz tag v1.0.0 → opis z CHANGELOG → Publish.
- Release może zawierać pliki do pobrania (np. ZIP), ale kod źródłowy GitHub dołącza sam.
### Przekazanie klientowi
- Instrukcja dla użytkownika (nie programisty): jak uruchomić, jak dodać/usunąć rezerwację, co robić, gdy coś nie działa.
- Dostępy: repozytorium (zaproszenie klienta jako właściciela/organizacji), hosting, domena — na konto klienta, nie Twoje.
- Plan utrzymania: aktualizacje zależności (np. raz na kwartał), kopie bazy, kto i za ile poprawia błędy po okresie gwarancyjnym.
### Retrospektywa
Po wydaniu 30 minut: co poszło dobrze, co źle, co zmienię w następnym projekcie (dla siebie i w AGENTS.md/szablonach). To najkrótsza droga do szybszych i tańszych projektów.

## 2 · Demonstracja — krok po kroku
**Wydanie z listą kontrolną — jedna wpadka złapana**

```
Opis release v1.0.0 na GitHubie:

**Pod Lipą — mini system rezerwacji 1.0.0**

Pierwsza stabilna wersja projektu szkoleniowego (dane fikcyjne).

- API rezerwacji: zapis z walidacją, kolizje (409), lista bez e-maili, wolne pokoje, usuwanie
- 46 testów, CI na GitHub Actions
- Bezpieczeństwo: SQL z parametrami, escape w HTML, sekrety ze zmiennych środowiskowych

Uruchomienie: README → Instalacja.
```

1. Lista kontrolna: testy zielone, CI zielone. Wyszukiwanie w repo „SECRET” — w system.py `SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "dev")`: domyślna wartość „dev”. Poprawka: brak zmiennej → RuntimeError; test.
2. README: test obcej osoby — OK. CHANGELOG według szablonu.
3. `git tag -a v1.0.0 -m "Wersja 1.0.0"`, `git push origin v1.0.0`. GitHub → Releases → nowy release z opisem.
4. Retrospektywa: dobrze — testy przed kodem; źle — kamień 2 trwał 2× dłużej (kolizje); zmiana — przypadki brzegowe dat do szablonu specyfikacji.

✔ **Oczekiwany wynik:** Wersja 1.0.0 z tagiem i release, bez domyślnego sekretu, z CHANGELOG i wnioskami na następny projekt.

## 3 · Jak to uruchomić
1. `git tag -a v1.0.0 -m "Wersja 1.0.0"` → `git push origin v1.0.0` → GitHub Releases.
2. Zadanie tygodnia „Wydanie 1.0.0” → „✔ Sprawdź wynik”.

## W praktyce
- Każde wydanie: lista kontrolna + CHANGELOG + tag.
- Retrospektywa po każdym projekcie — 30 minut.

## 4 · Ćwiczenie prowadzone
Dobierz numer wersji po 1.2.3 według SemVer: (1) poprawka błędu walidacji dat, (2) nowa funkcja — eksport CSV, zgodna wstecz, (3) zmiana formatu odpowiedzi API (stare aplikacje przestaną działać). Czas: 15 minut.

📄 `cwiczenia/tydzien_15/projekt_wydanie_1.md` · rozwiązanie: `rozwiazania/tydzien_15/projekt_wydanie_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Przekazanie klientce: na czyje konto rejestrujesz domenę i hosting (moje / klientki)? Jaką komendą wyślesz tag v1.0.0 na GitHub (pełna komenda)? Która sekcja CHANGELOG opisze „SQL z parametrami” (Dodano / Bezpieczeństwo / Naprawiono)? Czas: 15 minut.

📄 `cwiczenia/tydzien_15/projekt_wydanie_2.md` · rozwiązanie: `rozwiazania/tydzien_15/projekt_wydanie_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Tag jest lokalnie, ale nie ma go na GitHubie.**
  - Przyczyna: `git push` nie wysyła tagów domyślnie.
  - Jak sprawdzić: `git ls-remote --tags origin`.
  - Poprawka: `git push origin v1.0.0`.
- ✘ **Release zawiera plik .env albo bazę z danymi.**
  - Przyczyna: Ręcznie dołączony ZIP z całego folderu.
  - Jak sprawdzić: Lista plików w release.
  - Poprawka: Usuń zasób z release, unieważnij sekrety; ZIP buduj z `git archive` (tylko pliki z repo).

## Pułapki
- Wydanie w piątek wieczorem bez czasu na poprawki — zły pomysł także w małych projektach.
- Hosting i domena na Twoje konto = klient jest od Ciebie zależny; przenieś na konto klienta.

## Dodatkowe zadania
1. Lista kontrolna, CHANGELOG, tag v1.0.0 i release (zadanie tygodnia).
2. Instrukcja dla użytkownika (1 strona).
3. Retrospektywa w dzienniku.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co oznacza 2.0.0 w SemVer?**
  - Zmianę łamiącą zgodność wstecz.
- **Co zawiera CHANGELOG?**
  - Opis zmian dla ludzi w sekcjach Dodano/Zmieniono/Naprawiono/Usunięto/Bezpieczeństwo, najnowsze na górze.
- **Co przekazujesz klientowi?**
  - Instrukcję, dostępy na jego konto, plan utrzymania i dokumentację.

## Co potrafię teraz bez patrzenia na przykład?
Wydajesz wersję 1.0.0 z listą kontrolną, CHANGELOG, tagiem i release, przekazujesz projekt klientowi i robisz retrospektywę.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Semantic Versioning 2.0.0 (semver.org, wersja polska) (dostęp 20.11.2026) — <https://semver.org/lang/pl/>
- Keep a Changelog (wersja polska) (dostęp 20.11.2026) — <https://keepachangelog.com/pl/1.1.0/>
- GitHub Docs — About releases (tagi i wydania) (dostęp 20.11.2026) — <https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases>
- Atlassian — Retrospektywa: jak ją przeprowadzić (dostęp 20.11.2026) — <https://www.atlassian.com/team-playbook/plays/retrospective>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Pierwsza stabilna wersja według SemVer:
  - A) 0.1.0
  - B) 1.0.0
  - C) 1.1.1
  - D) 10
- Wysłanie tagu na GitHub:
  - A) git push
  - B) git push origin v1.0.0
  - C) git tag --push
  - D) git release
- Przed wydaniem sprawdzasz:
  - A) Tylko kolor strony
  - B) Testy, CI, sekrety, dane, README, CHANGELOG, licencję
  - C) Liczbę commitów
  - D) Nic
- Retrospektywa służy do:
  - A) Oceniania klienta
  - B) Wniosków na kolejny projekt
  - C) Usuwania historii
  - D) Marketingu

Odpowiedzi: B, B, B, B
