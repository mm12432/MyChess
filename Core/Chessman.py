# coding:utf8

from Point import Point


def num_between(max, min, current):
    return current >= min and current <= max


class Chessman(object):

    def __init__(self, name, is_red, chessboard):
        self.__name = name
        self.__is_red = is_red
        self.__chessboard = chessboard
        self.__position = Point(None, None)
        self.__moving_list = []
        self.__top = 9
        self.__bottom = 0
        self.__left = 0
        self.__right = 8

    @property
    def is_red(self):
        return self.__is_red

    @property
    def name(self):
        return self.__name

    def add_to_board(self, col_num, row_num):
        if self.border_check(col_num, row_num):
            self.__position.x = col_num
            self.__position.y = row_num
            self.__chessboard.add_chessman(self, col_num, row_num)
        else:
            print "the worng postion"

    def calc_moving_list(self):
        pass

    def border_check(self, col_num, row_num):
        return num_between(self.__top, self.__bottom, row_num) and num_between(self.__right, self.__left, col_num)


class Rook(Chessman):

    def __init__(self, name, is_red, chessboard):
        super(Rook, self).__init__(name, is_red, chessboard)
        self.__top = 9
        self.__bottom = 0
        self.__left = 0
        self.__right = 8

    def calc_moving_list(self):
        left = self.__chessboard.get_left_first_chessman(
            self.__position.x, self.__position.y)
        right = self.__chessboard.get_right_first_chessman(
            self.__position.x, self.__position.y)
        top = self.__chessboard.get_top_first_chessman(
            self.__position.x, self.__position.y)
        bottom = self.__chessboard.get_bottom_first_chessman(
            self.__position.x, self.__position.y)
        if left <> None:
            if left.is_red or (not self.is_red):
                for i in range(left.__position.x, self.__position.x, 1):
                    self.__moving_list.insert(Point(i, self.__position.y))
            else:
                for i in range(left.__position.x + 1, self.__position.x, 1):
                    self.__moving_list.insert(Point(i, self.__position.y))
        else:
            for i in range(0, self.__position.x, 1):
                self.__moving_list.insert(Point(i, self.__position.y))


class Knight(Chessman):

    def __init__(self, name, is_red, chessboard):
        super(Knight, self).__init__(name, is_red, chessboard)
        self.__top = 9
        self.__bottom = 0
        self.__left = 0
        self.__right = 8


class Cannon(Chessman):

    def __init__(self, name, is_red, chessboard):
        super(Cannon, self).__init__(name, is_red, chessboard)
        self.__top = 9
        self.__bottom = 0
        self.__left = 0
        self.__right = 8


class Mandarin(Chessman):

    def __init__(self, name, is_red, chessboard):
        super(Mandarin, self).__init__(name, is_red, chessboard)
        if self.is_red:
            self.__top = 2
            self.__bottom = 0
            self.__left = 3
            self.__right = 5
        else:
            self.__top = 9
            self.__bottom = 7
            self.__left = 3
            self.__right = 5


class Elephant(Chessman):

    def __init__(self, name, is_red, chessboard):
        super(Elephant, self).__init__(name, is_red, chessboard)
        if self.is_red:
            self.__top = 4
            self.__bottom = 0
            self.__left = 0
            self.__right = 8
        else:
            self.__top = 9
            self.__bottom = 5
            self.__left = 0
            self.__right = 8


class Pawn(Chessman):

    def __init__(self, name, is_red, chessboard):
        super(Pawn, self).__init__(name, is_red, chessboard)
        if self.is_red:
            self.__top = 9
            self.__bottom = 3
            self.__left = 0
            self.__right = 8
        else:
            self.__top = 6
            self.__bottom = 0
            self.__left = 0
            self.__right = 8


class King(Chessman):

    def __init__(self, name, is_red, chessboard):
        super(King, self).__init__(name, is_red, chessboard)
        if self.is_red:
            self.__top = 2
            self.__bottom = 0
            self.__left = 3
            self.__right = 5
        else:
            self.__top = 9
            self.__bottom = 7
            self.__left = 3
            self.__right = 5
