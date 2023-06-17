# with open('Words_db.txt', 'r', encoding='utf-8') as f:
#     comp_words = list(set(f.read().split()))
comp_words = []
with open('Words_db.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        comp_words.append(line[:-1])
print(comp_words)

class Word:
    answer = []

    def __init__(self, long_word: str):
        self.long_word = long_word.lower()

    def search_words(self):
        for word in comp_words:
            for symbol in word:
                if symbol not in self.long_word and word.count(symbol) > self.long_word.count(symbol):
                    break
            else:
                self.answer.append(word)
        if len(self.answer) == 0:
            return 'Я не составил ни одного слова'
        return f"Мои слова: {', '.join(self.answer)}"

    def check_user_words(self, user_words: list):
        if len(user_words) > len(self.answer):
            return f'Количество ваших слов: {len(user_words)}, моих - {len(self.answer)} \nВы победили!'
        elif len(user_words) < len(self.answer):
            return f'Количество ваших слов: {len(user_words)}, моих - {len(self.answer)} \nВы проиграли!'
        else:
            return f'Количество ваших слов: {len(user_words)}, моих - {len(self.answer)} \nНичья!'

    def __str__(self):
        return self.long_word


w = Word("контрацептив")

print(w)
user = input().split()
print(w.search_words())
print(w.check_user_words(user))


with open('Words_db.txt', 'a', encoding='utf-8') as f:
    for i in user:
        if i not in comp_words:
            f.write('\n')
            f.writelines(i)



