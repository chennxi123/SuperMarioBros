import pygame
from constants import *

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_S_HEIGHT, -t+HALF_S_HEIGHT, w, h

    l = min(0, l)                           
    l = max(-(camera.width-S_WIDTH), l)   
    t = max(-(camera.height-S_HEIGHT), t) 
    t = min(0, t)                           
    return pygame.Rect(l, t, w, h)
