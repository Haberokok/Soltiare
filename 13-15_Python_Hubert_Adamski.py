import random
import time
import copy

# Główne zmienne gry
moves_count = 0
start_time = 0
history = []
player_nickname = "Gracz" # Domyślny nick

# Ustawienia Poziomu Trudności
difficulty_level = "latwy" # Domyślny poziom
draw_count = 1             # Ile kart dobierać (1 lub 3)
max_passes = float('inf')  # Maksymalna liczba przejść przez talię (nieskończoność dla łatwego/średniego)
current_passes_count = 0   # Licznik obecnych przejść

# TUTAJ JEST NASZ HALL OF FAME!
hall_of_fame = []

def show_rules():
    print("""
---
ZASADY GRY W PASJANSA (KLONDIKE)
---

Witaj w konsolowej wersji klasycznego Pasjansa!

## Cel Gry

Twoim zadaniem jest przenieść wszystkie **52 karty** na **cztery stosy fundamentowe** (F-♥, F-♦, F-♣, F-♠) w prawym górnym rogu. Karty na fundamentach układasz **od Asa do Króla**, zachowując **ten sam kolor**.

## Układ Planszy

Gra toczy się na kilku obszarach:

* **Stos Rezerwy (STOCK):** Lewy górny róg, karty do dobierania.
* **Stos Odkryty (WASTE):** Obok Stosu Rezerwy, tu trafiają dobrane karty. Tylko wierzchnia jest grywalna.
* **Stosy Robocze (STACKS 1-7):** Główne kolumny kart. Układasz tu karty w kolejności **malejącej** i **na przemian kolorami** (czerwona na czarną, czarna na czerwoną). Puste miejsce zajmuje **tylko Król**.
* **Stosy Fundamentowe (FOUNDATION):** Prawy górny róg, cel gry. Układasz tu karty **rosnąco** i **tylko w tym samym kolorze**.

## Zasady Ruchów

* **Na stosach roboczych:** Przenosisz pojedyncze karty lub prawidłowe sekwencje. Odsłonięta zakryta karta staje się grywalna.
* **Na fundamentach:** Kładziesz karty w kolejności rosnącej, zaczynając od **Asa** danego koloru.
* **Dobieranie kart (STOCK):** Przenosisz karty do Stosu Odkrytego. Gdy Stock się skończy, Stos Odkryty może zostać zrecyklowany (wrócić do Stocka).

## Sterowanie w Grze

Wybierasz akcje, wpisując odpowiednie cyfry (np. dobierz kartę, przenieś między stosami, cofnij ruch). Możesz wpisać `0` lub `anuluj`, aby przerwać bieżącą operację.

## Poziomy Trudności

* **Łatwy:** Dobierasz **1 kartę**. Nieograniczone recyklingi talii.
* **Średni:** Dobierasz **3 karty**. Nieograniczone recyklingi talii.
* **Trudny:** Dobierasz **3 karty**. **Tylko 1** pełne przejście talii (recykling).

Życzymy powodzenia!
""")
    input("\nNaciśnij Enter, aby wrócić do menu...")

def get_player_nickname():
    global player_nickname
    nick = input("Podaj swój nick: ")
    if nick.strip():
        player_nickname = nick
    else:
        player_nickname = "Gracz"
    print(f"Witaj, {player_nickname}!")

def add_to_hall_of_fame(nickname, moves, time_taken):
    global hall_of_fame
    hall_of_fame.append({'nickname': nickname, 'moves': moves, 'time': time_taken})
    hall_of_fame.sort(key=lambda x: (x['moves'], x['time']))
    hall_of_fame = hall_of_fame[:10]

def display_hall_of_fame():
    print("\n--- HALL OF FAME (NAJLEPSI GRACZE) ---")
    if not hall_of_fame:
        print("Jeszcze nikt nie wygrał! Bądź pierwszy!")
    else:
        print("Nr. | Nickname       | Ruchy | Czas")
        print("---------------------------------")
        for i, entry in enumerate(hall_of_fame):
            minutes = entry['time'] // 60
            seconds = entry['time'] % 60
            print(f"{i+1:3} | {entry['nickname'][:14].ljust(14)} | {entry['moves']:5} | {minutes:02d}:{seconds:02d}")
    input("\nNaciśnij Enter, aby wrócić do menu...")

def select_difficulty_menu():
    global difficulty_level, draw_count, max_passes

    while True:
        print("\n--- WYBIERZ POZIOM TRUDNOŚCI ---")
        print("1 - Łatwy (Dobieraj 1 kartę, nieograniczone przejścia talii)")
        print("2 - Średni (Dobieraj 3 karty, nieograniczone przejścia talii)")
        print("3 - Trudny (Dobieraj 3 karty, tylko 1 przejście talii)")
        choice = input("Wybierz poziom (1-3): ")

        if choice == "1":
            difficulty_level = "latwy"
            draw_count = 1
            max_passes = float('inf')
            print("Wybrano poziom: Łatwy")
            return
        elif choice == "2":
            difficulty_level = "sredni"
            draw_count = 3
            max_passes = float('inf')
            print("Wybrano poziom: Średni")
            return
        elif choice == "3":
            difficulty_level = "trudny"
            draw_count = 3
            max_passes = 1 # Tylko jedno pełne przejście (po pierwszym zużyciu stosu)
            print("Wybrano poziom: Trudny")
            return
        else:
            print("Niepoprawna opcja. Spróbuj ponownie.")

def main_menu():
    while True:
        print("\n--- MENU GŁÓWNE PASJANSA ---")
        print("1 - Rozpocznij nową grę")
        print("2 - Pokaż zasady")
        print("3 - Hall of Fame (Najlepsi gracze)")
        print("0 - Wyjdź z gry")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            select_difficulty_menu() # Wybór poziomu trudności
            return "start"
        elif choice == "2":
            show_rules()
        elif choice == "3":
            display_hall_of_fame()
        elif choice == "0":
            return "exit"
        else:
            print("Niepoprawna opcja. Spróbuj ponownie.")

def start_new_game():
    global start_time, history, moves_count, current_passes_count

    moves_count = 0
    history.clear()
    start_time = time.time()
    current_passes_count = 0 # Resetuj licznik przejść dla nowej gry

    # Ustawienia trudności (draw_count, max_passes) są już ustawione globalnie

    deck = create_deck()
    stock_pile, waste_pile, stacks_dict, stacks_visible = create_stacks(deck)
    foundation_stacks = {'♥': [], '♦': [], '♣': [], '♠': []}

    save_game_state(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks, is_initial_state=True)
    return stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks

def create_deck():
    deck = []
    colors = ['♥', '♦', '♠', '♣']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for color in colors:
        for value in values:
            deck.append(f"{value}{color}")
    random.shuffle(deck)
    return deck

def create_stacks(deck):
    stock_pile = []
    waste_pile = []
    stacks_dict = {i: [] for i in range(1, 8)}
    stacks_visible = {i: [] for i in range(1, 8)}
    
    # Rozdanie kart na stosy robocze
    for i in range(7): # Dla każdego z 7 stosów
        for j in range(i + 1): # Stos 'i' otrzymuje 'i+1' kart
            card = deck.pop(0)
            stacks_dict[i+1].append(card)
            stacks_visible[i+1].append('visible' if j == i else 'invisible') # Ostatnia karta na stosie jest widoczna

    # Reszta kart do stosu rezerwy
    stock_pile.extend(deck)
    deck.clear()

    return stock_pile, waste_pile, stacks_dict, stacks_visible

def make_card(value, suit_symbol):
    if suit_symbol in ['♥', '♦']:
        color_code = '\033[91m' # Czerwony
    else:
        color_code = '\033[90m' # Czarny
    reset_code = '\033[0m'
    val_l = value.ljust(2)
    val_r = value.rjust(2)
    return [
        "┌───────┐",
        f"|{val_l}   {color_code}{suit_symbol}{reset_code} |",
        f"|       |",
        f"| {color_code}{suit_symbol}{reset_code}   {val_r}|",
        "└───────┘"
    ]

def make_empty_slot_card():
    return [
        "┌───────┐",
        "|       |",
        "|   □   |",
        "|       |",
        "└───────┘"
    ]

def make_card_back():
    return [
        "┌───────┐",
        "|*******|",
        "|*******|",
        "|*******|",
        "└───────┘"
    ]

def display_stacks(stacks_dict, stacks_visible, foundation_stacks, stock_pile, waste_pile, make_card_func):
    elapsed_time = int(time.time() - start_time)
    minutes = elapsed_time // 60
    seconds = elapsed_time % 60
    
    level_text = f"POZIOM: {difficulty_level.capitalize()}"
    passes_info = ""
    if max_passes != float('inf'):
        passes_info = f"PRZEJŚCIA TALII: {current_passes_count}/{max_passes}"
        if current_passes_count >= max_passes and not stock_pile :
             passes_info += " (LIMIT OSIĄGNIĘTY)"


    print(f"\nRUCHY: {moves_count}   CZAS: {minutes:02d}:{seconds:02d}   {level_text}   {passes_info}")
    print("  STOCK     WASTE      F-♥       F-♦       F-♣       F-♠")
    
    top_row_cards_ascii = []

    if stock_pile:
        top_row_cards_ascii.append(make_card_back())
    else:
        # Jeśli stos jest pusty, ale można go odnowić (nie osiągnięto limitu przejść lub są karty w waste)
        if waste_pile and current_passes_count < max_passes:
            top_row_cards_ascii.append(make_card_back()) # Pokaż "kliknięcie" do odnowienia
        else:
            top_row_cards_ascii.append(make_empty_slot_card())


    if waste_pile:
        last_card = waste_pile[-1]
        value = last_card[:-1]; suit = last_card[-1]
        top_row_cards_ascii.append(make_card_func(value, suit))
    else:
        top_row_cards_ascii.append(make_empty_slot_card())

    for color in ['♥', '♦', '♣', '♠']:
        if foundation_stacks[color]:
            card = foundation_stacks[color][-1]
            value = card[:-1]; suit = card[-1]
            top_row_cards_ascii.append(make_card_func(value, suit))
        else:
            top_row_cards_ascii.append(make_empty_slot_card())
    
    card_height = len(make_card_back())
    for i in range(card_height):
        line_parts = [card_ascii[i] for card_ascii in top_row_cards_ascii]
        print(" ".join(line_parts))
    print()

    print(" STOS 1     STOS 2    STOS 3    STOS 4    STOS 5    STOS 6    STOS 7")
    
    max_stack_len = 0
    for i in range(1, 8):
        if stacks_dict[i]: # Dodano sprawdzenie czy stos nie jest None
            max_stack_len = max(max_stack_len, len(stacks_dict[i]))

    card_width = len(make_card_back()[0])
    for card_pos_in_stack in range(max_stack_len):
        for card_line_idx in range(card_height):
            current_display_line = []
            for stack_num in range(1, 8):
                current_stack = stacks_dict[stack_num]
                current_vis = stacks_visible[stack_num]
                if card_pos_in_stack < len(current_stack):
                    card = current_stack[card_pos_in_stack]
                    if current_vis[card_pos_in_stack] == 'visible':
                        value = card[:-1]; suit = card[-1]
                        current_display_line.append(make_card_func(value, suit)[card_line_idx])
                    else:
                        current_display_line.append(make_card_back()[card_line_idx])
                else:
                    current_display_line.append(" " * card_width)
            print(" ".join(current_display_line))
    print()


def get_card_value(card):
    value = card[:-1]
    if value.isdigit(): return int(value)
    elif value == 'J': return 11
    elif value == 'Q': return 12
    elif value == 'K': return 13
    elif value == 'A': return 1
    return 0

def get_card_color(card):
    suit = card[-1]
    if suit in ['♥', '♦']: return 'czerwony'
    elif suit in ['♠', '♣']: return 'czarny'
    return ''

def save_game_state(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks, is_initial_state=False):
    global current_passes_count # Dodajemy do zapisu stanu
    state = {
        'stock_pile': copy.deepcopy(stock_pile),
        'waste_pile': copy.deepcopy(waste_pile),
        'stacks_dict': copy.deepcopy(stacks_dict),
        'stacks_visible': copy.deepcopy(stacks_visible),
        'foundation_stacks': copy.deepcopy(foundation_stacks),
        'moves_count': moves_count,
        'current_passes_count': current_passes_count # Zapisz aktualną liczbę przejść
    }
    if is_initial_state:
        history.clear()
    history.append(state)

def undo_last_move():
    global stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks, moves_count
    global current_passes_count # Dodajemy do przywracania stanu

    if len(history) >= 2:
        history.pop()
        previous_state = history[-1]
        
        stock_pile = copy.deepcopy(previous_state['stock_pile'])
        waste_pile = copy.deepcopy(previous_state['waste_pile'])
        stacks_dict = copy.deepcopy(previous_state['stacks_dict'])
        stacks_visible = copy.deepcopy(previous_state['stacks_visible'])
        foundation_stacks = copy.deepcopy(previous_state['foundation_stacks'])
        moves_count = previous_state['moves_count']
        current_passes_count = previous_state['current_passes_count'] # Przywróć liczbę przejść
        print("Cofnięto ostatni ruch.")
    else:
        print("Nie można cofnąć, brak wcześniejszych ruchów.")


def take_new_card(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks):
    global moves_count, current_passes_count, max_passes, draw_count
    
    action_taken = False # Czy jakakolwiek akcja (dobranie lub recykling) została podjęta

    if not stock_pile:  # Stos rezerwy jest pusty
        if waste_pile and current_passes_count < max_passes:
            print("Stos rezerwy pusty. Odtwarzam z kart odkrytych...")
            current_passes_count += 1
            stock_pile.extend(waste_pile[::-1])
            waste_pile.clear()
            print(f"Rozpoczęto {current_passes_count}. przejście talii.")
            if max_passes != float('inf'):
                remaining_passes = max_passes - current_passes_count
                print(f"Pozostało przejść talii (po tym): {remaining_passes if remaining_passes >= 0 else 0}")
            action_taken = True # Recykling jest akcją
            # Po recyklingu, karty są gotowe do dobrania w NASTĘPNYM ruchu "dobierz kartę"
            # LUB jeśli chcemy, by działo się to atomowo, dobieramy od razu:
        elif not waste_pile:
            print("Brak kart w stosie rezerwy i w stosie odkrytym.")
            return # Zakończ, jeśli nic nie można zrobić
        elif current_passes_count >= max_passes:
            print(f"Osiągnięto limit ({int(max_passes) if max_passes != float('inf') else 'nieograniczone'}) przejść talii. Nie można odtworzyć stosu rezerwy.")
            return # Zakończ, jeśli limit osiągnięty

    # Teraz próbujemy dobrać karty, jeśli stos rezerwy nie jest pusty (mógł zostać właśnie uzupełniony)
    if stock_pile:
        num_to_draw_actual = min(len(stock_pile), draw_count)
        if num_to_draw_actual > 0:
            for _ in range(num_to_draw_actual):
                waste_pile.append(stock_pile.pop())
            print(f"Dobrano {num_to_draw_actual} {'kartę' if num_to_draw_actual == 1 else 'karty'}." if draw_count > 0 else "")
            action_taken = True # Dobranie kart jest akcją
        # Jeśli stock_pile istnieje, ale num_to_draw_actual == 0 (co nie powinno się zdarzyć przy draw_count > 0)
        # lub jeśli stock_pile stał się pusty po recyklingu a przed dobraniem (też nie powinno przy tej logice)
    elif not action_taken : # Jeśli stos był pusty i nie było recyklingu (np. limit przejść)
        print("Brak kart do dobrania ze stosu rezerwy.")


    if action_taken:
        save_game_state(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks)
        moves_count += 1

# --- Funkcje przenoszenia kart (move_card_...) pozostają w większości takie same ---
# Należy upewnić się, że używają globalnych stock_pile, waste_pile etc.
# i poprawnie wywołują save_game_state po udanym ruchu.

def move_card_from_stack_to_stack(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks):
    global moves_count
    move_successful = False
    temp_stacks_dict = copy.deepcopy(stacks_dict)
    temp_stacks_visible = copy.deepcopy(stacks_visible)

    while True:
        try:
            source_stack_input = input('Z którego stosu chcesz przenieść kartę? (1-7, 0 lub "anuluj"): ')
            if source_stack_input.lower() == "anuluj" or source_stack_input == "0":
                print("Anulowano operację.")
                break
            source_stack = int(source_stack_input)
            
            if not (1 <= source_stack <= 7 and temp_stacks_dict[source_stack]): # Sprawdź czy stos istnieje i nie jest pusty
                print("Niepoprawny numer stosu źródłowego lub stos jest pusty.")
                continue

            visible_indices = [i for i, v in enumerate(temp_stacks_visible[source_stack]) if v == 'visible']
            if not visible_indices:
                print("Na tym stosie nie ma odkrytych kart do przeniesienia.")
                break
            
            num_visible = len(visible_indices)
            print(f"Na stosie {source_stack} jest {num_visible} odkrytych kart (lub grup kart).")
            print("Wybierz numer karty/grupy do przeniesienia (1 = najwyżej odkryta, 0 lub 'anuluj'):")
            card_to_move_from_input = input()
            
            if card_to_move_from_input.lower() == "anuluj" or card_to_move_from_input == "0":
                print("Anulowano operację.")
                break
            
            card_to_move_from_choice = int(card_to_move_from_input) # Np. 1 dla najwyższej, 2 dla drugiej od góry itd.
            if card_to_move_from_choice < 1 or card_to_move_from_choice > num_visible:
                print("Nie ma takiej odkrytej karty/grupy.")
                continue
            
            # Indeks pierwszej karty z grupy do przeniesienia
            # visible_indices przechowuje indeksy widocznych kart w stosie.
            # Np. [2, 3, 4] - karty na pozycjach 2, 3, 4 są widoczne.
            # Jeśli użytkownik wybierze 1 (najwyższa), to jest to karta o indeksie visible_indices[-1] (czyli 4)
            # Jeśli wybierze 2 (druga od góry), to jest to karta o indeksie visible_indices[-2] (czyli 3)
            # Itd.
            card_actual_index_in_stack = visible_indices[-card_to_move_from_choice]

            cards_to_move = temp_stacks_dict[source_stack][card_actual_index_in_stack:]
            vis_to_move = temp_stacks_visible[source_stack][card_actual_index_in_stack:]

            target_stack_input = input('Na który stos chcesz przenieść? (1-7, 0 lub "anuluj"): ')
            if target_stack_input.lower() == "anuluj" or target_stack_input == "0":
                print("Anulowano operację.")
                break
            target_stack = int(target_stack_input)
            
            if not (1 <= target_stack <= 7):
                print("Niepoprawny numer stosu docelowego.")
                continue

            if source_stack == target_stack:
                print("Nie możesz przenieść kart na ten sam stos.")
                continue

            moving_card = cards_to_move[0] # Pierwsza karta z przenoszonej grupy decyduje o zasadach
            if not temp_stacks_dict[target_stack]: 
                if get_card_value(moving_card) == 13:
                    move_successful = True
                else:
                    print("Na pusty stos można położyć tylko Króla.")
            else: 
                top_card_target = temp_stacks_dict[target_stack][-1]
                if get_card_color(moving_card) != get_card_color(top_card_target) and \
                   get_card_value(moving_card) == get_card_value(top_card_target) - 1:
                    move_successful = True
                else:
                    print("Kolory kart muszą być na przemian, a wartość przenoszonej karty o 1 mniejsza.")
            
            if move_successful:
                temp_stacks_dict[target_stack].extend(cards_to_move)
                temp_stacks_visible[target_stack].extend(vis_to_move)
                del temp_stacks_dict[source_stack][card_actual_index_in_stack:]
                del temp_stacks_visible[source_stack][card_actual_index_in_stack:]
                if temp_stacks_dict[source_stack] and temp_stacks_visible[source_stack]: # Jeśli coś zostało na stosie źródłowym
                     if temp_stacks_visible[source_stack][-1] == 'invisible': # I ostatnia jest zakryta
                        temp_stacks_visible[source_stack][-1] = 'visible' # Odkryj ją
                print(f"Przeniesiono {len(cards_to_move)} kart(y) ze stosu {source_stack} na stos {target_stack}.")
                break 
        except ValueError:
            print("Wpisz poprawny numer.")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")
            break 
    
    if move_successful:
        stacks_dict.clear(); stacks_dict.update(temp_stacks_dict)
        stacks_visible.clear(); stacks_visible.update(temp_stacks_visible)
        save_game_state(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks)
        moves_count += 1


def move_card_from_waste_to_stack(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks):
    global moves_count
    if not waste_pile:
        print("Stos odkryty jest pusty.")
        return

    move_successful = False
    card_to_move = waste_pile[-1]
    # Tworzenie tymczasowych kopii do modyfikacji
    temp_waste_pile = copy.deepcopy(waste_pile)
    temp_stacks_dict = copy.deepcopy(stacks_dict)
    temp_stacks_visible = copy.deepcopy(stacks_visible)


    while True:
        try:
            target_stack_input = input('Na który stos chcesz przenieść kartę ze stosu odkrytego? (1-7, 0 lub "anuluj"): ')
            if target_stack_input.lower() == "anuluj" or target_stack_input == "0":
                print("Anulowano operację.")
                break
            target_stack = int(target_stack_input)

            if not (1 <= target_stack <= 7):
                print("Niepoprawny numer stosu docelowego.")
                continue
            
            if not temp_stacks_dict[target_stack]: # Stos docelowy jest pusty
                if get_card_value(card_to_move) == 13: # Tylko Król
                    move_successful = True
                else:
                    print("Na pusty stos można położyć tylko Króla.")
            else: # Stos docelowy nie jest pusty
                top_card_target = temp_stacks_dict[target_stack][-1]
                if get_card_color(card_to_move) != get_card_color(top_card_target) and \
                   get_card_value(card_to_move) == get_card_value(top_card_target) - 1:
                    move_successful = True
                else:
                    print("Kolory kart muszą być na przemian, a wartość przenoszonej karty o 1 mniejsza.")
            
            if move_successful:
                moved_card = temp_waste_pile.pop()
                temp_stacks_dict[target_stack].append(moved_card)
                temp_stacks_visible[target_stack].append('visible') # Karta z waste jest zawsze widoczna
                print("Przeniesiono kartę ze stosu odkrytego na stos.")
                break
        except ValueError:
            print("Wpisz poprawny numer.")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")
            break
            
    if move_successful:
        waste_pile.clear(); waste_pile.extend(temp_waste_pile)
        stacks_dict.clear(); stacks_dict.update(temp_stacks_dict)
        stacks_visible.clear(); stacks_visible.update(temp_stacks_visible)
        save_game_state(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks)
        moves_count += 1


def move_card_from_stack_to_final_stack(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks):
    global moves_count
    move_successful = False
    temp_stacks_dict = copy.deepcopy(stacks_dict)
    temp_stacks_visible = copy.deepcopy(stacks_visible)
    temp_foundation_stacks = copy.deepcopy(foundation_stacks)

    while True:
        try:
            source_stack_input = input('Z którego stosu chcesz przenieść kartę na fundament? (1-7, 0 lub "anuluj"): ')
            if source_stack_input.lower() == "anuluj" or source_stack_input == "0":
                print("Anulowano operację.")
                break
            source_stack = int(source_stack_input)
            
            if not (1 <= source_stack <= 7 and temp_stacks_dict[source_stack]): # Sprawdź czy stos istnieje i nie jest pusty
                print("Niepoprawny numer stosu źródłowego lub stos jest pusty.")
                continue
            
            if not temp_stacks_visible[source_stack] or temp_stacks_visible[source_stack][-1] == 'invisible':
                print("Najwyższa karta na tym stosie jest zakryta.") # Powinno być rzadkie, ale dla pewności
                continue

            card_to_move = temp_stacks_dict[source_stack][-1] # Zawsze bierzemy najwyższą kartę
            card_value = get_card_value(card_to_move)
            card_suit_symbol = card_to_move[-1]

            final_stacks_mapping = {'♥': '♥', '♦': '♦', '♣': '♣', '♠': '♠'} # Mapowanie symbolu na klucz fundamentu
            target_foundation_symbol = card_suit_symbol # Karta musi trafić na fundament swojego koloru

            foundation_stack_list = temp_foundation_stacks[target_foundation_symbol]

            if not foundation_stack_list: # Fundament jest pusty
                if card_value == 1: # Tylko As
                    move_successful = True
                else:
                    print(f"Na pusty fundament {target_foundation_symbol} można położyć tylko Asa.")
            else: # Fundament nie jest pusty
                top_foundation_card = foundation_stack_list[-1]
                if card_value == get_card_value(top_foundation_card) + 1:
                    move_successful = True
                else:
                    print(f"Karta musi mieć wartość o 1 większą niż karta na fundamencie {target_foundation_symbol}.")
            
            if move_successful:
                moved_card = temp_stacks_dict[source_stack].pop()
                temp_stacks_visible[source_stack].pop()
                temp_foundation_stacks[target_foundation_symbol].append(moved_card)
                
                if temp_stacks_dict[source_stack] and temp_stacks_visible[source_stack]: # Jeśli coś zostało
                    if temp_stacks_visible[source_stack][-1] == 'invisible':
                        temp_stacks_visible[source_stack][-1] = 'visible' # Odkryj nową kartę
                print(f"Przeniesiono kartę {moved_card} na fundament {target_foundation_symbol}.")
                break

        except ValueError:
            print("Wpisz poprawny numer.")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")
            break
            
    if move_successful:
        stacks_dict.clear(); stacks_dict.update(temp_stacks_dict)
        stacks_visible.clear(); stacks_visible.update(temp_stacks_visible)
        foundation_stacks.clear(); foundation_stacks.update(temp_foundation_stacks)
        save_game_state(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks)
        moves_count += 1


def move_card_from_waste_to_foundation(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks):
    global moves_count
    if not waste_pile:
        print("Stos odkryty jest pusty.")
        return

    move_successful = False
    card_to_move = waste_pile[-1]
    card_value = get_card_value(card_to_move)
    card_suit_symbol = card_to_move[-1]

    temp_waste_pile = copy.deepcopy(waste_pile)
    temp_foundation_stacks = copy.deepcopy(foundation_stacks)
    
    target_foundation_symbol = card_suit_symbol
    foundation_stack_list = temp_foundation_stacks[target_foundation_symbol]

    if not foundation_stack_list: # Fundament jest pusty
        if card_value == 1: # Tylko As
            move_successful = True
        else:
            print(f"Na pusty fundament {target_foundation_symbol} można położyć tylko Asa.")
    else: # Fundament nie jest pusty
        top_foundation_card = foundation_stack_list[-1]
        if card_value == get_card_value(top_foundation_card) + 1:
            move_successful = True
        else:
            print(f"Karta musi mieć wartość o 1 większą niż karta na fundamencie {target_foundation_symbol}.")

    if move_successful:
        moved_card = temp_waste_pile.pop()
        temp_foundation_stacks[target_foundation_symbol].append(moved_card)
        print(f"Przeniesiono kartę {moved_card} ze stosu odkrytego na fundament {target_foundation_symbol}.")
        
        # Aktualizacja stanu globalnego
        waste_pile.clear(); waste_pile.extend(temp_waste_pile)
        foundation_stacks.clear(); foundation_stacks.update(temp_foundation_stacks)
        save_game_state(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks)
        moves_count += 1
    # else: nie ma potrzeby, komunikaty są już wyświetlone


def check_win(foundation_stacks):
    return all(len(stack) == 13 for stack in foundation_stacks.values())

# --- GŁÓWNA CZĘŚĆ PROGRAMU ---

if __name__ == "__main__":
    get_player_nickname()
    game_running = True
    while game_running:
        menu_choice = main_menu()

        if menu_choice == "start":
            stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks = start_new_game()
            
            while True:
                display_stacks(stacks_dict, stacks_visible, foundation_stacks, stock_pile, waste_pile, make_card)
                if check_win(foundation_stacks):
                    final_time = int(time.time() - start_time)
                    final_minutes = final_time // 60
                    final_seconds = final_time % 60
                    print(f"\n   GRATULACJE, {player_nickname}! WYGRAŁEŚ PASJANSA!")
                    print(f"Ukończono w {moves_count} ruchach i {final_minutes:02d}:{final_seconds:02d}!")
                    add_to_hall_of_fame(player_nickname, moves_count, final_time)
                    input("\nNaciśnij Enter, aby wrócić do menu...")
                    break 
                
                print("\nWybierz akcję:")
                print("1 - Dobierz kartę (ze stosu STOCK)")
                print("2 - Przenieś kartę między stosami (z 1-7 na 1-7)")
                print("3 - Przenieś kartę ze stosu odkrytego na stos (WASTE na 1-7)")
                print("4 - Przenieś kartę na fundament ze stosu (z 1-7 na F)")
                print("5 - Przenieś kartę ze stosu odkrytego na fundament (WASTE na F)")
                print("6 - Cofnij ostatni ruch")
                print("9 - Wróć do Menu Głównego")
                print("0 - Zakończ grę")
                action = input("Twój wybór: ")
                
                if action == "1":
                    take_new_card(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks)
                elif action == "2":
                    move_card_from_stack_to_stack(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks)
                elif action == "3":
                    move_card_from_waste_to_stack(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks)
                elif action == "4":
                    move_card_from_stack_to_final_stack(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks)
                elif action == "5":
                    move_card_from_waste_to_foundation(stock_pile, waste_pile, stacks_dict, stacks_visible, foundation_stacks)
                elif action == "6":
                    undo_last_move()
                elif action == "9":
                    print("Wracam do Menu Głównego...")
                    break
                elif action == "0":
                    print("Dziękujemy za grę!")
                    game_running = False
                    break 
                else:
                    print("Nieznana akcja.")

        elif menu_choice == "exit":
            print("Dziękujemy za grę!")
            game_running = False