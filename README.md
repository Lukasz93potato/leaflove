# Aplikacja internetowa LeafLove

Aplikacja skierowana jest do posiadaczy roślin doniczkowych i służy do zarządzania nimi.
ma za zadanie przechowywanie informacji o roślinach użytkownika 
oraz przypominanie mu o ich podlewaniu i nawożeniu.

##Funkcjonalności

 - Przechowywanie bazy danych z roślinami użytkownika, 
  ich nazwami, zdjęciami, cyklem podlewania i nawożenia określanym w liczbie dni oraz datami kiedy po raz ostatni były podlewane.
 - Aktualizacja ostatniej daty podlewania/nawożenia rośliny przez użytkownika.


##Zastosowane technologie
Xampp
Języki: PHP, JavaScript, PostgreSQL


##Front-end

Widoki:
 - Logowania użytkownika
    Zawiera formularz logowania użytkownika oraz link do widoku rejestracji.
 - Rejestracja nowego użytkownika
 - Widok roślin należących do użytkownika
 - Karta z wybraną rośliną 
 - Dodanie nowej rośliny

##Back-end

Baza danych projektu została utworzona za pomocą aplikacji Railway.app i składa się z 2 tabel: "Users" 
zawierającej dane zarejestrowanych użytkowników oraz "Plants" zawierającej dane utworzonych przez użytkownika roślin.
Poniżej została zamieszczona dokumentacja tabel bazy:

Users:
| Nazwa pola: | Typ danych:   | Opis:                                                     |
| ----------- | ------------- | --------------------------------------------------------- |
| id          | int           | Identyfikator użytkownika,  Klucz główny tabeli           |
| name        | varchar(100)  | Imię użytkownika                                          |
| surname     | varchar(100)  | Nazwisko użytkownika                                      |
| email       | varchar(100)  | adres email użytkownika                                   |
| password    | varchar(100)  | hasło użytkownika zahashowane za pomocą algorytmu bcrypt  |



Plants:
| Nazwa pola:        | Typ danych:     | Opis:                                                                                   |
| ------------------ | --------------- | --------------------------------------------------------------------------------------- |
| id                 | int             | Identyfikator rośliny,  Klucz główny tabeli                                             |
| id_user            | int             | Klucz obcy tabeli "Users"( relacja jeden do wielu z tabeli "Users" do tabeli "Plants")  |
| name               | varchar(100)    | Nazwa rośliny                                                                           |
| water_cycle        | int             | Ilość dni co którą należy podlewać roślinę                                              |
| water_last         | date            | Data kiedy roślina została ostatni raz podlana                                          |
| fertilizer_cycle   | int             | Ilość dni co którą należy nawozić roślinę                                               |
| fertilizer_last    | date            | Data kiedy roślina została ostatni raz nawieziona                                       |
| created_at         | date            | Data utworzenia rośliny                                                                 |
|image               | varchar(100)    | nazwa pliku ze zdjęciem rośliny wraz z rozszerzeniem                                    |





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