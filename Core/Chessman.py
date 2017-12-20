# coding:utf8

from Point import Point


class Chessman(object):

    def __init__(self, name, is_red, chessboard):
        self.__name = name
        self.__is_red = is_red
        self.__chessboard = chessboard
        self.__position = Point(None, None)
        self.__moving_list = []

    @property
    def is_red(self):
        return self.__is_red

    @property
    def name(self):
        return self.__name

    def add_to_board(self, col_num, row_num):
        self.__position.x = col_num
        self.__position.y = row_num
        self.__chessboard.add_chessman(self, col_num, row_num)

    def calc_moving_list(self):
        pass


class Rook(Chessman):

    def __init__(self, name, is_red, chessboard):
        super(Rook, self).__init__(name, is_red, chessboard)
        self.__top = 9
        self.__bottom = 0
        self.__left = 0
        self.__right = 8

    def calc_moving_list(self):
        pass

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
