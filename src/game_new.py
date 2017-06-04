import sys
import copy
import pygame
from ball import *

WIN_WIDTH = 800
WIN_HEIGHT = 640 
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
X_max = 800
Y_max = 600
pygame.init()
surface = pygame.display.set_mode(DISPLAY)
clock = pygame.time.Clock()


ball1 = Ball(RED, 50, [580., 300.],[ 0., 0.])
ball2 = Ball(RED, 50, [400., 300.],[ 0., 0.])
balls = [ball1,ball2]
dt = 0.01
while True:
    for event in pygame.event.get():
        if event.type == 12:  # exit button
            pygame.display.quit()
            sys.exit()
        if event.type == 5:
            xc, yc = event.pos
            for ball in balls:
                ball.change_v(xc, yc)
    surface.fill((0, 128, 0))
    balls2 = copy.copy(balls)
    for ball in balls:
        ball.move(dt)
        ball.draw(surface)
        balls2.remove(ball)
        for other_ball in balls2:
            ball.interact(other_ball, surface)
    clock.tick(60)
    pygame.display.update()
