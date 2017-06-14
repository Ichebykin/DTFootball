from pygame import sprite, Rect, Surface, Color
import numpy as np
from physics import Physics
from animation import boltAnimJump, boltAnimLeft, boltAnimRight, boltAnimStay

MOVE_SPEED = 200
WIDTH = 22
HEIGHT = 37
JUMP_POWER = 200
COLOR = "#888888"

class Player(sprite.Sprite):
    def __init__(self, r, pl_type):
        sprite.Sprite.__init__(self)
        self.v = np.array([-100., 0])
        self.r = np.array(r)
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.image.set_colorkey(Color(COLOR))
        self.rect = Rect(r[0], r[1], WIDTH, HEIGHT)
        self.onGround = True
        
    def update(self, left, right, up, display):
        
        if up:
            if self.onGround:
                self.v[1] = -JUMP_POWER
                self.onGround = False
            self.image.fill(Color(COLOR))
            boltAnimJump.blit(self.image, (0, 0))    
        
        if left:
            self.v[0] = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            boltAnimLeft.blit(self.image, (0, 0))
        
        if right:
            self.v[0] = MOVE_SPEED
            self.image.fill(Color(COLOR))
            boltAnimRight.blit(self.image, (0, 0))
            
        if not(left or right):
            self.v[0] = 0
            if not up:
                self.image.fill(Color(COLOR))
                boltAnimStay.blit(self.image, (0, 0))
        
        self.v += Physics.calc_dv(self.v)
        self.r += Physics.calc_dr(self.v)
        self.collide()  
        self.rect.x = self.r[0]
        self.rect.y = self.r[1]
        display.blit(self.image, (self.rect.x, self.rect.y))
        
    def collide(self):
        if self.r[1] > 280:
            self.r[1] = 280
            self.v[1] = 0
            self.onGround = True
        if self.r[0] < 60:
            self.r[0] = 60
        if self.r[0] > 720:
            self.r[0] = 720        
                
       
