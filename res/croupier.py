from random import *

# массив карт, которые будут выдаваться игроку, после чего из игральной колоды будут 
# исключаться выданные карты        
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

    
    
    # функция показа карт крупье
    def print_cards(self):
        print(self.cards)

    # фукнция выдачи карт
    def give_card(self, player): 
        rand_index = randint(0, len(cards) - 1) 
        # print("Выдана карта:", self.cards[rand_index])
        player.take_card(self.cards.pop(rand_index))
        return
        