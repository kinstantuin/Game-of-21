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


# Класс игрока 
class Player: 
    cards = []
    
    score = 0

    # функция вывода счета игрока
    def print_score(self):
        print(self.score)

    # фукнция взятия карты у крупье. После выполнения фукнции, карта добавится в список 
    # карт игрока, после чего уже может подсчитываться количество очков игрока
    def take_card(self, card): 
        self.cards.append(card)

    # фукнция подсчета количества очков у игрока 
    def count_score(self):
        for i in self.cards: 
            try: 
                self.score += int(i)
                # print(1 + 2)
            except:
                print("не число")
                




    # функия показа карт игрока 
    def print_cards(self):
        print("player cards:", self.cards)




class Croupier:
    # копия исходной колоды карт именно для крупье (заряженная в ларьке) 
    cards = cards

    # список игроков, закрепленных за одним крупье
    player1 = Player()
    player2 = Player()
    
    # функция показа карт крупье
    def print_cards(self):
        print(self.cards)

    # фукнция выдачи карт
    def give_card(self): 
        rand_index = randint(0, len(cards) - 1) 
        self.player1.take_card(self.cards.pop(rand_index))
        


# Класс игры. Является основным классом.
class Game: 
    croupier = Croupier()
    player1 = Player()
    player2 = Player()

    


a = Croupier()
a.give_card()
a.print_cards()

a.player1.print_cards()
a.player1.count_score()

# n = '2'
# print(int(n) + 2)