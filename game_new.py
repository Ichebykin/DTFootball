import sys
import pygame
import numpy as np
import numpy.linalg as la
import copy
import math

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.init()
surface = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
g = np.array([0, 100.0])


class Ball:
    def __init__(self, color, radius, x, y, vx, vy):
        self.m = 1.
        self.color = color
        self.radius = radius
        self.r = np.array([x, y])
        self.v = np.array([vx, vy])
        self.surface = pygame.Surface((2 * radius, 2 * radius)).convert_alpha()
        self.surface.fill((0, 0, 0))
        pygame.draw.circle(self.surface, color, (radius, radius), radius)

    def move(self, dt):
        self.v += g * dt
        self.r += self.v * dt
        self.v += g * dt / 2
        if self.r[1] > 560 or self.r[1] < 0:
            self.v[1] = - self.v[1]
        if self.r[0] > 760 or self.r[0] < 0:
            self.v[0] = -self.v[0]

    def draw(self, surface):
        surface.blit(self.surface, self.r)

    def change_v(self, xc, yc):
        self.v += [xc, yc] - self.r

    def interact(self, other,surface):
        if self is other:
            return
        if la.norm(self.r - other.r) <= self.radius + other.radius:
            v = self.v - other.v
            r = other.r - self.r
            tau = np.array([-r[1], r[0]]) / la.norm(r)
            alpha = math.acos(np.dot(v, r) / la.norm(v) / la.norm(r))
            v_r = la.norm(v) * math.cos(alpha) * r / la.norm(r)
            v_tau = la.norm(v) * math.sin(alpha) * tau / la.norm(tau)
            v = - v_r + v_tau
            self.v = v + other.v
            other.v = v_r + other.v

ball1 = Ball(RED, 10, 400., 100., 0., 0.)
ball2 = Ball(GREEN, 10, 500., 130., 0., 0.)
# ball3 = Ball(BLUE, 20, 100., 123., 0., 0.)
balls = [ball1, ball2]
dt = 0.02
while True:
    for event in pygame.event.get():
        if event.type == 12:  # exit button
            pygame.display.quit()
            sys.exit()
        if event.type == 5:
            xc, yc = event.pos
            for ball in balls:
                ball.change_v(xc, yc)
    surface.fill((0, 0, 0))
    balls2 = copy.copy(balls)
    for ball in balls:
        ball.move(dt)
        ball.draw(surface)
        for other_ball in balls2:
            ball.interact(other_ball,surface)
        balls2.remove(ball)
    clock.tick(50)
    pygame.display.update()
