import pygame as pg
import os
pg.font.init()

#Screen settings 
WIN_HEIGHT, WIN_WIDTH = 900,900
WIN = pg.display.set_mode((WIN_HEIGHT, WIN_WIDTH))
pg.display.set_caption("Space Invaders")
MAIN_SHIP_WIDTH,MAIN_SHIP_HEIGHT = 50,50
FOOD_WIDTH,FOOD_HEIGHT = 40,40
FINISHED_FONT = pg.font.SysFont("comicsans", 40)
POINTS_FONT = pg.font.SysFont("comicsans", 40)

#Other

HIDERANCE_CREATE = pg.USEREVENT + 1
FPS = 60
clock = pg.time.Clock()

#colors
DARK_BLUE = (5,1,50)
WHITE = (255,255,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)
GREEN = (216, 230, 173)
GREY = (128, 128, 128)