# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 16:58:55 2014

@author: zoherghadyali
"""

import pygame
from pygame.locals import *
import random
import math
import time

class Portal_Platformer_Model:
    """ Encodes the game state """
    def __init__(self):
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

class Platform:
    """ Encodes the state of a singular rectangular platform in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

class PyGameWindowView:
    """ A view of brick breaker rendered in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
        
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        for platform in self.model.level1:
            pygame.draw.rect(self.screen, pygame.Color(platform.color[0],platform.color[1],platform.color[2]),pygame.Rect(platform.x,platform.y,platform.width,platform.height))
        pygame.display.update()

if __name__ == '__main__':
    pygame.init()

    size = (700, 500)
    screen = pygame.display.set_mode(size)

    model = Portal_Platformer_Model()
    view = PyGameWindowView(model,screen)
#    controller = PyGameKeyboardController(model)
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
#            if event.type == KEYDOWN:
#                controller.handle_keyboard_event(event)
#        model.update()
        view.draw()
        time.sleep(.001)

    pygame.quit()