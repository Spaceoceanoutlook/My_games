from random import choice


def tick_tack():
    def start():
        a = 1
        b = 4
        for i in range(a, b):
            for j in range(a, b):
                print(f"[{j}]", end="")
            a += 3
            b += 3
            print()

    def game_round():
        a = 1
        b = 4
        for i in range(a, b):
            for j in range(a, b):
                if j in user:
                    j = "[x]"
                elif j in comp:
                    j = "[o]"
                else:
                    j = "[ ]"
                print(j, end="")
            a += 3
            b += 3
            print()

    def user_victory_check():
        nonlocal my_game, c
        for i in check_win:
            for j in i:
                if j in user:
                    c += 1
                if c == 3:
                    print("Вы победили")
                    my_game = False
                    break
            c = 0

    def computer_victory_check():
        nonlocal my_game, c
        for i in check_win:
            for j in i:
                if j in comp:
                    c += 1
                if c == 3:
                    print("Вы проиграли")
                    my_game = False
                    break
            c = 0

    def computer_protection_algorithm():
        nonlocal c, v
        comp_input = choice(game)
        count = 0
        count_2 = 0
        for i in check_win:
            for j in i:
                if j in comp:
                    v += 1
                    count_2 += j
                    if v == 2 and (sum(i) - count_2) in game:
                        comp_input = sum(i) - count_2
                        return comp_input
                if j in user:
                    c += 1
                    count += j
                    if c == 2 and (sum(i) - count) in game:
                        comp_input = sum(i) - count
            count = 0
            count_2 = 0
            v = 0
            c = 0
        return comp_input

    user = []
    comp = []
    game = [i for i in range(1, 10)]
    check_win = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    print("Крестики-нолики")
    start()
    print("Чтобы сделать ход, напишите номер клетки")
    my_game = True
    c = 0
    v = 0
    while my_game:
        comp_input_after = computer_protection_algorithm()     # компьютер выбирает ход
        comp.append(comp_input_after)                          # добавление хода в список ходов компьютера
        game.remove(comp_input_after)                          # удаление хода из списка возможных ходов
        if len(game) == 0:                                         # последний ход в игре
            game_round()                                           # отрисовка хода компьютера и игрока
            user_victory_check()                                   # проверка на победу игрока
            if my_game:                                            # если не победа игрока, то игра продолжается
                pass
            else:
                break                                             # если победа игрока, то выход из игры
            computer_victory_check()                              # проверка на победу компьютера
            if my_game:                                           # если не победа компьютера, то ничья и выход
                print("Ничья")
                break
            else:
                break                                             # если победа компьютера, то выход из игры
        game_round()                                          # отрисовка хода компьютера и игрока
        computer_victory_check()                              # проверка на победу компьютера
        user_victory_check()                                  # проверка на победу игрока
        if my_game:                                           # если кто-то победил, то выход из игры
            pass                                              # если никто не победил еще, то игра продолжается
        else:
            break
        user_input = input("Ваш ход: ")                       # ход игрока
        while int(user_input) in comp:
            print("Эта клетка занята")
            user_input = input("Ваш ход: ")
        user.append(int(user_input))                       # добавление хода в список ходов игрока
        game.remove(int(user_input))                       # удаление хода из списка возможных ходов
    input("Чтобы сыграть заново, нажмите Enter")
    tick_tack()


tick_tack()