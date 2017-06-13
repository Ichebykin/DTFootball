import pyganim

ICON_DIR = '../data/image/boy2'
#class animation():
#    def __init__(self,Idir):
#        self.ICON_DIR = Idir

ANIMATION_DELAY = 0.1

ANIMATION_RIGHT = [('%s/frame-r1.png' % ICON_DIR),
            ('%s/frame-r2.png' % ICON_DIR),
            ('%s/frame-r3.png' % ICON_DIR),
            ('%s/frame-r4.png' % ICON_DIR),
            ('%s/frame-r5.png' % ICON_DIR),
            ('%s/frame-r6.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/frame-l1.png' % ICON_DIR),
            ('%s/frame-l2.png' % ICON_DIR),
            ('%s/frame-l3.png' % ICON_DIR),
            ('%s/frame-l4.png' % ICON_DIR),
            ('%s/frame-l5.png' % ICON_DIR),
            ('%s/frame-l6.png' % ICON_DIR)]

ANIMATION_JUMP = [('%s/frame-J1.png' % ICON_DIR, 0.5)]
ANIMATION_STAY = [('%s/frame-I1.png' % ICON_DIR),
                   ('%s/frame-I2.png' % ICON_DIR)]

boltAnim = []
for anim in ANIMATION_RIGHT:
    boltAnim.append((anim, ANIMATION_DELAY))
boltAnimRight = pyganim.PygAnimation(boltAnim)
boltAnimRight.play()
           
boltAnim = []
for anim in ANIMATION_LEFT:
    boltAnim.append((anim, ANIMATION_DELAY))
boltAnimLeft = pyganim.PygAnimation(boltAnim)
boltAnimLeft.play()
        
boltAnim = []
for anim in ANIMATION_STAY:
    boltAnim.append((anim, ANIMATION_DELAY * 3))
boltAnimStay = pyganim.PygAnimation(boltAnim)
boltAnimStay.play()
                
boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
boltAnimJump.play()
