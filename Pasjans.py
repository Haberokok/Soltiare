import queue
import random

def display_rules():
    print("""
ZASADY GRY W PASJANSA

Cel gry:
- Ułóż wszystkie 52 karty na czterech stosach końcowych według koloru i rosnąco: od asa do króla.

Przygotowanie:
- Używana jest jedna talia 52 kart (bez jokerów).
- Karty mają 4 kolory: ♥ ♦ ♠ ♣, wartości od A do K.
- Tworzy się 7 kolumn:
  1. kolumna: 1 odkryta karta
  2. kolumna: 1 zakryta, 1 odkryta
  ...
  7. kolumna: 6 zakrytych, 1 odkryta
- Pozostałe karty trafiają na stos rezerwowy.
- Są 4 puste stosy końcowe (po jednym dla każdego koloru).

Ruchy:
- W kolumnach karty układa się malejąco (K → A), naprzemiennie kolorami (czarna–czerwona).
- Można przenosić pojedyncze karty lub całe poprawne sekwencje.
- Na pustą kolumnę można przenieść tylko króla (lub sekwencję zaczynającą się od króla).
- Na stos końcowy można przenieść tylko kartę kolejnej wartości i tego samego koloru (np. A♠ → 2♠ → 3♠ itd.).

Stos rezerwowy:
- Dobierasz jedną kartę na raz.
- Możesz przeglądać stos bez limitu.
- Po wyczerpaniu stosu można go przetasować i użyć ponownie.

Wygrana:
- Udało ci się ułożyć wszystkie karty w 4 stosach końcowych.

Przegrana:
- Jeśli nie ma już możliwych ruchów – możesz zakończyć grę i rozpocząć od nowa.


""")
    

def start_game():
    while True:
        start = input('Wpisz "START" aby rozpocząć: ')
        start = start.lower()
        if start == 'start':
            display_rules()
            break
        else:
            print('Wpisałeś błednie!!!')

    
def create_deck():
    deck = []
    colors = ['♥', '♦', '♠', '♣']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for color in colors:
        for value in values:
            deck.append(f"{value}{color}")
    random.shuffle(deck)
    return deck
        

def create_stacks():
    stock_get = queue.LifoQueue(24)
    waste_stack = []
    new_stock = queue.LifoQueue(24)
    while not stock_get.full():
        stock_get.put(deck[0])
        del deck[0]
    
    

    stack_1 = []
    stack_1_visible = []
    stack_2 = []
    stack_2_visible = []
    stack_3 = []
    stack_3_visible = []
    stack_4 = []
    stack_4_visible = []
    stack_5 = []
    stack_5_visible = []
    stack_6 = []
    stack_6_visible = []
    stack_7 = []
    stack_7_visible = []

    vis = 'visible'
    unvis = 'unvisible'

    for i in range(28):
        if len(deck) == 28:
            stack_1.append(deck[0])
            stack_1_visible.append(vis)
            del deck[0]
        elif len(deck) <= 27 and len(deck) >= 26:
            stack_2.append(deck[0])
            if len(deck) == 26:
                stack_2_visible.append(vis)
            else:
                stack_2_visible.append(unvis) 
            del deck[0]
        elif len(deck) <= 25 and len(deck) >= 23:
            stack_3.append(deck[0])
            if len(deck) == 23:
                stack_3_visible.append(vis)
            else:
                stack_3_visible.append(unvis)
            del deck[0]
        elif len(deck) <= 22 and len(deck) >= 19:
            stack_4.append(deck[0])
            if len(deck) == 19:
                stack_4_visible.append(vis)
            else:
                stack_4_visible.append(unvis)
            del deck[0]
        elif len(deck) <= 18 and len(deck) >= 14:
            stack_5.append(deck[0])
            if len(deck) == 14:
                stack_5_visible.append(vis)
            else:
                stack_5_visible.append(unvis)
            del deck[0]
        elif len(deck) <= 13 and len(deck) >= 8:
            stack_6.append(deck[0])
            if len(deck) == 8:
                stack_6_visible.append(vis)
            else:
                stack_6_visible.append(unvis)
            del deck[0]
        elif len(deck) <= 7:
            stack_7.append(deck[0])
            if len(deck) == 1:
                stack_7_visible.append(vis)
            else:
                stack_7_visible.append(unvis)
            del deck[0]

        
    
    trefl_stack = queue.LifoQueue(13)
    karo_stack = queue.LifoQueue(13)
    kier_stack = queue.LifoQueue(13)
    pik_stack = queue.LifoQueue(13)

    foundaments = [trefl_stack, karo_stack, kier_stack, pik_stack]
    
    stacks_dictionary = {1 : stack_1, 2 : stack_2, 3 : stack_3, 4 : stack_4, 5 : stack_5, 6 : stack_6, 7 : stack_7}
    stacks_visible = {1 : stack_1_visible, 2 : stack_2_visible, 3 : stack_3_visible, 4 : stack_4_visible, 5 : stack_5_visible, 6 : stack_6_visible, 7 : stack_7_visible}

    return stock_get, waste_stack, new_stock, stacks_dictionary, stacks_visible


def take_new_card():
    if not stock_get.empty():
        if len(waste_stack) == 3:
            del waste_stack[0]
        card = stock_get.get()
        waste_stack.append(card)
        if len(waste_stack) == 3 and new_stock.empty():
            new_stock.put(waste_stack[0])
    

def card_transfer_stack_to_stack():
    card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

    print(stacks_dictionary)
    while True:
        try:
            stack_out = int(input('Z którego stosu przenieść (1-7): '))
            stack_in = int(input('Na który stos przenieść (1-7): '))
            start_card = int(input('Od której karty przenieść: '))

            if 1 <= stack_out <= 7 and 1 <= stack_in <= 7 and stacks_dictionary.get(stack_out) and 1 <= start_card <= len(stacks_dictionary[stack_out]):
                start_index = start_card - 1

                if stacks_visible[stack_out][start_index] == 'visible':
                    card_to_move = stacks_dictionary[stack_out][start_index]
                    value_to_move = card_to_move[:-1] 
                
                    if stacks_dictionary[stack_in]:
                        top_card_in = stacks_dictionary[stack_in][-1]
                        value_top_card = top_card_in[:-1]
                        color_to_move = card_to_move[-1]
                        color_top_card = top_card_in[-1]
                        if (color_to_move == '♥' or color_to_move == '♦') and (color_top_card == '♠' or color_top_card == '♣'):
                            if value_to_move in card_values and value_top_card in card_values and card_values[value_to_move] == card_values[value_top_card] - 1:
                                cards_to_move = stacks_dictionary[stack_out][start_index:]
                                stacks_dictionary[stack_in].extend(cards_to_move)
                                del stacks_dictionary[stack_out][start_index:]
                                break 
                            else:
                                print('Karta posiada złą wartość (musi być o 1 mniejsza).')
                        elif (color_to_move == '♣' or color_to_move == '♠') and (color_top_card == '♦' or color_top_card == '♥'):
                            
                            if value_to_move in card_values and value_top_card in card_values and card_values[value_to_move] == card_values[value_top_card] - 1:
                                cards_to_move = stacks_dictionary[stack_out][start_index:]
                                stacks_dictionary[stack_in].extend(cards_to_move)
                                del stacks_dictionary[stack_out][start_index:]
                                break 
                            else:
                                print('Karta posiada złą wartość (musi być o 1 mniejsza).')
                        
                        else:
                            print('Nieprawidlowy kolor (kolor musi byc przeciwny, czyli czarny-czerwony, czerwony-czarny)')
                    elif not stacks_dictionary[stack_in] and value_to_move == 'K':
                        cards_to_move = stacks_dictionary[stack_out][start_index:]
                        stacks_dictionary[stack_in].extend(cards_to_move)
                        del stacks_dictionary[stack_out][start_index:]
                        break 
                    elif not stacks_dictionary[stack_in]:
                        print("Na pusty stos można przenieść tylko Króla.")

                else:
                    print(f"Karta {start_card} nie jest widoczna.")
            else:
                print("Nieprawidłowy numer stosu lub karty.")
        except ValueError:
            print("Wprowadź liczby.")
        except KeyError:
            print("Błąd: Nie znaleziono podanego numeru stosu w słowniku.")
        except IndexError:
            print("Błąd: Problem z dostępem do karty - czy stos docelowy jest pusty lub indeks poza zakresem?")


def card_transfer_stack_to_foundament():
    while True:
        try:
            stack_out = int(input('Z którego stosu przenieść (1-7): '))
            stack_in = int(input('Na który stos przenieść (1-7): '))
            start_card = int(input('Od której karty przenieść: '))

            if 1 <= stack_out <= 7 and 1 <= stack_in <= 7 and stacks_dictionary.get(stack_out) and 1 <= start_card <= len(stacks_dictionary[stack_out]):
                start_index = start_card - 1

                if stacks_visible[stack_out][start_index] == 'visible':
                    card_to_move = stacks_dictionary[stack_out][start_index]
                    value_to_move = card_to_move[:-1]
                    
                   
                    
                else:
                    print(f"Karta {start_card} nie jest widoczna.")
            else:
                print("Nieprawidłowy numer stosu lub karty.")
        except ValueError:
            print("Wprowadź liczby.")
        except KeyError:
            print("Błąd: Nie znaleziono podanego numeru stosu w słowniku.")
        except IndexError:
            print("Błąd: Problem z dostępem do karty - czy stos docelowy jest pusty lub indeks poza zakresem?")
                

                


                                


    

    
    
        


        


        


        

        
    







start_game()
deck = create_deck()
stock_get, waste_stack, new_stock, stacks_dictionary, stacks_visible, foundaments = create_stacks()
card_transfer_stack_to_stack()
print(stacks_dictionary)



