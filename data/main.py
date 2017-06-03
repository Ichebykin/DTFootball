import time
import pygame
from ResManager import*

if __name__ == '__main__':
	pygame.init()
	display = pygame.display.set_mode((800,600))
	manager = ResManager()
	pygame.display.set_icon(manager.get_image('DreamTeam.jpg'))
	pygame.display.set_caption("Football")
	display.fill((255,255,255))
	pygame.display.flip()

	time.sleep(10)