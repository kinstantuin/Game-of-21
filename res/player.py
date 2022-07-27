# Класс игрока 
class Player: 
    cards = None    
    score = None

    def __init__(self):
       self.cards = []
       self.score = 0 


    # функция вывода счета игрока
    def print_score(self):
        print(self.score)

    # функия получения счета 
    def get_score(self):
        return self.score

    # фукнция взятия карты у крупье. После выполнения фукнции, карта добавится в список 
    # карт игрока, после чего уже может подсчитываться количество очков игрока
    def take_card(self, card): 
        self.cards.append(card)
        # для большей автоматизации процесса игры я использую фукнцию подсчета очков 
        # непосредственно после каждого получения карт игроком
        self.count_score()

    # фукнция подсчета количества очков у игрока 
    def count_score(self):
        self.score = 0
        for i in self.cards: 
            # если выпало число, только в виде символа, перевести его в число и сложить 
            # с остальным количеством очков 
            try: 
                self.score += int(i)
                # print(1 + 2)
            # если выпало не число, перевести его в числовое значение 
            # и сложить с остальным количеством очков
            except:
                if i == 'J': 
                    self.score += 8
                elif i == 'Q': 
                    self.score += 9
                elif i == 'K': 
                    self.score += 10
                elif i == 'A': 
                    self.score += 11


    # функия показа карт игрока 
    def print_cards(self):
        print("player cards:", self.cards)



