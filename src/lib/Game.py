import pygame
from lib.ResManager import ResManager

class Game:
	def __init__(self,
				 width=640,  # ширина и высота окна,
				 height=480,
				 color=(255, 255, 255),  # цвет которым будет залит нарисованный экран,
				 fps=60, # максимальный fps
				 scene=None,
				 manager=ResManager()):
		#pygame.init()

		self.set_display(width, height)

		self.fps = fps
		self.__manager = manager
		self.scene = scene

		self.__display.fill(color)
		pygame.display.flip()

	def set_display(self, width, height):  # Создаем окно
		self.__display = pygame.display.set_mode((width, height))

	def set_caption(self, title=None, icon=None):
		if title == None:
			pygame.display.set_caption("game")
		else:
			pygame.display.set_caption(title)

		if icon != None:
			pygame.display.set_icon(self.__manager.get_image(icon))

	def game_loop(self):
		
		while self.scene != None:  # Если сцены нет, то все заканчивается.
			clock = pygame.time.Clock()
			dt = 0

			self.scene.start(self.__display, self.__manager)  # Инициализируем сцену, даем ей холст для рисования и ResManager.
			while not self.scene.is_end():
				
				self.scene.loop(dt)
				pygame.display.flip()
				dt = clock.tick(self.fps)
			self.scene = self.scene.next()
