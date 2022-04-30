import pygame


#resolution
S_WIDTH =  512 
S_HEIGHT = 448
HALF_S_WIDTH = S_WIDTH / 2
HALF_S_HEIGHT = S_HEIGHT / 2
SCALE = 2
TILESIZE = 16 * SCALE

#time
CLOCK = pygame.time.Clock()
FPS = 60
pause = False

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

running = False

#game_data
all_sprites = pygame.sprite.Group()
platforms = []
backgrounds = []
powerups = []
all_sfx = []

#player
up = down = left = right = run = False


