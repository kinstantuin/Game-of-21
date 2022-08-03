from random import *

# массив карт, которые будут выдаваться игроку, после чего из игральной колоды будут 
# исключаться выданные карты        
cards = [   
    '6_C', '6_S', '6_D', '6_H', 
    '7_C', '7_S', '7_D', '7_H', 
    '8_C', '8_S', '8_D', '8_H', 
    '9_C', '9_S', '9_D', '9_H', 
    '10_C','10_S','10_D','10_H',
    'J_C', 'J_S', 'J_D', 'J_H',
    'Q_C', 'Q_S', 'Q_D', 'Q_H',
    'K_C', 'K_S', 'K_D', 'K_H',
    'A_C', 'A_S', 'A_D', 'A_H',
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