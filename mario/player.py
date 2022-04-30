import pygame
from constants import *
from levels import *
from sound import *


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.jump = False
        self.fall = False

        self.maximum_velocity = 30
        self.gravity = 0.4
        self.max_speed = 3
        self.jump_speed = 10
        self.jump_cooldown = 0
        self.acceleration = 0.1
        self.friction = 0.04
        self.image_speed = 12  
        self.onscreen = True

        self.powerup_pause = False
        self.powertimer = 4
        self.powernum = 0
        self.pimgcount = 1

        self.walkframes_s = []
        self.walkframes_s.append(pygame.image.load('Graphics/Mario/smallmstill.png').convert_alpha())
        self.walkframes_s.append(pygame.image.load('Graphics/Mario/smallmwalk.png').convert_alpha())

        self.walkframes_b = []
        self.walkframes_b.append(pygame.image.load('Graphics/Mario/bigmstill.png').convert_alpha())
        self.walkframes_b.append(pygame.image.load('Graphics/Mario/bigmwalk1.png').convert_alpha())
        self.walkframes_b.append(pygame.image.load('Graphics/Mario/bigmwalk2.png').convert_alpha())

        self.jumpframe_s = []
        self.jumpframe_s.append(pygame.image.load('Graphics/Mario/smallmjump.png').convert_alpha())

        self.jumpframe_b = []
        self.jumpframe_b.append(pygame.image.load('Graphics/Mario/bigmjump.png').convert_alpha())

        self.quickturn_frame_s = []
        self.quickturn_frame_s.append(pygame.image.load('Graphics/Mario/smallmquickturn.png').convert_alpha())

        self.quickturn_frame_b = []
        self.quickturn_frame_b.append(pygame.image.load('Graphics/Mario/bigmquickturn.png').convert_alpha())

        self.crouch_frame_b = []
        self.crouch_frame_b.append(pygame.image.load('Graphics/Mario/bigmcrouch.png').convert_alpha())

        self.powerup_frames = []
        self.powerup_frames.append(pygame.image.load('Graphics/Mario/smallmstill.png').convert_alpha())
        self.powerup_frames.append(pygame.image.load('Graphics/Mario/bigmstill.png').convert_alpha())
        self.powerup_frames[0] = pygame.transform.scale(self.powerup_frames[0],(12 * SCALE, 15 * SCALE))
        self.powerup_frames[1] = pygame.transform.scale(self.powerup_frames[1],(14 * SCALE, 27 * SCALE))

        self.walkframes_s[0] = pygame.transform.scale(self.walkframes_s[0],(12 * SCALE, 15 * SCALE))
        self.walkframes_s[1] = pygame.transform.scale(self.walkframes_s[1],(15 * SCALE, 16 * SCALE))
        self.jumpframe_s[0] = pygame.transform.scale(self.jumpframe_s[0],(16 * SCALE, 16 * SCALE))
        self.quickturn_frame_s[0] = pygame.transform.scale(self.quickturn_frame_s[0],(14 * SCALE, 16 * SCALE))

        self.walkframes_b[0] = pygame.transform.scale(self.walkframes_b[0],(14 * SCALE, 27 * SCALE))
        self.walkframes_b[1] = pygame.transform.scale(self.walkframes_b[1],(16 * SCALE, 27 * SCALE))
        self.walkframes_b[2] = pygame.transform.scale(self.walkframes_b[2],(16 * SCALE, 26 * SCALE))
        self.jumpframe_b[0] = pygame.transform.scale(self.jumpframe_b[0],(16 * SCALE, 26 * SCALE))
        self.quickturn_frame_b[0] = pygame.transform.scale(self.quickturn_frame_b[0],(16 * SCALE, 28 * SCALE))
        self.crouch_frame_b[0] = pygame.transform.scale(self.crouch_frame_b[0],(14 * SCALE, 18 * SCALE))

        self.image = self.walkframes_s[0]
        self.rect = self.image.get_rect(x=TILESIZE,y=total_level_height - TILESIZE)

        self.direction = 'right'
        self.state = 'small'

       
     
    def update(self, up, down, left, right, run, platforms):

        if self.powerup_pause == True:
            self.state = 'big'
            self.xvel = 0
            self.right = False
            self.left = False
            if self.powernum < 8:
                if self.powertimer > 0:
                    self.powertimer -= 1

                else:
                    if self.pimgcount == 1:
                        self.image = self.walkframes_b[0]
                    elif self.pimgcount == 2:
                        self.image = self.walkframes_s[0]

                    if self.direction == 'left':
                        self.image = pygame.transform.flip(self.image,True,False)
                    self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,bottom=self.rect.bottom)
                    if self.pimgcount == 1:
                        self.pimgcount = 2
                    else:
                        self.pimgcount = 1
                    self.powertimer = 4
                    self.powernum += 1

            else:
                self.powerup_pause = False
                self.image = self.walkframes_b[0]
                if self.direction == 'left':
                    self.image = pygame.transform.flip(self.image,True,False)
                self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,bottom=self.rect.bottom)
            

        else:

            if self.state == 'small':
                self.jump_speed = 10

            else:
                self.jump_speed = 11

            if self.yvel > 0.8:
        	    self.fall = True

            if self.rect.x <= 0:
                self.rect.x = 1
                self.xvel = 0  

            if self.jump == True or self.fall == True:

                if self.state == 'small': 
                    self.image = self.jumpframe_s[0]
                elif self.state == 'big':
                    self.image = self.jumpframe_b[0]

                if self.direction == 'left':
                    self.image = pygame.transform.flip(self.image,True,False)

            if up and self.jump_cooldown == 0:
                if self.onGround:
                    self.jump_cooldown = 2
                    self.jump = True
                    jump_sfx.play()
                    self.yvel -= self.jump_speed
                    self.image = self.jumpframe_s[0]
                    if self.direction == 'left':
                        self.image = pygame.transform.flip(self.image,True,False)

            if down:
                pass

            if run:
                pass            

            if left and self.rect.x > 0 and not right:
                self.direction = 'left'

                if self.xvel > -self.max_speed:
                    self.xvel -= self.acceleration

                else:
                    self.xvel = -self.max_speed

                if not self.jump and not self.fall and self.xvel < -1:

                    if self.state == 'small':
                        self.frame = (self.rect.x // self.image_speed) % len(self.walkframes_s)
                        self.image = self.walkframes_s[self.frame]

                    elif self.state == 'big':
                        self.frame = (self.rect.x // self.image_speed) % len(self.walkframes_b)
                        self.image = self.walkframes_b[self.frame]
                    self.image = pygame.transform.flip(self.image,True,False)

                elif self.xvel > -1 and self.xvel < 0 and self.jump == False and self.fall == False and right == False:
                    if self.state == 'small':
                        self.image = self.walkframes_s[0]

                    elif self.state == 'big':
                        self.image = self.walkframes_b[0]

                    self.image = pygame.transform.flip(self.image,True,False)

                elif self.xvel > 1.5 and self.jump == False and self.fall == False:
                    if self.state == 'small':
                        self.image = self.quickturn_frame_s[0]

                    elif self.state == 'big':
                        self.image = self.quickturn_frame_b[0]

            if right and not left:
                self.direction = 'right'
                if self.xvel < self.max_speed:
                    self.xvel += self.acceleration

                else:
                    self.xvel = self.max_speed

                if not self.jump and not self.fall and self.xvel > 1:
                    if self.state == 'small':
                        self.frame = (self.rect.x // self.image_speed) % len(self.walkframes_s)
                        self.image = self.walkframes_s[self.frame]

                    elif self.state == 'big':
                        self.frame = (self.rect.x // self.image_speed) % len(self.walkframes_b)
                        self.image = self.walkframes_b[self.frame]

                elif self.xvel < 1 and self.xvel > 0 and self.jump == False and self.fall == False and left == False:
                    if self.state == 'small':
                        self.image = self.walkframes_s[0]

                    elif self.state == 'big':
                        self.image = self.walkframes_b[0]

                elif self.xvel < -1.5 and self.jump == False and self.fall == False:
                    if self.state == 'small':
                        self.image = self.quickturn_frame_s[0]
                    elif self.state == 'big':
                        self.image = self.quickturn_frame_b[0]
                    self.image = pygame.transform.flip(self.image,True,False)

            if not self.onGround:

                self.yvel += self.gravity
                if self.yvel > self.maximum_velocity:
                    self.yvel = self.maximum_velocity

            if not(left or right) or left and right :
                
                if self.xvel > 0.4:
                    self.xvel -= self.friction
                   
                elif self.xvel < 0.4:
                    self.xvel += self.friction
                 	
                else:
                    self.xvel = 0

                if self.jump == False and self.fall == False:
                    if self.state == 'small':
                        self.frame = (self.rect.x // self.image_speed) % len(self.walkframes_s)
                        self.image = self.walkframes_s[self.frame]

                    elif self.state == 'big':
                        self.frame = (self.rect.x // self.image_speed) % len(self.walkframes_b)
                        self.image = self.walkframes_b[self.frame]
                  
                    if self.direction == 'left':
                        self.image = pygame.transform.flip(self.image,True,False)    
                if self.jump == False and self.fall == False and self.xvel < 0.8 and self.xvel > 0:
                    if self.state == 'small':
                        self.image = self.walkframes_s[0]

                    elif self.state == 'big':
                        self.image = self.walkframes_b[0]

                    if self.direction == 'left':
                        self.image = pygame.transform.flip(self.image,True,False)  
        
            self.rect.left += self.xvel
       
            self.collide(self.xvel, 0, platforms)
      
            self.rect.top += self.yvel
        
            self.onGround = False;

            self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if p.solid == True:

                    if xvel > 0:
                        self.rect.right = p.rect.left
                        self.xvel = 0

                    if xvel < 0:
                        self.rect.left = p.rect.right
                        self.xvel = 0
     
                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.yvel = 0
                        if p.id == 8:
                        	p.state = 'hit'

                           
                    if yvel > 0 and p.semisolid == False:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.jump = False
                        self.fall = False
                        self.yvel = 0  

                        if self.jump_cooldown > 0:
                            self.jump_cooldown -= 0.5  

                else:
                    if yvel > 0 and self.rect.centery + self.rect.h / 2 < p.rect.centery and p.semisolid == True:   
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.jump = False
                        self.fall = False
                        self.yvel = 0
                        if self.jump_cooldown > 0:
                            self.jump_cooldown -= 0.5 
        
        for m in powerups:
            if pygame.sprite.collide_rect(self, m):
                m.removed = True
                all_sprites.remove(m) 
                powerups.remove(m) 
                powerup_sfx.play()
                if self.state == 'small':
                    self.powerup_pause = True                    




   