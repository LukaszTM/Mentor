# Portfolio i ścieżki zawodowe vibe codera
Tydzień 14 · lekcja 44 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** wybierasz ścieżkę (praca w firmie, zlecenia, automatyzacja we własnej branży), budujesz portfolio z 3 projektów z dowodami (testy, CI, README, opis procesu) i przygotowujesz profil GitHub oraz CV pod tę ścieżkę.

**Po co mi to?** Rekruter i klient nie widzą Twojej nauki — widzą repozytoria. Ankieta Stack Overflow 2025: większość zawodowych programistów nie uznaje „vibe codingu” za część swojej pracy — wyróżnia Cię dyscyplina: testy, przegląd, dokumentacja.

## Czego potrzebujesz
- Repozytoria z kursu (pod-lipa, pod-lipa-strona).
- Lekcje „README” i „CI”.

## 1 · Wyjaśnienie od podstaw
### Trzy realistyczne ścieżki
| ścieżka | co sprzedajesz | czego się dalej uczysz |
|---|---|---|
| automatyzacja we własnej branży | skrypty, raporty, małe narzędzia w Twojej obecnej pracy (biuro, handel, rolnictwo, logistyka) | dane (Excel/CSV), API usług, bezpieczeństwo danych |
| zlecenia dla małych firm | strony, kalkulatory, proste aplikacje, integracje | komunikacja z klientem, wycena, utrzymanie, hosting |
| praca w firmie IT (junior / tester / wsparcie) | umiejętność czytania, testowania i przeglądu kodu z AI | podstawy programowania głębiej (Python, SQL, Git), testy automatyczne |
Uczciwie: sam „vibe coding” rzadko jest nazwą stanowiska. Stanowiska wymagają umiejętności, które ćwiczyłeś: testów, Gita, przeglądu, specyfikacji. Kurs „Python od zera → Junior QA” w Mentorze to naturalne pogłębienie ścieżki testera.
### Portfolio: 3 projekty, każdy z dowodami
- Projekt końcowy (tydzień 15) — główny.
- Strona na GitHub Pages — widoczny efekt.
- Jedno małe narzędzie z Twojej branży (automatyzacja, raport) — pokazuje, że rozwiązujesz realne problemy.
Każdy z: README (z sekcją „Jak powstał”), testami, zielonym CI, licencją, sensowną historią commitów, bez sekretów i danych osobowych.
### Profil GitHub
- Repozytorium o nazwie takiej jak login → jego README wyświetla się na profilu (dokumentacja GitHub „profile README”): 5 zdań o Tobie, umiejętności, linki do projektów.
- Przypnij (pin) 3 najlepsze repozytoria.
- Zdjęcie i opis profesjonalne; e-mail kontaktowy osobny od prywatnego.
### CV i opis projektów
Projekt w CV: problem → co zbudowałeś → jak sprawdziłeś (testy, CI) → wynik. Przykład: „System rezerwacji dla agroturystyki (Python, Flask, SQLite): API rezerwacji z walidacją, 40 testów, CI na GitHub Actions; kod z agentami AI pod moją specyfikacją i przeglądem.” Nie ukrywaj AI — pokaż, że umiesz z nim pracować odpowiedzialnie.
### Gdzie szukać
Portale z ofertami IT (np. justjoin.it, nofluffjobs.com, pracuj.pl), lokalne firmy i znajomi przedsiębiorcy (zlecenia), grupy i meetupy, platformy freelancerskie. Ucz się angielskiego technicznego — dokumentacja narzędzi jest po angielsku.

## 2 · Demonstracja — krok po kroku
**Przegląd portfolio oczami rekrutera — 3 minuty na profil**

```
README profilu (github.com/NAZWA/NAZWA):

# Cześć, jestem Anna
Buduję małe aplikacje i automatyzacje w Pythonie z pomocą agentów AI — zawsze ze specyfikacją, testami i przeglądem kodu.

**Projekty**
- [Pod Lipą — mini system rezerwacji](…) — Flask, SQLite, 40 testów, CI
- [Strona z kalkulatorem](…) — HTML/CSS/JS, GitHub Pages
- [Porządkowanie faktur](…) — automatyzacja plików z trybem próby

**Narzędzia:** Python, Git/GitHub, pytest, Claude Code, Codex
```

1. Otwierasz swój profil w oknie prywatnym (tak widzi go obcy). Pierwsze 10 sekund: czy wiadomo, kim jesteś i co umiesz? Jeśli nie — profile README.
2. Przypięte repozytoria: każde ma opis (About) i README z sekcją „Jak uruchomić”? Repo bez README rekruter zamyka.
3. Zakładka Actions: zielone przebiegi = dowód testów.
4. Historia commitów: „fix”, „asdf” vs „Dodaj walidację dat w /api/wolne (400)” — to też ocenia rekruter.
5. Szukasz sekretów i danych: wyszukiwarka w repo („key”, „password”, „@gmail”). Czysto.

✔ **Oczekiwany wynik:** Profil, na którym w 3 minuty widać ścieżkę, 3 projekty z dowodami jakości i brak wpadek.

## 3 · Jak to uruchomić
1. github.com → nowe repo o nazwie loginu → README profilu; profil → Customize your pins.
2. Zadanie tygodnia „portfolio.md” (plan i lista kontrolna).

## W praktyce
- Raz w miesiącu przegląd profilu oczami rekrutera.
- Każdy nowy projekt od razu z README i CI.

## 4 · Ćwiczenie prowadzone
Lista kontrolna projektu do portfolio ma 6 pozycji: README z „Jak powstał”, testy, zielone CI, licencja, historia commitów z opisami, brak sekretów i danych. Projekt ma: README bez sekcji „Jak powstał”, 25 testów, CI zielone, brak LICENSE, commity „fix” i „zmiany”, czysto z sekretami. Ile pozycji jest spełnionych? Którą poprawisz najszybciej (opcje: licencja, historia commitów)? Czas: 15 minut.

📄 `cwiczenia/tydzien_14/portfolio_praca_1.md` · rozwiązanie: `rozwiazania/tydzien_14/portfolio_praca_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dopasuj ścieżkę: (1) pracujesz w biurze rachunkowym i chcesz automatyzować raporty, (2) chcesz robić strony i kalkulatory dla lokalnych firm, (3) chcesz etat w firmie IT i lubisz szukać błędów. Opcje: automatyzacja we własnej branży / zlecenia dla małych firm / praca w firmie IT (tester/junior). Czas: 15 minut.

📄 `cwiczenia/tydzien_14/portfolio_praca_2.md` · rozwiązanie: `rozwiazania/tydzien_14/portfolio_praca_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Rekruter: „nie widzę, co Pan/Pani umie”.**
  - Przyczyna: Repozytoria bez README, brak opisu profilu.
  - Jak sprawdzić: Profil w oknie prywatnym.
  - Poprawka: Profile README, przypięte 3 projekty z README i CI.
- ✘ **W publicznym repo znaleziono stary klucz.**
  - Przyczyna: Klucz w historii commitów.
  - Jak sprawdzić: Wyszukiwarka GitHuba w repo / secret scanning.
  - Poprawka: Unieważnij klucz; jeśli repo to portfolio — rozważ nowe repo bez tej historii.

## Pułapki
- Ilość nie zastępuje jakości: 3 dopracowane projekty > 20 porzuconych.
- Nie publikuj projektów z kursu jako pracy dla prawdziwego klienta — opisz uczciwie: projekt szkoleniowy, dane fikcyjne.

## Dodatkowe zadania
1. Wybierz ścieżkę i zaplanuj portfolio (zadanie tygodnia).
2. Profile README i 3 przypięte repozytoria.
3. Opis projektu końcowego do CV (4 zdania).

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co powinien mieć projekt w portfolio?**
  - README z opisem procesu, testy, zielone CI, licencję, czytelną historię i brak sekretów.
- **Dlaczego nie ukrywać pracy z AI?**
  - Bo firmy jej używają — wyróżnia odpowiedzialny proces: specyfikacja, testy, przegląd.
- **Jak wygląda opis projektu w CV?**
  - Problem → rozwiązanie → jak sprawdzone → wynik, z technologiami.

## Co potrafię teraz bez patrzenia na przykład?
Wybierasz ścieżkę, budujesz portfolio 3 projektów z dowodami jakości, profil GitHub i opis projektów do CV — uczciwie wobec pracy z AI.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- GitHub Docs — Managing your profile README (dostęp 20.11.2026) — <https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme>
- GitHub Docs — Pinning items to your profile (dostęp 20.11.2026) — <https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/pinning-items-to-your-profile>
- Stack Overflow Developer Survey 2025 — AI (zaufanie, vibe coding w pracy zawodowej) (dostęp 19.11.2026) — <https://survey.stackoverflow.co/2025/ai>
- choosealicense.com — wybór licencji open source (GitHub) (dostęp 20.11.2026) — <https://choosealicense.com/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Rekruter ma 3 minuty na profil. Najważniejsze:
  - A) Liczba repozytoriów
  - B) Profile README i 3 dopracowane projekty z README i CI
  - C) Kolorowy avatar
  - D) Liczba gwiazdek
- README profilu GitHub to repozytorium o nazwie:
  - A) profile
  - B) takiej jak login
  - C) readme
  - D) about
- Praca z AI w CV:
  - A) Ukryć
  - B) Opisać z procesem: specyfikacja, testy, przegląd
  - C) Napisać, że AI zrobiło wszystko
  - D) Pominąć projekt

Odpowiedzi: B, B, B
