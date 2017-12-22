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
    chessman = cbd.get_chessman(1,2)
    print_chessman_name(chessman)     
    chessman = cbd.get_left_first_chessman(1,2)
    print_chessman_name(chessman)
    chessman = cbd.get_right_first_chessman(1,2)
    print_chessman_name(chessman)
    chessman = cbd.get_top_first_chessman(1,2)
    print_chessman_name(chessman)
    chessman = cbd.get_bottom_first_chessman(1,2)
    print_chessman_name(chessman)
    chessman = cbd.get_chessman(4,3)
    print_chessman_name(chessman)   
    chessman = cbd.get_left_second_chessman(4,3)
    print_chessman_name(chessman)
    chessman = cbd.get_right_second_chessman(4,3)
    print_chessman_name(chessman)
    chessman = cbd.get_top_second_chessman(4,3)
    print_chessman_name(chessman)
    chessman = cbd.get_bottom_second_chessman(4,6)
    print_chessman_name(chessman)
if __name__ == '__main__':
    main()
