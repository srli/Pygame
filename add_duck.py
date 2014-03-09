# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 16:58:55 2014

@author: zoherghadyali, jaywoo, sophiali
"""

import pygame, random, math, time
from pygame.locals import *

#class Wall(object):
#    def __init__(self, pos):
#        walls.append(self)
#        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
#
#def hold_levels():
#    """Normal function that holds our levels as lists. Any other way is too hard"""
#    level = [[
#        "WWWWWWWWWWWWWWWWWWWW",
#        "W                  W",
#        "W         WWWWWW   W",
#        "W   WWWW       W   W",
#        "W   W        WWWW  W",
#        "W WWW  WWWW        W",
#        "W   W     W W      W",
#        "W   W     W   WWW WW",
#        "W   WWW WWW   W W  W",
#        "W     W   W   W W  W",
#        "WWW   W   WWWWW W  W",
#        "W W      WW        W",
#        "W W   WWWW   WWW   W",
#        "W     W    W   W   W",
#        "WWWWWWWWWWWWWWWWWWWW",
#                              ]]
#    print level
#    return level
#
#def change_to_list(num):
#    level = hold_levels()  
#    walls = []      
#    for platform in level[num]:
#        x = y = 0
#        for row in level[num]:
#            for col in row:
#                if col == "W":
#                    Wall((x, y))
##                    if col == "E":
##                        end_rect = pygame.Rect(x, y, 16, 16)
#                x += 16
#            y += 16
#            x = 0
#    return walls
#    
#        
class Portal_Platformer_Model:
    """ Encodes the game state """
    """TO-DO: Clean up these level lists"""
    def __init__(self):
#        self.level1 = change_to_list(0)
#        print type(self.level1)
#        self.level = [[
#        "WWWWWWWWWWWWWWWWWWWW",
#        "W                  W",
#        "W         WWWWWW   W",
#        "W   WWWW       W   W",
#        "W   W        WWWW  W",
#        "W WWW  WWWW        W",
#        "W   W     W W      W",
#        "W   W     W   WWW WW",
#        "W   WWW WWW   W W  W",
#        "W     W   W   W W  W",
#        "WWW   W   WWWWW W  W",
#        "W W      WW        W",
#        "W W   WWWW   WWW   W",
#        "W     W    W   W   W",
#        "WWWWWWWWWWWWWWWWWWWW",
#                               ]]
#        
        self.level1 = []
        platform1 = Platform((255,255,255), 20, 700, 0,480)
        platform2 = Platform((255,255,255), 20, 700, 0,0)
        platform3 = Platform((255,255,255), 100,20, 250,380)
        platform4 = Platform((255,255,255), 100,20, 450,380)
        platform5 = Platform((255,255,255), 20, 220, 250,360)

        self.level1.append(platform1)
        self.level1.append(platform2)
        self.level1.append(platform3)
        self.level1.append(platform4)
        self.level1.append(platform5)
        
        self.level2 = []
        platform1 = Platform((255,255, 255),20,150,0,485)
        platform2 = Platform((255,255, 255),75,20,150,425)
        platform3 = Platform((255,255, 255),20,150,100,0)
        platform4 = Platform((255,255, 255),20,175,170,250)
        platform5 = Platform((255,255, 255),75,20,150+175,195)
        platform6 = Platform((255,255, 255),20,175,325,0)
        platform7 = Platform((255,255,255), 20, 375, 325, 185)

        self.level2.append(platform1)        
        self.level2.append(platform2)
        self.level2.append(platform3)
        self.level2.append(platform4)
        self.level2.append(platform5)
        self.level2.append(platform6)
        self.level2.append(platform7)
        
        self.duck = Duck((155,230,249),20,20,16,16)
    
    def update(self):
        self.duck.update()

class Duck:
    """Code for our moving duck"""
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.vy = 0.0
        self.vx = 0.0
        self.friction = 0.1
        self.gravity = 0.1
        
    def update(self):
        self.x += self.vx + self.friction
        self.y += self.vy + self.gravity
        

        
class Platform:
    """ Encodes the state of a singular rectangular platform in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

class PyGameWindowView:
    """ Draws our game in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
                   
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.rect(self.screen, pygame.Color(self.model.duck.color[0], self.model.duck.color[1], self.model.duck.color[2]), pygame.Rect(self.model.duck.x, self.model.duck.y, self.model.duck.width, self.model.duck.height))
        pygame.draw.rect(self.screen, pygame.Color(self.model.platform.color[0],self.model.platform.color[1],self.model.platform.color[2]),pygame.Rect(self.model.platform.x,self.model.platform.y,self.model.platform.width,self.model.platform.height))
#        for wall in self.model.level1:
#            pygame.draw.rect(screen, pygame.Color(255, 255, 255), wall.rect)          
        pygame.display.update()


class PyGameKeyboardController:
    """ Manipulate game state based on keyboard input """
    def __init__(self, model):
        self.model = model
    
    def handle_pygame_event(self, event):
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            self.model.duck.vx += -0.5
        if event.key == pygame.K_RIGHT:
            self.model.duck.vx += 0.5
        if event.key == pygame.K_UP:
            self.model.duck.vy += -0.5
        if event.key == pygame.K_DOWN:
            self.model.duck.vy += 0.5


if __name__ == '__main__':
    pygame.init()

    size = (700, 500)
    screen = pygame.display.set_mode(size)
    model = Portal_Platformer_Model()
    view = PyGameWindowView(model,screen)
    controller = PyGameKeyboardController(model)

    running = True

    while running:
           
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                controller.handle_pygame_event(event)
        
        model.update()
        view.draw()
        time.sleep(0.001)

    pygame.quit()
