# Класс игрока 
class Player: 
    cards = None    
    score = None
    money = None

    def __init__(self):
       self.cards = []
       self.score = 0 
       self.money = 1000

    def clear_cards(self): 
        self.cards = []

    # функция вывода счета игрока
    def print_score(self):
        print(self.score)

    # функия получения счета 
    def get_score(self):
        return self.score

    # фунукия вывода валюты игрока 
    def print_money(self):
        print(self.money)

    # функция получения валюты игрока
    def get_money(self):
        return self.money

    # функция выставления нужного уровня денег. Вызывается в классе крупье.
    def set_money(self, money):
        self.money = money


    # фукнция взятия карты у крупье. После выполнения фукнции, карта добавится в список 
    # карт игрока, после чего уже может подсчитываться количество очков игрока
    def take_card(self, card): 
        self.cards.append(card)
        # для большей автоматизации процесса игры я использую фукнцию подсчета очков 
        # непосредственно после каждого получения карт игроком
        self.count_score()

    # функция парсинга значения карты. Необходима для корректного вычисления счета игрока
    def parse_card(self, card): 
        result_string = ""
        i = 0
        while card[i] != "_": 
            result_string = result_string + card[i] 
            i = i + 1
        return result_string


    # фукнция подсчета количества очков у игрока 
    def count_score(self):
        self.score = 0
        for i in self.cards: 
            card = self.parse_card(i)
            print(card)
            # если выпало число, только в виде символа, перевести его в число и сложить 
            # с остальным количеством очков 
            try: 
                self.score += int(card)
                # print(1 + 2)
            # если выпало не число, перевести его в числовое значение 
            # и сложить с остальным количеством очков
            except:
                if card == "J": 
                    self.score += 8
                elif card == "Q": 
                    self.score += 9
                elif card == "K": 
                    self.score += 10
                elif card == "A": 
                    self.score += 11


    # функия показа карт игрока 
    def print_cards(self):
        print("player cards:", self.cards)



