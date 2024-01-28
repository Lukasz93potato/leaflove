# Aplikacja internetowa LeafLove

Aplikacja skierowana jest do posiadaczy roślin doniczkowych i służy do zarządzania nimi.
ma za zadanie przechowywanie informacji o roślinach użytkownika 
oraz przypominanie mu o ich podlewaniu i nawożeniu.

##Funkcjonalności

 - Przechowywanie bazy danych z roślinami użytkownika, 
  ich nazwami, zdjęciami, cyklem podlewania i nawożenia określanym w liczbie dni oraz datami kiedy po raz ostatni były podlewane.
 - Aktualizacja ostatniej daty podlewania/nawożenia rośliny przez użytkownika.


##Zastosowane technologie
Django, React
Języki: Python, JavaScript, PostgreSQL


##Front-end

Widoki:
 - Logowania użytkownika
    Zawiera formularz logowania użytkownika oraz link do widoku rejestracji.

![Zrzut ekranu 2024-01-28 175853.png](Zrzut%20ekranu%202024-01-28%20175853.png)

 - Rejestracja nowego użytkownika

![Zrzut ekranu 2024-01-28 175910.png](Zrzut%20ekranu%202024-01-28%20175910.png)

 - Widok roślin należących do użytkownika oraz karta z wybraną rośliną

![Zrzut ekranu 2024-01-28 180106.png](Zrzut%20ekranu%202024-01-28%20180106.png)

 - Dodanie nowej rośliny

![Zrzut ekranu 2024-01-28 180120.png](Zrzut%20ekranu%202024-01-28%20180120.png)

##Back-end

Poniżej została zamieszczona dokumentacja tabel bazy:

auth_user:

| Nazwa pola:  | Typ danych:             | Opis:                                           |
|--------------|-------------------------|-------------------------------------------------|
| id           | int                     | Identyfikator użytkownika,  Klucz główny tabeli |
| password     | varchar(128)            | hasło użytkownika                               |
| last_login   | timestamp with timezone | ostatni czas logowania użytkownika              |
| is_superuser | boolean                 | Czy użytkownik to "superuser"                   |
| username     | varchar(150)            | Nazwa użytkownika                               |
| first_name   | varchar(150)            | Imię użytkownika                                |
| last_name    | varchar(150)            | Nazwisko użytkownika                            |
| email        | varchar(100)            | adres email użytkownika                         |
| is_staff     | boolean                 | czy użytkownik należy do grupy "staff"          |
| is_active    | boolean                 | czy użytkownik jest aktywny                     |
| date_joined  | timestamp with timezone | czas dołączenia                                 |



app_plants:

| Nazwa pola:      | Typ danych:  | Opis:                                             |
|------------------|--------------|---------------------------------------------------|
| id               | int          | Identyfikator rośliny,  Klucz główny tabeli       |
| name             | varchar(100) | Nazwa rośliny                                     |
| image            | varchar(100) | ścieżka do pliku                                  |
| water_last       | date         | Data kiedy roślina została ostatni raz podlana    |
| water_cycle      | int          | Ilość dni co którą należy podlewać roślinę        |
| fertilizer_last  | date         | Data kiedy roślina została ostatni raz nawieziona |
| fertilizer_cycle | int          | Ilość dni co którą należy nawozić roślinę         |
| user_id          | int          | Id użytkownika, do którego należy roślina         |
| description_id   | bigint       | Id opisu rośliny                                  |

app_description:

| Nazwa pola: | Typ danych: | Opis:                       |
|-------------|-------------|-----------------------------|
| id          | int         | Identyfikator opisu rośliny |
| text        | text        | Opis rośliny                |

app_plants_tags:

| Nazwa pola: | Typ danych: | Opis:                 |
|-------------|-------------|-----------------------|
| id          | int         | Identyfikator rekordu |
| plant_id    | bigint      | Identyfikator rośliny |
| tag_id      | bigint      | Identyfikator tagu    |

app_tag:

| Nazwa pola: | Typ danych: | Opis:              |
|-------------|-------------|--------------------|
| id          | int         | Identyfikator tagu |
| name        | varchar(50) | Nazwa tagu         |


##Scenariusze użycia aplikacji

*Rejestracja nowego użytkownika
Wymagania:
ekran logowania aplikacji

 - Użytkownik wybiera przycisk "Sign up"
 - Aplikacja wyświetla widok rejestracji nowych użytkowników
 - Użytkownik wprowadza swój adres mailowy w formularzu
 - Aplikacja sprawdza czy wprowadzony adres ma poprawny format. W przeciwnym wypadku podkreśla pole tekstowe na czerwono
 - Użytkownik wprowadza dwukrotnie hasło
 - Aplikacja sprawdza czy oba ciągi znaków są takie same. W przeciwnym wypadku podkreśla pola na czerwono
 - Użytkownik wprowadza swoje imię i nazwisko, po czym wybiera przycisk "Sign up"
 - Aplikacja pobiera z formularza dane i zapisuje je w bazie danych w tabeli Users, przydzielając użytkownikowi numer ID

*Logowanie zarejestrowanego użytkownika
Wymagania:
Zarejestrowany użytkownik, ekran logowania aplikacji

 - Użytkownik wpisuje swój adres email oraz hasło w formularzu oraz wybiera przycisk "Log in"
 - Aplikacja odnajduje w bazie danych w tabeli "Users" wiersz według podanego email-a i sprawdza
   czy wprowadzone hasło zgadza się z hasłem przechowywanym w tabeli. 
 - Jeśli użytkownik zostaje odnaleziony i hasło jest poprawne, aplikacja przeszukuje tabelę "Plants"
   według ID użytkownika i pobiera dane na temat należących do niego roślin.
 - Aplikacja wyświetla widok roślin użytkownika.

*Dodawanie Nowej rośliny
Wymagania:
Zalogowany użytkownik, widok roślin użytkownika

 - Użytkownik wybiera przycisk "add plant" umieszczony na końcu listy roślin
 - Aplikacja przez link pod przyciskiem przenosi użytkownika do widoku dodawania nowej rośliny
 - Użytkownik uzupełnia nazwę rośliny, wybiera daty kiedy roślina ostatni raz była podlewana, nawożona
   oraz wybiera liczby dni co ile roślina powinna być nawożona i podlewana
 - Użytkownik wybiera przycisk "add plant"
 - Aplikacja pobiera dane z formularza i zapisuje je w tabeli "Plants"
 - Aplikacja przenosi użytkownika z powrotem do widoku roślin użytkownika pobierając przedtem rośliny z bazy danych
   wraz z nowo utworzoną rośliną. 

*Przeglądanie listy roślin
Wymagania:
Zalogowany użytkownik, widok roślin użytkownika, Istniejące rośliny użytkownika w bazie

 - Użytkownik wybiera roślinę w widoku
 - Aplikacja wyświetla w bocznym panelu zdjęcie rośliny, jej nazwę, daty ostatniego podlewania, nawożenia rośliny
   oraz przyciski aktualizacji tych dat
 - Użytkownik wybiera inną roślinę z listy
 - Aplikacja zmienia prezentowane w bocznym panelu dane na dotyczące wybranej rośliny

*Podlewanie/Nawożenie rośliny
Wymagania:
Zalogowany użytkownik, widok roślin użytkownika, Istniejące rośliny użytkownika w bazie

 - Użytkownik wybiera roślinę w widoku
 - Aplikacja wyświetla w bocznym panelu zdjęcie rośliny, jej nazwę, daty ostatniego podlewania, nawożenia rośliny
    oraz przyciski aktualizacji tych dat
 - Użytkownik wybiera przycisk "add water"/"add fertilizer"
 - Aplikacja aktualizuje datę ostatniego nawożenia/podlewania na dzisiejszą zarówno w widoku jak i bazie danych.