# Automatyzacje: skrypt porządkujący pliki z trybem próby i harmonogram
Tydzień 11 · lekcja 35 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** zlecasz i sprawdzasz skrypt, który porządkuje pliki (z obowiązkowym trybem próby, bez nadpisywania), oraz uruchamiasz go automatycznie Harmonogramem zadań Windows.

**Po co mi to?** „Codziennie przenoszę faktury i zdjęcia do folderów” — klienci płacą za oszczędzony czas. Skrypt działający na prawdziwych plikach musi być bezpieczny, bo pomyłka niszczy dane.

## Czego potrzebujesz
- Lekcje „Pliki, foldery…” i „Terminal”.
- Folder testowy z kopiami plików (NIE prawdziwe dokumenty przy pierwszych próbach).

## 1 · Wyjaśnienie od podstaw
### Zasady bezpiecznej automatyzacji plików
| zasada | jak w kodzie |
|---|---|
| najpierw tryb próby | `uporzadkuj(katalog, wykonaj=False)` tylko zwraca plan „plik → cel”, nic nie zmienia |
| nigdy nie nadpisuj | gdy cel istnieje: `faktura_1.pdf`, `faktura_2.pdf`… |
| nie usuwaj | przenoś; kasowanie zostaw człowiekowi |
| działaj tylko w podanym katalogu | bez rekurencji w górę, bez ścieżek absolutnych z danych |
| zapisuj, co zrobiłeś | log: data, plik, skąd, dokąd |
| najpierw na kopii | folder testowy przed prawdziwym |
### pathlib i shutil
`from pathlib import Path`: `Path(katalog).iterdir()` — zawartość folderu, `p.suffix.lower()` — rozszerzenie (`.JPG` → `.jpg`), `p.is_file()`, `cel.exists()`, `(katalog / "zdjecia").mkdir(exist_ok=True)`. `shutil.move(str(p), str(cel))` przenosi. Path działa tak samo w Windows i Linuksie.
### Reguły porządkowania (zadanie tygodnia)
| rozszerzenia | folder |
|---|---|
| .jpg .jpeg .png .heic | zdjecia |
| .pdf .doc .docx | dokumenty |
| .csv .xlsx .xls | dane |
| pozostałe pliki | inne |
Foldery i pliki ukryte (zaczynające się od kropki) pomijasz. Plik bez rozszerzenia → inne.
### Harmonogram zadań Windows
Graficznie: Start → „Harmonogram zadań” → Utwórz zadanie podstawowe → codziennie 20:00 → Uruchom program: pełna ścieżka do python.exe środowiska kursu, argument: pełna ścieżka do skryptu. Z wiersza poleceń: `schtasks /create /sc daily /tn "PodLipa_porzadki" /tr "\"C:\…\python.exe\" \"C:\…\porzadki.py\" --wykonaj" /st 20:00`. Sprawdzenie: `schtasks /query /tn "PodLipa_porzadki"`, usunięcie: `schtasks /delete /tn "PodLipa_porzadki"`.
Skrypt uruchamiany z harmonogramu nie ma okna — dlatego log w pliku jest jedynym śladem jego pracy.
### Agent a pliki poza projektem
Agent pracuje w katalogu projektu; skrypt, który napisał, uruchamiasz TY na wskazanym folderze. Nie dawaj agentowi dostępu do całego dysku „żeby sam poprzenosił”.

## 2 · Demonstracja — krok po kroku
**Tryb próby ratuje 200 zdjęć**

```
from pathlib import Path

REGULY = {".jpg": "zdjecia", ".png": "zdjecia", ".pdf": "dokumenty", ".csv": "dane"}

def cel_dla(nazwa):
    return REGULY.get(Path(nazwa).suffix.lower(), "inne")

for n in ["Lipa.JPG", "faktura.pdf", "notatka", "goscie.csv", "plan.txt"]:
    print(n, "->", cel_dla(n))

```

1. Agent napisał porzadki.py. Tworzysz folder testowy z 6 kopiami plików, w tym zdjecia/lipa.jpg i drugi lipa.jpg w korzeniu.
2. Tryb próby: plan pokazuje „lipa.jpg → zdjecia/lipa.jpg” — konflikt nazw! Kod agenta użyłby shutil.move, który w tej sytuacji nadpisałby istniejący plik.
3. Prośba: „gdy cel istnieje, dodaj _1, _2… przed rozszerzeniem; dodaj test na konflikt”. Plan: „lipa.jpg → zdjecia/lipa_1.jpg”.
4. Uruchomienie z --wykonaj na kopii: pliki przeniesione, log zawiera 6 linii. Porównujesz liczbę plików przed i po — zgodna.
5. Dopiero teraz harmonogram na prawdziwy folder — z logiem.

✔ **Oczekiwany wynik:** Skrypt bez nadpisywania i bez usuwania, sprawdzony trybem próby i na kopii, uruchamiany codziennie z logiem.

## 3 · Jak to uruchomić
1. `python porzadki.py C:\sciezka\folder_testowy` (tryb próby), potem z `--wykonaj`.
2. Harmonogram zadań → Utwórz zadanie podstawowe albo `schtasks /create …`.

## W praktyce
- Każdy skrypt na plikach klienta: tryb próby jako domyślny.
- Log w pliku z datą przy każdej automatyzacji.

## 4 · Ćwiczenie prowadzone
Co wypisze przykład lekcji? Wpisz cel (folder) dla: (1) Lipa.JPG, (2) notatka (bez rozszerzenia), (3) plan.txt. Dlaczego Lipa.JPG trafia do zdjęć mimo wielkich liter? Czas: 15 minut.

📄 `cwiczenia/tydzien_11/automatyzacje_1.md` · rozwiązanie: `rozwiazania/tydzien_11/automatyzacje_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
W folderze jest już `dokumenty/faktura.pdf` oraz `dokumenty/faktura_1.pdf`. Porządkujesz nowy `faktura.pdf`. Jaką nazwę dostanie według zasady „nie nadpisuj”? Drugie: jakie polecenie pokaże, czy zadanie harmonogramu „PodLipa_porzadki” istnieje (pierwsze dwa słowa polecenia)? Czas: 15 minut.

📄 `cwiczenia/tydzien_11/automatyzacje_2.md` · rozwiązanie: `rozwiazania/tydzien_11/automatyzacje_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Pliki zniknęły / zostały nadpisane.**
  - Przyczyna: shutil.move do istniejącej nazwy, brak trybu próby.
  - Jak sprawdzić: Kosz, kopia zapasowa, log.
  - Poprawka: Zasada „nie nadpisuj” + test konfliktu + zawsze najpierw tryb próby na kopii.
- ✘ **Zadanie harmonogramu „działa”, ale nic się nie dzieje.**
  - Przyczyna: Względne ścieżki albo inny Python (bez bibliotek) w harmonogramie.
  - Jak sprawdzić: Historia zadania w Harmonogramie, plik logu.
  - Poprawka: Pełne ścieżki do python.exe środowiska kursu i do skryptu; katalog roboczy jako argument.
- ✘ **„PermissionError: [WinError 32] The process cannot access the file”.**
  - Przyczyna: Plik otwarty w innym programie (np. Excel) albo synchronizowany przez OneDrive.
  - Jak sprawdzić: Czy plik jest otwarty?
  - Poprawka: Pomiń plik z wpisem w logu zamiast przerywać całość; uruchamiaj, gdy pliki nie są używane.

## Pułapki
- Skrypt z „rekursywnym” przeszukiwaniem (`rglob`) na folderze Dokumenty może przenieść pliki z podfolderów programów — działaj tylko na jednym poziomie, chyba że specyfikacja mówi inaczej.
- Automatyczne usuwanie plików zostawiasz człowiekowi; skrypt najwyżej przenosi do folderu „do_usuniecia”.

## Dodatkowe zadania
1. Zbuduj porzadki.py z trybem próby i bez nadpisywania (zadanie tygodnia).
2. Przetestuj na kopii plików.
3. Opcjonalnie: zadanie w Harmonogramie z logiem.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Po co tryb próby?**
  - Żeby zobaczyć plan zmian bez dotykania plików i wyłapać konflikty.
- **Co robisz, gdy plik o tej nazwie już jest w celu?**
  - Dodaję numer _1, _2… — nigdy nie nadpisuję.
- **Dlaczego log jest obowiązkowy przy harmonogramie?**
  - Skrypt działa bez okna — log to jedyny ślad, co zrobił.

## Co potrafię teraz bez patrzenia na przykład?
Zlecasz i sprawdzasz bezpieczną automatyzację plików: tryb próby, brak nadpisywania i usuwania, log, test na kopii i uruchamianie z Harmonogramu zadań.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — pathlib (ścieżki niezależne od systemu) (dostęp 20.11.2026) — <https://docs.python.org/3/library/pathlib.html>
- Python — shutil.move i operacje na plikach (dostęp 20.11.2026) — <https://docs.python.org/3/library/shutil.html>
- Microsoft Learn — schtasks create (Harmonogram zadań z wiersza poleceń) (dostęp 20.11.2026) — <https://learn.microsoft.com/windows-server/administration/windows-commands/schtasks-create>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Pierwsze uruchomienie skryptu porządkującego:
  - A) Od razu na prawdziwych plikach
  - B) Tryb próby na kopii
  - C) Jako administrator
  - D) Bez logu
- `Path("Foto.PNG").suffix.lower()` to:
  - A) "PNG"
  - B) ".png"
  - C) "Foto"
  - D) "png"
- Skrypt ma usuwać duplikaty automatycznie. Zasada kursu:
  - A) Tak, od razu
  - B) Przenieś do folderu do decyzji człowieka
  - C) Usuń i nie loguj
  - D) Usuń cały folder
- Polecenie tworzące zadanie w Harmonogramie z wiersza poleceń:
  - A) schtasks /create
  - B) cron add
  - C) at now
  - D) task new

Odpowiedzi: B, B, B, A
