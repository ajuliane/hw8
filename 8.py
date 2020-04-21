import random

class LotoGame:
    def __init__(self, player):
        self.player = player

        self.result_number = random.sample(range(1,91), 90)


    def present_number(self):
        return self.result_number[0]
        del result_number[0]

    def play(self):
        for i in range(91):
            print(f' Новый бочонок: {self.present_number()} (осталось {len(self.result_number)})')

            decision = input ('Зачеркнуть цифру? (y/n)')
            if decision == 'y' or decision == 'Y':
                if self.player.check_number(self.present_number()) == false:
                    print('Вы проиграли')
                    break
            elif decision == 'n' or decision == 'N':
                if self.player.check_number(self.present_number()) == True:
                    print('Вы проиграли')
                    break
        print('Вы выиграли!')



class Player:
    def __init__(self, player):
        self.player = player
        self.card = [[],[],[]]
        for i in self.card:
            x = range(1, 91)
            list_number = random.sample(x, 5).sort()
            list_places = random.sample(range(1, 10), 5).sort()
            y = int()
            y = 1
            for i in range(5):
                if int(list_places[y-1]) == y:
                    self.card.append(list_number[i])
                else:
                    self.card.append(' ')
                    y = y + 1
            x = x - list_number

        def check_number(self, number):
            for x in self.card:
                if number in x:
                    return true

person = Player('Игрок')
game = LotoGame(person)