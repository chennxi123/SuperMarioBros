import pygame,time
from levels import *
from constants import *



class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,ID,solid,semi):
        pygame.sprite.Sprite.__init__(self)
        self.ID = ID

        
        if self.ID == 1:
            self.image = pygame.image.load('Graphics/Tiles/gtileleft.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 1
            self.solid = solid

        if self.ID == 2:
            self.image = pygame.image.load('Graphics/Tiles/gtilemid.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 2
            self.solid = solid

        if self.ID == 3:
            self.image = pygame.image.load('Graphics/Tiles/gtileright.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 3
            self.solid = solid

        if self.ID == 4:
            self.image = pygame.image.load('Graphics/Tiles/stillblock.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 4
            self.solid = solid

        if self.ID == 5:
            self.image = pygame.image.load('Graphics/Tiles/hills1.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(128*SCALE,64*SCALE))
            self.id = 5
            self.solid = solid # rect is not to scale

        if self.ID == 6:
            self.image = pygame.image.load('Graphics/Tiles/hills2.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(80*SCALE,64*SCALE))
            self.id = 6
            self.solid = solid

        if self.ID == 7:
            self.image = pygame.image.load('Graphics/Tiles/cloudtile.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 7
            self.solid = solid

        if self.ID == 8:
            self.qblockframes = []
            self.qblockhitframe = []
            self.qblockframes.append(pygame.image.load('Graphics/Tiles/qblock1.png').convert_alpha())
            self.qblockframes.append(pygame.image.load('Graphics/Tiles/qblock2.png').convert_alpha())
            self.qblockframes.append(pygame.image.load('Graphics/Tiles/qblock3.png').convert_alpha())
            self.qblockframes.append(pygame.image.load('Graphics/Tiles/qblock4.png').convert_alpha())
            self.qblockhitframe.append(pygame.image.load('Graphics/Tiles/qblockhit.png').convert_alpha())
            self.qblockframes[0] = pygame.transform.scale(self.qblockframes[0],(TILESIZE,TILESIZE))
            self.qblockframes[1] = pygame.transform.scale(self.qblockframes[1],(TILESIZE,TILESIZE))
            self.qblockframes[2] = pygame.transform.scale(self.qblockframes[2],(TILESIZE,TILESIZE))
            self.qblockframes[3] = pygame.transform.scale(self.qblockframes[3],(TILESIZE,TILESIZE))
            self.qblockhitframe[0] = pygame.transform.scale(self.qblockhitframe[0],(TILESIZE,TILESIZE))
            self.id = 8
            self.solid = solid
            self.state = 'nothit'
            self.anim_timer = 2
            self.anim_num = 0
            self.image = self.qblockframes[0]
            self.hit_timer = 3
            self.hit_move = False
            self.newrect = False

        self.semisolid = semi
        self.rect = pygame.Rect(x,y,TILESIZE,TILESIZE)
        self.onscreen = False

    def update(self,playerx):

        if self.rect.x > playerx and self.rect.x - playerx > S_WIDTH or self.rect.x < playerx and playerx - self.rect.x > S_WIDTH:
            self.onscreen = False

        else:
            self.onscreen = True

            if self.id == 8 and self.state == 'nothit':
                if self.anim_timer > 0:
                    self.anim_timer -= 0.5

                else:
                    self.image = self.qblockframes[self.anim_num]
                    if self.anim_num < len(self.qblockframes) - 1:
                        self.anim_num += 1
                    else:
                        self.anim_num = 0
                    self.anim_timer = 2

            elif self.id == 8 and self.state == 'hit':
                self.image = self.qblockhitframe[0]

 
                if self.hit_timer > 0:
                    self.hit_timer -= 1
                    self.rect.y -= 4

                else:
                    if self.hit_timer == 0 and self.hit_move == False:
                        self.hit_timer = -3
                        self.hit_move = True
                    if self.hit_timer < 0:
                        self.hit_timer += 1
                        self.rect.y += 4

                    else:
                        self.hit_timer = 0
                        for m in powerups:
                            if m.rect.x == self.rect.x and m.rect.y == self.rect.y:
                                m.move = True


                                    


                                







 

