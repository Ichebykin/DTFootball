import sys
import copy
import pygame
from ball import *



WIN_WIDTH = 800
WIN_HEIGHT = 400 
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
X_max = 800
Y_max = 600
pygame.init()
surface = pygame.display.set_mode(DISPLAY)
clock = pygame.time.Clock()


ball1 = Ball(RED, 10, [580., 300.],[ 0., 0.])

balls = [ball1]
dt = 0.01
while True:
    for e in pygame.event.get():
        if e.type == 12:  # exit button
            pygame.display.quit()
            sys.exit()
        if e.type == 5:
            xc, yc = e.pos
            for ball in balls:
                ball.change_v(xc, yc)
        if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
            up = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            left = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            right = True
        if e.type == pygame.KEYUP and e.key == pygame.K_UP:
            up = False
        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
            right = False
        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
            left = False
        #print(right,left,up)        
    surface.fill((0, 0, 100))
    balls2 = copy.copy(balls)
    for ball in balls:
        ball.update(dt, surface)
        balls2.remove(ball)
        for other_ball in balls2:
            ball.interact(other_ball, surface)
    clock.tick(200)
    pygame.display.update()
