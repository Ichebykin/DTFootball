import numpy as np
from pygame import image,sprite,Rect
from physics import Physics

radius = 25

class Ball(sprite.Sprite):
    def __init__(self, r, v):
        sprite.Sprite.__init__(self)
        self.r = np.array(r)
        self.v = np.array(v)
        self.image = image.load('../data/image/mach.png')
        self.rect = Rect(r[0],r[1], 20, 20)
        
    def update(self, surface):
        size = surface.get_size()
        self.r += Physics.calc_dr(self.v)
        self.v += Physics.calc_dv(self.v)
        if self.r[1] > size[1]-100:
            self.v[1] =  -self.v[1]
            self.r[1] = size[1]-100
        if self.r[0] > size[0] - radius:
            self.v[0] = -self.v[0]
            self.r[0] = size[0] - radius 
        if self.r[0] < 0:
            self.v[0] = -self.v[0]
            self.r[0] = 0     
        self.rect.x = self.r[0]
        self.rect.y = self.r[1]
        self.draw(surface)
        
    def draw(self, surface):
        self.drawTrace(surface)
        surface.blit(self.image, self.r)

    def drawTrace(self,surface):
        return 