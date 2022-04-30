import pygame
from constants import *

class Background(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,filename,ID):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.oldx = x
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.w,self.h))
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.onscreen = True
        self.delay = 0
        self.id = ID

    def update(self,camx,playerxvel):


        if playerxvel > 0.9 or playerxvel < 0:

            if self.id == 1:
                self.rect.x = self.oldx + camx / 10
            
            else:
                self.rect.x = self.oldx - camx / 3









