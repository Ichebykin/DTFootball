import math
import numpy as np
import numpy.linalg as la
from pygame import Surface
from pygame import draw

g = np.array([0, 100.0])

class Ball:
    def __init__(self, color, radius, r, v):
        self.m = 1.
        self.color = color
        self.radius = radius
        self.r0 = np.array([self.radius,self.radius])
        self.r = np.array(r)
        self.v = np.array(v)
        self.surface = Surface((2 * radius, 2 * radius)).convert_alpha()
        self.surface.fill((0,0,0,0))
        draw.circle(self.surface, color, (radius, radius), radius)
    
    def update(self, dt, surface):
        size = surface.get_size()
        self.move(dt,size)
        self.draw(surface)
        
    def move(self, dt, size):
        self.v += g * dt/2
        self.r += self.v * dt
        self.v += g * dt / 2
        if self.r[1] > size[1] - self.radius or self.r[1] < 0:
            self.v[1] =  -self.v[1]
        if self.r[0] > size[0] - self.radius or self.r[0] < 0:
            self.v[0] = -self.v[0]
            
    def draw(self, surface):
        self.drawTrace(surface)
        surface.blit(self.surface, self.r)

    def change_v(self, xc, yc):
        self.v += [xc, yc] - self.r

    def interact(self, other, surface):
        if la.norm(self.r - other.r) <= self.radius + other.radius:
            v = self.v - other.v
            r = other.r - self.r
            tau = np.array([-r[1], r[0]])
            alpha = math.acos(np.dot(v, r) / la.norm(v) / la.norm(r))
            v_r = la.norm(v) * math.cos(alpha) * r / la.norm(r)
            v_tau = la.norm(v) * math.sin(alpha) * tau / la.norm(tau)
            if np.dot(v, tau)<0:
                v_tau = - v_tau
            self.v = v_tau + other.v
            other.v = v_r + other.v
            other.r = self.r + r/la.norm(r)*(self.radius+other.radius)
    def drawTrace(self,surface):
        return 