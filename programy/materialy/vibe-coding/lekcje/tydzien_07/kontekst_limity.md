# Kontekst, limity i koszt sesji: /context, /clear, /compact, /usage
Tydzień 7 · lekcja 22 z 48 · ≈ 45 min

**Po tej lekcji potrafisz:** mierzysz zajętość kontekstu, czyścisz i streszczasz rozmowę, dobierasz model i wysiłek do zadania oraz planujesz pracę tak, by nie przekraczać limitów.

**Po co mi to?** Dokumentacja Claude Code: koszt rośnie z rozmiarem kontekstu, a `/clear` to najtańsza praktyka. Kto zarządza kontekstem, robi więcej w tym samym planie i dostaje lepsze odpowiedzi.

## Czego potrzebujesz
- Lekcje „Konta, plany i koszty” i „Małe kroki”.

## 1 · Wyjaśnienie od podstaw
### Dlaczego kontekst kosztuje
Przy każdej Twojej wiadomości agent wysyła modelowi całą dotychczasową rozmowę: instrukcje (CLAUDE.md/AGENTS.md), przeczytane pliki, wyniki komend, swoje odpowiedzi. Godzinna sesja to dziesiątki tysięcy tokenów przy KAŻDEJ wiadomości. Dlatego długie sesje szybciej zużywają limit i — gdy okno się zapełnia — gorzej pamiętają wcześniejsze ustalenia.
### Polecenia
| cel | Claude Code | Codex |
|---|---|---|
| ile kontekstu zajęte | `/context` (wykres: instrukcje, pliki, rozmowa) | `/status` |
| limity planu | `/usage` | `/usage` |
| nowy temat, czysta kartka | `/clear` | `/new` |
| streszczenie zamiast kasowania | `/compact` (można dodać, co zachować: `/compact zachowaj decyzje o rabatach`) | `/compact` |
| zmiana modelu | `/model` | `/model` |
| wysiłek rozumowania | `/effort` | (wybór modelu/ustawień) |
| powrót do starej sesji | `/resume`, nazwanie `/rename` | (historia sesji w aplikacji) |
### Strategie z dokumentacji (w skrócie)
- `/clear` między niezwiązanymi zadaniami — najtańsze.
- Konkretne prośby zamiast „popraw cały projekt” — agent czyta mniej plików.
- Tryb planu przy złożonych zadaniach — mniej prób i błędów.
- Lżejszy model do prostych zadań, mocniejszy do trudnych (nazwy modeli sprawdzasz w `/model` — zmieniają się).
- Krótkie pliki instrukcji (każda linia CLAUDE.md jest wysyłana przy każdej wiadomości).
### Notatka przekazania (handoff)
Przed `/clear` po dłuższej pracy poproś: „Zapisz w notatki/stan.md: co zrobione, decyzje, co dalej, otwarte pytania — maks. 15 linii”. Nowa sesja: „Przeczytaj notatki/stan.md i AGENTS.md”. To tańsze i pewniejsze niż wielogodzinna rozmowa.
### Planowanie dnia pod limity
Okno ok. 5 godzin: rozkładaj trudne zadania na początek okna, nie zostawiaj ich na koniec. Gdy limit się kończy — przejdź do pracy bez agenta: przegląd diffów, testy, README, dziennik.

## 2 · Demonstracja — krok po kroku
**Sesja, która „zgłupiała”, i jej naprawa**

```
Sesja przed i po porządkach (wartości przykładowe):

/context → 142 tys. tokenów: instrukcje 3 tys., pliki 61 tys., rozmowa 78 tys.
Prośba: „Zapisz notatki/stan.md (maks. 15 linii)”.
/clear
„Przeczytaj notatki/stan.md i AGENTS.md, potem zrób punkt 3 planu.”
/context → 18 tys. tokenów.
```

1. Po 2 godzinach pracy agent zaczyna przywracać rozwiązanie, które 40 minut temu odrzuciłeś. `/context` pokazuje okno zapełnione w ok. 80%.
2. Zamiast się kłócić: „Zapisz notatki/stan.md: zrobione, decyzje (w tym: NIE używamy biblioteki X), następny krok”. Przeglądasz plik, poprawiasz jedną decyzję ręcznie.
3. Commit stanu kodu (git), `/clear`.
4. Nowa prośba z odwołaniem do stan.md. Agent pracuje zgodnie z decyzjami; `/context` — kilkanaście tysięcy tokenów.
5. `/usage` — widzisz, ile okna 5-godzinnego zostało; planujesz resztę dnia.

✔ **Oczekiwany wynik:** Agent znów trzyma się ustaleń, koszt kolejnych wiadomości spadł kilkukrotnie, a decyzje są zapisane w repozytorium.

## 3 · Jak to uruchomić
1. Claude Code: `/context`, `/usage`, `/clear`, `/compact`, `/model`.
2. Codex: `/status`, `/new`, `/compact`, `/model`.

## W praktyce
- Każda sesja kończy się notatką stan.md albo commitem.
- Raz w tygodniu porównaj /usage z planem.

## 4 · Ćwiczenie prowadzone
Okno kontekstu ma 200 000 tokenów. `/context` pokazuje: instrukcje 4 000, pliki 56 000, rozmowa 100 000. (1) Ile tokenów jest zajętych? (2) Jaki to procent okna? (3) Po `/clear` i wczytaniu instrukcji oraz notatki stan.md (1 000 tokenów) — ile będzie zajęte? Czas: 15 minut.

📄 `cwiczenia/tydzien_07/kontekst_limity_1.md` · rozwiązanie: `rozwiazania/tydzien_07/kontekst_limity_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dobierz polecenie Claude Code: (1) kończysz zadanie o rabatach, zaczynasz niezwiązane — formularz; (2) w połowie dużego zadania kontekst ma 85%, chcesz zachować decyzje; (3) chcesz sprawdzić, ile limitu planu zostało; (4) proste zadanie — zmiana tekstu komunikatu; chcesz tańszy model. Opcje: /clear, /compact, /usage, /model. Czas: 15 minut.

📄 `cwiczenia/tydzien_07/kontekst_limity_2.md` · rozwiązanie: `rozwiazania/tydzien_07/kontekst_limity_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Agent „zapomina” ustalenia z początku sesji.**
  - Przyczyna: Zapełnione okno — wcześniejsze fragmenty streszczone lub rozmyte.
  - Jak sprawdzić: `/context`.
  - Poprawka: Notatka stan.md + /clear; ważne decyzje do AGENTS.md.
- ✘ **Limit kończy się w 2 godziny.**
  - Przyczyna: Długie sesje, ogólne prośby, mocny model do wszystkiego.
  - Jak sprawdzić: `/usage`, `/context`.
  - Poprawka: /clear między zadaniami, konkretne prośby, lżejszy model do prostych zmian.

## Pułapki
- /compact streszcza — streszczenie może zgubić szczegół. Decyzje ważne na dłużej zapisuj w plikach, nie licz na pamięć rozmowy.
- Wklejanie długich logów i całych plików do rozmowy zapycha kontekst — wskaż agentowi plik i fragment zamiast wklejać.

## Dodatkowe zadania
1. Zmierz /context na początku i końcu sesji (zadanie tygodnia).
2. Przećwicz notatkę stan.md i /clear.
3. Zapisz w dzienniku stan /usage na koniec dnia przez 3 dni.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Dlaczego długa sesja kosztuje więcej?**
  - Bo przy każdej wiadomości wysyłana jest cała rozmowa z plikami i instrukcjami.
- **Czym różni się /clear od /compact?**
  - /clear czyści rozmowę; /compact zastępuje ją streszczeniem.
- **Co to jest notatka przekazania?**
  - Krótki plik ze stanem pracy, decyzjami i następnym krokiem, czytany na początku nowej sesji.

## Co potrafię teraz bez patrzenia na przykład?
Mierzysz kontekst, czyścisz i streszczasz rozmowę, przekazujesz stan przez plik, dobierasz model i planujesz pracę pod okna limitów.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Claude Code — Manage costs effectively (/usage, /context, /clear, /compact) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/costs>
- Codex CLI — slash commands (/init, /diff, /status, /compact, /new, /review, /permissions) (dostęp 20.11.2026) — <https://developers.openai.com/codex/cli/slash-commands>
- Claude Code — Best practices (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Najtańsza praktyka według dokumentacji Claude Code:
  - A) Większy model
  - B) /clear między niezwiązanymi zadaniami
  - C) Dłuższe prośby
  - D) Wklejanie całych plików
- Polecenie pokazujące zajętość kontekstu w Claude Code:
  - A) /context
  - B) /memory
  - C) /status
  - D) /tokens
- Notatka przekazania powinna mieć:
  - A) Całą rozmowę
  - B) Zrobione, decyzje, następny krok — krótko
  - C) Hasła
  - D) Kod wszystkich plików
- Gdzie zapisujesz decyzję ważną dla całego projektu?
  - A) W rozmowie
  - B) W AGENTS.md lub specyfikacji
  - C) Nigdzie
  - D) W komentarzu na GitHubie

Odpowiedzi: B, A, B, B
