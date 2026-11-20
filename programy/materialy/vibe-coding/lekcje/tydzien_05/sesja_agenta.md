# Sesja z agentem: prośba, zgody, tryby, przerwanie i cofnięcie
Tydzień 5 · lekcja 16 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** prowadzisz sesję z agentem od prośby do zatwierdzonej zmiany: czytasz prośby o zgodę, wybierasz tryb (ręczny, akceptuj edycje, plan), przerywasz Esc i cofasz zmiany /rewind.

**Po co mi to?** Każda zgoda to decyzja o Twoich plikach. Kto rozumie tryby i cofanie, pracuje szybko i bez strachu.

## Czego potrzebujesz
- Zainstalowany Claude Code lub Codex (albo ścieżka bez konta — lekcja przez demonstrację).
- Lekcja „Instalacja…”.

## 1 · Wyjaśnienie od podstaw
### Co dzieje się po wysłaniu prośby
Agent: (1) czyta pliki, żeby zrozumieć projekt, (2) planuje, (3) proponuje działania — edycję pliku, komendę w terminalu, pobranie strony, (4) po każdej akcji sprawdza wynik i decyduje, co dalej. Ty widzisz każdą proponowaną akcję i — zależnie od trybu — zatwierdzasz ją.
### Prośba o zgodę w Claude Code
W trybie ręcznym (domyślnym) odczyt plików w katalogu roboczym nie wymaga zgody; komendy (z wyjątkiem wbudowanej listy komend tylko do odczytu) i edycje plików — wymagają. Okno zgody pokazuje, co agent chce zrobić, i opcje: Tak / Tak i nie pytaj ponownie / Nie. Przy Tak lub Nie klawisz Tab otwiera pole na krótką uwagę dla agenta („nie, najpierw uruchom testy”).
„Nie pytaj ponownie” dla komendy zapisuje regułę na stałe w `.claude/settings.local.json` — dla edycji plików działa tylko do końca sesji.
### Tryby uprawnień Claude Code (Shift + Tab przełącza)
| tryb | co robi | kiedy w kursie |
|---|---|---|
| default (ręczny) | pyta o edycje i komendy | początek, zadania z nowym typem zmian |
| acceptEdits | edycje plików bez pytania, komendy dalej z pytaniem | gdy plan jest zatwierdzony, a zmiany przeglądasz w Git |
| plan | tylko czyta i proponuje plan; edycje zablokowane do Twojej akceptacji; Ctrl + G otwiera plan do edycji | każde zadanie większe niż jedna funkcja |
| auto | klasyfikator ocenia akcje zamiast Ciebie, blokuje m.in. pobierz-i-uruchom (curl … \| bash), wysyłanie danych, force push | dopiero gdy pewnie czytasz zmiany; dokumentacja: „nie gwarantuje bezpieczeństwa” |
| bypassPermissions | bez żadnych pytań | nigdy na komputerze z Twoimi danymi (tylko izolowane maszyny) |
Uwaga: od niedawnych wersji Claude Code może startować w trybie auto — sprawdź tryb na dole ekranu przy starcie i przełącz Shift + Tab na ręczny lub planu, jeśli chcesz kontrolować każdą zmianę. Tryb planu od razu: `claude --permission-mode plan`.
### Codex — odpowiedniki
„Ask for approval” ≈ ręczny w obrębie projektu; „Approve for me” ≈ auto; „Full access” ≈ bypass. Przełączasz `/permissions`. Plan: poproś „najpierw plan, nie zmieniaj plików, dopóki nie zatwierdzę”.
### Przerwanie i cofnięcie
- Esc przerywa agenta w połowie (oba narzędzia). Kontekst zostaje — możesz skorygować kierunek.
- Claude Code tworzy punkt kontrolny (checkpoint) przed każdą Twoją prośbą. `/rewind` albo dwa razy Esc przy pustym polu otwiera menu: przywróć kod i rozmowę / tylko rozmowę / tylko kod / podsumuj od tego miejsca.
- Ograniczenia z dokumentacji: zmiany zrobione komendami w terminalu nie zawsze są śledzone; checkpointy to NIE zamiennik systemu kontroli wersji — od tygodnia 6 każdą dobrą wersję zapisujesz w Git.
### Dobra pierwsza prośba w sesji
„Przeczytaj specyfikacja.md i walidacja.py. Zaproponuj plan zmian w punktach, nie zmieniaj plików. Gotowe, gdy: przechodzą testy Mentora.”

## 2 · Demonstracja — krok po kroku
**Zadanie w trybie planu, potem cofnięcie złej zmiany**

```
Okno zgody (tryb ręczny), agent chce uruchomić testy — wygląd przybliżony, dokładne słowa zależą od wersji:

  Bash command: python -m pytest -q
  Do you want to proceed?
  ❯ 1. Yes
    2. Yes, and don't ask again for python -m pytest commands in this project
    3. No, and tell Claude what to do differently (esc)

Wybór 2 jest rozsądny dla testów (bezpieczne, często powtarzane). Dla `del`, `rmdir`, `git push --force` — zawsze tylko 1 albo 3.
```

1. Claude Code w PRACA, Shift + Tab do „plan mode”. Prośba: „Dodaj do rabaty.py funkcję rabat_lojalnosciowy(liczba_pobytow): 3% od 3. pobytu. Najpierw plan.”
2. Agent czyta pliki i pokazuje plan: nowa funkcja, test w osobnym pliku, bez zmian w istniejących funkcjach. Ctrl + G — dopisujesz w planie „maks. 15% łącznie z innymi rabatami — NIE zmieniaj funkcji rabat()”. Zatwierdzasz.
3. Agent proponuje edycję rabaty.py — widzisz różnicę (linie dodane). Akceptujesz. Proponuje `python -m pytest -q` — akceptujesz; testy przechodzą.
4. Druga prośba: „Uprość cały plik”. Agent przepisuje 4 funkcje. Testy Mentora robią się czerwone.
5. Esc Esc → menu checkpointów → wybierasz punkt sprzed „Uprość cały plik” → „Restore code and conversation”. Plik wraca do stanu z zielonym testem.
6. Wniosek do dziennika: „ogólne prośby (uprość wszystko) = ryzyko; jedna funkcja na prośbę”.

✔ **Oczekiwany wynik:** Nowa funkcja dodana przez plan → zgodę → test, a zła ogólna zmiana cofnięta checkpointem w kilka sekund.

## 3 · Jak to uruchomić
1. Claude Code: Shift + Tab (tryby), Esc (przerwij), Esc Esc lub /rewind (cofnij).
2. Codex: /permissions (tryby), Esc (przerwij), /diff (zobacz zmiany).

## W praktyce
- Każde zadanie > 1 funkcja zaczynaj w trybie planu.
- „Nie pytaj ponownie” tylko dla testów i komend tylko do odczytu.

## 4 · Ćwiczenie prowadzone
Agent w trybie ręcznym proponuje kolejno: (1) odczyt rabaty.py, (2) edycję rabaty.py, (3) komendę `python -m pytest -q`, (4) komendę `rmdir /s /q dane`. Przy których Claude Code w ogóle zapyta o zgodę (w trybie ręcznym)? Przy której wybierzesz „Nie” i dlaczego (numer)? Czas: 15 minut.

📄 `cwiczenia/tydzien_05/sesja_agenta_1.md` · rozwiązanie: `rozwiazania/tydzien_05/sesja_agenta_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dobierz tryb Claude Code: (1) nowe, większe zadanie (3 pliki) — chcesz najpierw zobaczyć plan; (2) plan zatwierdzony, zmiany i tak przejrzysz w Git, nie chcesz klikać każdej edycji; (3) pierwszy dzień z agentem, chcesz widzieć każdą akcję. Opcje: default, acceptEdits, plan, bypassPermissions. Czy checkpoint cofnie zmianę zrobioną komendą `del raport.txt` na pewno (tak/nie)? Czas: 15 minut.

📄 `cwiczenia/tydzien_05/sesja_agenta_2.md` · rozwiązanie: `rozwiazania/tydzien_05/sesja_agenta_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Agent zmienił 6 plików, a prosiłeś o jedną funkcję.**
  - Przyczyna: Ogólna prośba i tryb bez planu.
  - Jak sprawdzić: Czy prośba mówiła, których plików nie ruszać?
  - Poprawka: Tryb planu, lista plików w prośbie, potem /rewind do stanu sprzed zmiany.
- ✘ **Kliknąłeś „don't ask again” dla komendy, której nie chcesz.**
  - Przyczyna: Reguła zapisana na stałe w .claude/settings.local.json.
  - Jak sprawdzić: `/permissions` — lista reguł i plików, z których pochodzą.
  - Poprawka: Usuń regułę w /permissions.
- ✘ **Agent „myśli” od kilku minut i zużywa limit.**
  - Przyczyna: Zbyt szerokie zadanie, pętla prób.
  - Jak sprawdzić: Co pokazuje ostatnia akcja?
  - Poprawka: Esc, potem krótsza, konkretniejsza prośba albo tryb planu.

## Pułapki
- Tryb auto i „Approve for me” nie zastępują Twojego przeglądu — dokumentacja Claude Code mówi wprost, że auto nie gwarantuje bezpieczeństwa.
- Checkpointy przechowywane są lokalnie przez ok. 30 dni i obejmują 100 ostatnich punktów — to bezpieczeństwo na teraz, nie archiwum projektu.

## Dodatkowe zadania
1. Wykonaj jedno zadanie w trybie planu z edycją planu Ctrl + G.
2. Przećwicz /rewind na celowo złej zmianie.
3. Zapisz w sesja_agenta.md każdą decyzję o zgodzie (zadanie tygodnia).

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jak przerwiesz agenta w połowie?**
  - Esc.
- **Co robi tryb planu?**
  - Agent tylko czyta i proponuje plan; zmiany plików czekają na moją akceptację.
- **Dlaczego checkpoint nie zastępuje Gita?**
  - Nie śledzi wszystkich zmian z komend, jest lokalny i krótkotrwały; Git zapisuje trwałą historię wersji.

## Co potrafię teraz bez patrzenia na przykład?
Rozumiesz cykl sesji, czytasz prośby o zgodę, dobierasz tryb, przerywasz Esc i cofasz /rewind — z świadomością ograniczeń checkpointów.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Claude Code — Permission modes (default, acceptEdits, plan, auto…) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/permission-modes>
- Claude Code — Configure permissions (reguły allow/ask/deny, /permissions) (dostęp 20.11.2026) — <https://code.claude.com/docs/en/permissions>
- Claude Code — Checkpointing (/rewind, Esc Esc) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/checkpointing>
- Codex — Permission modes (Ask for approval, Approve for me, Full access) (dostęp 19.11.2026) — <https://learn.chatgpt.com/docs/permission-modes>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Skrót przełączający tryby w Claude Code:
  - A) Ctrl + T
  - B) Shift + Tab
  - C) Alt + M
  - D) F5
- W trybie ręcznym bez pytania agent może:
  - A) Usuwać pliki
  - B) Czytać pliki w katalogu roboczym
  - C) Instalować paczki
  - D) Robić git push
- „Yes, and don't ask again” dla komendy zapisuje regułę:
  - A) Na 5 minut
  - B) Na stałe w .claude/settings.local.json
  - C) Nigdzie
  - D) W CLAUDE.md
- Który tryb jest tylko dla izolowanych maszyn?
  - A) plan
  - B) default
  - C) bypassPermissions
  - D) acceptEdits

Odpowiedzi: B, B, B, C
