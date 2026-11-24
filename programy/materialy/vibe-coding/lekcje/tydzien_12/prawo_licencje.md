# Prawo: prawa do kodu z AI, licencje, RODO i AI Act
Tydzień 12 · lekcja 39 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** wiesz, kto ma prawa do kodu powstałego z AI w Polsce, wybierasz licencję dla swojego repozytorium, sprawdzasz licencje zależności, stosujesz minimum RODO przy pracy z agentem i znasz terminy AI Act, które mogą dotyczyć Twoich projektów.

**Po co mi to?** Klient zapyta „czy to moje?”, rekruter — „czy wolno pokazać?”, a dane gości to RODO. Odpowiedzi „AI to napisało” nie da się obronić; trzeba znać zasady.

## Czego potrzebujesz
- Lekcje „GitHub” i „Bezpieczeństwo kodu”.
- Uwaga: to nie jest porada prawna — przy umowach z klientem skonsultuj się z prawnikiem.

## 1 · Wyjaśnienie od podstaw
### Prawo autorskie do kodu z AI (Polska)
Utworem w rozumieniu ustawy o prawie autorskim jest wyłącznie przejaw działalności twórczej CZŁOWIEKA. PARP (2024) podsumowuje: wytwór wygenerowany samym promptem co do zasady nie jest chroniony; gdy AI jest narzędziem, a człowiek wnosi twórczy wkład (koncepcja, wybór, układ, istotne zmiany), ochrona może dotyczyć tego wkładu — ocenia się konkretny przypadek. Praktyka: dokumentuj swój wkład (specyfikacje, decyzje, przeglądy, commity z Twoimi zmianami).
### Co mówią warunki dostawców
Warunki Anthropic (konsumenckie) i OpenAI przewidują, że użytkownik zachowuje prawa do treści wejściowych, a dostawca przenosi na niego swoje prawa do wyników (o ile jakieś ma). To nie tworzy praw autorskich tam, gdzie prawo ich nie przyznaje — ale oznacza, że dostawca nie rości sobie prawa do Twojego kodu. Warunki zmieniają się — sprawdzasz aktualną wersję.
### Licencja Twojego repozytorium
| licencja | w skrócie | kiedy |
|---|---|---|
| MIT | rób, co chcesz, zachowaj informację o licencji; bez gwarancji | portfolio, małe narzędzia |
| Apache-2.0 | jak MIT + wyraźna licencja patentowa i zasady zmian | większe projekty, firmy (tak jest licencjonowany Codex CLI) |
| GPL-3.0 | kto rozpowszechnia zmienioną wersję, musi udostępnić kod na GPL | gdy chcesz, by pochodne zostały otwarte |
| brak licencji | domyślnie wszystkie prawa zastrzeżone — inni nie mogą legalnie używać | kod klienta, prywatne repo |
Plik LICENSE dodasz na GitHubie: Add file → Create new file → nazwa LICENSE → „Choose a license template”. Kod dla klienta: licencja i przeniesienie praw zapisujesz w UMOWIE (pola eksploatacji), nie w pliku.
### Licencje zależności i fragmentów kodu
Agent może odtworzyć fragment cudzego kodu. Przy dłuższych, „gotowych” fragmentach pytaj o źródło; każdą zależność sprawdzasz też pod kątem licencji (na pypi.org i w repozytorium). Licencje typu GPL w zależnościach mogą nakładać obowiązki przy rozpowszechnianiu.
### RODO przy pracy z agentem
- Minimalizacja: agentowi i czatowi dajesz dane fikcyjne lub zanonimizowane, nie prawdziwe dane gości.
- Jeśli przetwarzasz dane osobowe klienta (np. bazę gości) — jesteś podmiotem przetwarzającym: potrzebna umowa powierzenia (art. 28 RODO), a usługi AI, do których trafiają dane, muszą być na to przygotowane (umowy, ustawienia firmowe).
- Pliki z danymi (*.db, eksporty CSV) poza Gitem i poza publicznym internetem.
### AI Act (UE) — co i kiedy
Rozporządzenie 2024/1689, zmienione w 2026 r. pakietem „Digital Omnibus” (rozporządzenie 2026/1744, w mocy od 27.07.2026): zakazane praktyki i (złagodzony) obowiązek wspierania kompetencji w zakresie AI — od 2.02.2025; obowiązki dostawców modeli ogólnego przeznaczenia — od 2.08.2025; obowiązki przejrzystości z art. 50 (np. informowanie, że rozmawia się z chatbotem; oznaczanie treści generowanych) — od 2.08.2026, z okresem przejściowym do 2.12.2026 dla systemów wprowadzonych wcześniej; systemy wysokiego ryzyka — od 2.12.2027 (załącznik III) i 2.08.2028 (załącznik I). Dla vibe codera: sam fakt pisania kodu z AI nie podlega AI Act; ale jeśli budujesz klientowi czatbota albo system oceniający ludzi (np. rekrutacja) — sprawdzasz obowiązki.
### Własna działalność
Pierwsze drobne zlecenia możesz rozliczać w działalności nierejestrowanej, jeśli przychód w kwartale nie przekracza 225% minimalnego wynagrodzenia — w 2026 r. 10 813,50 zł; po przekroczeniu masz 7 dni na wpis do CEIDG. Zawsze sprawdź aktualne przepisy.

## 2 · Demonstracja — krok po kroku
**Trzy decyzje prawne przed publikacją projektu**

```
Fragment README sekcji „Licencja i pochodzenie kodu”:

## Licencja
MIT — zobacz plik LICENSE.

## Jak powstał ten projekt
Kod powstał z pomocą agentów AI (Claude Code / Codex) na podstawie moich specyfikacji;
każdą zmianę przejrzałem i przetestowałem (historia w Gicie). Dane w projekcie są fikcyjne.
```

1. Repo portfolio: dodajesz LICENSE (MIT) przez szablon GitHuba; w README sekcja „Jak powstał” — uczciwie o AI i o Twoim wkładzie.
2. Przegląd zależności: flask (BSD-3-Clause), requests (Apache-2.0), pytest (MIT) — licencje liberalne, zgodne z MIT Twojego projektu. Zapisujesz w README.
3. Dane: rezerwacje.csv jest fikcyjny — OK. Plik pod_lipa.db z testów usuwasz z repozytorium i dopisujesz *.db do .gitignore.
4. Kod dla prawdziwej klientki: nie dajesz licencji MIT; w umowie (z pomocą prawnika) — przeniesienie praw lub licencja, pola eksploatacji, kto odpowiada za dane gości, umowa powierzenia.

✔ **Oczekiwany wynik:** Repozytorium z jasną licencją, uczciwą informacją o AI, sprawdzonymi licencjami zależności i bez danych osobowych.

## 3 · Jak to uruchomić
1. GitHub → Add file → Create new file → LICENSE → Choose a license template.
2. choosealicense.com — porównanie licencji.

## W praktyce
- Każde repo publiczne: LICENSE i sekcja „Jak powstał”.
- Dane klienta nigdy w rozmowie z AI bez umowy i anonimizacji.

## 4 · Ćwiczenie prowadzone
Daty AI Act: (1) od kiedy obowiązują obowiązki przejrzystości z art. 50 (RRRR-MM-DD), (2) do kiedy trwa okres przejściowy dla systemów wprowadzonych wcześniej, (3) od kiedy obowiązki dla systemów wysokiego ryzyka z załącznika III. Czas: 15 minut.

📄 `cwiczenia/tydzien_12/prawo_licencje_1.md` · rozwiązanie: `rozwiazania/tydzien_12/prawo_licencje_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dopasuj licencję: (1) projekt do portfolio, chcesz maksymalnej swobody dla innych, (2) chcesz, by każda rozpowszechniana zmieniona wersja pozostała otwarta, (3) kod dla klientki „Pod Lipą” z umową przeniesienia praw. Opcje: MIT, GPL-3.0, brak publicznej licencji (umowa). Do tego: limit przychodu działalności nierejestrowanej na kwartał 2026 (zł). Czas: 15 minut.

📄 `cwiczenia/tydzien_12/prawo_licencje_2.md` · rozwiązanie: `rozwiazania/tydzien_12/prawo_licencje_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Publiczne repo bez pliku LICENSE, ktoś pyta, czy może użyć kodu.**
  - Przyczyna: Brak licencji = wszystkie prawa zastrzeżone.
  - Jak sprawdzić: Czy jest plik LICENSE?
  - Poprawka: Dodaj licencję (np. MIT) — albo świadomie zostaw bez, jeśli nie chcesz udostępniać.
- ✘ **Do czatu trafił eksport z prawdziwymi danymi gości.**
  - Przyczyna: Brak minimalizacji danych.
  - Jak sprawdzić: Co dokładnie zostało wysłane?
  - Poprawka: Usuń rozmowę, poinformuj administratora danych (klienta) zgodnie z umową; na przyszłość — dane fikcyjne lub zanonimizowane.

## Pułapki
- „Kod od AI nie ma autora, więc mogę go dać komukolwiek” — nie: zależności mają licencje, a klient może mieć prawa do specyfikacji i danych.
- To nie jest porada prawna — przy pierwszej umowie z klientem warto zapłacić za konsultację.

## Dodatkowe zadania
1. Dodaj LICENSE do repozytorium portfolio (zadanie tygodnia).
2. Sprawdź licencje 3 zależności projektu.
3. Zapisz w rodo.md zasady pracy z danymi klientów (zadanie tygodnia).

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Czy kod wygenerowany samym promptem jest utworem w PL?**
  - Co do zasady nie — utworem jest tylko przejaw twórczości człowieka; liczy się Twój twórczy wkład.
- **Co oznacza brak licencji w publicznym repozytorium?**
  - Wszystkie prawa zastrzeżone — inni nie mogą legalnie używać kodu.
- **Od kiedy obowiązują obowiązki przejrzystości AI Act?**
  - Od 2.08.2026 (okres przejściowy do 2.12.2026 dla wcześniejszych systemów).

## Co potrafię teraz bez patrzenia na przykład?
Znasz zasady praw do kodu z AI, wybierasz licencję, sprawdzasz licencje zależności, stosujesz minimalizację danych (RODO) i terminy AI Act.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- PARP — Wytwory powstałe przy udziale AI — w jaki sposób je chronić? (13.05.2024) (dostęp 24.11.2026) — <https://www.parp.gov.pl/component/content/article/86364:wytwory-powstale-przy-udziale-ai-w-jaki-sposob-je-chronic>
- choosealicense.com — wybór licencji open source (GitHub) (dostęp 20.11.2026) — <https://choosealicense.com/>
- UODO — RODO: zasady przetwarzania danych osobowych (art. 5) (dostęp 20.11.2026) — <https://uodo.gov.pl/pl/p/rodo>
- Rozporządzenie (UE) 2026/1744 („Digital Omnibus” dla AI Act) — EUR-Lex, w mocy od 27.07.2026 (dostęp 24.11.2026) — <https://eur-lex.europa.eu/eli/reg/2026/1744/oj>
- Anthropic — Consumer Terms of Service (prawa do Outputs) (dostęp 20.11.2026) — <https://www.anthropic.com/legal/consumer-terms>
- OpenAI — Terms of Use (własność Output) (dostęp 20.11.2026) — <https://openai.com/policies/terms-of-use/>
- Działalność nierejestrowana 2026: limit 10 813,50 zł (money.pl) (dostęp 20.11.2026) — <https://direct.money.pl/artykuly/porady/dzialalnosc-nierejestrowana-2026-limit-10-813,50-zl,-po-przekroczeniu-7-dni-na-ceidg>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Licencja z wyraźną klauzulą patentową:
  - A) MIT
  - B) Apache-2.0
  - C) brak
  - D) CC0
- Dane gości do agenta AI:
  - A) Prawdziwe, bo szybciej
  - B) Fikcyjne lub zanonimizowane
  - C) Tylko e-maile
  - D) Wszystkie w ZIP
- Kod dla klienta — prawa reguluje:
  - A) Plik LICENSE MIT
  - B) Umowa (przeniesienie praw lub licencja)
  - C) README
  - D) Nic
- Limit działalności nierejestrowanej w 2026 r.:
  - A) 10 813,50 zł na kwartał
  - B) 3 499,50 zł na miesiąc
  - C) Bez limitu
  - D) 100 000 zł rocznie

Odpowiedzi: B, B, B, A
