# MENTOR — STANDARD TWORZENIA KURSÓW
**Wersja:** 1.0  
**Przeznaczenie:** wszystkie nowe i aktualizowane kursy w aplikacji Mentor  
**Zasada nadrzędna:** *Najpierw wyjaśnij i pokaż, potem pozwól przećwiczyć, na końcu sprawdź samodzielność.*

## 1. Cel dokumentu

Dokument jest obowiązującą specyfikacją dla autora kursu — człowieka lub asystenta AI. Kurs ma prowadzić osobę uczącą się od jasno określonego poziomu początkowego do sprawdzalnych umiejętności, bez konieczności samodzielnego wyszukiwania plików, programów i instrukcji po internecie.

**Zakazane:** lekcje będące jedynie krótkim streszczeniem, zadania bez demonstracji potrzebnej umiejętności, polecenia typu „zainstaluj odpowiednie narzędzia” bez gotowej procedury, wymaganie nieomówionych pojęć oraz uznawanie samego istnienia pliku za dowód opanowania tematu.

## 2. Profil odbiorcy i poziomy trudności

1. Na początku kursu zapisz: wymagania wstępne, poziom (od podstaw / początkujący po kursie / średni), cel, liczbę tygodni, przewidywany czas dzienny, system operacyjny i konkretne umiejętności końcowe.
2. Nie zakładaj znajomości terminala, katalogów, instalacji zależności, Git ani składni, jeśli nie są wymienione w wymaganiach wstępnych i zweryfikowane w krótkiej diagnozie.
3. Zaproponuj na początku proste zadanie diagnostyczne, które **nie blokuje** nauki. Wynik służy do wskazania powtórki.
4. Ściągawki, dokumentacja, IDE i AI są dozwolone. Oceniaj rozumienie, poprawne działanie i zdolność wyjaśnienia rozwiązania, a nie pamięć składni.
5. Każdy następny moduł ma korzystać tylko z umiejętności już pokazanych i przećwiczonych; każdą nową zależność wyjaśnij przed jej użyciem.

## 3. Wymagany przebieg każdej lekcji

Każda lekcja obowiązkowo zawiera:

1. **Po co mi to?** Jednozdaniowe zastosowanie w prawdziwym projekcie.
2. **Cel w języku ucznia:** „Po tej lekcji potrafię…”.
3. **Wymagania:** czego uczeń potrzebuje i gdzie znajdują się pliki.
4. **Wyjaśnienie od podstaw:** każde nowe pojęcie prostym językiem, z analogią lub krótkim przykładem; bez nieobjaśnionego żargonu.
5. **Demonstracja kompletna:** gotowy, działający przykład, który można uruchomić bez dopisywania niepokazanego kodu.
6. **Omówienie linia po linii:** co robi kod, dlaczego ta instrukcja jest potrzebna i co się stanie po zmianie jej wartości.
7. **Jak uruchomić:** dokładna ścieżka do pliku, komenda lub kliknięcia, oczekiwany wynik.
8. **Ćwiczenie prowadzone:** bardzo podobne do demonstracji, ze wskazówkami.
9. **Ćwiczenie samodzielne:** niewielka zmiana, która wymaga podjęcia decyzji, a nie jedynie kopiowania.
10. **Trzy poziomy pomocy:** (1) pytanie naprowadzające, (2) wskazanie konkretnego fragmentu, (3) częściowy przykład; pełne rozwiązanie w osobnym katalogu do samosprawdzenia.
11. **Typowe błędy i naprawa:** komunikat, prawdopodobna przyczyna, krok diagnostyczny i poprawka.
12. **Sprawdzenie i krótkie podsumowanie:** wynik działania, 2–4 pytania sprawdzające oraz pytanie „co potrafię teraz zrobić bez patrzenia na przykład?”.

**Reguła jakości:** jeżeli uczeń musi zgadywać, skąd wziąć plik, co kliknąć lub jaki wynik jest poprawny, lekcja jest niekompletna.

### Przykład wymaganego poziomu instrukcji

Zamiast: „Napisz test logowania Selenium”.

Użyj: „Otwórz `cwiczenia/05_selenium/login_start.py`. Uruchom `URUCHOM_CWICZENIE_05.bat`. Obejrzyj gotowy przykład `przyklady/05_selenium/login_demo.py`. W demonstracji `driver.get()` otwiera stronę, `find_element()` szuka pola, a `send_keys()` wpisuje tekst. Teraz w swoim pliku dodaj obsługę hasła na wzór pola loginu. Uruchom test ponownie. Prawidłowy wynik: komunikat `TEST PASSED` i kod wyjścia 0. Jeśli pojawia się `NoSuchElementException`, porównaj identyfikator pola z plikiem HTML w `projekty/qa_sandbox/`. Pierwsza wskazówka…”.

## 4. Zasady tworzenia ćwiczeń

- Każde zadanie ma jednoznaczny rezultat: plik, działający skrypt, test, raport lub zmianę w aplikacji.
- Zawsze podaj: punkt startowy, nazwy plików, instrukcję w małych krokach, oczekiwane zachowanie, sposób sprawdzenia i przewidywany czas.
- Zadania układaj w sekwencji **obserwuję → odtwarzam → modyfikuję → wykonuję samodzielnie → wyjaśniam**.
- Nie zadawaj projektu większego niż wcześniej przećwiczone elementy bez rozbicia go na kamienie milowe.
- Umożliwiaj powtórzenie ćwiczenia od czystego stanu; nie wymagaj kopiowania rozwiązania na istniejące pliki bez ostrzeżenia.
- Sprawdzanie obejmuje zarówno przypadek poprawny, jak i co najmniej jeden negatywny / błędny, gdy ma to sens.
- Dla zadań programistycznych dołącz oczekiwany wynik i, jeśli to możliwe, automatyczne testy. **PASS nie zastępuje wyjaśnienia wyniku.**
- Dla kursów wielotygodniowych przewidź regularne mini-projekty i jeden projekt końcowy z demonstracją działania.

## 5. Kompletność paczki — zero samodzielnego szukania

Uczeń pobiera **jedną paczkę ZIP**. W niej znajdują się wszystkie materiały i narzędzia, które można legalnie rozpowszechniać:

```text
NAZWA_KURSU/
├── START_TUTAJ.md
├── SPRAWDZ_SRODOWISKO.bat
├── INSTALACJA.bat
├── URUCHOM_KURS.bat
├── kurs_mentor.json
├── manifest.json
├── instalatory/            # legalne do redystrybucji pliki, zależności offline
├── lekcje/                 # rozwinięte materiały i przykłady
├── przyklady/               # kompletne działające programy
├── cwiczenia/               # pliki startowe, dane, zadania
├── rozwiazania/             # rozwiązania, wskazówki, omówienie
├── projekty/                # lokalne strony, API, bazy i inne sandboxy
├── testy/                   # testy poprawności i diagnostyka
└── pomoc/                   # FAQ, komunikaty błędów, odzyskiwanie
```

To struktura **wzorcowa**, nie obietnica, że każda z tych funkcji już istnieje w aplikacji Mentor.

1. Dołącz wszystkie własne pliki lekcji, dane przykładowe, projekty, skrypty, konfiguracje i rozwiązania.
2. Jeśli zależność może być legalnie dołączona (np. pakiet Pythona), dostarcz ją offline wraz z informacją o licencji i wersji.
3. Jeśli pliku **nie wolno lub nie da się dołączyć**, uczeń nadal nie może go wyszukiwać: umieść dokładny oficjalny adres, nazwę i wersję; najlepiej udostępnij przycisk/skrypt pobrania z weryfikacją integralności. **Nie nazywaj takiej ścieżki instalacją offline.**
4. Nie załączaj pirackich kopii, cudzych płatnych materiałów, tokenów API, haseł ani prywatnych danych.
5. Jeśli zadanie wymaga internetu, płatnej usługi, konta, klucza API lub przeglądarki o konkretnej wersji — wyraźnie napisz o tym **przed rozpoczęciem kursu**, podaj koszt lub informację o nieznanej opłacie i oferuj lokalną alternatywę, gdy to możliwe.
6. Linki do dokumentacji służą pogłębianiu wiedzy, **nie mogą być jedynym źródłem koniecznym do wykonania obowiązkowego ćwiczenia**.

## 6. Instalacja i uruchomienie na Windows

- `START_TUTAJ.md` prowadzi ucznia od rozpakowania ZIP do pierwszego działającego ćwiczenia.
- `SPRAWDZ_SRODOWISKO.bat` informuje po polsku, co wykrył, czego brakuje i jaki jest następny krok. Nie wprowadza zmian.
- `INSTALACJA.bat` informuje, co zainstaluje i gdzie, oraz prosi o potwierdzenie przed zmianami. Korzysta z lokalnych plików lub kontrolowanego pobrania oficjalnego źródła.
- Preferuj instalację bez uprawnień administratora; środowisko zależności oddziel od systemowego Pythona (np. `.venv`).
- Uwzględnij ścieżki ze spacjami i polskimi znakami, brak dostępu do internetu, odmowę uprawnień, brak miejsca na dysku i możliwość ponownego uruchomienia instalatora.
- Wersje narzędzi i bibliotek muszą być określone i testowane; instalator nie może pobierać przypadkowych „najnowszych” wersji bez kontroli zgodności.
- Użytkownik musi wiedzieć, jak wycofać zmiany, zresetować zadanie i odinstalować środowisko kursu.
- Wszystkie skrypty instalacyjne są jawne i czytelne, a ich działanie opisane w dokumentacji.

## 7. Nauka z asystentem AI

Asystent ma być **nauczycielem i recenzentem**, nie automatem do oddawania gotowych odpowiedzi.

1. Najpierw zapytaj ucznia, co już rozumie i jaki ma pomysł.
2. Wyjaśniaj trudność małymi krokami. Nie wymagaj samodzielnej walki przez sztywny czas, gdy uczeń nie wie nawet, jak zacząć.
3. Udzielaj pomocy stopniowo: pytanie → wskazówka → fragment przykładu → pełne rozwiązanie na prośbę, z omówieniem.
4. Pozwól korzystać ze ściągawek i generowania kodu, ale proś ucznia o wyjaśnienie własnymi słowami, uruchomienie i przetestowanie rezultatu.
5. Przy błędzie pokazuj, jak znaleźć jego przyczynę, zamiast wyłącznie podawać poprawiony kod.
6. Oznacz, kiedy AI wymaga osobnego konta, internetu lub opłat. Każde podstawowe zadanie powinno mieć ścieżkę niewymagającą płatnego modelu, o ile cele kursu na to pozwalają.
7. Nie wysyłaj automatycznie kodu użytkownika, haseł, tokenów ani prywatnych plików do usługi zewnętrznej bez czytelnej zgody.

## 8. Powtórki, quizy i ocena postępów

- Co najmniej jedna rozbudowana powtórka na moduł: przypomnienie pojęć, przykłady, typowe błędy, zadanie prowadzone i zadanie samodzielne.
- Nie ograniczaj powtórki do listy haseł lub trzech lakonicznych zdań.
- Pytania powinny badać rozumienie i zastosowanie, a nie zgadywanie definicji. Każda odpowiedź zawiera wyjaśnienie.
- Zapewnij powrót do tematów, z którymi uczeń miał trudność, bez karania za przerwy w nauce.
- Zaliczenie umiejętności to działające zadanie **plus** umiejętność wyjaśnienia, co i dlaczego działa. Obecność pliku lub zdobycie XP to tylko pomocnicza informacja o postępie.
- Wprowadź zadania diagnostyczne po każdym większym etapie; w razie niepowodzenia zaproponuj konkretne lekcje do powtórzenia.

## 9. Zgodność techniczna z Mentorem

Kurs importowany do obecnej aplikacji musi stosować format **`mentor-program/1`** zgodnie z plikiem `programy/FORMAT.md` dostarczonym z Mentorem.

**Obowiązkowe struktury w JSON:**

- `nazwa` — czytelna nazwa kursu;
- `etapy` — etapy z numerami, listą tygodni i celami;
- `tygodnie` — tygodnie z odwołaniami do lekcji i listą zadań;
- `lekcje` — lekcje z identyfikatorem, nazwą i wyjaśnieniem.

**Zadanie** powinno mieć: unikalne `id`, `tytul`, `opis`, `kroki`, `sprawdz`, `problemy`, `pliki`, `xp` i `czas_min`.  
**Lekcja** powinna mieć: `id`, `tydzien`, `nazwa`, `slowa`, `wyjasnienie`, `przyklad`, `zadania`, `pytania`, `pulapki` i `test`.  
**Quiz**: odpowiedź `odp` to numer opcji **od zera**.

**Zasady techniczne:**

1. Wszystkie `id` zadań są unikalne i stabilne między aktualizacjami — Mentor używa ich do zapisywania postępów.
2. Wszystkie odwołania do lekcji, etapów i tygodni wskazują istniejące elementy.
3. Pola `pliki` odnoszą się do rzeczywiście przewidzianych artefaktów ćwiczenia. Mentor wykrywa ich istnienie, **ale samo wykrycie nie oznacza zaliczenia**.
4. Kod w `przyklad` oraz instrukcje w `kroki` mają być kompletne, testowane i zgodne z plikami w ZIP.
5. Zmiana treści kursu zwiększa `wersja`; nie zmieniaj istniejącego `id` kursu ani ćwiczeń bez przemyślanej migracji postępów.
6. Przed wydaniem przetestuj import JSON przez aktualną wersję Mentora. Dodatkowe pliki w ZIP **nie są automatycznie importowane** przez przycisk „Wgraj program z pliku…” — `START_TUTAJ.md` musi wyjaśniać, gdzie umieścić katalog ćwiczeń i jak go wskazać w aplikacji.

## 10. Testy jakości przed publikacją

Autor kursu ma wykonać następujące testy:

- **Import:** JSON jest prawidłowy; Mentor przyjmuje kurs; wyświetla wszystkie etapy, tygodnie, lekcje, zadania i quizy.
- **Świeży komputer/środowisko:** osoba bez wcześniejszej konfiguracji potrafi uruchomić pierwszą lekcję, używając wyłącznie zawartości ZIP i jasno wskazanych kroków pobierania, jeżeli konieczne.
- **Offline:** zadania deklarowane jako offline działają przy odłączonej sieci.
- **Przejście ucznia:** ktoś nieznający kursu wykonuje pierwsze dwa zadania bez pomocy autora. Zapisz wszystkie punkty, w których musi zgadywać.
- **Ćwiczenia:** uruchamiają się przykłady, rozwiązania i testy kontrolne; wyniki zgadzają się z opisem.
- **Błędy:** przetestuj co najmniej brak zależności, błędną ścieżkę, niewłaściwą wersję, zajęty port i brak internetu (gdy dotyczy).
- **Dostępność:** czytelne polskie instrukcje, oznaczenia kodu, kontrast, brak zależności od samego koloru, użycie bez długich sesji.
- **Aktualizacja:** ponowny import / nowa wersja nie niszczy postępów; kopia zapasowa i procedura przywrócenia są opisane.
- **Licencje i bezpieczeństwo:** zweryfikowano licencje wszystkich dołączonych plików, źródła pobrań i brak sekretów.

## 11. Kryteria publikacji — obowiązkowa checklista

Kurs można oznaczyć jako **GOTOWY**, dopiero gdy wszystkie odpowiedzi brzmią TAK:

- [ ] Uczeń od razu wie, co będzie umiał po kursie i ile czasu nauka zajmie.
- [ ] Każda lekcja wyjaśnia nowy temat, pokazuje działający przykład i omawia go krok po kroku.
- [ ] Żadne zadanie nie wymaga umiejętności, których wcześniej nie pokazano.
- [ ] Wszystkie obowiązkowe pliki startowe, dane, przykłady i rozwiązania są w paczce.
- [ ] Narzędzia i zależności są dołączone legalnie lub pobierane z dokładnie wskazanego oficjalnego źródła bez ręcznego wyszukiwania.
- [ ] Uczeń potrafi zainstalować lub uruchomić środowisko według instrukcji, także gdy pojawi się typowy błąd.
- [ ] W każdym zadaniu jest oczekiwany wynik, instrukcja sprawdzenia i stopniowane podpowiedzi.
- [ ] Quizy i powtórki zawierają wyjaśnienia, a postępy odzwierciedlają wykonanie pracy, nie tylko kliknięcia.
- [ ] Przykłady i pliki rzeczywiście działają na deklarowanym systemie i w deklarowanych wersjach narzędzi.
- [ ] JSON `mentor-program/1` przechodzi walidację oraz import w docelowej wersji Mentora.
- [ ] ZIP nie zawiera sekretów, pirackich plików ani zależności o niezweryfikowanej licencji.
- [ ] Osoba testująca, niebędąca autorem kursu, potrafi rozpocząć naukę bez dopytywania o podstawowe kroki.

**Jeżeli choć jeden punkt obowiązkowy nie jest spełniony, kurs ma status DO POPRAWY, a nie GOTOWY.**

## 12. Instrukcja dla AI tworzącego kursy

> Twórz kursy do aplikacji Mentor według dokumentu „MENTOR — STANDARD TWORZENIA KURSÓW, v1.0”. Najpierw ustal poziom ucznia i cele. Następnie stwórz kompletny plan oraz wszystkie lekcje z wyjaśnieniami, działającymi przykładami omówionymi linia po linii, ćwiczeniami prowadzonymi, samodzielnymi, trzema poziomami podpowiedzi i metodami sprawdzenia. Przygotuj jedną paczkę ZIP ze wszystkimi dozwolonymi do rozpowszechniania narzędziami i plikami. Nie odsyłaj ucznia do samodzielnego szukania materiałów. Jeśli zależności nie można dołączyć, zapewnij dokładną oficjalną ścieżkę pobrania i kontrolowaną instalację. Plik programu musi być zgodny z formatem `mentor-program/1`. Przetestuj import, instrukcje uruchamiania, przykłady i zadania. Nie deklaruj kursu jako gotowego, dopóki nie przejdzie checklisty publikacyjnej.
