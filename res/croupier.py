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

    bet = None
    
    # функция показа карт крупье
    def print_cards(self):
        print(self.cards)

    # фукнция выдачи карт
    def give_card(self, player): 
        rand_index = randint(0, len(cards) - 1) 
        # print("Выдана карта:", self.cards[rand_index])
        player.take_card(self.cards.pop(rand_index))
        return
    

    # функция для того, чтобы добавить валюту опредлеенному игроку 
    def give_money(self, player, money): 
        player.set_money(player.money + money)

    def take_money(self, player, money): 
        player.set_money(player.money - money)

    # функция для вывода ставки на текущий раунд 
    def print_bet(self):
        print(self.bet)

    # геттер для ставки крупье
    def get_bet(self):
        return self.bet

    # сеттер для ставки крупье (будет использоваться как изменение ставки игроком)
    def set_bet(self, bet):
        self.bet = bet