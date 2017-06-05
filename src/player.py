
from pygame import sprite,image,Rect
import numpy as np


MOVE_SPEED = 3
WIDTH = 22
HEIGHT = 40
JUMP_POWER = 6
GRAVITY = 0.3

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
        
        if up:
            if self.onGround:
                self.v[1] = -JUMP_POWER
        if not self.onGround:
            self.v[1] +=  GRAVITY        
        if left:
            self.v[0] = -MOVE_SPEED
        if right:
            self.v[0] = MOVE_SPEED
            
        if not(left or right):
            self.v[0] = 0
        
        self.collide(self.v)  
        self.rect.x += self.v[0]
        self.rect.y += self.v[1]
           
        self.draw(surface)
          
    def draw(self,surface):
        surface.blit(self.image, (self.rect.x,self.rect.y))
    def collide(self, v):
        nextx = self.rect.x + self.v[0]
        if nextx<=60 or nextx>720:
            self.v[0]=0
        nexty = self.rect.y +self.v[1]   
        if nexty<280:
            self.onGround = False
        if nexty>280:
            self.onGround = True
            self.rect.y = 280
            self.v[1]=0
    def kick(self, ball): 
        return       
                
       
