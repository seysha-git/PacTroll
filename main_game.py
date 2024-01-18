import pygame as pg
import sys
from settings import *
from models import *
import pandas as pd
from utils import *

"""
"""


print("newest version")

def main(win):
    speed = 5
    points = 0
    top_score = get_highscore()
    game_finished = False
    print(speed)
    start_time = pg.time.get_ticks()
    main_troll = Troll(WIN_WIDTH//2-MAIN_SHIP_WIDTH, WIN_HEIGHT//2-MAIN_SHIP_HEIGHT, MAIN_SHIP_WIDTH, MAIN_SHIP_HEIGHT, speed)
    food_bites = []
    hinderances = []
    run = True
    while run:
        clock.tick(FPS)
        while len(food_bites) < 3:
            combined = food_bites+hinderances
            create_objects(food_bites, *combined)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        win.fill("black")
        points_label = POINTS_FONT.render(f"FoodPoints: {points}", 1, "white")
        win.blit(points_label, (30, 100))
        if main_troll.within_screen():
            main_troll.draw()
            main_troll.move()
            main_troll.update(speed)
        else:
            game_finished = True
            sys.exit()
        for bite in food_bites:
            bite.draw()
            if bite.collided_with(main_troll):
                points += 1
                food_bites.remove(bite)
                speed += 0.3
                hinderances.append(Hinderance(bite.x, bite.y, FOOD_WIDTH, FOOD_HEIGHT))
        for hinderance in hinderances:
                hinderance.draw()
                hinderance.cooldown_time()
                if main_troll.collided_with(hinderance) and hinderance.ready:
                    game_finished = True
                    sys.exit()
        pg.display.update()
        if points > top_score:
            store_highscore(points, top_score)


if __name__ == "__main__":
    main(WIN)



