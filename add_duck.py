# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 16:58:55 2014

@author: zoherghadyali, jaywoo, sophiali
"""

import pygame, random, math, time
from pygame.locals import *

class Wall(object):
    """Build walls out of the level map"""
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)
        
class Portal(object):
    """This is a portal"""
    def __init__(self,wall):
        if wall == 'null':
            pass
        else:
            box = wall
            self.rectp = box.inflate(10,10)
    
    def update(event_pos):
        print "updating portal"
        

def hold_levels():
    """Normal function that holds our levels as lists. Any other way is too hard"""
    level = [[
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                 W",
        "W         WWWWWW                  W",
        "W   WWWW       W                  W",
        "W   W        WWWW                 W",
        "W WWW  WWWW                       W",
        "W   W     W W                     W",
        "W   W     W   WWW                WW",
        "W   WWW WWW   W W                 W",
        "W     W   W   W W                 W",
        "WWW   W   WWWWW W                 W",
        "W W      WW                       W",
        "W W   WWWW   WWW                  W",
        "W     W    W   W                  W",
        "W                                 W",
        "W                                 W",
        "W                                 W",
        "W                                 W",
        "W                                 W",
        "W                                 W",
        "W               WWWWWWWWWWWWWWWWW W",
        "W                                 W",
        "W                                 W",
        "WW                                W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                              ]]
    print level
    return level

def change_to_list(num):
    """Changes level map into rectangles pygame can use to build world"""
    level = hold_levels()       
    for platform in level[num]:
        x = y = 0
        for row in level[num]:
            for col in row:
                if col == "W":
                    Wall((x, y))
#                    if col == "E":
#                        end_rect = pygame.Rect(x, y, 16, 16)
                x += 20
            y += 20
            x = 0
    return walls
    
        
class Portal_Platformer_Model:
    """ Encodes the game state """
    def __init__(self):
        self.level1 = change_to_list(0)
#        if click:
        self.portal_orange = 'null'
        self.portal_blue = 'null'
        self.duck = Duck((155,230,249),20,20,40,40)
    
    def update(self):
        self.duck.update()
#        
    def portal_update_orange(self,portalclick):
        self.portal_orange = Portal(portalclick)
        
    def portal_update_blue(self,portalclick):
        self.portal_blue = Portal(portalclick)
        
        
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
        for wall in walls:
            pygame.draw.rect(screen, pygame.Color(255, 255, 255), wall.rect)        
        if self.model.portal_orange != 'null':
            pygame.draw.rect(self.screen, pygame.Color(0,255,0),self.model.portal_orange.rectp)
        if self.model.portal_blue != 'null':
            pygame.draw.rect(self.screen, pygame.Color(0,0,255),self.model.portal_blue.rectp)  
        
        
        pygame.display.update()


class PyGameKeyboardController:
    """ Manipulate game state based on keyboard input """
    def __init__(self, model):
        self.model = model
    
    def handle_pygame_key(self, event):
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
            
    def handle_pygame_mouse(self, event):
        x, y = event.pos
        for wall in walls:
            if wall.rect.collidepoint(event.pos):
                portalclick = pygame.Rect.copy(wall.rect)
                print portalclick
                print "there's collision"
                if event.button == 1:
                    self.model.portal_update_orange(portalclick)
                if event.button == 3:
                    self.model.portal_update_blue(portalclick)
                return



if __name__ == '__main__':
    pygame.init()
    walls = []
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
                controller.handle_pygame_key(event)
            if event.type == MOUSEBUTTONDOWN:
                controller.handle_pygame_mouse(event)
        
        model.update()
        view.draw()
        time.sleep(0.001)

    pygame.quit()
