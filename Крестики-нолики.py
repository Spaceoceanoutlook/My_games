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
        c = 0
        s = 0
        if_not_game_for_player = []
        if_not_game_for_comp = []
        for i in self.win_tuple:
            for j in i:
                if j in self.comp_cage:
                    s += 1
                else:
                    if_not_game_for_comp.append(j)
            if s == 2 and if_not_game_for_comp[0] not in self.player_cage:
                comp_turn = if_not_game_for_comp[0]
                self.comp_cage.append(comp_turn)
                if_not_game_for_comp.clear()
                return
            s = 0
            if_not_game_for_player.clear()
            if_not_game_for_comp.clear()
        for i in self.win_tuple:
            for j in i:
                if j in self.player_cage:
                    c += 1
                else:
                    if_not_game_for_player.append(j)
            if c == 2 and if_not_game_for_player[0] not in self.comp_cage:
                comp_turn = if_not_game_for_player[0]
                self.comp_cage.append(comp_turn)
                if_not_game_for_player.clear()
                return
            c = 0
            if_not_game_for_player.clear()
            if_not_game_for_comp.clear()
        comp_list = [i for i in range(1, 9) if i not in self.player_cage and i not in self.comp_cage]
        if len(comp_list) > 0:
            comp_turn = choice(comp_list)
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

    def win(self):
        for i in self.win_tuple:
            if set(i) <= set(self.player_cage):
                print('ПОБЕДА ИГРОКА')
                return False
            elif set(i) <= set(self.comp_cage):
                print('ПОБЕДА КОМПА')
                return False
            elif len(self.player_cage) + len(self.comp_cage) == 9:
                print('НИЧЬЯ')
                return False
        return True


m = Matrix()
m.create_matrix()
while True:
    player_num = int(input('ТВОЙ ХОД: '))
    m.game_round(player_num)
    if not m.win():
        break
