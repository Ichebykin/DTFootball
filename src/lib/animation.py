import lib.pyganim

class Animation:
	def __init__(self,anim_type):
		if anim_type == 'player2':
			self.icon_dir = '../data/image/boy1'
		if anim_type == 'player1':
			self.icon_dir = '../data/image/boy2'
		if anim_type == 'loadbar':
			self.icon_dir = '../data/image/loadbar'	
	def get_right_animation(self):
		ANIMATION_DELAY = 0.05
		ANIMATION_RIGHT = [('%s/frame-r1.png' % self.icon_dir),
					('%s/frame-r2.png' % self.icon_dir),
					('%s/frame-r3.png' % self.icon_dir),
					('%s/frame-r4.png' % self.icon_dir),
					('%s/frame-r5.png' % self.icon_dir),
					('%s/frame-r6.png' % self.icon_dir)]
		boltAnim = []
		for anim in ANIMATION_RIGHT:
			boltAnim.append((anim, ANIMATION_DELAY))
		boltAnimRight = lib.pyganim.PygAnimation(boltAnim)
		boltAnimRight.play()
		return boltAnimRight
	def get_left_animation(self):
		ANIMATION_DELAY = 0.05
		ANIMATION_LEFT = [('%s/frame-l1.png' % self.icon_dir),
					('%s/frame-l2.png' % self.icon_dir),
					('%s/frame-l3.png' % self.icon_dir),
					('%s/frame-l4.png' % self.icon_dir),
					('%s/frame-l5.png' % self.icon_dir),
					('%s/frame-l6.png' % self.icon_dir)]
		boltAnim = []
		for anim in ANIMATION_LEFT:
			boltAnim.append((anim, ANIMATION_DELAY))
		boltAnimLeft = lib.pyganim.PygAnimation(boltAnim)
		boltAnimLeft.play()
		return boltAnimLeft
	def get_jump_animation(self):
		ANIMATION_JUMP = [('%s/frame-J1.png' % self.icon_dir, 0.5)]
		boltAnimJump = lib.pyganim.PygAnimation(ANIMATION_JUMP)
		boltAnimJump.play()
		return boltAnimJump
	def get_stay_animation(self):
		ANIMATION_STAY = [('%s/frame-I1.png' % self.icon_dir),
						   ('%s/frame-I2.png' % self.icon_dir)]
		ANIMATION_DELAY = 0.1
		boltAnim = []
		for anim in ANIMATION_STAY:
			boltAnim.append((anim, ANIMATION_DELAY * 3))
		boltAnimStay = lib.pyganim.PygAnimation(boltAnim)
		boltAnimStay.play()
		return boltAnimStay	
	def get_loadbar_animation(self):
		ANIMATION_DELAY = 1
		load = [('%s/10.png' % self.icon_dir),
					('%s/20.png' % self.icon_dir),
					('%s/50.png' % self.icon_dir),
					('%s/70.png' % self.icon_dir),
					('%s/90.png' % self.icon_dir)]
		boltAnim = []
		for anim in load:
			boltAnim.append((anim, ANIMATION_DELAY))
		loadAnim = lib.pyganim.PygAnimation(boltAnim)
		loadAnim.play()
		return loadAnim
		