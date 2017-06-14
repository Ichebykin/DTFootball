import os
import pygame

class ResManager: #класс загрузки ресурсов
	def __init__(self, data_dir = 'data',image_dir = 'image',sound_dir = 'sound',music_dir = 'music'):
		self.data_dir = data_dir #каталог ресурсов
		self.image_dir = image_dir #каталог изображений
		self.sound_dir = sound_dir #каталог звуков
		self.music_dir = music_dir #каталог музыки
           #...........
	def get_image(self, name): #метод загрузки файла по имени
		#fullname = os.path.join(self.data_dir, os.path.join(self.image_dir, name)) #получение имени нужного файла вместе с путями к нему
		fullname = os.path.join(os.path.join(self.image_dir, name))
		try:
			image = pygame.image.load(fullname)
		except pygame.error:
			print('Cannot load image: {0}'.format(name))
			raise SystemExit
		else:
			image = image.convert_alpha()

			return image