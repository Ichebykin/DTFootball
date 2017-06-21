import pygame
from pygame import sprite 

class Scoreboard(sprite.Sprite):
	"""docstring for Scoreboard"""
	def __init__(self, goalcounter):
		sprite.Sprite.__init__(self)
		self.goalcounter = goalcounter
		#self.font = pygame.font.Font(None, 25)
		self.font = pygame.font.SysFont("Monospace", 20, bold=False, italic=False)

	def goal_team1(self):
		self.goalcounter[0] += 1

	def goal_team2(self):
		self.goalcounter[1] += 1

	def update(self,display):
		#size = display.get_size()
		self.text = self.font.render("Счет: %i - %i" % (self.goalcounter[0], self.goalcounter[1]), True, [0, 0, 0])
		display.blit(self.text, [0, 0])
		