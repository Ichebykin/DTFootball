import sys
import pygame
import numpy as np
import numpy.linalg as la
import copy
import math

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
X_max = 800
Y_max = 600
pygame.init()
surface = pygame.display.set_mode((X_max, Y_max), pygame.SRCALPHA, 32)
clock = pygame.time.Clock()
g = np.array([0, 0.0])


class Ball:
    def __init__(self, color, radius, x, y, vx, vy):
        self.m = 1.
        self.color = color
        self.radius = radius
        self.r0 = np.array([self.radius,self.radius])
        self.r = np.array([x, y])
        self.v = np.array([vx, vy])
        self.surface = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32).convert_alpha()
        self.surface.fill((0,0,0,0))
        pygame.draw.circle(self.surface, color, (radius, radius), radius)

    def move(self, dt):
        self.v += g * dt/2
        self.r += self.v * dt
        self.v += g * dt / 2
        if self.r[1] > Y_max - ball.radius or self.r[1] < 0:
            self.v[1] =  -self.v[1]
        if self.r[0] > X_max - ball.radius or self.r[0] < 0:
            self.v[0] = -self.v[0]

    def draw(self, surface):
        surface.blit(self.surface, self.r)

    def change_v(self, xc, yc):
        self.v += [xc, yc] - self.r

    def interact(self, other, surface):
        if la.norm(self.r - other.r) <= self.radius + other.radius:
            v = self.v - other.v
            r = other.r - self.r
            tau = np.array([-r[1], r[0]])


            alpha = math.acos(np.dot(v, r) / la.norm(v) / la.norm(r))
            # if np.dot(v,r) < 0:
            #     alpha = 180 + alpha
            v_r = la.norm(v) * math.cos(alpha) * r / la.norm(r)
            v_tau = la.norm(v) * math.sin(alpha) * tau / la.norm(tau)
            if np.dot(v, tau)<0:
                v_tau = - v_tau
            self.v = v_tau + other.v
            other.v = v_r + other.v
            other.r = self.r + r/la.norm(r)*(self.radius+other.radius)


ball1 = Ball(RED, 50, 580., 300., 0., 0.)
ball2 = Ball(GREEN, 50, 500., 100., 0., 0.)
ball3 = Ball(BLUE, 50, 100., 123., 0., 0.)
balls = [ball1, ball2, ball3]
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
    e = 0
    for ball in balls:
        ball.move(dt)
        e = e+(560- ball.r[1])*la.norm(g)+la.norm(ball.v)**2/2
        ball.draw(surface)
        balls2.remove(ball)
        for other_ball in balls2:
            ball.interact(other_ball, surface)
    print(e)
    clock.tick(60)
    pygame.display.update()
