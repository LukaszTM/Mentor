# JavaScript na stronie: formularz liczy koszt bez serwera
Tydzień 9 · lekcja 29 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** czytasz prosty skrypt JS (funkcja, zdarzenie submit, odczyt pól, wypisanie wyniku), sprawdzasz go w konsoli przeglądarki i zlecasz agentowi kalkulator z obsługą złych danych.

**Po co mi to?** Kalkulator ceny na stronie to typowe pierwsze „żywe” zlecenie. JavaScript działa w przeglądarce gościa — błędy widać od razu u klienta.

## Czego potrzebujesz
- Lekcja „Strona internetowa: HTML i CSS”.
- Przeglądarka z narzędziami deweloperskimi (F12).

## 1 · Wyjaśnienie od podstaw
### Ten sam pomysł co w Pythonie, inny zapis
| Python | JavaScript |
|---|---|
| `def koszt(noce, osoby):` | `function obliczKoszt(noce, osoby) {` |
| wcięcia | nawiasy klamrowe `{ }` i średniki |
| `if noce >= 7:` | `if (noce >= 7) {` |
| `raise ValueError` | `throw new Error("…")` |
| `int("3")` | `Number("3")` (albo `parseInt`) |
| `print(x)` | `console.log(x)` (konsola F12) |
### DOM — strona jako obiekty
`document.querySelector("#noce")` znajduje element o id="noce". `.value` to wpisany tekst (ZAWSZE napis — jak input() w Pythonie!). `document.querySelector("#wynik").textContent = "…"` wypisuje wynik na stronie.
### Zdarzenia
```
document.querySelector("#kalkulator").addEventListener("submit", (e) => {
  e.preventDefault();               // nie przeładowuj strony
  const noce = Number(document.querySelector("#noce").value);
  const osoby = Number(document.querySelector("#osoby").value);
  try {
    const koszt = obliczKoszt(noce, osoby);
    document.querySelector("#wynik").textContent = `Koszt: ${koszt.toFixed(2)} zł`;
  } catch (err) {
    document.querySelector("#wynik").textContent = err.message;
  }
});
```
`e.preventDefault()` jest kluczowe: bez niego przeglądarka wyśle formularz i przeładuje stronę — wynik mignie i zniknie.
### Dwie pułapki JS, które łapiesz u agenta
- `"3" + 2` daje `"32"` (sklejenie), `"3" * 2` daje 6. Dlatego Number() na wartościach pól.
- `Number("")` daje 0, a `Number("abc")` daje `NaN` (nie-liczba). Walidacja: `if (!Number.isInteger(noce) || noce < 1) throw new Error("Podaj liczbę nocy (co najmniej 1)")`.
### Logika osobno, strona osobno
Funkcję `obliczKoszt` trzymaj bez odwołań do strony (dostaje liczby, zwraca liczbę albo rzuca błąd). Wtedy da się ją przetestować osobno (np. Node.js) — test zadania tak robi, jeśli masz Node.
### Konsola przeglądarki
F12 → Console: czerwone błędy (np. „Uncaught TypeError: Cannot read properties of null”) zwykle znaczą, że skrypt szuka elementu o id, którego nie ma, albo wczytał się przed formularzem (dlatego `<script>` na końcu body).

## 2 · Demonstracja — krok po kroku
**Wynik, który miga i znika — i NaN zł**

```
function obliczKoszt(noce, osoby, cenaZaOsobeNoc = 120) {
  if (!Number.isInteger(noce) || noce < 1) throw new Error("Podaj liczbę nocy (co najmniej 1)");
  if (!Number.isInteger(osoby) || osoby < 1) throw new Error("Podaj liczbę osób (co najmniej 1)");
  let koszt = noce * osoby * cenaZaOsobeNoc;
  if (noce >= 7) koszt = koszt * 0.9;
  return Math.round(koszt * 100) / 100;
}
```

1. Agent dodał kalkulator.js. Klikasz „Policz koszt” — wynik mignął, strona się przeładowała. Konsola czysta. Diagnoza: brak e.preventDefault() w obsłudze submit.
2. Po poprawce: 2 noce, 2 osoby → „Koszt: 480.00 zł”. Czyścisz pole nocy → „Koszt: 0.00 zł”. Number("") = 0, a walidacja w kodzie agenta to `if (noce < 0)`.
3. Wpisujesz „abc” w polu (type=number to blokuje, ale gdy agent zmieni type na text) → „Koszt: NaN zł”.
4. Prośba: „W obliczKoszt: noce i osoby muszą być liczbami całkowitymi ≥ 1, inaczej throw new Error z polskim komunikatem; obsługa submit wypisuje komunikat w #wynik”.
5. Konsola F12: `obliczKoszt(7, 1)` → 756. `obliczKoszt(0, 1)` → Error z komunikatem. Działa.

✔ **Oczekiwany wynik:** Kalkulator nie przeładowuje strony, liczy poprawnie z rabatem i pokazuje polski komunikat dla pustych i błędnych pól.

## 3 · Jak to uruchomić
1. Otwórz index.html → F12 → Console: wywołuj obliczKoszt(…) ręcznie.
2. Zadanie tygodnia → „✔ Sprawdź wynik” (jeśli masz Node.js, test uruchomi też logikę JS).

## W praktyce
- Logika w osobnej funkcji bez DOM — łatwa do testu.
- Przed oddaniem: konsola F12 bez czerwonych błędów.

## 4 · Ćwiczenie prowadzone
Co zwróci JavaScript: (1) `"3" + 2`, (2) `"3" * 2`, (3) `Number("")`? Wpisz wyniki tak, jak pokazałaby je konsola (napisy bez cudzysłowu). Czas: 15 minut.

📄 `cwiczenia/tydzien_09/javascript_interakcja_1.md` · rozwiązanie: `rozwiazania/tydzien_09/javascript_interakcja_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Konsola pokazuje „Uncaught TypeError: Cannot read properties of null (reading 'value')” w linii `document.querySelector("#noc").value`. W HTML pole ma id="noce". (1) Co zwrócił querySelector? (2) Co poprawisz — selektor w JS czy id w HTML (wybierz to, co zgodne ze specyfikacją pól noce/osoby)? (3) Czego brakuje, gdy wynik miga i znika po kliknięciu? Czas: 15 minut.

📄 `cwiczenia/tydzien_09/javascript_interakcja_2.md` · rozwiązanie: `rozwiazania/tydzien_09/javascript_interakcja_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„Uncaught ReferenceError: obliczKoszt is not defined”.**
  - Przyczyna: Plik JS nie wczytany (zła ścieżka) albo literówka w nazwie.
  - Jak sprawdzić: F12 → Network: kalkulator.js 404?
  - Poprawka: `<script src="kalkulator.js"></script>` przed `</body>`, plik obok index.html.
- ✘ **Wynik „NaN zł”.**
  - Przyczyna: Wartość pola nie jest liczbą (pusta, tekst).
  - Jak sprawdzić: console.log(noce, typeof noce).
  - Poprawka: Number() + walidacja Number.isInteger i ≥ 1 z komunikatem.
- ✘ **Wynik pojawia się na ułamek sekundy.**
  - Przyczyna: Brak e.preventDefault() w submit.
  - Jak sprawdzić: Obsługa zdarzenia.
  - Poprawka: Pierwsza linia obsługi: e.preventDefault();

## Pułapki
- Walidacja w przeglądarce (min="1") to wygoda gościa, nie bezpieczeństwo — każdy może ją obejść. Serwer (tydzień 10) sprawdza dane ponownie.
- Nie wstawiaj tekstu od użytkownika przez innerHTML — używaj textContent (tydzień 12: XSS).

## Dodatkowe zadania
1. Dodaj kalkulator.js z obsługą złych danych (zadanie tygodnia).
2. Przetestuj w konsoli 5 wywołań obliczKoszt.
3. Commit + push.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Po co e.preventDefault() w submit?**
  - Żeby przeglądarka nie wysłała formularza i nie przeładowała strony.
- **Dlaczego Number() na wartościach pól?**
  - Bo .value zawsze jest napisem; + z napisem skleja.
- **Czym różni się textContent od innerHTML?**
  - textContent wstawia czysty tekst; innerHTML interpretuje HTML (ryzyko XSS).

## Co potrafię teraz bez patrzenia na przykład?
Czytasz skrypt z funkcją, zdarzeniem i DOM, rozpoznajesz pułapki napisów i NaN, debugujesz w konsoli i trzymasz logikę osobno od strony.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- MDN — JavaScript: zdarzenia i DOM (Learn web development) (dostęp 20.11.2026) — <https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting>
- MDN — Event.preventDefault() (dostęp 20.11.2026) — <https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault>
- MDN — Node.textContent (różnica z innerHTML, bezpieczeństwo) (dostęp 20.11.2026) — <https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent>

## Test (w Mentorze: Lekcje → Sprawdź się)
- `"5" + 1` w JavaScript:
  - A) 6
  - B) "51"
  - C) Błąd
  - D) NaN
- Funkcja znajdująca element o id="wynik":
  - A) document.querySelector("#wynik")
  - B) find(wynik)
  - C) getId.wynik
  - D) select(".wynik")
- Bezpieczne wstawienie tekstu na stronę:
  - A) innerHTML
  - B) textContent
  - C) eval
  - D) document.write
- Gdzie zobaczysz błędy JavaScript?
  - A) W terminalu Mentora
  - B) F12 → Console
  - C) W Gicie
  - D) W README

Odpowiedzi: B, A, B, B
