# coding:utf8

import Chessboard
import Point
import Chessman


def print_chessman_name(chessman):
    if chessman:
        print chessman.name.decode("utf-8")
    else:
        print "None"


def main():
    cbd = Chessboard.Chessboard('123')
    cbd.init_board()
    cbd.print_to_cl()
    # chessman = cbd.get_chessman(1,2)
    # print_chessman_name(chessman)
    # chessman = cbd.get_left_first_chessman(1,2)
    # print_chessman_name(chessman)
    # chessman = cbd.get_right_first_chessman(1,2)
    # print_chessman_name(chessman)
    # chessman = cbd.get_top_first_chessman(1,2)
    # print_chessman_name(chessman)
    # chessman = cbd.get_bottom_first_chessman(1,2)
    # print_chessman_name(chessman)
    # chessman = cbd.get_chessman(4,3)
    # print_chessman_name(chessman)
    # chessman = cbd.get_left_second_chessman(4,3)
    # print_chessman_name(chessman)
    # chessman = cbd.get_right_second_chessman(4,3)
    # print_chessman_name(chessman)
    # chessman = cbd.get_top_second_chessman(4,3)
    # print_chessman_name(chessman)
    # chessman = cbd.get_bottom_second_chessman(4,6)
    # print_chessman_name(chessman)

    # chessman = cbd.get_chessman(1,7)
    # print_chessman_name(chessman)
    # chessman.calc_moving_list()
    # for point in chessman.moving_list:
    #     print point.x,point.y
    total = 0
    for i in range(0, 9):
        for j in range(0, 10):
            chessman = cbd.chessmans[i][j]
            if chessman <> None and chessman.is_red:
                print_chessman_name(chessman)
                chessman.calc_moving_list()
                for point in chessman.moving_list:
                    total += 1
                    print point.x, point.y
    print 'total is ' + str(total)


if __name__ == '__main__':
    main()
