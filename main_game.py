import pygame as pg
import sys
from settings import *
from models import *
import pandas as pd

"""
"""

def store_highscore(score, top_score):
    data_sett = [[score]]
    data_sett = pd.DataFrame(data = data_sett, columns = ["Topscores"])
    data_sett.to_csv("highscore", sep="\t", index=False)
def get_highscore():
    df = pd.read_csv("highscore", sep="\t")
    highscore = df.iloc[0,0]
    return highscore

def create_objects(food_bites:list, hinderances:list):
    ...

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
            no_collision = False
            collision_items = food_bites + hinderances
            count = 0
            while not no_collision:
                x,y = rd.randint(0, WIN_WIDTH-MAIN_SHIP_WIDTH), rd.randint(0, WIN_HEIGHT-MAIN_SHIP_HEIGHT)
                no_collision = True
                new_food = FoodBite(x,y,FOOD_WIDTH, FOOD_HEIGHT)
                for i in range(len(collision_items)):
                    if new_food.collided_with(collision_items[i]):
                        no_collision = False
            food_bites.append(new_food)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        win.fill("black")
        points_label = POINTS_FONT.render(f"Points: {points}", 1, "white")
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



