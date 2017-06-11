
from pygame import sprite,image,Rect
import numpy as np
from physics import Physics

MOVE_SPEED = 30
WIDTH = 22
HEIGHT = 40
JUMP_POWER = 30


class Player(sprite.Sprite):
    def __init__(self, r):
        sprite.Sprite.__init__(self)
        self.v = np.array([0.,0])
        self.r = np.array(r)
        self.onGround = False
        self.image = image.load('../data/image/mario/l1.png')
        self.rect = Rect(r[0],r[1], WIDTH, HEIGHT)
        self.onGround = True
              
    def update(self, left, right, up, surface):
        dt = 0.1
        if up:
            if self.onGround:
                self.v[1] = -JUMP_POWER
                self.onGround = False
        
        if left:
            self.v[0] = -MOVE_SPEED
        
        if right:
            self.v[0] = MOVE_SPEED
            
        if not(left or right):
            self.v[0] = 0
        
        self.v += Physics.calc_dv(self.v, dt)
        self.r +=  Physics.calc_dr(self.v, dt)
        self.collide(self.r)  
        self.rect.x = self.r[0]
        self.rect.y = self.r[1]
           
        self.draw(surface)
          
    def draw(self,surface):
        surface.blit(self.image, (self.rect.x,self.rect.y))
    def collide(self, r):
        if self.r[1]>280:
            self.r[1]=280
            self.onGround = True
        if self.r[0]<60:
            self.r[0]=60
        if self.r[0]>720:
            self.r[0]=720        
    def kick(self, ball): 
        return       
                
       
