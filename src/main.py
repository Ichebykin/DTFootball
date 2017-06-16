import pygame
import lib
import Scenes

pygame.init()

def play_music(music_file):
	try:
		pygame.mixer.music.load(music_file)

	except pygame.error:
		print("error music")
		return
	pygame.mixer.music.play(0)

play_music('../data/music/Wavin Flag.mp3')

def get_center(surface, sprite):
	return(surface.w / 2 - sprite.w / 2, surface.h / 2 - sprite.h / 2)

class WaitScene(lib.Scene):
	def __init__(self, time=1000, *argv):
		lib.Scene.__init__(self, *argv)
		self.run = 0
		self.time = time

	def _event(self, event):
		for e in event.get():
			if e.type == pygame.KEYDOWN:
				self.the_end()
				self.set_next_scene(MenuScene())
		if not self.run < self.time:
			self.the_end()

	def _update(self, dt):
		self.run += dt

class ShowScene(lib.Scene):
	def _start(self):
		self.sprite = self.manager.get_image('DreamTeam.jpg')
		self.football = lib.Transparent(3000)
		self.football.start()

	def _event(self, event):
		for e in event.get():
			if e.type == pygame.KEYDOWN:
				self.the_end()
				self.set_next_scene(PresentScene())

		if not self.football.is_start():
			self.the_end()

	def _update(self, dt):
		self.football.update(dt)

	def _draw(self, dt):
		self.display.fill((255, 255, 255))
		self.display.blit(self.football.get_sprite(self.sprite), get_center(self.display.get_rect(), self.sprite.get_rect()))

class HideScene(ShowScene):
	def _start(self):
		ShowScene._start(self)
		self.football.toggle()
		self.football.set_time(1000)

class PresentScene(lib.Scene):
	def _start(self):
		self.sprite = self.manager.get_image('Present.png')
		self.football = lib.Transparent(3000)
		self.football.start()

	def _event(self, event):
		for e in event.get():
			if e.type == pygame.KEYDOWN:
				self.the_end()
				self.set_next_scene(PresentDFScene())

		if not self.football.is_start():
			self.the_end()

	def _update(self, dt):
		self.football.update(dt)

	def _draw(self, dt):
		self.display.fill((255, 255, 255))
		self.display.blit(self.football.get_sprite(self.sprite), get_center(self.display.get_rect(), self.sprite.get_rect()))

class HidePresentScene(PresentScene):
	def _start(self):
		PresentScene._start(self)
		self.football.toggle()
		self.football.set_time(1000)

class PresentDFScene(lib.Scene):
	def _start(self):
# 		self.sprite = self.manager.get_image('PresentDF.png')
# 		self.sprite2 = self.manager.get_image('download10.png')
# 		self.sprite3 = self.manager.get_image('download20.png')
# 		self.sprite4 = self.manager.get_image('download50.png')
# 		self.sprite5 = self.manager.get_image('download70.png')
# 		self.sprite6 = self.manager.get_image('download90.png')
# 		self.sprite7 = self.manager.get_image('download100.png')
		#self.football = lib.Transparent(3000)
		#self.football.start()
		self.t = 0
		anim = lib.Animation('loadbar')
		self.load = anim.get_loadbar_animation()

	def _event(self, event):
		for e in event.get():
			if e.type == pygame.KEYDOWN:
				self.the_end()
				self.set_next_scene(MenuScene())
		if self.t>4500:
			self.the_end()
			self.set_next_scene(MenuScene())		
	def _update(self, dt):
		#self.football.update(dt)
		pass

	def _draw(self, dt):
		self.display.fill((255, 255, 255))
		self.load.blit(self.display, (250,200))
		self.t +=dt
# 		self.display.blit(self.load, (200,200))
		# time.sleep(5)
		#self.display.blit(self.football.get_sprite(self.sprite2), get_center(self.display.get_rect(), self.sprite2.get_rect()))

class Menu:
	def __init__(self, position=(0, 0), loop=True):
		self.index = 0
		self.x = position[0]
		self.y = position[1]
		self.menu = list()

	def down(self):  # перемещение вниз
		self.index += 1
		if self.index >= len(self.menu):
			self.index = 0

	def up(self):  # перемещение вверх
		self.index -= 1
		if self.index < 0:
			self.index = len(self.menu) - 1

	def add_menu_item(self, no_select, select, func):
		self.menu.append({ 'no select' : no_select, 'select' : select, 'func' : func })

	def call(self):
		self.menu[self.index]['func']()

	def draw(self, display):
		index = 0
		x = self.x
		y = self.y
		for item in self.menu:
			if self.index == index:
				display.blit(item['select'], (x, y))
				y += item['select'].get_rect().h
			else:
				display.blit(item['no select'], (x, y))
				y += item['no select'].get_rect().h
			index += 1

class AboutScene(lib.Scene):
	def _start(self):
		self.sprite = self.manager.get_image('aboutGame.png')
		self.football = lib.Transparent(3000)
		self.football.start()

	def _event(self, event):
		for e in event.get():
			if e.type == pygame.KEYDOWN:
				self.the_end()
				self.set_next_scene(PresentDFScene())

		if not self.football.is_start():
			self.the_end()

	def _update(self, dt):
		self.football.update(dt)

	def _draw(self, dt):
		self.display.fill((255, 255, 255))
		self.display.blit(self.football.get_sprite(self.sprite), get_center(self.display.get_rect(), self.sprite.get_rect()))

class MenuScene(lib.Scene):
	def item_call(self):
		print("item_call")
		self.the_end()
	def game_call(self):
		self.set_next_scene(Scenes.GameScene(MenuScene()))
		self.the_end()
	def about_call(self):
		self.set_next_scene(AboutScene(MenuScene()))
		self.the_end()

	def _start(self):
		self.sprite = self.manager.get_image('PresentDF.png')
		self.sprite2 = self.manager.get_image('aboutGame.png')
		self.football = lib.Transparent(3000)
		self.football.start()
		self.menu = Menu((330, 200))
		font = pygame.font.SysFont("Monospace", 40, bold=False, italic=False)
		font_bold = pygame.font.SysFont("Monospace", 40, bold=True, italic=False)
		item = "Мультиплеер"
		self.menu.add_menu_item(font.render(item, True, (0, 0, 0)),
								font_bold.render(item, True, (0, 0, 0)),
								self.game_call)
		item = "Об игре"
		self.menu.add_menu_item(font.render(item, True, (0, 0, 0)),
								font_bold.render(item, True, (0, 0, 0)),
								self.about_call)
		item = "Выход"
		self.menu.add_menu_item(font.render(item, True, (0, 0, 0)),
								font_bold.render(item, True, (0, 0, 0)),
								self.item_call)

	def _event(self, event):
		for e in event.get():
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_DOWN:
					self.menu.down()
				elif e.key == pygame.K_UP:
					self.menu.up()
				elif e.key == pygame.K_RETURN:
					self.menu.call()

	def _draw(self, dt):
		self.display.fill((255, 255, 255))
		self.menu.draw(self.display)
		self.display.blit(self.football.get_sprite(self.sprite), get_center(self.display.get_rect(), self.sprite.get_rect()))

if __name__ == '__main__':
	scene = WaitScene(1000, ShowScene(WaitScene(500, HideScene(WaitScene(1000, PresentScene(WaitScene(500, HidePresentScene(WaitScene(1000, PresentDFScene(WaitScene(1000, MenuScene())))))))))))
	# scene = GameScene()
	game = lib.Game(800, 400, scene=scene)
	game.set_caption("Dream Football", "icon2.png")
	game.game_loop()
