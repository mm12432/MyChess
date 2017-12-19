# coding:utf8

from Point import Point


class Chessman(object):

    def __init__(self, name, is_red, chessboard):
        self.__name = name
        self.__is_red = is_red
        self.__chessboard = chessboard
        self.__position = Point(None, None)

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

class Rook(Chessman):
    pass

class Knight(Chessman):
    pass

class Cannon(Chessman):
    pass

class Mandarin(Chessman):
    pass

class Elephant(Chessman):
    pass

class Pawn(Chessman):
    pass

class King(Chessman):
    pass