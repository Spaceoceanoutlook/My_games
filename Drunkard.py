from random import shuffle


class Deck:
    suits = ['Буба', 'Черви', 'Пики', 'Крести']
    weight = [i for i in range(6, 15)]
    numbers = ['6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']

    """ Создание колоды """

    def __init__(self):
        self.deck = [(n, s, w) for s in self.suits for w, n in zip(self.weight, self.numbers)]

    """ Раздача карт игроку 1"""

    def distribution_player(self):
        deck_player = self.deck[:len(self.deck) // 2]
        return deck_player

    """ Раздача карт игроку 2 """

    def distribution_computer(self):
        deck_computer = self.deck[len(self.deck) // 2:]
        return deck_computer

    """ Перетусовать колоду """

    @staticmethod
    def mix(deck_for_mix):
        shuffle(deck_for_mix)
        return deck_for_mix

    """ Проверка хода """

    @staticmethod
    def check(pl1: list, pl2: list):
        counter = 1
        list_for_noun = []
        while True:
            print(f'Ход № {counter}')
            temporary = [pl1[0], pl2[0]]
            if len(list_for_noun) > 0:
                temporary = list_for_noun + temporary
            pl1.remove(pl1[0])
            pl2.remove(pl2[0])
            print(f'Игрок 1 - {temporary[-2][0]} vs Игрок 2 - {temporary[-1][0]}')
            if temporary[-2][2] > temporary[-1][2]:
                pl1 += temporary
                print('Игрок 1 забирает')
                temporary.clear()
                list_for_noun.clear()
            elif temporary[-2][2] == temporary[-1][2]:
                list_for_noun += temporary
                print('Ничья')
            else:
                pl2 += temporary
                print('Игрок 2 забирает')
                temporary.clear()
                list_for_noun.clear()
            counter += 1
            if counter % 18 == 0:
                print('Тусую карты')
                Deck.mix(pl1)
                Deck.mix(pl2)
            if len(pl1) == 0 and len(list_for_noun) > 0:
                print('У Игрока 1 нет карт и при этом ничья. Берется карта у Игрока 2')
                pl1.append(pl2[0])
                pl2.remove(pl2[0])
            if len(pl2) == 0 and len(list_for_noun) > 0:
                print('У Игрока 2 нет карт и при этом ничья. Берется карта у Игрока 1')
                pl2.append(pl1[0])
                pl1.remove(pl1[0])
            if len(pl1) == 0:
                print('Игрок 1 проиграл')
                break
            if len(pl2) == 0:
                print('Игрок 2 проиграл')
                break


class Players:
    pass


# Создаем колоду и игроков
deck = Deck()
player1 = Players()
player2 = Players()

# Раздаем колоду игрокам
player1.deck = deck.distribution_player()
player2.deck = deck.distribution_computer()

# Тусуем колоду
Deck.mix(player1.deck)
Deck.mix(player2.deck)

# Запускаем игру
Deck.check(player1.deck, player2.deck)
