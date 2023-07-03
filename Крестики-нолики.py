from random import choice


class Matrix:
    player_cage = []
    comp_cage = []

    @staticmethod
    def create_matrix():
        c = 1
        for i in range(3):
            for j in range(3):
                print(f'[ {c} ]', end="")
                c += 1
            print()

    def game_round(self, num):
        self.player_cage.append(num)
        comp_move_options = [i for i in range(1, 10) if i not in self.player_cage and i not in self.comp_cage]
        comp_turn = choice(comp_move_options)
        self.comp_cage.append(comp_turn)
        print('МОЙ ХОДЫ', self.player_cage)
        print("ВЫБОР У КОМПА ДЛЯ ХОДА", comp_move_options)
        print('ХОД КОМПА', comp_turn)
        print('УЖЕ СХОДИЛ КАКИМИ КОМП', self.comp_cage)
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
        win_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        for i in win_tuple:
            if set(i) <= set(self.player_cage):
                print('ПОБЕДА ИГРОКА')
                return False
            else:
                if set(i) <= set(self.comp_cage):
                    print('ПОБЕДА КОМПА')
                    return False
        return True


m = Matrix()
m.create_matrix()
while True:
    if not m.win():
        break
    player_num = int(input('Ходи: '))
    m.game_round(player_num)




