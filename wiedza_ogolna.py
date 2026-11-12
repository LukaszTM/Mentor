# -*- coding: utf-8 -*-
"""Słownik błędów Pythona używany przez Asystenta Offline, gdy program nie definiuje własnego pola „bledy”."""

BLEDY_OGOLNE = {
    "SyntaxError": {
        "co": "Python nie rozumie składni — zwykle brak dwukropka po if/for/def, niedomknięty nawias lub cudzysłów, albo literówka w słowie kluczowym.",
        "pytanie": "Spójrz na linię wskazaną w błędzie I NA POPRZEDNIĄ. Czy każdy if/for/def kończy się dwukropkiem? Czy liczba nawiasów otwierających równa się zamykającym?"},
    "IndentationError": {
        "co": "Wcięcia są nierówne albo mieszasz tabulatory ze spacjami. Python wcięciami rozpoznaje, co należy do bloku.",
        "pytanie": "Czy wszystkie linie w tym bloku zaczynają się od tej samej liczby spacji (4)? PyCharm: Edit → Convert Indents → To Spaces."},
    "NameError": {
        "co": "Używasz nazwy, której Python nie zna — literówka, zmienna zdefiniowana później, albo zmienna z wnętrza funkcji użyta na zewnątrz.",
        "pytanie": "Gdzie ta nazwa dostaje wartość po raz pierwszy? Czy to miejsce wykonuje się PRZED linią z błędem — i w tym samym zakresie (funkcja/poza funkcją)?"},
    "TypeError": {
        "co": "Operacja na niepasujących typach: napis + liczba, wywołanie funkcji ze złą liczbą argumentów, indeksowanie liczby.",
        "pytanie": "Jakiego typu są wartości po obu stronach operatora w tej linii? Wypisz je przez print(type(x)). Czy jedna z nich przyszła z input()?"},
    "ValueError": {
        "co": "Typ się zgadza, ale wartość nie — int(\"abc\"), float(\"\"), lista.remove(czegoś, czego nie ma).",
        "pytanie": "Jaka dokładnie wartość trafia do tej funkcji? Czy użytkownik mógł wpisać coś, co nie jest liczbą — i czy try/except by to złapał?"},
    "ZeroDivisionError": {
        "co": "Dzielisz przez zero. Często: średnia z pustej listy (sum / len == 0).",
        "pytanie": "Co jest dzielnikiem w tej linii i w jakiej sytuacji może być zerem? Pusta lista? Wpisane 0? Jaki warunek przed dzieleniem by to wykluczył?"},
    "IndexError": {
        "co": "Indeks poza listą — lista ma 3 elementy (0,1,2), a prosisz o [3]; albo lista jest pusta.",
        "pytanie": "Ile elementów ma lista w chwili błędu (print(len(lista)))? Czy pętla używa range(len(lista)) i sięga o jeden za daleko?"},
    "KeyError": {
        "co": "Słownik nie ma takiego klucza — literówka w kluczu, inna wielkość liter, albo klucz jeszcze nie dodany.",
        "pytanie": "Wypisz słownik.keys() tuż przed tą linią. Czy klucz, którego szukasz, jest tam DOKŁADNIE tak zapisany? Czy .get() z wartością domyślną by pomogło?"},
    "AttributeError": {
        "co": "Obiekt nie ma takiej metody/atrybutu: 'NoneType' object has no attribute — funkcja zwróciła None (brak return); 'list' object has no attribute 'push' — zła nazwa metody.",
        "pytanie": "Co dokładnie jest po lewej stronie kropki i jakiego jest typu? Jeśli NoneType — która funkcja zwróciła None zamiast wartości (sprawdź jej return)?"},
    "ModuleNotFoundError": {
        "co": "Nie ma takiej biblioteki w tym środowisku — nie zainstalowana (pip install), albo zainstalowana w innym venv, albo literówka w nazwie.",
        "pytanie": "Czy venv jest aktywny w terminalu, z którego uruchamiasz (nazwa w nawiasie przed ścieżką)? Co pokazuje pip list? Czy PyCharm używa tego samego interpretera?"},
    "ImportError": {
        "co": "Moduł jest, ale nie ma w nim tej nazwy — literówka w from X import Y, import kołowy, albo własny plik nazwany jak biblioteka.",
        "pytanie": "Czy nazwa po import jest dokładnie taka jak w pliku źródłowym? Czy masz w projekcie plik o nazwie biblioteki (np. random.py, csv.py)?"},
    "FileNotFoundError": {
        "co": "Pliku nie ma tam, gdzie program szuka. Ścieżka względna liczy się od katalogu, z którego uruchomiono program, nie od pliku .py.",
        "pytanie": "Z jakiego katalogu uruchamiasz program (print(os.getcwd()))? Czy plik leży właśnie tam? Czy nazwa i rozszerzenie zgadzają się co do litery?"},
    "UnboundLocalError": {
        "co": "Zmienna w funkcji jest użyta przed przypisaniem — Python uznał ją za lokalną, bo gdzieś w funkcji ją przypisujesz.",
        "pytanie": "Czy w tej funkcji przypisujesz tej zmiennej wartość (x = ...) i jednocześnie czytasz ją wcześniej? Może powinna być argumentem funkcji?"},
    "RecursionError": {
        "co": "Funkcja wywołuje samą siebie bez końca — brak warunku stopu w rekurencji (np. silnia bez if n == 0).",
        "pytanie": "Jaki jest warunek, przy którym funkcja NIE wywołuje siebie? Czy argument na pewno zbliża się do tego warunku w każdym wywołaniu?"},
    "AssertionError": {
        "co": "assert był fałszywy — w teście znaczy: kod zwrócił inny wynik niż oczekiwany. To nie awaria, to informacja.",
        "pytanie": "Jaką wartość zwrócił kod, a jakiej oczekiwał test (pytest pokazuje obie)? Który z nich jest w błędzie — kod czy oczekiwanie w teście?"},
    "TimeoutException": {
        "co": "Selenium: element nie pojawił się w zadanym czasie — zły lokator, strona jeszcze się ładuje, element w innej ramce/karcie.",
        "pytanie": "Czy lokator znajduje element w konsoli przeglądarki (F12 → $(\"#id\") lub $x(\"//...\"))? Czy element pojawia się dopiero po jakiejś akcji?"},
    "NoSuchElementException": {
        "co": "Selenium nie znalazło elementu — lokator nie pasuje albo strona nie zdążyła się załadować (brak WebDriverWait).",
        "pytanie": "Czy szukasz elementu zaraz po get()/click(), bez czekania? Czy ten sam lokator działa w narzędziach deweloperskich przeglądarki?"},
    "KeyboardInterrupt": {
        "co": "Przerwałeś program klawiszem Ctrl+C — zwykle przy pętli nieskończonej.",
        "pytanie": "Który warunek pętli nigdy nie stał się fałszywy? Czy w pętli zmieniasz zmienną, od której zależy warunek?"},
}
