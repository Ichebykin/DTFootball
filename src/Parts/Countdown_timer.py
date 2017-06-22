import pygame
from pygame import sprite
pygame.init()
class Countdown_timer(sprite.Sprite):
	def __init__(self, Match):
		sprite.Sprite.__init__(self)
		self.Match = Match
		#self.font = pygame.font.Font(None, 25)
		self.font = pygame.font.SysFont("Monospace", 20, bold=False, italic=False)

	def update(self, display,currentTime):
		size = display.get_size()
<<<<<<< HEAD
		self.text = self.font.render("Время до конца матча %d " % ((self.Match - pygame.time.get_ticks())//1000), True, [0, 0, 0])
		display.blit(self.text, [450, 0])
=======
		self.text = self.font.render("Время до конца матча %d " % ((self.Match - currentTime)//1000), True, [0, 0, 0])
		display.blit(self.text, [575, 0])
>>>>>>> 7e47ea8939c68a3bb028690c6aafd12f93101bb0
	