import pygame as pg
import sys
from settings import *
from models import *

"""



"""


def main(win):
    speed = 3
    points = 0
    game_finished = False
    print(speed)
    start_time = pg.time.get_ticks()
    main_troll = Troll(WIN_WIDTH//2-MAIN_SHIP_WIDTH, WIN_HEIGHT//2-MAIN_SHIP_HEIGHT, MAIN_SHIP_WIDTH, MAIN_SHIP_HEIGHT, speed)
    food_bites = []
    hinderances = []
    run = True
    while run:
        while len(food_bites) < 3:
            x,y = rd.randint(0, WIN_WIDTH-MAIN_SHIP_WIDTH), rd.randint(0, WIN_HEIGHT-MAIN_SHIP_HEIGHT)
            for bite in food_bites:
                for hinderance in hinderances:
                    if bite.collided_with(hinderance):
                        x,y = rd.randint(0, WIN_WIDTH-MAIN_SHIP_WIDTH), rd.randint(0, WIN_HEIGHT-MAIN_SHIP_HEIGHT)
            for i in range(len(food_bites)):
                for j in range(i, len(food_bites)):
                    if food_bites[i].collided_with(food_bites[j]):
                        x,y = rd.randint(0, WIN_WIDTH-MAIN_SHIP_WIDTH), rd.randint(0, WIN_HEIGHT-MAIN_SHIP_HEIGHT)
            for i in range(len(hinderances)):
                for j in range(i, len(hinderances)):
                    if hinderances[i].collided_with(hinderances[j]):
                        x,y = rd.randint(0, WIN_WIDTH-MAIN_SHIP_WIDTH), rd.randint(0, WIN_HEIGHT-MAIN_SHIP_HEIGHT)
            
            food_bites.append(FoodBite(x,y,FOOD_WIDTH, FOOD_HEIGHT))

        
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            #if event.type == HIDERANCE_CREATE:
            
        
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
                print(bite.x, bite.y)
                hinderances.append(Hinderance(bite.x, bite.y, FOOD_WIDTH, FOOD_HEIGHT))
                print("appendedd")
        for hinderance in hinderances:
                hinderance.draw()
                hinderance.cooldown_time()
                if main_troll.collided_with(hinderance) and hinderance.ready:
                    game_finished = True
                    sys.exit()
        pg.display.update()


if __name__ == "__main__":
    main(WIN)




