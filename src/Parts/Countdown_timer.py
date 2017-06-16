import pygame
from pygame import sprite, Rect, font

class Countdown_timer(sprite.Sprite):
	def __init__(self, Match):
		sprite.Sprite.__init__(self)
		self.Match = Match
		self.font = pygame.font.Font(None, 25)

	def update(self, display):
		size = display.get_size()
		self.text = self.font.render("Время до конца матча %d " % ((self.Match - pygame.time.get_ticks())//1000), True, [0, 0, 0])
		display.blit(self.text, [575, 0])
	