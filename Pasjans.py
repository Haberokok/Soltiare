from asyncio.constants import DEBUG_STACK_DEPTH
import queue
import random


def start_game():
    while True:
        start = input('Wpisz "START" aby rozpocząć: ')
        start = start.lower()
        if start == 'start':
            wypisz_zasady()
            break
        else:
            print('Wpisałeś błednie!!!')


def wypisz_zasady():
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
    
def create_deck():
    deck = []
    colors = ['♥', '♦', '♠', '♣']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
    for color in colors:
        for value in values:
            deck.append(f"{value}{color}")
    random.shuffle(deck)
    return deck
        

def create_stacks(deck):
    used = []
    stock = queue.LifoQueue(24)
    while not stock.full():
        stock.put(deck[0])
        del deck[0]
    print(stock)
     
    


start_game()
create_deck()
create_stacks()

