import sys
import pygame
from ball import Ball
from player import Player
from pygame import image, time
from physics import Physics
import copy
from Effects.cloud import Cloud_effect as c_e
from Parts.Scoreboard import Scoreboard
from Parts.Atstart import AtStart

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
right2 = False
left2 = False
kick1 = False
kick2 = False



Startpoint_Ball = [400., 200.]

ball = Ball(Startpoint_Ball, [ 0., 0.])



Startpoint_player_team1 = [450., 280.]

player1 = Player(Startpoint_player_team1, 1)



Startpoint_player_team2 = [20., 280.]

player2 = Player(Startpoint_player_team2, 1)

scoreboard = Scoreboard([0, 0])

cloud_effect1 = c_e(Startpoint_Ball)
cloud_effect2 = c_e(Startpoint_Ball)
cloud_effect3 = c_e(Startpoint_Ball)

while True:
    for e in pygame.event.get():
        if e.type == 12:  # exit button
            pygame.display.quit()
            sys.exit()
       
    if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
        up1 = True
    if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
        up2 = True    
    if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
        left1 = True
    if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
        left2 = True    
    if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
        right1 = True
    if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
        right2 = True    
    if e.type == pygame.KEYUP and e.key == pygame.K_UP:
        up1 = False
    if e.type == pygame.KEYUP and e.key == pygame.K_w:
        up2 = False        
    if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
        right1 = False
    if e.type == pygame.KEYUP and e.key == pygame.K_d:
        right2 = False     
    if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
        left1 = False
    if e.type == pygame.KEYUP and e.key == pygame.K_a:
        left2 = False  
    if e.type == pygame.KEYDOWN and e.key == pygame.K_LSHIFT:
        kick2 = True
    if e.type == pygame.KEYDOWN and e.key == pygame.K_RSHIFT: 
        kick1 = True 


    if ball.r[0] <= 45 and ball.r[1]>=190:
        scoreboard.goal_team1()
        ball = Ball(Startpoint_Ball, [ 0., 0.])
        player1.r = Startpoint_player_team1
        player2.r = Startpoint_player_team2
        pygame.time.delay(1000)


    if ball.r[0] >= 744 and ball.r[1]>=190:
        scoreboard.goal_team2()
        ball = Ball(Startpoint_Ball, [ 0., 0.])
        player1.r = Startpoint_player_team1
        player2.r = Startpoint_player_team2
        pygame.time.delay(1000)


    display.blit(bg_image, (0, 0))

    cloud_effect1.update(display)
    cloud_effect2.update(display)
    cloud_effect3.update(display)

    ball.update(display)
    player1.update(left1, right1, up1, display)
    player2.update(left2, right2, up2, display)

    cloud_effect3.r=copy.copy(cloud_effect2.r)
    cloud_effect2.r=copy.copy(cloud_effect1.r)
    cloud_effect1.r=copy.copy(ball.r)

    if pygame.sprite.collide_rect(ball, player1):
        Physics.interact(ball, player1)
    if pygame.sprite.collide_rect(ball, player2):
        Physics.interact(ball, player2)
    
    if kick1:
        player1.kick(ball)
    if kick2:
        player2.kick(ball)    
    kick1 = False
    kick2 = False

    scoreboard.update(display)

    clock.tick(120)
    pygame.display.update()
