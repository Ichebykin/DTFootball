import pygame
from pygame import image
from physics import Physics
import copy
import Effects
import Parts
import lib

bg_image = image.load('../data/image/field.jpg')
up1 = False
right1 = False
left1 = False
kick1 = False
move1 = [up1,right1,left1,kick1]
zeroMove = [False,False,False,False]
up2 = False
right2 = False
left2 = False
kick2 = False
move2 = [up2,right2,left2,kick2]

Match = 60000 * 1.5  # 1 minute in milliseconds
countdown_timer = Parts.Countdown_timer(Match)
Startpoint_Ball = [400., 200.]
Startpoint_player_team1 = [780., 280.]
Startpoint_player_team2 = [20., 280.]


cloud_effect1 = Effects.Cloud_effect([400., 200.])
cloud_effect2 = Effects.Cloud_effect([400., 200.])
cloud_effect3 = Effects.Cloud_effect([400., 200.])
class GameScene(lib.Scene):
	ball = Parts.Ball(Startpoint_Ball, [ 0., 0.])
	player1 = Parts.Player(Startpoint_player_team1, 1)
	player2 = Parts.Player(Startpoint_player_team2, 2)
	scoreboard = Parts.Scoreboard([0, 0])
	def _event(self, event):
		global move1
		global move2
	
		for e in event.get():
			if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
				move1[0] = True
			if e.type == pygame.KEYUP and e.key == pygame.K_UP:
				move1[0]= False
					
			if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
				move1[1] = True
			if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
				move1[1] = False
					
			if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
				move1[2] = True
			if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
				move1[2] = False
					
			if e.type == pygame.KEYDOWN and e.key == pygame.K_LSHIFT:
				move2[3] = True
				
			if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
				move2[0] = True	
			if e.type == pygame.KEYUP and e.key == pygame.K_w:
				move2[0] = False			
			
			if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
				move2[1] = True	
			if e.type == pygame.KEYUP and e.key == pygame.K_d:
				move2[1] = False	
			
			if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
				move2[2] = True	
			if e.type == pygame.KEYUP and e.key == pygame.K_a:
				move2[2] = False  
			
			if e.type == pygame.KEYDOWN and e.key == pygame.K_RSHIFT: 
				move1[3] = True

	def _update(self,dt):
		if self.ball.r[0] <= 45 and self.ball.r[1] >= 190:
			self.scoreboard.goal_team2()
			self.ball = Parts.Ball(Startpoint_Ball, [ 0., 0.])
			self.player1.r = Startpoint_player_team1
			self.player2.r = Startpoint_player_team2
			pygame.time.delay(1000)
		if self.ball.r[0] >= 744 and self.ball.r[1] >= 190:
			self.scoreboard.goal_team1()
			self.ball = Parts.Ball(Startpoint_Ball, [ 0., 0.])
			self.player1.r = Startpoint_player_team1
			self.player2.r = Startpoint_player_team2
			pygame.time.delay(1000)
		
		self.display.fill((255, 255, 255))
		self.display.blit(bg_image, (0, 0))
		self.player1.update(move1, self.display)
		self.player2.update(move2, self.display)
		self.scoreboard.update(self.display)
		countdown_timer.update(self.display)
		cloud_effect3.r = copy.copy(cloud_effect2.r)
		cloud_effect2.r = copy.copy(cloud_effect1.r)
		cloud_effect1.r = copy.copy(self.ball.r)
		cloud_effect1.update(self.display)
		cloud_effect2.update(self.display)
		cloud_effect3.update(self.display)
		self.ball.update(self.display)
		if pygame.sprite.collide_rect(self.ball, self.player1):
			Physics.interact(self.ball, self.player1)
		if pygame.sprite.collide_rect(self.ball, self.player2):
			Physics.interact(self.ball, self.player2)
		if move1[3]:
			self.player1.kick(self.ball)
		if move2[3]:
			self.player2.kick(self.ball)	
		move1[3] = False
		move2[3] = False
		if pygame.time.get_ticks()>=Match:
			self.__end = True
			self.set_next_scene(None)
	