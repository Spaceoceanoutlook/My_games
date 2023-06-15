cityes = set()

with open('Cityes_db.txt', encoding='utf-8') as file:
    for i in file.readlines():
        cityes.add(i[:-1])


class Cityes:
    cityes_in_game = []
    last_letter = []

    def __init__(self, enter_city):
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
                i_cut = self.check_letter(i)
                if i_cut not in self.cityes_in_game and self.user_city[-1].lower() == i_cut[0].lower():
                    self.cityes_in_game.append(i_cut)
                    self.last_letter.append(i_cut[-1].upper())
                    return i, True
            return f'Я больше не знаю городов на букву "{self.letter}". Вы победили', False
        return 'Такой город уже был', True


game = True
while game:
    city = input('Введите название города: ')
    check_city = Cityes.check_letter(city)
    c = Cityes(check_city)
    response, game = c.check_city()
    print(response)