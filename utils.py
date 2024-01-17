import pygame as pg
import random as rd
from settings import *
from models import *
import pandas as pd
def store_highscore(score, top_score):
    data_sett = [[score]]
    data_sett = pd.DataFrame(data = data_sett, columns = ["Topscores"])
    data_sett.to_csv("highscore", sep="\t", index=False)
def get_highscore():
    df = pd.read_csv("highscore", sep="\t")
    highscore = df.iloc[0,0]
    return highscore

def create_objects(food_bites, *argv):
    no_collision = False
    count = 0
    while not no_collision:
        x,y = rd.randint(0, WIN_WIDTH-MAIN_SHIP_WIDTH), rd.randint(0, WIN_HEIGHT-MAIN_SHIP_HEIGHT)
        no_collision = True
        new_food = FoodBite(x,y,FOOD_WIDTH, FOOD_HEIGHT)
        for arg in argv:
            if new_food.collided_with(arg):
                no_collision = False 
    food_bites.append(new_food)