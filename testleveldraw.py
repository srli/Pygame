# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 13:49:29 2014

@author: sophie
"""

import pygame, random, math, time
from pygame.locals import *

class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        
class Portal_Platformer_Model:
    """ Encodes the game state """
    """TO-DO: Clean up these level lists"""
    def __init__(self):
        self.level = [[
        "WWWWWWWWWWWWWWWWWWWW",
        "W                  W",
        "W         WWWWWW   W",
        "W   WWWW       W   W",
        "W   W        WWWW  W",
        "W WWW  WWWW        W",
        "W   W     W W      W",
        "W   W     W   WWW WW",
        "W   WWW WWW   W W  W",
        "W     W   W   W W  W",
        "WWW   W   WWWWW W  W",
        "W W      WW        W",
        "W W   WWWW   WWW   W",
        "W     W    W   W   W",
        "WWWWWWWWWWWWWWWWWWWW",
                               ]]
class PyGameWindowView:
    """ Our game in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
                   
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        walls = []
        for platform in self.model.level[0]:
            x = y = 0
            for row in self.model.level[0]:
                for col in row:
                    if col == "W":
                        Wall((x, y))
#                    if col == "E":
#                        end_rect = pygame.Rect(x, y, 16, 16)
                    x += 16
                y += 16
                x = 0
        print walls
        for wall in walls:
            pygame.draw.rect(screen, pygame.Color(255, 255, 255), wall.rect)
        
        
if __name__ == '__main__':
    pygame.init()

    size = (320, 240)
    screen = pygame.display.set_mode(size)
#    walls = []
    model = Portal_Platformer_Model()
    view = PyGameWindowView(model,screen)
   
    running = True

    while running:
           
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        view.draw()
        time.sleep(0.001)

    pygame.quit()
