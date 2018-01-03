# coding:utf-8
import sys
import pygame
import random
import os.path
from Core import Chessboard
from Core import Point
from Core import Chessman
from pygame.locals import *

main_dir = os.path.split(os.path.abspath(__file__))[0]
SCREENRECT = Rect(0, 0, 720, 800)


def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'Img', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' %
                         (file, pygame.get_error()))
    return surface.convert()


def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs


class Chessman_Sprite(pygame.sprite.Sprite):
    is_selected = False
    images = []
    is_transparent = False

    def __init__(self, images, chessman):
        pygame.sprite.Sprite.__init__(self)
        self.chessman = chessman
        self.images = images
        self.image = self.images[0]
        self.rect = Rect(chessman.col_num * 80,
                         (9 - chessman.row_num) * 80,  80,  80)

    def move(self, col_num, row_num):
        is_correct_position = self.chessman.move(col_num, row_num)
        if is_correct_position:
            self.rect.move_ip((col_num - self.chessman.col_num)
                              * 80, (self.chessman.col_num - col_num) * 80)
            self.rect = self.rect.clamp(SCREENRECT)
            self.chessman.chessboard.clear_chessmans_moving_list()
            self.chessman.chessboard.calc_chessmans_moving_list()

    def update(self):
        if self.is_selected:
            if self.is_transparent:
                self.image = self.images[1]
            else:
                self.image = self.images[0]
            self.is_transparent = not self.is_transparent


def main(winstyle=0):

    pygame.init()
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    pygame.display.set_caption("中国象棋最强AI")

    # create the background, tile the bgd image
    bgdtile = load_image('boardchess.gif')
    background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    cbd = Chessboard.Chessboard('000')
    cbd.init_board()
    #chessman_sprites_hash = {}

    chessmans = pygame.sprite.Group()
    framerate = pygame.time.Clock()

    for chessman in cbd.chessmans_hash.values():
        if chessman.is_red:
            if isinstance(chessman, Chessman.Rook):
                images = load_images("red_rook.gif", "transparent.gif")
            elif isinstance(chessman, Chessman.Cannon):
                images = load_images("red_cannon.gif", "transparent.gif")
            elif isinstance(chessman, Chessman.Knight):
                images = load_images("red_knight.gif", "transparent.gif")
            elif isinstance(chessman, Chessman.King):
                images = load_images("red_king.gif", "transparent.gif")
            elif isinstance(chessman, Chessman.Elephant):
                images = load_images("red_elephant.gif", "transparent.gif")
            elif isinstance(chessman, Chessman.Mandarin):
                images = load_images("red_mandarin.gif", "transparent.gif")
            else:
                images = load_images("red_pawn.gif", "transparent.gif")
        else:
            if isinstance(chessman, Chessman.Rook):
                images = load_images("black_rook.gif", "transparent.gif")
            elif isinstance(chessman, Chessman.Cannon):
                images = load_images("black_cannon.gif", "transparent.gif")
            elif isinstance(chessman, Chessman.Knight):
                images = load_images("black_knight.gif", "transparent.gif")
            elif isinstance(chessman, Chessman.King):
                images = load_images("black_king.gif", "transparent.gif")
            elif isinstance(chessman, Chessman.Elephant):
                images = load_images("black_elephant.gif", "transparent.gif")
            elif isinstance(chessman, Chessman.Mandarin):
                images = load_images("black_mandarin.gif", "transparent.gif")
            else:
                images = load_images("black_pawn.gif", "transparent.gif")
        chessman_sprite = Chessman_Sprite(images, chessman)
        chessmans.add(chessman_sprite)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        framerate.tick(5)
        # clear/erase the last drawn sprites
        chessmans.clear(screen, background)

        # update all the sprites
        chessmans.update()
        chessmans.draw(screen)
        pygame.display.update()
        
if __name__ == '__main__':
    main()
