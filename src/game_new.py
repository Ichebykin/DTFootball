import sys
import pygame
from ball import Ball
from player import Player
from pygame import image
WIN_WIDTH = 800
WIN_HEIGHT = 400 
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

X_max = 800
Y_max = 600
pygame.init()
surface = pygame.display.set_mode(DISPLAY)
bg_image = image.load('../data/image/field.jpg').convert()
clock = pygame.time.Clock()
up = False
right = False
left = False

ball = Ball([400., 200.], [ 0., 0.])
player1 = Player([720., 280.],1)
player2 = Player([20,280.],1)

while True:
    for e in pygame.event.get():
        if e.type == 12:  # exit button
            pygame.display.quit()
            sys.exit()
       
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
    surface.blit(bg_image,(0,0))
    ball.update(surface)
    player1.update(left, right, up, surface)
    player2.update(left, right, up, surface)
    if pygame.sprite.collide_rect(ball,player1):
        ball.v = -ball.v+1.5*player1.v
    if pygame.sprite.collide_rect(ball,player2):
        ball.v = -ball.v+1.5*player2.v    
    clock.tick(120)
    pygame.display.update()
