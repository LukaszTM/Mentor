# Ćwiczenie 2 (samodzielne) — WebDriverWait i Page Object Model
Tydzień 8 · lekcja `wait_pom`

## Zadanie
Test czasem pada (flaky): `driver.find_element(By.ID, "promocja")` zaraz po get(); promocja pokazuje się po ok. 1,5 s. Wybierz: (1) najlepsza poprawka: time.sleep(5) / WebDriverWait(driver, 10).until(EC.visibility_of_element_located(...)) / implicitly_wait(60); (2) jaki wyjątek, jeśli promocja nie pojawi się w 10 s; (3) gdzie umieścisz asercję „promocja zawiera −10%”: w metodzie klasy strony / w teście. Czas: 15 minut.

## Jak sprawdzić
1. Zrób ćwiczenie (w Mentorze: Lekcje → ta lekcja → pola „Twoje odpowiedzi”; kod uruchamiasz w pliku .py w PRACA).
2. Utknąłeś? Podpowiedzi po kolei w Mentorze albo w pliku rozwiązania — najpierw podpowiedź 1.
3. Po własnej próbie: `rozwiazania/tydzien_08/wait_pom_2.md`.

## Twoja odpowiedź

(pisz tutaj)
