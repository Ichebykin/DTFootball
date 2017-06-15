import sys
import pygame
from ball import Ball
from player import Player
from pygame import image, time
from physics import Physics
import copy
from Effects.cloud import Cloud_effect as c_e
# from Effects.goalcounter import Scoreboard

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



Startpoint_Ball_x = 400.
Startpoint_Ball_y = 200.

ball = Ball([Startpoint_Ball_x, Startpoint_Ball_y], [ 0., 0.])



Startpoint_player_team1_x = 450.
Startpoint_player_team1_y = 280.

player1 = Player([Startpoint_player_team1_x , Startpoint_player_team1_y], 1)



Startpoint_player_team2_x = 20.
Startpoint_player_team2_y = 280.

player2 = Player([Startpoint_player_team2_x, Startpoint_player_team2_y], 1)

goalcounter = [0, 0]

cloud_effect1 = c_e([Startpoint_Ball_x, Startpoint_Ball_y])
cloud_effect2 = c_e([Startpoint_Ball_x, Startpoint_Ball_y])
cloud_effect3 = c_e([Startpoint_Ball_x, Startpoint_Ball_y])

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
    	goalcounter[0] += 1
    	ball = Ball([Startpoint_Ball_x, Startpoint_Ball_y], [ 0., 0.])
    	player1.r = [Startpoint_player_team1_x , Startpoint_player_team1_y]
    	player2.r = [Startpoint_player_team2_x, Startpoint_player_team2_y]
    	pygame.time.delay(1000)


    if ball.r[0] >= 744 and ball.r[1]>=190:
    	goalcounter[1] += 1
    	ball = Ball([Startpoint_Ball_x, Startpoint_Ball_y], [ 0., 0.])
    	player1.r = [Startpoint_player_team1_x , Startpoint_player_team1_y]
    	player2.r = [Startpoint_player_team2_x, Startpoint_player_team2_y]
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

    font = pygame.font.Font(None, 25)
    text = font.render("Счет: %i - %i" % (goalcounter[0], goalcounter[1]), True, [0, 0, 0])
    display.blit(text, [0, 0] )
    # Scoreboard(goalcounter)         
    clock.tick(120)
    pygame.display.update()
