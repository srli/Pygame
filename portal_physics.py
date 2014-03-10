# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 16:58:55 2014

@author: zoherghadyali
"""

import pygame, random, math, time
from pygame.locals import *
from world import *

class Portal_Platformer_Model:
    """ Encodes the game state """
    def __init__(self):
        self.player = Duck(20,20)
        self.level = 1
        self.walls = Walls(self.level)
        
    def moveX(self, dx):
        self.player.rect.x += dx
        
        for wall in self.walls.walls:
            if self.player.rect.colliderect(wall):
                if dx > 0:
                    self.player.rect.right = wall.left                    
                if dx < 0:
                    self.player.rect.left = wall.right
                    
    def moveY(self):
        self.player.vy += self.player.ay
        if self.player.vy >= 5.0:
            self.player.vy = 5.0
        if self.player.vy <= -5.0:
            self.player.vy = -5.0
            
        self.player.rect.y += self.player.vy
        
        for wall in self.walls.walls:
            if self.player.rect.colliderect(wall):
                if self.player.vy > 0:
                    self.player.rect.bottom = wall.top
                    self.player.canJump = True
                if self.player.vy < 0:
                    self.player.rect.top = wall.bottom
            
    def update(self):
        self.moveY()

class Duck:
    """Code for our moving duck"""
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,20,20)
        self.canJump = False
        self.vy = 0.0
        self.ay = 0.1
        
    def move(self):
        self.vy += self.ay
        if self.vy >= 2.0:
            self.vy = 2.0
        elif self.vy <= -2.0:
            self.vy = -2.0
            
        if self.moveUp or self.moveDown:
            self.rect.y += self.vy
        if self.moveLeft or self.moveRight:
            self.rect.x += self.vx
        
        
class Walls:
    """ Encodes the state of a singular rectangular platform in the game """
    def __init__(self, level):
        self.level = level
        self.world = []
        
        if self.level == 1:
            self.world = world1
        elif self.level == 2:
            self.world = world2
        elif self.level == 3:
            self.world = world3           
            
        self.walls = self.generateWalls()
        
    def generateWalls(self):
        listofwalls= []        

        for i in range(len(self.world)):
            for j in range(len(self.world[0])):
                if self.world[i][j] == "W":
                    listofwalls.append(pygame.Rect(j*20, i*20, 20, 20))
        
        return listofwalls
        
class PyGameWindowView:
    """ A view of brick breaker rendered in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
        
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.rect(self.screen, pygame.Color(0, 0, 255), self.model.player.rect)
        for wall in self.model.walls.walls:
            pygame.draw.rect(self.screen, pygame.Color(255, 255, 255), wall)
        pygame.display.update()

class PyGameKeyboardController:
    """ Manipulate game state based on keyboard input """
    def __init__(self, model):
        self.model = model
    
    def handle_pygame_event(self, event):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_LEFT]:
            self.model.moveX(-2)
        if keypressed[pygame.K_RIGHT]:
            self.model.moveX(2)
        if keypressed[pygame.K_UP] and self.model.player.canJump:
            self.model.player.vy = -5.0
            self.model.player.canJump = False
                        

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
        controller.handle_pygame_event(event)
        model.update()
        view.draw()
        time.sleep(.001)
    pygame.quit()