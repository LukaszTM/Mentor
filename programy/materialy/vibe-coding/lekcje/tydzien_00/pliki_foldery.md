# Pliki, foldery, rozszerzenia i ścieżki
Tydzień 0 · lekcja 3 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** pokazujesz rozszerzenia plików, rozumiesz ścieżkę C:\Users\Ty\Documents\..., rozpakowujesz ZIP i wiesz, gdzie Mentor trzyma Twoje pliki.

**Po co mi to?** Agent AI pracuje na plikach w konkretnym folderze — jeśli nie wiesz, gdzie on jest, nie sprawdzisz, co agent zmienił.

## Czego potrzebujesz
- Windows 10/11, Eksplorator plików (Win + E).
- Katalog roboczy kursu utworzony w Mentorze (Mój projekt → „📁 Utwórz katalog roboczy kursu”).

## 1 · Wyjaśnienie od podstaw
### Plik i folder
Plik to porcja danych z nazwą (dokument, zdjęcie, program). Folder (katalog — w programowaniu mówi się raczej „katalog”) to pudełko na pliki i inne foldery. Projekt programistyczny to po prostu folder z plikami: kodem (.py, .html, .js), danymi (.csv, .json) i opisami (.md).
### Rozszerzenie mówi, czym jest plik
Rozszerzenie to końcówka nazwy po kropce: `raport.csv`, `app.py`, `index.html`. Windows domyślnie UKRYWA rozszerzenia — wtedy plik `notatki.txt.py` wygląda jak `notatki.txt`. Pierwsza rzecz w tym kursie: włącz pokazywanie rozszerzeń. Windows 11: Eksplorator → Widok → Pokaż → „Rozszerzenia nazw plików”. Windows 10: Eksplorator → karta Widok → zaznacz „Rozszerzenia nazw plików”.
| rozszerzenie | co to | czym otwierasz |
|---|---|---|
| .py | program w Pythonie | edytor (VS Code, PyCharm, Notatnik); uruchamia go Python |
| .md | notatka w Markdown (nagłówki #, listy -) | edytor; GitHub pokazuje ją ładnie |
| .html / .css / .js | strona internetowa: treść / wygląd / zachowanie | przeglądarka (podwójne kliknięcie .html) i edytor |
| .csv | tabela w tekście, kolumny oddzielone przecinkiem lub średnikiem | edytor, arkusz |
| .json | dane w nawiasach { } — format wymiany między programami | edytor |
| .zip | spakowane archiwum wielu plików | Eksplorator → „Wyodrębnij wszystkie” |
### Ścieżka — adres pliku
Ścieżka to adres pliku na dysku: `C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA\app.py`. Czytasz ją od lewej: dysk C:, folder Users, folder użytkownika, Dokumenty (na dysku folder nazywa się „Documents”) itd. Separator w Windows to ukośnik wsteczny `\`; w Pythonie i w internecie zwykle `/` — Python w Windows rozumie oba.
- Ścieżka bezwzględna zaczyna się od dysku: `C:\...`.
- Ścieżka względna liczy się od bieżącego folderu: `dane\rezerwacje.csv` znaczy „folder dane w miejscu, w którym jestem”.
- Spacje i polskie znaki w nazwach działają, ale w terminalu ścieżkę ze spacją trzeba ująć w cudzysłów. Dlatego w projektach używamy nazw bez spacji i bez polskich liter: `lista_gosci.py`.
### Gdzie są Twoje pliki w tym kursie
- Katalog roboczy (PRACA): `Dokumenty\Mentor\vibe-coding\PRACA` — tu powstają wszystkie pliki zadań i tu pracuje agent. Mentor → Mój projekt pokazuje dokładną ścieżkę.
- Materiały kursu (lekcje, przykłady, rozwiązania, testy): kopiujesz je przyciskiem „📂 Skopiuj materiały kursu tutaj” — Mentor nie nadpisuje Twoich plików.
### ZIP
Kurs i programy często przychodzą jako .zip. Nie pracuj „w środku” ZIP-a (podwójne kliknięcie tylko pokazuje zawartość) — najpierw prawy przycisk → „Wyodrębnij wszystkie…”.

## 2 · Demonstracja — krok po kroku
**Od ZIP-a do pliku z widocznym rozszerzeniem**

```
Struktura katalogu roboczego po tygodniu 3 (tak ma wyglądać u Ciebie):

PRACA\
├── notatki\
│   └── o_mnie.md
├── dane\
│   └── rezerwacje.csv
├── witaj.py
├── kalkulator_pobytu.py
└── dziennik.md
```

1. Win + E otwiera Eksplorator. Włącz „Rozszerzenia nazw plików” (Widok → Pokaż). Od teraz widzisz `dziennik.md`, a nie `dziennik`.
2. Mentor → Mój projekt → „Otwórz folder” — Eksplorator otwiera katalog PRACA. Pasek adresu na górze: kliknij w niego, zobaczysz pełną ścieżkę (zaznacz i skopiuj Ctrl+C — przyda się agentowi).
3. W PRACA: prawy przycisk → Nowy → Folder → nazwa `notatki`. W środku: prawy przycisk → Nowy → Dokument tekstowy → zmień nazwę na `o_mnie.md` (Windows zapyta, czy zmienić rozszerzenie — Tak).
4. Otwórz `o_mnie.md` Notatnikiem (prawy przycisk → Otwórz za pomocą → Notatnik), wpisz trzy linie: `# O mnie`, `- uczę się vibe codingu`, `- cel: …`, zapisz Ctrl+S.
5. Sprawdź: w Eksploratorze plik ma nazwę `o_mnie.md`, a nie `o_mnie.md.txt`. Jeśli widzisz `.txt` na końcu — rozszerzenia były ukryte przy tworzeniu; zmień nazwę.

✔ **Oczekiwany wynik:** W PRACA jest folder notatki z plikiem o_mnie.md; widzisz rozszerzenia i znasz pełną ścieżkę katalogu roboczego.

## 3 · Jak to uruchomić
1. Win + E → Widok → Pokaż → Rozszerzenia nazw plików (Windows 11).
2. Mentor → Mój projekt → „Otwórz folder”.

## W praktyce
- Przed każdą sesją z agentem sprawdź, w jakim folderze jesteś.
- Nazwy plików: małe litery, bez spacji i polskich znaków.

## 4 · Ćwiczenie prowadzone
Przeanalizuj ścieżkę `C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA\dane\rezerwacje.csv`. Odpowiedz: jak nazywa się plik (z rozszerzeniem), jakie ma rozszerzenie (bez kropki), w jakim folderze bezpośrednio leży, i jaka jest jego ścieżka względna, jeśli jesteś w folderze PRACA. Czas: 15 minut.

📄 `cwiczenia/tydzien_00/pliki_foldery_1.md` · rozwiązanie: `rozwiazania/tydzien_00/pliki_foldery_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dostajesz plik `cennik.pdf.exe` z załącznika maila od „klienta”. Co to jest naprawdę (jakie rozszerzenie decyduje)? Czy go otworzysz? Druga sytuacja: plik `notatki.txt` po włączeniu rozszerzeń okazuje się nazywać `notatki.txt.txt` — ile kropek ma pełna nazwa? Czas: 15 minut.

📄 `cwiczenia/tydzien_00/pliki_foldery_2.md` · rozwiązanie: `rozwiazania/tydzien_00/pliki_foldery_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Plik nazywa się `witaj.py.txt` i Python mówi „can't open file 'witaj.py'”.**
  - Przyczyna: Notatnik dopisał .txt, a rozszerzenia były ukryte.
  - Jak sprawdzić: Włącz rozszerzenia w Eksploratorze i spójrz na pełną nazwę.
  - Poprawka: Zmień nazwę na `witaj.py`; w Notatniku przy zapisie wybierz „Wszystkie pliki (*.*)”.
- ✘ **„Nie mogę znaleźć pliku, który utworzył agent”.**
  - Przyczyna: Agent pracował w innym folderze niż myślisz.
  - Jak sprawdzić: Mentor → Mój projekt → ścieżka; w terminalu `cd` pokazuje bieżący folder.
  - Poprawka: Uruchamiaj agenta zawsze w katalogu PRACA (przycisk „Otwórz Claude Code tutaj”).
- ✘ **Program nie widzi pliku `dane\rezerwacje.csv`.**
  - Przyczyna: Uruchomiony z innego folderu — ścieżka względna liczy się od bieżącego folderu.
  - Jak sprawdzić: Sprawdź, gdzie jest terminal (`cd` bez argumentów).
  - Poprawka: Uruchamiaj programy z katalogu PRACA albo użyj ścieżki bezwzględnej.

## Pułapki
- Spacje i polskie znaki w nazwach plików projektu utrudniają pracę w terminalu — używaj `male_litery_z_podkresleniem`.
- Nie trzymaj projektu na Pulpicie synchronizowanym z OneDrive — synchronizacja potrafi blokować pliki w trakcie pracy agenta. Katalog PRACA w Dokumentach jest bezpieczniejszy (jeśli Dokumenty też są w OneDrive, wybierz w Mentorze inny katalog, np. C:\Projekty).

## Dodatkowe zadania
1. Włącz rozszerzenia i znajdź na dysku 3 pliki o różnych rozszerzeniach z tabeli lekcji.
2. Utwórz w PRACA foldery `notatki` i `dane`.
3. Rozpakuj dowolny ZIP („Wyodrębnij wszystkie”) i sprawdź, czy rozumiesz strukturę folderów.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Dlaczego trzeba włączyć widoczne rozszerzenia?**
  - Bo Windows je ukrywa — nie odróżnisz `app.py` od `app.py.txt`, a oszustwa typu `faktura.pdf.exe` stają się niewidoczne.
- **Czym różni się ścieżka bezwzględna od względnej?**
  - Bezwzględna zaczyna się od dysku (C:\...), względna liczy się od bieżącego folderu (dane\plik.csv).
- **Gdzie powstają pliki zadań w tym kursie?**
  - W katalogu roboczym PRACA (Dokumenty\Mentor\vibe-coding\PRACA, dokładna ścieżka w Mój projekt).

## Co potrafię teraz bez patrzenia na przykład?
Widzisz rozszerzenia, czytasz ścieżki bezwzględne i względne, znasz katalog PRACA i rozpakowujesz ZIP przed pracą.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Microsoft — Jak pokazać rozszerzenia nazw plików w Eksploratorze plików (dostęp 19.11.2026) — <https://support.microsoft.com/windows/common-file-name-extensions-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01>
- Microsoft Learn — polecenia wiersza poleceń Windows (cd, dir, mkdir, type) (dostęp 19.11.2026) — <https://learn.microsoft.com/windows-server/administration/windows-commands/windows-commands>
- Claude Code — przewodnik po terminalu dla nowych użytkowników (oficjalna dokumentacja) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/terminal-guide>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Jakie rozszerzenie ma program w Pythonie?
  - A) .txt
  - B) .py
  - C) .exe
  - D) .md
- Plik `zdjecie.jpg.exe` to:
  - A) Zdjęcie
  - B) Program wykonywalny
  - C) Dokument
  - D) Archiwum
- Jesteś w folderze PRACA. Ścieżka `dane\goscie.csv` wskazuje:
  - A) C:\dane\goscie.csv
  - B) PRACA\dane\goscie.csv
  - C) Pulpit\goscie.csv
  - D) Nic
- Jak poprawnie otworzyć zawartość ZIP do pracy?
  - A) Podwójnym kliknięciem i edycją w środku
  - B) Prawy przycisk → Wyodrębnij wszystkie
  - C) Zmienić rozszerzenie na .py
  - D) Wysłać mailem

Odpowiedzi: B, B, B, B
