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
    cards = None    
    score = None

    def __init__(self):
       self.cards = []
       self.score = 0 


    # функция вывода счета игрока
    def print_score(self):
        print(self.score)

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
        


# Класс игры. Является основным классом.
class Game: 
    # создание всех необходимых переменных для начала и функционирования игры 
    croupier = Croupier()
    is_game = True

    # список игроков
    player1 = Player()
    player2 = Player()
    
    def determine_winner(self):
        player1_score = self.player1.get_score() # 10
        player2_score = self.player2.get_score() # 15
        if player1_score > 21 or player2_score > 21: 
            print(min(player1_score, player2_score))
            self.is_game = False
        else: 
            if player1_score - player2_score < 0: 
                print("Player 2 is Winner!")
                self.is_game = False
            else:
                print("Player 1 is Winner!")
                self.is_game = False

    def play(self):
        print("Player1: ")
        self.croupier.give_card(self.player1)
        self.player1.print_cards()
        print("Score: ", end="")
        self.player1.print_score()



        print()
        print()
        
        print("Player2: ")
        self.croupier.give_card(self.player2)
        self.player2.print_cards()
        print("Score: ", end="")
        self.player2.print_score()

        while self.is_game == True: 
            continue_game1 = input("Player1: Do you want to take another card? (y/n): ")
            if continue_game1 == "y": 
                self.croupier.give_card(self.player1)
            continue_game2 = input("Player2: Do you want to take another card? (y/n): ")
            if continue_game2 == "y": 
                self.croupier.give_card(self.player2)
            elif continue_game1 == "n" and continue_game2 == "n": 
                self.is_game = False
            print("Player1: ")
            self.player1.print_cards()
            print("Score: ", end="")
            self.player1.print_score()



            print()
            print()
            print("Player2: ")
            self.player2.print_cards()
            print("Score: ", end="")
            self.player2.print_score()

        self.determine_winner()
        # print("Player1: ", end="")
        # self.croupier.give_card(self.player1)
        # print("Score: ", end = "")
        # self.croupier.player1.print_score()


        # self.croupier.give_card("Player2: ", self.player2)
        # print("Player2: score: ", end = "")
        # self.croupier.player2.print_score()
        # while self.is_game:
            
        #     continue_game1 = input("Player1: Do you want to take another card? (y/n): ")
        #     continue_game2 = input("Player2: Do you want to take another card? (y/n): ")
        #     if continue_game1 == "y": 
        #         self.croupier.give_card("Player1: ", self.player1)
        #     if continue_game2 == "y": 
        #         self.croupier.give_card("Player2: ", self.player2)
        #     elif continue_game1 == "n" and continue_game2 == "n": 
        #         self.is_game = False
        #     print("Player1: score: ", end = "")
        #     self.croupier.player1.print_score()

        #     print("Player2: score: ", end = "")
        #     self.croupier.player2.print_score()
        # self.determine_winner()
        
    

# основной цикл игры состоит из раздачи карты игроку, уточнение продолжения игры и 
# как финальная стадия, подсчет очков и вывод игрока и его карт

# a = Croupier()
# a.give_card()
# a.give_card()
# a.give_card()
# a.print_cards()

# a.player1.print_cards()
# a.player1.count_score()
# a.player1.print_score()

# n = '2'
# print(int(n) + 2)

g = Game()
g.play()




# p1 = Player()
# p2 = Player()
# p3 = Player()
# p4 = Player()
# p5 = Player()
# c = Croupier()
# c.give_card(p1)
# c.give_card(p2)
# c.give_card(p3)

# p1.print_cards()
# p2.print_cards()
# p3.print_cards()
# p4.print_cards()
# p5.print_cards()

# p1.cards = ['A']
# p2.cards.append('Q')

# p1.print_cards()
# p2.print_cards()







# версия функции play, в которой класс крупье реализован с полями класса игрока 
# def play(self):
#         print("Player1: ")
#         self.croupier.give_card(self.croupier.player1)
#         self.croupier.player1.print_cards()
#         print("Score: ", end="")
#         self.croupier.player1.print_score()



#         print()
#         print()
        
#         print("Player2: ")
#         self.croupier.give_card(self.croupier.player2)
#         self.croupier.player2.print_cards()
#         print("Score: ", end="")
#         self.croupier.player2.print_score()

#         while self.is_game == True: 
#             continue_game1 = input("Player1: Do you want to take another card? (y/n): ")
#             if continue_game1 == "y": 
#                 self.croupier.give_card(self.croupier.player1)
#             continue_game2 = input("Player2: Do you want to take another card? (y/n): ")
#             if continue_game2 == "y": 
#                 self.croupier.give_card(self.croupier.player2)
#             elif continue_game1 == "n" and continue_game2 == "n": 
#                 self.is_game = False
#             print("Player1: ")
#             self.croupier.player1.print_cards()
#             print("Score: ", end="")
#             self.croupier.player1.print_score()



#             print()
#             print()
#             print("Player2: ")
#             self.croupier.player2.print_cards()
#             print("Score: ", end="")
#             self.croupier.player2.print_score()

#         self.determine_winner()