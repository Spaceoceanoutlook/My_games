from random import choice


base = ["корова", "молоко", "стекло", "лопата", "корыто", "дорога", "синьор", "ракета", "ворота", "ананас"]

word_from_base = choice(base).lower()
print(word_from_base)
print(f"Какое слово из {len(word_from_base)} букв я загадал?")


class BullsAndCows:
    def __init__(self, user_word: str):
        self.user_word = user_word.lower()

    def check(self):
        if self.user_word == word_from_base:
            return 'Вы угадали!', False
        else:
            return 'Попробуйте еще раз', True


status = True
while status:
    word = input("Ваш вариант: ")
    new_game = BullsAndCows(word)
    answer, status = new_game.check()
    print(answer)