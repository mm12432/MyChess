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


def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'Img', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' %
                         (file, pygame.get_error()))
    return surface.convert()


def main(winstyle=0):
    SCREENRECT = Rect(0, 0, 720, 800)
    pygame.init()
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    pygame.display.set_caption("中国象棋最强AI")

    # create the background, tile the bgd image
    bgdtile = load_image('boardchess.jpg')
    background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pygame.display.update()
if __name__ == '__main__':
    main()
