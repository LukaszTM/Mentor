# Strona internetowa: HTML (treść) i CSS (wygląd), także na telefonie
Tydzień 9 · lekcja 28 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** czytasz i zlecasz stronę HTML z poprawną strukturą (lang, title, viewport, nagłówki, formularz z etykietami, alt obrazków) i prostym CSS, który działa na telefonie.

**Po co mi to?** Strona to najczęstsze pierwsze zlecenie vibe codera. Agent ją wygeneruje w minutę — Ty sprawdzasz, czy jest poprawna, dostępna i czytelna na telefonie.

## Czego potrzebujesz
- Przeglądarka (Edge/Chrome/Firefox).
- Edytor (VS Code zalecany).
- Lekcje etapu 1 (agent, Git).

## 1 · Wyjaśnienie od podstaw
### HTML — szkielet i treść
HTML opisuje, CZYM jest każdy fragment strony, za pomocą znaczników: `<h1>Tytuł</h1>`, `<p>akapit</p>`, `<a href="…">link</a>`. Przeglądarka czyta plik index.html i rysuje stronę.
```
<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pod Lipą — agroturystyka</title>
  <link rel="stylesheet" href="styl.css">
</head>
<body>
  <h1>Pod Lipą</h1>
  …
  <script src="kalkulator.js"></script>
</body>
</html>
```
| element | po co | co sprawdzasz u agenta |
|---|---|---|
| `lang="pl"` | czytniki ekranu czytają po polsku, wyszukiwarki znają język | jest w `<html>` |
| `meta charset` | polskie znaki | utf-8 |
| `meta viewport` | strona dopasowuje się do telefonu | dokładnie jak wyżej |
| `<title>` | nazwa karty i wyniku w wyszukiwarce | konkretna, nie „Document” |
| jeden `<h1>`, potem `<h2>` | struktura dokumentu | nagłówki w kolejności |
| `<img alt="…">` | opis obrazka dla niewidomych i gdy obrazek się nie wczyta | alt opisuje treść (nie „obrazek”) |
| `<label for="noce">` + `<input id="noce">` | kliknięcie w etykietę i czytniki ekranu | for = id |
### Formularz kalkulatora
`<label for="noce">Liczba nocy</label> <input id="noce" name="noce" type="number" min="1" value="2">` — type="number" daje klawiaturę numeryczną na telefonie, min blokuje 0 w przeglądarce (ale i tak sprawdzasz w kodzie!).
### CSS — wygląd
CSS w osobnym pliku styl.css: `body { font-family: system-ui, sans-serif; max-width: 40rem; margin: 0 auto; padding: 1rem; }`. Media query zmienia wygląd na wąskim ekranie: `@media (max-width: 600px) { … }`. Zasada: zaczynasz od wersji na telefon (jedna kolumna), szerszy ekran tylko powiększa odstępy.
### Dostępność — minimum, które sprawdzasz
Wytyczne WCAG (W3C) są standardem dostępności; w UE od 28.06.2025 obowiązuje Europejski akt w sprawie dostępności dla wielu usług cyfrowych (w Polsce ustawa o zapewnianiu spełniania wymagań dostępności niektórych produktów i usług). Mała agroturystyka może nie podlegać obowiązkowi (mikroprzedsiębiorcy świadczący usługi są wyłączeni), ale minimum i tak robisz zawsze: alt, label, kontrast tekstu, działanie klawiaturą (Tab).
### Jak sprawdzić stronę od agenta
- Otwórz index.html w przeglądarce (podwójne kliknięcie).
- F12 → narzędzia deweloperskie → ikona telefonu (tryb urządzenia) — jak wygląda na 375 px szerokości?
- Przejdź formularz samym Tab i Enter.
- Test w zadaniu sprawdza strukturę automatycznie.

## 2 · Demonstracja — krok po kroku
**Strona od agenta — przegląd w 10 minut**

```
<form id="kalkulator">
  <label for="noce">Liczba nocy</label>
  <input id="noce" name="noce" type="number" min="1" value="2">
  <label for="osoby">Liczba osób</label>
  <input id="osoby" name="osoby" type="number" min="1" value="2">
  <button type="submit">Policz koszt</button>
</form>
<p id="wynik" aria-live="polite"></p>
<img src="lipa.jpg" alt="Drewniany dom pod rozłożystą lipą, przed nim ławka">
```

1. Prośba: „Utwórz index.html i styl.css dla agroturystyki Pod Lipą: nagłówek, 3 sekcje (O nas, Pokoje, Kontakt), formularz kalkulatora z polami noce i osoby (label + input), miejsce na wynik, zdjęcie z opisem alt. lang=pl, viewport, bez frameworków, bez zewnętrznych czcionek.”
2. Otwierasz index.html: wygląda dobrze. F12 → tryb urządzenia 375 px: formularz wychodzi poza ekran — w CSS jest `width: 600px` na formularzu. Prośba: „formularz max-width: 100%”.
3. Przegląd kodu: `<img src="lipa.jpg" alt="image">` — alt bezużyteczny. Poprawiasz opis.
4. Tab po stronie: fokus przechodzi przez pola i przycisk — OK. Kliknięcie w napis „Liczba nocy” zaznacza pole — label działa.
5. „✔ Sprawdź wynik” — testy struktury zielone. Commit.

✔ **Oczekiwany wynik:** Strona z poprawną strukturą, działająca na telefonie i z sensownym alt; dwa błędy agenta złapane przeglądem, nie przez klientkę.

## 3 · Jak to uruchomić
1. Podwójne kliknięcie index.html w PRACA → przeglądarka; F12 → tryb urządzenia.
2. Zadanie tygodnia → „✔ Sprawdź wynik” (testy struktury HTML).

## W praktyce
- Każda strona: lang, title, viewport, alt, label — lista przed oddaniem.
- Test na telefonie przed pokazaniem klientowi.

## 4 · Ćwiczenie prowadzone
Przejrzyj fragment od agenta: `<html>` (bez lang), `<title>Document</title>`, `<img src="dom.jpg">`, `<input id="noce">` bez etykiety, brak meta viewport. Ile problemów z tabeli lekcji tu jest? Jaką wartość wpiszesz w atrybut lang? Czas: 15 minut.

📄 `cwiczenia/tydzien_09/strona_html_css_1.md` · rozwiązanie: `rozwiazania/tydzien_09/strona_html_css_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dopasuj: (1) strona za mała/za szeroka na telefonie, (2) czytnik ekranu nie wie, co jest na zdjęciu, (3) kliknięcie w napis „Liczba osób” nie zaznacza pola, (4) w wyszukiwarce wynik ma nazwę „Document”. Poprawki: meta viewport / alt / label for=id / title. Czas: 15 minut.

📄 `cwiczenia/tydzien_09/strona_html_css_2.md` · rozwiązanie: `rozwiazania/tydzien_09/strona_html_css_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Polskie znaki wyświetlają się jako krzaczki („Ä…”).**
  - Przyczyna: Brak meta charset utf-8 albo plik zapisany w innym kodowaniu.
  - Jak sprawdzić: Pierwsze linie head; kodowanie w edytorze (VS Code: prawy dolny róg).
  - Poprawka: `<meta charset="utf-8">` jako pierwszy element head; zapisz plik w UTF-8.
- ✘ **CSS nie działa.**
  - Przyczyna: Zła ścieżka w link href (wielkość liter, folder).
  - Jak sprawdzić: F12 → Console/Network: 404 dla styl.css?
  - Poprawka: href="styl.css" i plik obok index.html (albo poprawna ścieżka do folderu).
- ✘ **Na telefonie trzeba przewijać w bok.**
  - Przyczyna: Stała szerokość w px albo brak viewport.
  - Jak sprawdzić: F12 → tryb urządzenia.
  - Poprawka: max-width zamiast width, meta viewport.

## Pułapki
- Agent chętnie dodaje frameworki CSS i czcionki z zewnętrznych serwerów — to wolniej, zależność od obcych serwerów i kwestie RODO (adres IP gościa trafia do dostawcy czcionek). W kursie: czcionki systemowe.
- Zdjęcia z internetu „bo agent znalazł” — prawa autorskie. Używaj własnych zdjęć klienta albo z licencją (tydzień 12).

## Dodatkowe zadania
1. Zbuduj index.html i styl.css z agentem (zadanie tygodnia).
2. Sprawdź stronę w trybie urządzenia 375 px.
3. Przejdź formularz samą klawiaturą.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Po co meta viewport?**
  - Żeby strona dopasowała szerokość do ekranu telefonu.
- **Jak powiązać etykietę z polem?**
  - label for="x" i input id="x".
- **Co powinien zawierać alt?**
  - Opis treści obrazka ważnej dla odbiorcy, nie słowo „obrazek”.

## Co potrafię teraz bez patrzenia na przykład?
Czytasz i zlecasz poprawną strukturę HTML, prosty CSS z myślą o telefonie i minimum dostępności — i sprawdzasz to w przeglądarce oraz testem.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- MDN — Podstawy HTML (Learn web development) (dostęp 20.11.2026) — <https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content>
- MDN — Podstawy CSS i media queries (dostęp 20.11.2026) — <https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics>
- MDN — Formularze w HTML (label, input) (dostęp 20.11.2026) — <https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms>
- W3C — WCAG 2.2 w skrócie (Web Content Accessibility Guidelines) (dostęp 20.11.2026) — <https://www.w3.org/WAI/standards-guidelines/wcag/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Atrybut języka strony:
  - A) <html lang="pl">
  - B) <body pl>
  - C) <meta lang>
  - D) <title pl>
- Pole formularza bez etykiety — poprawka:
  - A) placeholder wystarczy
  - B) label for=id
  - C) większa czcionka
  - D) kolor
- Strona za szeroka na telefonie — najpierw sprawdzasz:
  - A) meta viewport i stałe szerokości w px
  - B) kolor tła
  - C) favicon
  - D) title
- Plik z wyglądem strony to zwykle:
  - A) index.html
  - B) styl.css
  - C) kalkulator.js
  - D) README.md

Odpowiedzi: A, B, A, B
