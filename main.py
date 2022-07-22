# массив карт, которые будут выдаваться игроку, после чего из игральной колоды будут 
# исключаться выданные карты
from random import *


cards = [
    '6', '6', '6', '6', 
    '7', '7', '7', '7', 
    '8', '8', '8', '8', 
    '9', '9', '9', '9', 
    '10', '10', '10', '10',
    'J', 'J', 'J', 'J',
    'Q', 'Q', 'Q', 'Q',
    'K', 'K', 'K', 'K',
    'A', 'A', 'A', 'A',
]

class Croupier:
    # копия исходной колоды карт именно для крупье (заряженная в ларьке) 
    cards = cards


    def print_cards(self):
        print(self.cards)

    # фукнция выдачи карт
    def give_card(self): 
        rand_index = randint(0, len(cards) - 1)
        print(self.cards[rand_index])
        self.cards.pop(rand_index)  


class Player: 
    cards = []
    score = 0


class Game: 
    


a = Croupier()
a.give_card()
