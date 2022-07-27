from croupier import Croupier
import player


# Класс игры. Является основным классом.
class Game: 
    # создание всех необходимых переменных для начала и функционирования игры 
    croupier = Croupier()
    is_game = True

    # список игроков
    player1 = player.Player()
    player2 = player.Player()

    # функия для проверки счета игроков на перебор очков. Вызывается каждую итерацию после того 
    # как игрок возьмет карты. Если хоть у одного игрока количество очков больше 21, игра заканчивается и определяется победитель
    def check_loose(self): 
        # создаются переменные для хранения очков игрока
        player1_score = self.player1.get_score() # 10
        player2_score = self.player2.get_score() # 15

        # если у двух игроков сразу больше максимального количества очков, они оба проигрывают
        # возвращается значение -1 для того, чтобы знать, вызывать фукнию determine_winner или нет
        if player1_score > 21 and player2_score > 21: 
            print("Both loose!")
            self.is_game = False
            return -1
        # если у первого игрока колиество очков больше максимального, он проигрывает 
        elif player1_score > 21: 
            print("Player 2 is Winner!")
            self.is_game = False
            return -1
        # если у второго игрока количество очков больше максимального, он проигрывает
        elif player2_score > 21:
            print("Player 1 is Winner!")
            self.is_game = False
            return -1

        
    # Определяется победитель. Функция вызывается в том случае, если оба игрока отказались брать карты
    def determine_winner(self):
        # создаю переменные с очками каждого из игроков 
        player1_score = self.player1.get_score() # 10
        player2_score = self.player2.get_score() # 15
        
        # если разность очков второго игрока от первого будет меньше нуля, значит выиграл второй игрок 
        if player1_score - player2_score < 0: 
            print("Player 2 is Winner!")
            self.is_game = False
        # в обратном случае выигрывает первый игрок
        else:
            print("Player 1 is Winner!")
            self.is_game = False


    # основная функция, которая реализует остальные функции и классы
    def play(self):
        # флаг для определения перебора больше положенного количества очков у игрока
        flag_check_loose = False

        # первоначальная раздача карт первому игроку и последующий вывод карт с набранными очками
        print("Player1: ")
        self.croupier.give_card(self.player1)
        print("Money: ", end="")
        self.player1.print_money()
        self.player1.print_cards()
        print("Score: ", end="")
        self.player1.print_score()


        # отделение вывода первого игрока от второго новыми строками
        print()
        print()

        # первоначальная раздача карт второму игроку и последующий вывод карт с набранными очками
        print("Player2: ")
        self.croupier.give_card(self.player2)
        print("Money: ", end="")
        self.player2.print_money()
        self.player2.print_cards()
        print("Score: ", end="")
        self.player2.print_score()

        # основной цикл игры. Будет продолжаться до того момента, как двое из игроков откажутся брать карты 
        # или один (или оба) из игроков не наберет количество очков сверх нормы (> 21)
        while self.is_game == True: 
            # "Флаг" для обозначения продолжения игры первым игроком
            continue_game1 = input("Player1: Do you want to take another card? (y/n): ")
            # если игрок согласился взять карту - выдается карта
            if continue_game1 == "y": 
                self.croupier.give_card(self.player1)

            # "Флаг" для обозначения продолжения игры вторым игроком
            continue_game2 = input("Player2: Do you want to take another card? (y/n): ")
            # если игрок согласился взять карту - выдается карта
            if continue_game2 == "y": 
                self.croupier.give_card(self.player2)
            # если оба игрока ответили отрицательно на вопрос взять еще карты 
            # основной цикл игры заканчивается
            elif continue_game1 == "n" and continue_game2 == "n": 
                self.is_game = False

            # каждую итерацию цикла выводятся деньги, карты и счет первого игрока 
            print("Player1: ")
            print("Money: ", end="")
            self.player1.print_money()
            self.player1.print_cards()
            print("Score: ", end="")
            self.player1.print_score()
            
            

            # отделение вывода игроков пустыми строчками
            print()
            print()
            # каждую итерацию цикла выводятся деньги, карты и счет второго игрока 
            print("Player2: ")
            print("Money: ", end="")
            self.player2.print_money()
            self.player2.print_cards()
            print("Score: ", end="")
            self.player2.print_score()

            # вызывается функция для слежения за превышением максимально допустимого количества очков
            # если кто-то из игроков набрал больше положенного - функция возвращает значение -1, исходя из которого
            # я ставлю флагу flag_check_loose значение True, чтобы в дальнейшем не вызывать функцию determine_winner
            # после всего этого цикл сразу завершается
            if self.check_loose() == -1: 
                flag_check_loose = True
                break 

        # если флаг False (функция проверки превышения максимального количества очков у игрока check_false не определила
        # то, что у какого-то из игроков количество очков больше максимального) - вызывается фукнция определения победителя
        if flag_check_loose == False:
            self.determine_winner()        
    
