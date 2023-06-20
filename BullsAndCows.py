from random import choice

base = []
with open('BullsAndCows_db.txt', 'r', encoding='utf-8') as file:
    for line in file:
        base.append(line[:-1])

word_from_base = choice(base).lower()
print(f"Какое слово из {len(word_from_base)} букв я загадал?")


class BullsAndCows:
    def __init__(self, user_word: str):
        self.user_word = user_word.lower()

    def check(self):
        a = []
        if self.user_word == word_from_base:
            return 'Вы угадали!', False
        elif len(self.user_word) == len(word_from_base):
            for i, j in zip(self.user_word, word_from_base):
                if i == j:
                    a.append('Bull')
                elif i in word_from_base:
                    a.append('Cow')
                else:
                    a.append('[ ]')
            return " ".join(a), True
        else:
            return 'Вы ввели слово неправильной длины', True


status = True
while status:
    word = input("Ваш вариант: ")
    new_game = BullsAndCows(word)
    answer, status = new_game.check()
    print(answer)

end = input('Чтобы закончить игру нажмите Enter')