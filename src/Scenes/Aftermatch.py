import pygame
from pygame import image

import copy
import Parts
import lib
import Scenes
import sys
sys.path.insert(0, '..')
import main

class Aftermatch(lib.Scene):
	def _start(self):
		self.t = 0
	def _event(self, event):
		# print(Scenes.game_scene.scoreboard)
		for e in event.get():
			if e.type == pygame.KEYDOWN:
				self.__end = True
				self.set_next_scene(main.MenuScene())
				self.the_end()

	def _update(self, dt):
		#print(self.scoreboard)
		self.display.fill((255, 255, 255))
		self.font = pygame.font.Font(None, 25)
		self.text = self.font.render('Для выхода в меню нажмите "Enter"', True, [0, 0, 0])
		self.display.blit(self.text, [250, 370])