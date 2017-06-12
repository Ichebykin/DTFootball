import sys
import pygame
from ball import Ball
from player import Player
from pygame import image
WIN_WIDTH = 800
WIN_HEIGHT = 400 
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

pygame.init()
display = pygame.display.set_mode(DISPLAY)
bg_image = image.load('../data/image/field.jpg')
clock = pygame.time.Clock()
up1 = False
right1 = False
left1 = False
up2 = False
right2= False
left2 = False
ball = Ball([400., 200.], [ 0., 0.])
player1 = Player([720., 280.],1)
player2 = Player([20,280.],1)

while True:
    for e in pygame.event.get():
        if e.type == 12:  # exit button
            pygame.display.quit()
            sys.exit()
        
    if e.type == pygame.KEYDOWN: 
        if e.key == pygame.K_UP:
            up1 = True
        if e.key == pygame.K_w:
            up2 = True    
        if e.key == pygame.K_LEFT:
            left1 = True
        if e.key == pygame.K_a:
            left2 = True    
        if e.key == pygame.K_RIGHT:
            right1 = True
        if e.key == pygame.K_d:
            right2 = True    
    if e.type == pygame.KEYUP:
        if e.key == pygame.K_UP:
            up1 = False
        if e.key == pygame.K_w:
            up2 = False        
        if e.key == pygame.K_RIGHT:
            right1 = False
        if e.key == pygame.K_d:
            right2 = False     
        if e.key == pygame.K_LEFT:
            left1 = False
        if e.key == pygame.K_a:
            left2 = False    
    display.blit(bg_image,(0,0))
    ball.update(display)
    player1.update(left1, right1, up1, display)
    player2.update(left2, right2, up2, display)
    
    if pygame.sprite.collide_rect(ball,player1):
        ball.v = -ball.v+1.5*player1.v
    if pygame.sprite.collide_rect(ball,player2):
        ball.v = -ball.v+1.5*player2.v    
    clock.tick(120)
    pygame.display.update()
