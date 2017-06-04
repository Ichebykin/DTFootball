from pygame import sprite,Surface,Color,Rect
import numpy as np


MOVE_SPEED = np.array([1.,0])
WIDTH = 22
HEIGHT = 32
COLOR =  "#888888"
JUMP_POWER = 10
GRAVITY = np.array([0,0.35])

class Player(sprite.Sprite):
    def __init__(self, r):
        sprite.Sprite.__init__(self)
        self.v = np.array([0.,0])
        self.r = np.array(r)
        self.onGround = False
        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(r[0],r[1], WIDTH, HEIGHT)
        self.image.set_colorkey((255, 0, 0)) 
        #draw.circle(self.image, (255, 0, 0), (10, 10), 10)
      

    def update(self, left, right, up, surface):
        
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
        if left:
            self.v = -MOVE_SPEED 
        if right:
            self.v = MOVE_SPEED 
        if not self.onGround:
            self.v +=  GRAVITY
        self.draw(surface)   
        self.rect.x += self.v[0]
    def draw(self,surface):
        print('ww')
        surface.blit(self.image, (self.rect.x,self.rect.y))
    def collide(self, v):
        return
       
