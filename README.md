# Pasjans (Solitaire) - Konsolowa Gra Python

---

## 🎲 Wprowadzenie

Witaj w konsolowej grze w Pasjansa! Ten projekt to klasyczna gra karciana Klondike Solitaire, zaimplementowana w języku Python. Gra oferuje intuicyjny interfejs tekstowy, możliwość cofania ruchów, a także tablicę najlepszych wyników (Hall of Fame) oraz różne poziomy trudności, aby dostosować rozgrywkę do swoich preferencji.

---

## ▶️ 1. Jak uruchomić projekt

Aby cieszyć się grą w Pasjansa na swoim komputerze, wykonaj następujące proste kroki:

### 1.1. Wymagania systemowe

Projekt został napisany w języku **Python**. Upewnij się, że masz zainstalowaną na swoim systemie wersję **Pythona 3.8** lub nowszą.

Aby sprawdzić swoją wersję Pythona, otwórz terminal (na Linux/macOS) lub wiersz poleceń (na Windowsie) i wpisz jedno z poniższych poleceń:

```bash
python --version
# lub (jeśli pierwsze nie zadziała)
python3 --version

Jeśli Python nie jest zainstalowany lub masz starszą wersję, możesz go pobrać z oficjalnej strony: python.org.
```
### 1.2. Pobieranie plików projektu

Upewnij się, że wszystkie pliki źródłowe gry (np. main.py oraz wszelkie inne moduły, jeśli projekt jest podzielony na wiele plików) znajdują się w jednym, wspólnym katalogu na Twoim komputerze. Jeśli otrzymałeś projekt w formie skompresowanego archiwum (.zip, .rar itp.), rozpakuj je do osobnego folderu.
### 1.3. Uruchamianie gry

    Otwórz terminal/wiersz poleceń:
        Windows: Naciśnij Win + R, wpisz cmd i naciśnij Enter.
        macOS/Linux: Otwórz aplikację "Terminal".

    Przejdź do katalogu projektu:
    Użyj polecenia cd (change directory), aby przenieść się do folderu, w którym zapisałeś pliki gry. Na przykład, jeśli pliki są w C:\MojeProjekty\Pasjans, wpisz:
    Bash

cd C:\MojeProjekty\Pasjans

Na Linux/macOS może to być:
Bash

cd ~/Dokumenty/Pasjans

Uruchom główny skrypt:
Gdy już znajdziesz się w odpowiednim katalogu, wpisz następujące polecenie, aby uruchomić grę:
Bash

    python main.py

    (Jeśli Twój główny plik ma inną nazwę niż main.py, zastąp ją odpowiednią nazwą).

Po uruchomieniu gry, w konsoli pojawi się menu główne, a program poprosi Cię o podanie swojego nicku.
## 📜 2. Instrukcje rozgrywki

Pasjans to gra dla jednego gracza, której celem jest ułożenie wszystkich kart w porządku rosnącym na stosach fundamentowych.
### 2.1. Cel gry

Twoim głównym celem jest przeniesienie wszystkich 52 kart na cztery stosy fundamentowe (oznaczone jako F-♥, F-♦, F-♣, F-♠). Karty na fundamentach muszą być ułożone od Asa do Króla (A, 2, 3, ..., Q, K), z zachowaniem tego samego koloru (np. wszystkie karty kierów na stosie F-♥).
### 2.2. Układ kart na stole

Plansza Pasjansa składa się z kilku kluczowych obszarów:

    Stock (Stos rezerwy): Znajduje się w lewym górnym rogu. Są to karty, które nie zostały rozdane na stosy robocze. Możesz z nich dobierać karty, aby uzupełnić stos odkryty.
    Waste (Stos odkryty): Położony obok stosu rezerwy. Tutaj trafiają karty dobrane ze Stocka. Zawsze widoczna jest tylko wierzchnia karta tego stosu, i tylko ona jest grywalna.
    Stacks (Stosy robocze 1-7): To siedem pionowych kolumn kart, które stanowią główny obszar gry. Liczba kart w każdej kolumnie rośnie od lewej do prawej (od 1 do 7 kart). W każdej kolumnie tylko ostatnia karta jest odkryta; pozostałe są zakryte.
    Foundation (Stosy fundamentowe F-♥, F-♦, F-♣, F-♠): Cztery puste miejsca w prawym górnym rogu planszy. To tutaj będziesz układać karty od Asa do Króla, posortowane według koloru.

### 2.3. Zasady ruchów

Zrozumienie zasad ruchów jest kluczowe do wygranej:

    Ruchy na stosach roboczych (Stacks 1-7):
        Karty muszą być układane w porządku malejącym i na przemian kolorami (czerwona na czarną, czarna na czerwoną). Na przykład, możesz położyć 7♠ na 8♦, ale nie na 8♣.
        Możesz przenosić pojedyncze odkryte karty lub całe prawidłowe sekwencje odkrytych kart (np. 8♥, 7♠, 6♦ możesz przenieść razem).
        Puste miejsce na stosie roboczym (gdzie nie ma żadnych kart) może zająć wyłącznie Król (K).
        Gdy usuniesz odkrytą kartę ze stosu roboczego i odsłonisz zakrytą kartę pod nią, ta zakryta karta automatycznie staje się odkryta i grywalna.

    Ruchy na stosach fundamentowych (Foundation F-♥, F-♦, F-♣, F-♠):
        Karty muszą być układane w porządku rosnącym i tylko w tym samym kolorze. Na przykład, na stosie F-♥ możesz układać tylko A♥, 2♥, 3♥ itd.
        Pierwszą kartą, którą możesz położyć na pustym fundamencie, musi być As (np. A♠ na pustym fundamencie dla pików).

    Dobieranie kart ze stosu rezerwy (Stock):
        Wybór akcji "Dobierz kartę" przenosi jedną lub więcej kart ze stosu rezerwy do stosu odkrytego (Waste). Liczba dobieranych kart zależy od wybranego poziomu trudności.
        Jeśli stos rezerwy jest pusty, a stos odkryty zawiera karty, stos odkryty jest "recyklowany" – jego karty wracają do stosu rezerwy, aby można było je ponownie dobierać. Na trudnym poziomie trudności liczba recyklingów jest ograniczona.

### 2.4. Sterowanie w grze (interakcja w konsoli)

Po każdym ruchu lub wyświetleniu planszy, gra wyświetli dostępne opcje i poprosi o wybranie akcji poprzez wpisanie odpowiedniej cyfry i naciśnięcie klawisza Enter:

    1 - Dobierz kartę (ze stosu STOCK): Przenosi kartę/karty ze stosu rezerwy na stos odkryty (Waste).
    2 - Przenieś kartę między stosami (z STACKS na STACKS): Pozwala na przeniesienie pojedynczej karty lub grupy kart z jednego stosu roboczego (1-7) na inny stos roboczy (1-7). Gra poprosi o podanie:
        Numeru stosu źródłowego (1-7).
        Numeru karty/grupy do przeniesienia (licząc od góry stosu, gdzie 1 to najwyżej odkryta karta).
        Numeru stosu docelowego (1-7).
    3 - Przenieś kartę ze stosu odkrytego na stos (WASTE na STACKS): Przenosi wierzchnią kartę ze stosu odkrytego (Waste) na wybrany stos roboczy (1-7).
    4 - Przenieś kartę na fundament ze stosu (z STACKS na F): Przenosi wierzchnią kartę z wybranego stosu roboczego (1-7) na odpowiedni stos fundamentowy.
    5 - Przenieś kartę ze stosu odkrytego na fundament (WASTE na F): Przenosi wierzchnią kartę ze stosu odkrytego (Waste) na odpowiedni stos fundamentowy.
    6 - Cofnij ostatni ruch: Przywraca stan gry do poprzedniego zapisu. Możesz cofnąć wiele ruchów, aż do początkowego stanu gry.
    9 - Wróć do Menu Głównego: Zakończ bieżącą partię i wróć do ekranu startowego.
    0 - Zakończ grę: Całkowicie zamyka program.

Anulowanie operacji: W trakcie podawania numerów stosów lub kart, możesz wpisać 0 lub słowo anuluj (bez cudzysłowów), aby przerwać bieżącą operację i wrócić do głównego wyboru akcji.
### 2.5. Menu Główne

Przy starcie gry i po jej zakończeniu, zostaniesz przeniesiony do menu głównego, które oferuje następujące opcje:

    1 - Rozpocznij nową grę: Rozpoczyna świeżą partię Pasjansa. Przed rozpoczęciem zostaniesz poproszony o wybór poziomu trudności.
    2 - Pokaż zasady: Wyświetla szczegółowe zasady gry i opis sterowania.
    3 - Hall of Fame (Najlepsi gracze): Prezentuje listę najlepszych wyników, posortowaną według liczby ruchów i czasu gry.
    0 - Wyjdź z gry: Zamyka aplikację Pasjansa.

### 2.6. Poziomy Trudności

Gra oferuje trzy poziomy trudności, które wpływają na mechanikę dobierania kart ze stosu rezerwy:

    Łatwy:
        Dobierasz 1 kartę ze stosu rezerwy (Stock) na stos odkryty (Waste) za każdym razem.
        Możesz przejść przez talię (zrecyklingować stos odkryty, gdy Stock jest pusty) nieskończoną liczbę razy.
    Średni:
        Dobierasz 3 karty ze stosu rezerwy (Stock) na stos odkryty (Waste) za każdym razem. Tylko wierzchnia z tych trzech kart jest od razu grywalna.
        Możesz przejść przez talię nieskończoną liczbę razy.
    Trudny:
        Dobierasz 3 karty ze stosu rezerwy (Stock) na stos odkryty (Waste) za każdym razem. Tylko wierzchnia z tych trzech kart jest od razu grywalna.
        Możesz przejść przez talię tylko 1 raz (po pierwszym recyklingu stosu odkrytego do Stocka, nie możesz już ponownie dobierać kart z pustego Stocka).

## 💻 3. Opis kodu (struktura i funkcjonalność)

Projekt Pasjansa został zaimplementowany w języku Python, wykorzystując podejście proceduralne. Oznacza to, że logika gry jest zorganizowana w funkcje, które operują na globalnych strukturach danych.
### 3.1. Główne zmienne globalne

Kilka kluczowych zmiennych jest zarządzanych globalnie, aby śledzić stan gry i ustawienia użytkownika:

    moves_count: $int$ - Zlicza liczbę wykonanych ruchów w bieżącej partii. Zwiększa się po każdym udanym i zatwierdzonym ruchu.
    start_time: $float$ - Przechowuje znacznik czasu rozpoczęcia bieżącej gry. Służy do obliczania całkowitego czasu rozgrywki.
    history: $list$ - Lista kopii stanów gry (głębokich kopii wszystkich stosów i liczników). Umożliwia funkcję cofania ruchów.
    player_nickname: $str$ - Nickname gracza, który jest pobierany na początku gry. Domyślnie ustawiony na "Gracz".
    difficulty_level: $str$ - Przechowuje aktualnie wybrany poziom trudności ("latwy", "sredni", "trudny").
    draw_count: $int$ - Liczba kart, które są dobierane ze stosu rezerwy (1 dla łatwego, 3 dla średniego/trudnego).
    max_passes: $float$ - Określa maksymalną liczbę przejść przez talię (recylklingów stosu Waste do Stocka). Ustawione na float('inf') dla poziomów łatwego i średniego, a na 1 dla trudnego.
    current_passes_count: $int$ - Aktualny licznik recyklingów talii w bieżącej grze.
    hall_of_fame: $list$ - Lista słowników, gdzie każdy słownik reprezentuje wynik gracza i zawiera jego nickname, moves (liczbę ruchów) oraz time_taken (czas gry).

### 3.2. Funkcje interfejsu użytkownika i menu

Te funkcje odpowiadają za interakcję z użytkownikiem poza samą planszą gry.

    show_rules():
        Wyświetla na ekranie szczegółowe zasady gry w Pasjansa, w tym opis celów, układu kart i dostępnych ruchów, a także wyjaśnienie poziomów trudności.
        Wstrzymuje wykonanie programu, oczekując na naciśnięcie klawisza Enter, co pozwala użytkownikowi na spokojne zapoznanie się z treścią.
    get_player_nickname():
        Prosi użytkownika o podanie swojego nicku na początku programu.
        Ustawia pobrany nick jako globalną zmienną player_nickname, która będzie używana w Hall of Fame.
    add_to_hall_of_fame(nickname, moves, time_taken):
        Funkcja wywoływana po wygranej grze.
        Tworzy nowy wpis (słownik) z danymi gracza i dodaje go do globalnej listy hall_of_fame.
        Sortuje listę hall_of_fame w pierwszej kolejności według moves (rosnąco), a następnie według time_taken (rosnąco), aby zapewnić ranking najlepszych graczy.
        Ogranicza listę do 10 najlepszych wyników, aby Hall of Fame nie rozrastał się w nieskończoność.
    display_hall_of_fame():
        Odpowiedzialna za wyświetlanie zawartości hall_of_fame w czytelnym i sformatowanym widoku tabelarycznym w konsoli.
        Wyświetla nick, liczbę ruchów i czas każdego gracza.
    select_difficulty_menu():
        Prezentuje użytkownikowi opcje wyboru poziomu trudności (łatwy, średni, trudny).
        Na podstawie wyboru użytkownika, ustawia globalne zmienne difficulty_level, draw_count (liczbę dobieranych kart) oraz max_passes (limit recyklingu talii), co bezpośrednio wpływa na mechanikę rozgrywki.
    main_menu():
        Jest to główna pętla menu, która steruje przepływem programu.
        Umożliwia użytkownikowi wybranie akcji: rozpoczęcie nowej gry, wyświetlenie zasad, sprawdzenie Hall of Fame lub wyjście z aplikacji.
        Zwraca string "start" lub "exit", kierując dalszym działaniem programu głównego.

### 3.3. Funkcje zarządzające stanem gry i inicjalizacją

Te funkcje są odpowiedzialne za przygotowanie planszy do gry i śledzenie jej zmian.

    start_new_game():
        Kompletnie inicjalizuje nową partię Pasjansa.
        Resetuje globalne liczniki (moves_count, current_passes_count), czyści historię ruchów (history), i ustawia czas startowy gry (start_time).
        Wywołuje create_deck() w celu stworzenia i potasowania standardowej talii 52 kart.
        Następnie wywołuje create_stacks() do rozdania kart na stosy robocze i stos rezerwy.
        Na koniec, zapisuje początkowy stan gry do history, aby umożliwić cofanie ruchu od samego początku.
        Zwraca początkowe stany wszystkich stosów gry.
    create_deck():
        Tworzy nową talię 52 kart, zawierającą 13 kart dla każdego z czterech kolorów (kier, karo, trefl, pik).
        Używa funkcji random.shuffle() do losowego potasowania talii, zapewniając różnorodne układy w każdej grze.
        Zwraca potasowaną listę kart.
    create_stacks(deck):
        Rozdaje karty z potasowanej talii (deck) na siedem stosów roboczych (stacks_dict). Zgodnie z zasadami Pasjansa, pierwszy stos ma 1 kartę, drugi 2 itd.
        Ustawia początkową widoczność kart na stosach roboczych (stacks_visible), gdzie tylko wierzchnia karta każdego stosu jest odkryta.
        Pozostałe karty z talii umieszcza w stosie rezerwy (stock_pile).
        Zwraca zainicjowane stosy: stock_pile, pusty waste_pile, stacks_dict (słownik zawierający listy kart dla każdego stosu) i stacks_visible (słownik zawierający listy wartości boolowskich dla widoczności kart).
    save_game_state(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks, is_initial_state=False):
        Kluczowa funkcja dla mechaniki cofania ruchów.
        Tworzy głębokie kopie wszystkich aktualnych stosów gry (Stock, Waste, Stacks, Foundation) oraz ich widoczności, a także bieżących liczników. copy.deepcopy() jest używane, aby mieć pewność, że zmiany w bieżącej grze nie wpłyną na zapisane stany.
        Zapisuje ten skopiowany stan do globalnej listy history.
        Jeśli is_initial_state jest True, cała historia jest najpierw czyszczona (używane na początku nowej gry).
    undo_last_move():
        Pobiera ostatnio zapisany stan gry z listy history i przywraca go.
        Aktualizuje wszystkie globalne zmienne (stosy, liczniki, czas) do poprzedniego stanu, efektywnie cofając ruch.
        Wyświetla informację, jeśli nie ma żadnych wcześniejszych ruchów do cofnięcia.

### 3.4. Funkcje graficzne (ASCII Art)

Te funkcje odpowiadają za wizualne przedstawienie kart i planszy w konsoli.

    make_card(value, suit_symbol):
        Generuje tekstową reprezentację (ASCII Art) pojedynczej karty.
        Odpowiada za formatowanie karty (np. dodawanie obramowania, symboli wartości i koloru).
        Zawiera logikę kolorowania kart (czerwone dla kierów/kar, czarne dla trefli/pików) w konsoli, co zwiększa czytelność.
        Zwraca listę stringów, gdzie każdy string to jedna linia karty.
    make_empty_slot_card():
        Generuje ASCII Art dla pustego miejsca, np. na pustym stosie fundamentowym lub roboczym.
        Zwraca listę stringów reprezentujących puste miejsce.
    make_card_back():
        Generuje ASCII Art dla zakrytej karty, czyli "rewersu" karty.
        Jest używana do wizualizacji kart, które nie są jeszcze odkryte na stosach roboczych.
        Zwraca listę stringów.
    display_stacks(stacks_dict, stacks_visible, foundation_stacks, stock_pile, waste_pile, make_card_func):
        Jest to główna funkcja odpowiedzialna za rysowanie całej planszy gry w konsoli.
        Koordynuje wywołania make_card, make_card_back, make_empty_slot_card do zbudowania wizualizacji każdego stosu.
        Oblicza i wyświetla ważne informacje o stanie gry: aktualny czas rozgrywki, liczbę wykonanych ruchów, wybrany poziom trudności oraz informację o liczbie dostępnych recyklingów talii.
        Dba o prawidłowe wyrównanie i formatowanie, aby plansza była czytelna.

### 3.5. Funkcje logiki kart

Proste funkcje pomocnicze do manipulacji danymi kart.

    get_card_value(card):
        Pobiera pełną nazwę karty (np. "10♥", "K♠") i zwraca jej wartość numeryczną (np. 10, 13 dla Króla).
        Jest to kluczowe do sprawdzania, czy karty mogą być układane w prawidłowej sekwencji (wartość o jeden mniejsza/większa).
    get_card_color(card):
        Na podstawie symbolu koloru karty (♥, ♦, ♣, ♠) określa, czy karta jest czerwona (kier, karo) czy czarna (trefl, pik).
        Niezbędne do egzekwowania zasady układania kart na przemian kolorami na stosach roboczych.
    check_win(foundation_stacks):
        Sprawdza warunek zakończenia gry i zwycięstwa.
        Iteruje przez wszystkie cztery stosy fundamentowe i sprawdza, czy każdy z nich zawiera dokładnie 13 kart (od Asa do Króla w danym kolorze).
        Zwraca True jeśli gra jest wygrana, w przeciwnym razie False.

3.6. Funkcje ruchów w grze

Te funkcje implementują logikę poszczególnych rodzajów ruchów, włączając w to walidację zgodną z zasadami Pasjansa oraz aktualizację stanu gry. Po każdym udanym i prawidłowym ruchu, funkcja wywołuje save_game_state() w celu zapisania nowej pozycji do historii i zwiększa moves_count.

    take_new_card(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks):
        Obsługuje dobieranie kart ze stosu rezerwy (Stock).
        Jeśli Stock nie jest pusty, przenosi odpowiednią liczbę kart (zależną od draw_count) do stosu odkrytego (Waste).
        Jeśli Stock jest pusty, zarządza recyklingiem Waste z powrotem do Stocka, sprawdzając jednocześnie limit max_passes dla trudnego poziomu trudności.
        Wyświetla odpowiednie komunikaty o braku kart lub limitach.
    move_card_from_stack_to_stack(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks):
        Pozwala na przenoszenie pojedynczych kart lub grup kart pomiędzy dwoma stosami roboczymi (Stacks).
        Zawiera złożoną logikę walidacji: sprawdzanie poprawności koloru, wartości, czy Król trafia na puste miejsce, i czy przenoszona sekwencja jest prawidłowa.
        Po udanym ruchu, odkrywa zakrytą kartę na stosie źródłowym, jeśli jest to konieczne.
    move_card_from_waste_to_stack(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks):
        Umożliwia przeniesienie wierzchniej karty ze stosu odkrytego (Waste) na wybrany stos roboczy.
        Sprawdza zasady Pasjansa dotyczące koloru i wartości karty docelowej.
    move_card_from_stack_to_final_stack(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks):
        Pozwala na przeniesienie wierzchniej karty z wybranego stosu roboczego na odpowiedni stos fundamentowy.
        Weryfikuje, czy karta może być położona na fundamencie (As na pustym stosie, kolejna karta w rosnącym ciągu tego samego koloru).
        Po udanym ruchu, odkrywa zakrytą kartę na stosie źródłowym, jeśli jest to konieczne.
    move_card_from_waste_to_foundation(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks):
        Umożliwia przeniesienie wierzchniej karty ze stosu odkrytego (Waste) na odpowiedni stos fundamentowy.
        Sprawdza analogiczne zasady jak move_card_from_stack_to_final_stack.
