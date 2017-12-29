# coding:utf-8
import Chessboard
import Point
import Chessman


def print_chessman_name(chessman):
    if chessman:
        print chessman.name
    else:
        print "None"


def main():
    cbd = Chessboard.Chessboard('123')
    cbd.init_board()
    cbd.print_to_cl()
    # cbd.remove_chessman_source(0,0)
    # cbd.print_to_cl()
    while not cbd.is_end():
        cbd.calc_chessmans_moving_list()
        if cbd.is_red_turn:
            print "is_red_turn"
        else:
            print "is_green_turn"
        is_correct_chessman = False
        is_correct_position = False
        chessman = None
        while not is_correct_chessman:
            title = "请输入棋子名字: ".decode("utf-8").encode("gbk")
            input_chessman_name = input(title)
            chessman = cbd.get_chessman_by_name(input_chessman_name)
            if chessman <> None and chessman.is_red == cbd.is_red_turn:
                is_correct_chessman = True
                print "当前可以落子的位置有：".decode("utf-8").encode("gbk")
                for point in chessman.moving_list:
                    print point.x, point.y
            else:
                print "没有找到此名字的棋子或未轮到此方走子".decode("utf-8").encode("gbk")
        while not is_correct_position:
            title = "请输入落子的位置: ".decode("utf-8").encode("gbk")
            input_chessman_position = input(title)
            is_correct_position = chessman.move(
                input_chessman_position[0], input_chessman_position[1])
            if is_correct_position:
                cbd.print_to_cl()
                cbd.clear_chessmans_moving_list()
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
    # total = 0
    # for i in range(0, 9):
    #     for j in range(0, 10):
    #         chessman = cbd.chessmans[i][j]
    #         if chessman <> None and chessman.is_red:
    #             print_chessman_name(chessman)
    #             chessman.calc_moving_list()
    #             for point in chessman.moving_list:
    #                 total += 1
    #                 print point.x, point.y
    # print 'total is ' + str(total)


if __name__ == '__main__':
    main()
