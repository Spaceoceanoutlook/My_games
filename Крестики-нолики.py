from random import choice


class Matrix:
    player_cage = []
    comp_cage = []
    win_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))

    @staticmethod
    def create_matrix():
        c = 1
        for i in range(3):
            for j in range(3):
                print(f'[ {c} ]', end="")
                c += 1
            print()

    def brain(self):
        comp_list = [i for i in range(1, 9) if i not in self.player_cage and i not in self.comp_cage]
        if len(comp_list) > 0:
            comp_turn = choice(comp_list)
        else:
            return
        count_comp = sum_comp = count_user = sum_user = 0
        for i in self.win_tuple:
            for j in i:
                if j in self.comp_cage:
                    count_comp += 1
                    sum_comp += j
                    if count_comp == 2 and (sum(i) - sum_comp) not in self.player_cage:
                        comp_turn = sum(i) - sum_comp
                        self.comp_cage.append(comp_turn)
                        return
                if j in self.player_cage:
                    count_user += 1
                    sum_user += j
                    if count_user == 2 and (sum(i) - sum_user) not in self.comp_cage:
                        comp_turn = sum(i) - sum_user
            count_comp = sum_comp = count_user = sum_user = 0
        self.comp_cage.append(comp_turn)
        return

    def game_round(self, num):
        self.player_cage.append(num)
        self.brain()
        c = 1
        for i in range(3):
            for j in range(3):
                if c in self.player_cage:
                    print('[ X ]', end="")
                elif c in self.comp_cage:
                    print('[ O ]', end="")
                else:
                    print('[   ]', end="")
                c += 1
            print()

    def win_player(self):
        for i in self.win_tuple:
            if set(i) <= set(self.player_cage):
                print('ПОБЕДА ИГРОКА')
                return False
        return True

    def win_comp(self):
        for i in self.win_tuple:
            if set(i) <= set(self.comp_cage):
                print('ПОБЕДА КОМПА')
                return False
        return True

    def standoff(self):
        if len(self.player_cage) + len(self.comp_cage) == 9:
            print('НИЧЬЯ')
            return False
        return True


m = Matrix()
m.create_matrix()
while True:
    while True:
        player_num = input('ТВОЙ ХОД: ')
        try:
            player_num = int(player_num)
            if player_num not in [i for i in range(1, 10)]:
                print('ЦИФРА ХОДА ДОЛЖНА БЫТЬ ОТ 1 ДО 9')
                continue
            if player_num in m.player_cage or player_num in m.comp_cage:
                print('ЭТА КЛЕТКА ЗАНЯТА')
                continue
            break
        except ValueError:
            print('ХОД ДОЛЖЕН БЫТЬ ЦИФРОЙ')
    m.game_round(player_num)
    if not m.win_player() or not m.win_comp() or not m.standoff():
        break
