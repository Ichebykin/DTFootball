import numpy as np
from pygame import image, sprite, Rect
from physics import Physics

class cloud_effect(sprite.Sprite):
	"""docstring for cloud_effect """
	def __init__(self, r):
		sprite.Sprite.__init__(self)
		self.image = image.load('../data/image/Effects/Cloud1.png')
		self.r = r
		self.rect = Rect(r[0], r[1], 20, 20)

	def update(self, display):
		self.rect.x = self.r[0]
		self.rect.y = self.r[1]
		display.blit(self.image, self.r)