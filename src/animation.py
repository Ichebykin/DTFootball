import pyganim

ANIMATION_DELAY = 0.1
ICON_DIR = '../data/image'
ANIMATION_RIGHT = [('%s/boy1/frame-r1.png' % ICON_DIR),
            ('%s/boy1/frame-r2.png' % ICON_DIR),
            ('%s/boy1/frame-r3.png' % ICON_DIR),
            ('%s/boy1/frame-r4.png' % ICON_DIR),
            ('%s/boy1/frame-r5.png' % ICON_DIR),
            ('%s/boy1/frame-r6.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/boy1/frame-l1.png' % ICON_DIR),
            ('%s/boy1/frame-l2.png' % ICON_DIR),
            ('%s/boy1/frame-l3.png' % ICON_DIR),
            ('%s/boy1/frame-l4.png' % ICON_DIR),
            ('%s/boy1/frame-l5.png' % ICON_DIR),
            ('%s/boy1/frame-l6.png' % ICON_DIR)]

ANIMATION_JUMP = [('%s/boy1/frame-J1.png' % ICON_DIR, 0.5)]
ANIMATION_STAY = [('%s/boy1/frame-I1.png' % ICON_DIR),
                   ('%s/boy1/frame-I2.png' % ICON_DIR)]

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
    boltAnim.append((anim, ANIMATION_DELAY*3))
boltAnimStay = pyganim.PygAnimation(boltAnim)
boltAnimStay.play()
                
boltAnimJump= pyganim.PygAnimation(ANIMATION_JUMP)
boltAnimJump.play()