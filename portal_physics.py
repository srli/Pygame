import pygame, random, math, time
from pygame.locals import *
from world import *

class Portal_Platformer_Model:
    """ Encodes the game state """
    def __init__(self):
        self.player = Duck(20,20)
        self.level = 1
        self.walls = Walls(self.level)
        
    def updateDuck(self):
        self.checkMovement()
        
        if (self.player.moveLeft and self.player.ax < 0) or (self.player.moveRight and self.player.ax > 0):
            self.player.vx += self.player.ax
            if self.player.vx >= 2.0:
                self.player.vx == 2.0
            elif self.player.vx <= -2.0:
                self.player.vx == -2.0
            self.player.rect.x += self.player.vx
        if (self.player.moveUp and self.player.ay < 0) or (self.player.moveDown and self.player.ay > 0):
            self.player.vy += self.player.ay
            if self.player.vy >= 2.0:
                self.player.vy == 2.0
            elif self.player.vy <= -2.0:
                self.player.vy = -2.0
            self.player.rect.y += self.player.vy
            
        self.checkCollision()

    def checkCollision(self):
        for wall in self.walls.walls:
            if self.player.rect.colliderect(wall):
                if self.player.vx > 0:
                    self.player.rect.right = wall.left
                    self.player.vx = 0.0
                if self.player.vx < 0:
                    self.player.rect.left = wall.right
                    self.player.vx = 0.0
                if self.player.vy > 0:
                    self.player.rect.bottom = wall.top
                    self.player.vy = 0.0
                if self.player.vy < 0:
                    self.player.rect.top = wall.bottom
                    self.player.vy = 0.0

    def checkMovement(self):
        for wall in self.walls.walls:
            if self.player.rect.left == wall.right:
                self.player.moveLeft = False
            else:
                self.player.moveLeft = True
            if self.player.rect.right == wall.left:
                self.player.moveRight = False
            else:
                self.player.moveRight = True
            if self.player.rect.top == wall.bottom:
                self.player.moveUp = False
            else:
                self.player.moveUp = True
            if self.player.rect.bottom == wall.top:
                self.player.moveDown = False
            else:
                self.player.moveDown = True

            
    def update(self):
        self.updateDuck()
        print self.player.rect.y
        print self.player.vy
        print self.player.ay

class Duck:
    """Code for our moving duck"""
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,20,20)
        self.color = (155,230,249)
        self.vx = 0.0
        self.vy = 0.0
        self.ax = 0.0
        self.ay = 0.15
        self.moveUp = True
        self.moveDown = True
        self.moveLeft = True
        self.moveRight = True
        
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
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            self.model.player.ax = -1.0
        if event.key == pygame.K_RIGHT:
            self.model.player.ax = 1.0
        if event.key == pygame.K_UP:
            self.model.player.ay += -1.0
        if event.key == pygame.K_DOWN:
            self.model.player.ay += 1.0

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
