from random import shuffle

with open('Cityes_db.txt', encoding='utf-8') as file:
    cityes = [line[:-1] for line in file.readlines()]


class Cityes:
    cityes_in_game = []
    last_letter = []

    def __init__(self, enter_city: str):
        self.user_city = enter_city.capitalize()
        self.letter = self.user_city[-1].upper()

    @staticmethod
    def check_letter(check: str) -> str:
        while check[-1].upper() in 'ЙЪЫЬ':
            check = check[:-1]
        return check

    def check_city(self):
        if len(self.last_letter) > 0 and self.user_city[0] != self.last_letter[-1]:
            return f'Город должен начинаться на букву "{self.last_letter[-1]}"', True
        if self.user_city not in self.cityes_in_game:
            self.cityes_in_game.append(self.user_city)
            for i in cityes:
                new_i = self.check_letter(i)
                if new_i not in self.cityes_in_game and self.user_city[-1].lower() == new_i[0].lower():
                    self.cityes_in_game.append(new_i)
                    self.last_letter.append(new_i[-1].upper())
                    return i, True
            return f'Я больше не знаю городов на букву "{self.letter}". Вы победили', False
        return 'Такой город уже был', True


game = True
shuffle(cityes)
who = input("Кто начинает? Ты - 1, Я - любой символ ")
if who == str(1):
    first_city = cityes[0]
    print(first_city)
    first_city = Cityes.check_letter(first_city)
    Cityes.cityes_in_game.append(first_city)
    Cityes.last_letter.append(first_city[-1].upper())

while game:
    your_city = input('Введите название города: ')
    check_city = Cityes.check_letter(your_city)
    city = Cityes(check_city)
    response, game = city.check_city()
    print(response)
