#import math
import numpy as np
#import numpy.linalg as la
from pygame import image,sprite,Rect

G = np.array([0, 500.0])
radius = 25
class Ball(sprite.Sprite):
    def __init__(self, r, v):
        sprite.Sprite.__init__(self)
        self.m = 1.
        #self.radius = radius
        self.r = np.array(r)
        self.v = np.array(v)
        self.image = image.load('../data/image/mach.png')
        self.rect = Rect(r[0],r[1], 20, 20)
        
    def update(self, surface):
        dt = 0.01
        size = surface.get_size()
        self.v += G * dt/2
        self.r += self.v * dt
        self.v += G * dt / 2
        if self.r[1] > size[1]-100:
            self.v[1] =  -self.v[1]
        if self.r[0] > size[0] - radius or self.r[0] < 0:
            self.v[0] = -self.v[0]
        self.rect.x = self.r[0]
        self.rect.y = self.r[1]
        self.draw(surface)
        
            
    def draw(self, surface):
        self.drawTrace(surface)
        surface.blit(self.image, self.r)

    #     def interact(self, other, surface):
#         if la.norm(self.r - other.r) <= self.radius + other.radius:
#             v = self.v - other.v
#             r = other.r - self.r
#             tau = np.array([-r[1], r[0]])
#             alpha = math.acos(np.dot(v, r) / la.norm(v) / la.norm(r))
#             v_r = la.norm(v) * math.cos(alpha) * r / la.norm(r)
#             v_tau = la.norm(v) * math.sin(alpha) * tau / la.norm(tau)
#             if np.dot(v, tau)<0:
#                 v_tau = - v_tau
#             self.v = v_tau + other.v
#             other.v = v_r + other.v
#             other.r = self.r + r/la.norm(r)*(self.radius+other.radius)
    def drawTrace(self,surface):
        return 