import pygame, random
from constants import *
from sound import *

class Powerup(pygame.sprite.Sprite):

 	def __init__(self,x,y,p_type):
 		pygame.sprite.Sprite.__init__(self)
 		if p_type == 'mushroom':
 			self.image= pygame.image.load('Graphics/Objects/mushroom.png').convert_alpha()
 			self.image = pygame.transform.scale(self.image,(16 * SCALE, 16 * SCALE))
 			self.rect = self.image.get_rect()
 			self.rect.x = x
 			self.rect.y = y
 		self.xvel = 0
 		self.yvel = 0
 		self.onGround = False
 		self.x = random.randint(0,1)
 		if self.x == 0:
 			self.direction = 'right'
 		else:
 			self.direction = 'left'
 		self.removed = False
 		self.dormant = True
 		self.move = False
 		self.timer = 1
 		self.timer_num = 0
 		self.sound = False
 		self.onscreen = False

 	def update(self,playerx):

 		if self.rect.x > playerx and self.rect.x - playerx > S_WIDTH or self.rect.x < playerx and playerx - self.rect.x > S_WIDTH:
 			self.onscreen = False
 		else:
 			self.onscreen = True

 		if self.move == True:
 			if self.sound == False:
 				powerup_appear_sfx.play()
 				self.sound = True

 			if self.timer_num < TILESIZE:

		 		if self.timer > 1:
		 			self.timer -= 0.5

		 		else:
		 			self.rect.y -= 1
		 			self.timer = 1
		 			self.timer_num += 1

		 	else:

 				self.dormant = False

 		if self.dormant == False and self.move == True:

 			if self.timer == 0:

 				for p in powerups:

			 		if p.rect.x > playerx and p.rect.x - playerx >= S_WIDTH and p.dormant == False or p.rect.x < playerx and playerx - p.rect.x >= S_WIDTH and p.dormant == False:
			 			all_sprites.remove(p)
			 			powerups.remove(p)
			 			p.removed = True

			 	else:
			 		pass


		 		if self.removed == False:
				 		
			 		if self.direction == 'right':
			 			if self.xvel < 2:
			 				self.xvel += 1

			 			else:
			 				self.xvel = 2

			 		if self.direction == 'left':
			 			if self.xvel > -2:

			 				self.xvel -= 1

			 			else:
			 				self.xvel = -2

			 		if self.onGround == False:
			 			self.yvel += 0.6

			 			if self.yvel > 10:
			 				self.yvel = 10

			 		self.rect.left += self.xvel

			 		self.collide(self.xvel, 0, platforms)

			 		self.rect.top += self.yvel

			 		self.onGround = False;

			 		self.collide(0, self.yvel, platforms)

 			else:
 				self.timer -= 1

 		if self.dormant == True:
 			pass



 	def collide(self,xvel,yvel,platforms):
 		for p in platforms:
 			if pygame.sprite.collide_rect(self,p):

 				if xvel > 0:
 					self.rect.right = p.rect.left
 					self.direction = 'left'
 				if xvel < 0:
 					self.rect.left = p.rect.right
 					self.direction = 'right'
 				if yvel > 0:
 					self.rect.bottom = p.rect.top
 					self.onGround = True
 					self.yvel = 0
 				if yvel < 0:
 					self.rect.top = p.rect.bottom
 					self.yvel = 0