#import sys
#sys.path.append("C:\\Users\\Тимур\\Desktop\\игра\\data\\music")
import time
import pygame
import lib

pygame.init()
#pygame.mixer.music.load('Wavin_Flag.mp3')
#pygame.mixer.music.play()
#while pygame.mixer.music.get_busy():
#    pass

#song = pygame.mixer.Sound('Wavin_Flag.mp3')
#song.play()
#while song.get_busy():
#    pass

def play_music(music_file):
    try:
        pygame.mixer.music.load(music_file)

    except pygame.error:
        print("error music")
        return
    pygame.mixer.music.play(0)
    # while pygame.mixer.music.get_busy():
    #     print("playing")
    #     pass

play_music('../data/music/Wavin Flag.mp3')

def get_center(surface, sprite):
    return(surface.w/2 - sprite.w/2, surface.h/2 - sprite.h/2)

class WaitScene(lib.Scene):
    def __init__(self, time = 1000, *argv):
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

    #def _present(self):
    #    sprite = self.manager.get_image('present.png')
    #    self.football = lib.Transparent(3000)
    #    self.football.start()

    #def _presentDF(self):
    #    sprite = self.manager.get_image('presentDF.png')
    #    self.football = lib.Transparent(3000)
    #    self.football.start()


    def _event(self, event):
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                self.the_end()
                self.set_next_scene(MenuScene())

        if not self.football.is_start():
            self.the_end()

    def _update(self, dt):
        self.football.update(dt)

    def _draw(self, dt):
        self.display.fill((255, 255, 255))
        self.display.blit(self.football.get_sprite(self.sprite), get_center(self.display.get_rect(),self.sprite.get_rect()))

class HideScene(ShowScene):
    def _start(self):
        ShowScene._start(self)
        #ShowScene._present(self)
        #ShowScene._presentDF(self)

        self.football.toggle()
        self.football.set_time(1000)

class Menu:
    def __init__(self, position = (0,0), loop = True):
        self.index = 0
        self.x = position[0]
        self.y = position[1]
        self.menu = list()

    def down(self): #перемещение вниз
        self.index += 1
        if self.index >= len(self.menu):
            self.index = 0

    def up(self): #перемещение вверх
        self.index -= 1
        if self.index < 0:
            self.index = len(self.menu)-1

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

class MenuScene(lib.Scene):
    def item_call(self):
        print("item_call")
        self.the_end()

    def _start(self):
        self.sprite = self.manager.get_image('DreamTeam.jpg')
        self.football = lib.Transparent(3000)
        self.football.start()
        self.menu = Menu((330,200))
        font      = pygame.font.SysFont("Monospace", 40, bold=False, italic=False)
        font_bold = pygame.font.SysFont("Monospace", 40, bold=True, italic=False)
        item = u"Один игрок"
        self.menu.add_menu_item(font.render(item,True,(0,0,0)),
                                font_bold.render(item,True,(0,0,0)),
                                self.item_call)
        item = u"Мультиплеер"
        self.menu.add_menu_item(font.render(item,True,(0,0,0)),
                                font_bold.render(item,True,(0,0,0)),
                                self.item_call)
        item = u"Настройки"
        self.menu.add_menu_item(font.render(item,True,(0,0,0)),
                                font_bold.render(item,True,(0,0,0)),
                                self.item_call)
        item = u"Об игре"
        self.menu.add_menu_item(font.render(item,True,(0,0,0)),
                                font_bold.render(item,True,(0,0,0)),
                                self.item_call)
        item = u"Выход"
        self.menu.add_menu_item(font.render(item,True,(0,0,0)),
                                font_bold.render(item,True,(0,0,0)),
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
        self.display.fill((255,255,255))
        self.menu.draw(self.display)
        self.display.blit(self.football.get_sprite(self.sprite), get_center(self.display.get_rect(),self.sprite.get_rect()))

if __name__ == '__main__':
    scene = WaitScene(1000, ShowScene(WaitScene(500, HideScene(WaitScene(1000, MenuScene())))))
    #scene2 = ...
    game = lib.Game(640, 480, scene=scene)
    game.set_caption("Dream Football", "icon2.png")
    game.game_loop()