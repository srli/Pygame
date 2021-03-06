# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 16:58:55 2014

@author: zoherghadyali, jaywoo, sophiali
"""

import pygame, random, math, time
from pygame.locals import *
from world import *


class Wall:
    """ Encodes the state of a singular rectangular platform in the game """
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)
    
class Cake(object):
     def __init__(self, pos):
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

         
class Portal_Platformer_Model:
    def __init__(self):
        self.player = Duck(40,40)
        self.portal_orange = 'null'
        self.portal_blue = 'null'
        self.walls = []
        self.cake = None
        self.level = 0
        self.construct_environment(0)
        
    def construct_environment(self, number):
        self.walls = []
        self.cake = None
        level = world
        for platform in level:
            x = y = 0
            for row in level[number]:
                for col in row:
                    if col == "W":
                        self.walls.append(Wall((x, y)))
                    if col == "C":
                        self.cake = Cake((x,y))
                        print "I see cake!"
                    x += 20
                y += 20
                x = 0
        
    def moveX(self, dx):
        self.player.rect.x += dx
        
        for wall in self.walls:
            if self.player.rect.colliderect(wall):
                if dx > 0:
                    self.player.rect.right = wall.rect.left                    
                if dx < 0:
                    self.player.rect.left = wall.rect.right
                    
    def moveY(self):
        self.player.vy += self.player.ay
        if self.player.vy >= 5.0:
            self.player.vy = 5.0
        if self.player.vy <= -5.0:
            self.player.vy = -5.0
            
        self.player.rect.y += self.player.vy
        
        for wall in self.walls:
            if self.player.rect.colliderect(wall):
                if self.player.vy > 0:
                    self.player.rect.bottom = wall.rect.top
                    self.player.canJump = True
                if self.player.vy < 0:
                    self.player.rect.top = wall.rect.bottom
            
   
    def update(self):
        self.moveY()
        
        if self.player.rect.colliderect(self.cake.rect):
            self.level += 1
            self.walls = []
            self.player.rect.x = 40
            self.player.rect.y = 40
            self.player.vx= 0
            self.player.vy = 0
            self.portal_blue = 'null'
            self.portal_orange = 'null'
            self.construct_environment(self.level)

        
        if self.portal_blue != 'null' and self.portal_orange != 'null':

#            if self.duck.rect.colliderect(self.portal_orange.rectp):
#                if self.duck.vx > 0: # Moving right; Hit the left side of the wall
#                    self.duck.rect.right = self.portal_blue.rectp.right
#                if self.duck.vx < 0: # Moving left; Hit the right side of the wall
#                    self.duck.rect.left = self.portal_blue.rectp.left
#                if self.duck.vy > 0: # Moving down; Hit the top side of the wall
#                    self.duck.rect.bottom = self.portal_blue.rectp.top
#                if self.duck.vy < 0: # Moving up; Hit the bottom side of the wall
#                    self.duck.rect.top = self.portal_blue.rectp.x
                    
            if self.player.rect.colliderect(self.portal_orange.rectp):
#                self.duck.vx = 0.0
#                self.duck.vy = 0.0
                print "Collision detected!"
                print "I'm still repeating"
                xp = self.portal_blue.rectp.x
                yp = self.portal_blue.rectp.y
                self.player.rect.x = xp
                self.player.rect.y = yp
#                self.duck.rect.move_ip(self.duck.rect.x+xp, self.duck.rect.y+yp)
                return
                
            if self.player.rect.colliderect(self.portal_blue.rectp):
#                self.duck.vx = 0.0
#                self.duck.vy = 0.0
                print "Collision detected!"
                print "I'm still repeating!"
                xp = self.portal_orange.rectp.x
                yp = self.portal_orange.rectp.y
                self.player.rect.x = xp
                self.player.rect.y = yp
#                self.duck.rect.move_ip(xp,yp)
#                self.duck.rect.move_ip(self.duck.rect.x-xp, self.duck.rect.y-yp)
                return  
            else:
                pass
            
    def portal_update_orange(self,portalclick):
        self.portal_orange = Portal(portalclick)
        
    def portal_update_blue(self,portalclick):
        self.portal_blue = Portal(portalclick)
        
class Duck:
    """Code for our moving duck"""
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,20,20)
        self.canJump = False
        self.vy = 0.0
        self.ay = 0.15
        
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


        
class PyGameWindowView:
    """ Draws our game in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
    
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.rect(self.screen, pygame.Color(0, 0, 255), self.model.player.rect)
        for wall in self.model.walls:
            pygame.draw.rect(screen, pygame.Color(255, 255, 255), wall.rect)
        pygame.draw.rect(screen, pygame.Color(255,105,201), self.model.cake.rect)
   
        if self.model.portal_orange != 'null':
            pygame.draw.rect(self.screen, pygame.Color(255,153,0),self.model.portal_orange.rectp)
        if self.model.portal_blue != 'null':
            pygame.draw.rect(self.screen, pygame.Color(102,204,255),self.model.portal_blue.rectp)    
       
        pygame.display.update()


class PyGameKeyboardController:
    """ Manipulate game state based on keyboard input """
    def __init__(self, model):
        self.model = model
    
    def handle_pygame_key(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_LEFT]:
            self.model.moveX(-2)
        if keypressed[pygame.K_RIGHT]:
            self.model.moveX(2)
        if keypressed[pygame.K_UP] and self.model.player.canJump:
            self.model.player.vy = -5.0
            self.model.player.canJump = False
            
    def handle_pygame_mouse(self, event):
        x, y = event.pos
        for wall in self.model.walls:
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
            if event.type == MOUSEBUTTONDOWN:
                controller.handle_pygame_mouse(event)
        controller.handle_pygame_key()
        model.update()
        view.draw()
        time.sleep(0.001)

    pygame.quit()
