import pygame
from pygame import sprite
pygame.init()
class Countdown_timer(sprite.Sprite):
	def __init__(self, Match):
		sprite.Sprite.__init__(self)
		self.Match = Match
		self.font = pygame.font.Font(None, 25)

	def update(self, display,currentTime):
		size = display.get_size()
		self.text = self.font.render("Время до конца матча %d " % ((self.Match - currentTime)//1000), True, [0, 0, 0])
		display.blit(self.text, [575, 0])
	