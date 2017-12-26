# coding:utf8

import Chessman


class Chessboard(object):

    def __init__(self, name):
        self.__name = name
        self.__is_red_turn = True
        self.__chessmans = [([None] * 10) for i in range(9)]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def chessmans(self):
        return self.__chessmans

    def init_board(self):
        red_rook_left = Chessman.Rook(" 车l红 ", True, self)
        red_rook_left.add_to_board(0, 0)
        red_rook_right = Chessman.Rook(" 车r红 ", True, self)
        red_rook_right.add_to_board(8, 0)
        green_rook_left = Chessman.Rook(" 车l绿 ", False, self)
        green_rook_left.add_to_board(0, 9)
        green_rook_right = Chessman.Rook(" 车r绿 ", False, self)
        green_rook_right.add_to_board(8, 9)
        red_knight_left = Chessman.Knight(" 马l红 ", True, self)
        red_knight_left.add_to_board(1, 0)
        red_knight_right = Chessman.Knight(" 马r红 ", True, self)
        red_knight_right.add_to_board(7, 0)
        green_knight_left = Chessman.Knight(" 马l绿 ", False, self)
        green_knight_left.add_to_board(1, 9)
        green_knight_right = Chessman.Knight(" 马r绿 ", False, self)
        green_knight_right.add_to_board(7, 9)
        red_cannon_left = Chessman.Cannon(" 炮l红 ", True, self)
        red_cannon_left.add_to_board(1, 2)
        red_cannon_right = Chessman.Cannon(" 炮r红 ", True, self)
        red_cannon_right.add_to_board(7, 2)
        green_cannon_left = Chessman.Cannon(" 炮l绿 ", False, self)
        green_cannon_left.add_to_board(1, 7)
        green_cannon_right = Chessman.Cannon(" 炮r绿 ", False, self)
        green_cannon_right.add_to_board(7, 7)
        red_elephant_left = Chessman.Elephant(" 相l红 ", True, self)
        red_elephant_left.add_to_board(2, 0)
        red_elephant_right = Chessman.Elephant(" 相r红 ", True, self)
        red_elephant_right.add_to_board(6, 0)
        green_elephant_left = Chessman.Elephant(" 象l绿 ", False, self)
        green_elephant_left.add_to_board(2, 9)
        green_elephant_right = Chessman.Elephant(" 象r绿 ", False, self)
        green_elephant_right.add_to_board(6, 9)
        red_mandarin_left = Chessman.Mandarin(" 仕l红 ", True, self)
        red_mandarin_left.add_to_board(3, 0)
        red_mandarin_right = Chessman.Mandarin(" 仕r红 ", True, self)
        red_mandarin_right.add_to_board(5, 0)
        green_mandarin_left = Chessman.Mandarin(" 仕l绿 ", False, self)
        green_mandarin_left.add_to_board(3, 9)
        green_mandarin_right = Chessman.Mandarin(" 仕r绿 ", False, self)
        green_mandarin_right.add_to_board(5, 9)
        red_king = Chessman.King(" 帅 红 ", True, self)
        red_king.add_to_board(4, 0)
        green_king = Chessman.King(" 将 绿 ", False, self)
        green_king.add_to_board(4, 9)
        red_pawn_1 = Chessman.Pawn(" 兵1红 ", True, self)
        red_pawn_1.add_to_board(0, 3)
        red_pawn_2 = Chessman.Pawn(" 兵2红 ", True, self)
        red_pawn_2.add_to_board(2, 3)
        red_pawn_3 = Chessman.Pawn(" 兵3红 ", True, self)
        red_pawn_3.add_to_board(4, 3)
        red_pawn_4 = Chessman.Pawn(" 兵4红 ", True, self)
        red_pawn_4.add_to_board(6, 3)
        red_pawn_5 = Chessman.Pawn(" 兵5红 ", True, self)
        red_pawn_5.add_to_board(8, 3)
        green_pawn_1 = Chessman.Pawn(" 卒1绿 ", False, self)
        green_pawn_1.add_to_board(0, 6)
        green_pawn_2 = Chessman.Pawn(" 卒2绿 ", False, self)
        green_pawn_2.add_to_board(2, 6)
        green_pawn_3 = Chessman.Pawn(" 卒3绿 ", False, self)
        green_pawn_3.add_to_board(4, 6)
        green_pawn_4 = Chessman.Pawn(" 卒4绿 ", False, self)
        green_pawn_4.add_to_board(6, 6)
        green_pawn_5 = Chessman.Pawn(" 卒5绿 ", False, self)
        green_pawn_5.add_to_board(8, 6)

    def add_chessman(self, chessman, col_num, row_num):
        self.chessmans[col_num][row_num] = chessman

    def remove_chessman(self, col_num, row_num):
        self.chessmans[col_num][row_num] = None

    def move_chessman(self, chessman, col_num, row_num):
        self.remove_chessman(chessman.col_num, chessman.row_num)
        self.add_chessman(chessman, col_num, row_num)

    def get_chessman(self, col_num, row_num):
        return self.__chessmans[col_num][row_num]

    def get_top_first_chessman(self, col_num, row_num):
        for i in range(row_num + 1, 10, 1):
            current = self.chessmans[col_num][i]
            if current <> None:
                return current

    def get_bottom_first_chessman(self, col_num, row_num):
        for i in range(row_num - 1, -1, -1):
            current = self.chessmans[col_num][i]
            if current <> None:
                return current

    def get_left_first_chessman(self, col_num, row_num):
        for i in range(col_num - 1, -1, -1):
            current = self.chessmans[i][row_num]
            if current <> None:
                return current

    def get_right_first_chessman(self, col_num, row_num):
        for i in range(col_num + 1, 9, 1):
            current = self.chessmans[i][row_num]
            if current <> None:
                return current

    def get_top_second_chessman(self, col_num, row_num):
        count = 0
        for i in range(row_num + 1, 10, 1):
            current = self.chessmans[col_num][i]
            if current <> None:
                if count == 1:
                    return current
                else:
                    count += 1

    def get_bottom_second_chessman(self, col_num, row_num):
        count = 0
        for i in range(row_num - 1, -1, -1):
            current = self.chessmans[col_num][i]
            if current <> None:
                if count == 1:
                    return current
                else:
                    count += 1

    def get_left_second_chessman(self, col_num, row_num):
        count = 0
        for i in range(col_num - 1, -1, -1):
            current = self.chessmans[i][row_num]
            if current <> None:
                if count == 1:
                    return current
                else:
                    count += 1

    def get_right_second_chessman(self, col_num, row_num):
        count = 0
        for i in range(col_num + 1, 9, 1):
            current = self.chessmans[i][row_num]
            if current <> None:
                if count == 1:
                    return current
                else:
                    count += 1

    def print_to_cl(self):
        screen = "\r\n"
        for i in range(9, -1, -1):
            for j in range(9):
                if self.__chessmans[j][i] <> None:
                    screen += self.__chessmans[j][i].name
                else:
                    screen += "   .   "
            screen += "\r\n" * 3
        print screen.decode("utf-8")
