import pygame, random, math, time
from pygame.locals import *
from levels import *

class PortalModel:
    def __init__(self):
        self.level = level1
        self.world = []
        self.make_world()
    
    def make_world(self):
        self.world = []
        
        for i in range(len(self.level)):
            for j in range(len(self.level[0]):
                if self.level[i][j] == 1:   #Finds all of the 1's
                    self.world.append(Wall(j*40,i*40))
                    
class PyGamePortalView:
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen
        
    def draw(self)
        self.screen.fill(pygame.Color(0,0,0))
        for element in self.model.world:
            if isinstance(element, Wall):
                pygame.draw.rect(self.screen, pygame.Color(255,255,255), pygame.Rect(element.x, element.y, 40, 40))
        pygame.display.update()
        

class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
if __name__ == '__main__':
    pygame.init()
    
    size = (640, 480)
    screen = pygame.display.set_mode(size)
    
    model = PortalModel()
    view = PyGamePortalView(model, screen)
    
    running = True
    
    while running:
        for event in pygame.event.get()
            if event.type == QUIT:
                running = False
        model.update()
        view.draw()
        time.sleep(0.001)
        
    pygame.quit()
    
