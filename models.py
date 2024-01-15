import pygame as pg
from settings import *
import random as rd 
import sys



class RectangelObject:
    def __init__(self, x,y,width,height, color="gray"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 

        self.collided_rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.color = color
    def draw(self):
        rect = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(WIN, self.color, rect)
        self.collided_rect = pg.Rect(rect.x, rect.y, rect.width, rect.height)
    def collided_with(self, other_obj):
        return self.collided_rect.colliderect(other_obj.collided_rect)
    def collided_within(self, other_obj, margin=300):
        # Check if self is to the left of the other object with margin
        if (self.x + self.width + margin) < other_obj.x:
            return False
        if self.x > (other_obj.x + other_obj.width + margin):
            return False

        if (self.y + self.height + margin) < other_obj.y:
            return False

        if self.y > (other_obj.y + other_obj.height + margin):
            return False

        return True

        #return self.collided_rect.colliderect(other_obj.collided_rect)



class Troll(RectangelObject):
    def __init__(self, x,y,width, height, speed, color="green"):
        super().__init__(x,y,width, height, color)
        self.vx = 0
        self.vy = 0
        self.speed = speed
    def update(self, new_speed):
        self.speed = new_speed
        self.x += self.vx
        self.y += self.vy 
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]> 0:
            self.vx = 0
            self.vy = -self.speed
        if keys[pg.K_s]:
            self.vx = 0
            self.vy = self.speed
        if keys[pg.K_d]:
            self.vy = 0
            self.vx = self.speed
        if keys[pg.K_a]:
            self.vy = 0
            self.vx = -self.speed
    def within_screen(self):
        if self.x + self.width + self.speed > WIN_WIDTH + MAIN_SHIP_WIDTH*1.5:
            return False
        if self.y + self.speed < -MAIN_SHIP_HEIGHT:
            return False
        if self.y + self.height + self.speed > WIN_HEIGHT + MAIN_SHIP_HEIGHT*1.5:
            return False
        if self.x + self.speed < -MAIN_SHIP_WIDTH*1.5:
            return False
        return True


class FoodBite(RectangelObject):
    def __init__(self, x,y,width,height, color="yellow"):
        super().__init__(x,y,width,height, color)



class Hinderance(FoodBite):
    COOLDOWN_TIME = 5
    def __init__(self, x,y,width,height, color="grey"):
        self.time = 0
        self.ready = False
        super().__init__(x,y,width,height, color)
    def cooldown_time(self, ):
        self.time += 0.05
        if self.time > self.COOLDOWN_TIME:
            self.ready = True
        #print(f'{self.time} > {self.COOLDOWN_TIME}')
        #print(f'Ready = {self.ready}')

        


        