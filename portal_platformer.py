# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 16:58:55 2014

@author: zoherghadyali
"""

import pygame, random, math, time
from pygame.locals import *

class Portal_Platformer_Model:
    """ Encodes the game state """
    def __init__(self):
        self.level1 = []
        platform1 = Platform((255,255,255), 20, 700, 0,480) #bottom edge
        platform2 = Platform((255,255,255), 20, 700, 0,0) #top edge
        platform3 = Platform((255,255,255), 500,20, 0, 0) #right edge
        platform4 = Platform((255,255,255), 500,20, 680, 0) #left edge
        platform5 = Platform((255,255,255), 100,20, 250,380)
        platform6 = Platform((255,255,255), 100,20, 450,380)
        platform7 = Platform((255,255,255), 20, 220, 250,360)


        self.level1.append(platform1)
        self.level1.append(platform2)
        self.level1.append(platform3)
        self.level1.append(platform4)
        self.level1.append(platform5)
        self.level1.append(platform6)
        self.level1.append(platform7)
        
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
        
        self.duck = Duck(16,16)
    
    def update(self):
        self.duck.update()

class Duck:
    """Code for our moving duck"""
    def __init__(self,x,y):
        self.color = (155,230,249)
        self.height = 20
        self.width = 20
        self.x = x
        self.y = y
        self.vy = 0.0
        self.vx = 0.0
        self.friction = 0.1
        self.gravity = 0.1
        
    def update(self):
        if self.vx > 0:
            self.x += self.vx - self.friction
        else:
            self.x += self.vx + self.friction
        self.y += self.vy + self.gravity
         
         
#    def update(self,vx,vy):
#        # Move each axis separately. Note that this checks for collisions both times.
#        if self.vx != 0:
#            self.move_single_axis(vx, 0)
#        if self.vy != 0:
#            self.move_single_axis(0, vy)
#    
#    def move_single_axis(self, vx, vy):
#        # Move the rect
#        self.x += vx
#        self.y += vy
#                
#        # If you collide with a wall, move out based on velocity
#        for platform in self.model.level1:
#            platformrect = pygame.Rect(platform.x,platform.y,platform.width,platform.height)
#            if self.rect.colliderect(platformrect):
#                if vx > 0: # Moving right; Hit the left side of the wall
#                    self.rect.right = platformrect.left
#                if vx < 0: # Moving left; Hit the right side of the wall
#                    self.rect.left = platformrect.right
#                if vy > 0: # Moving down; Hit the top side of the wall
#                    self.rect.bottom = platformrect.top
#                if vy < 0: # Moving up; Hit the bottom side of the wall
#                    self.rect.top = platformrect.bottom

class Platform:
    """ Encodes the state of a singular rectangular platform in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
#        self.rect = pygame.Rect(x, y, height, width)
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
        pygame.draw.rect(self.screen, pygame.Color(self.model.duck.color[0], self.model.duck.color[1], self.model.duck.color[2]), pygame.Rect(self.model.duck.x, self.model.duck.y, self.model.duck.width, self.model.duck.height))
        for platform in self.model.level1:
            pygame.draw.rect(self.screen, pygame.Color(platform.color[0],platform.color[1],platform.color[2]),pygame.Rect(platform.x,platform.y,platform.width,platform.height))
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
        time.sleep(.001)
    pygame.quit()
