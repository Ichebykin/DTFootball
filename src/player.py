
from pygame import sprite,Rect,Surface,Color
import numpy as np
from physics import Physics
import pyganim

MOVE_SPEED = 150
WIDTH = 22
HEIGHT = 40
JUMP_POWER = 200
COLOR =  "#888888"

ANIMATION_DELAY = 0.1
ICON_DIR = '../data/image'
ANIMATION_RIGHT = [('%s/mario/r1.png' % ICON_DIR),
            ('%s/mario/r2.png' % ICON_DIR),
            ('%s/mario/r3.png' % ICON_DIR),
            ('%s/mario/r4.png' % ICON_DIR),
            ('%s/mario/r5.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/mario/l1.png' % ICON_DIR),
            ('%s/mario/l2.png' % ICON_DIR),
            ('%s/mario/l3.png' % ICON_DIR),
            ('%s/mario/l4.png' % ICON_DIR),
            ('%s/mario/l5.png' % ICON_DIR)]

ANIMATION_JUMP = [('%s/mario/j.png' % ICON_DIR, 0.1)]
ANIMATION_STAY = [('%s/mario/0.png' % ICON_DIR, 0.1)]

class Player(sprite.Sprite):
    def __init__(self, r, pl_type):
        sprite.Sprite.__init__(self)
        self.v = np.array([0.,0])
        self.r = np.array(r)
        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.image.set_colorkey(Color(COLOR))
        self.rect = Rect(r[0],r[1], WIDTH, HEIGHT)
        self.onGround = True
        #Анимация движения вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #Анимация движения влево        
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        
        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0)) # По-умолчанию, стоим
                
        self.boltAnimJump= pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()
        
              
    def update(self, left, right, up, display):
        
        if up:
            if self.onGround:
                self.v[1] = -JUMP_POWER
                self.onGround = False
            self.image.fill(Color(COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))    
        
        if left:
            self.v[0] = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            self.boltAnimLeft.blit(self.image, (0, 0))
        
        if right:
            self.v[0] = MOVE_SPEED
            self.image.fill(Color(COLOR))
            self.boltAnimRight.blit(self.image, (0, 0))
            
        if not(left or right):
            self.v[0] = 0
            self.image.fill(Color(COLOR))
            self.boltAnimStay.blit(self.image, (0, 0))
        
        self.v += Physics.calc_dv(self.v)
        self.r +=  Physics.calc_dr(self.v)
        self.collide(self.r)  
        self.rect.x = self.r[0]
        self.rect.y = self.r[1]
        display.blit(self.image, (self.rect.x,self.rect.y))
        
    def collide(self, r):
        if self.r[1]>280:
            self.r[1]=280
            self.v[1]=0
            self.onGround = True
        if self.r[0]<60:
            self.r[0]=60
        if self.r[0]>720:
            self.r[0]=720        
    def kick(self, ball): 
        return       
                
       
