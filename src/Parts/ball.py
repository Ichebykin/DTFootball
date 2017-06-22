import numpy as np
from pygame import image, sprite, Rect
import lib

radius = 10

class Ball(sprite.Sprite):
    def __init__(self, r, v):
        sprite.Sprite.__init__(self)
        self.r = np.array(r)
        self.v = np.array(v)
        self.image = image.load('../data/image/mach.png')
        self.rect = Rect(r[0], r[1], 20, 20)
        
    def update(self, display,dt):
        size = display.get_size()
        self.r += lib.Physics.calc_dr(self.v,dt)
        self.v += lib.Physics.calc_dv(self.v,dt)
        self.collide(size)
        self.rect.x = self.r[0]
        self.rect.y = self.r[1]
        display.blit(self.image, self.r)
    
    def collide(self, size):
        if self.r[1] > size[1] - 106:
            self.v[1] = -self.v[1]
            if abs(self.v[1]) < 200:
                self.v[1] = 0
            self.r[1] = size[1] - 106
            
        if self.r[0] > size[0] - radius:
            self.v[0] = -self.v[0]
            self.r[0] = size[0] - radius 
        if self.r[0] < 0:
            self.v[0] = -self.v[0]
            self.r[0] = 0     
        
    def drawTrace(self, display):
        pass 
