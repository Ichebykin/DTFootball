import sys
import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.init()
surface = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
g = 100


class Ball:
    def __init__(self, color, radius, x, y, vx, vy):
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.surface = pygame.Surface((2 * radius, 2 * radius)).convert_alpha()
        self.surface.fill((0, 0, 0))
        pygame.draw.circle(self.surface, color, (radius, radius), radius)

    def move(self, dt):
        self.vy += g * dt / 2.
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy += g * dt / 2
        if self.y > 560 or self.y < 0:
            self.vy = - self.vy
        if self.x > 760 or self.x < 0:
            self.vx = -self.vx

    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y))

    def change_v(self, xc, yc):
        self.vx += xc - self.x
        self.vy += yc - self.y

    def interact(self, other):
        if self is other:
            return
        

ball = Ball(RED, 20, 400, 100, 0, 0)
ball2 = Ball(GREEN, 30, 500, 130, 0, 0)
ball3 = Ball(BLUE, 20, 100, 123, 0, 0)
balls = [ball, ball2, ball3]
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
    for ball in balls:
        ball.move(dt)
        ball.draw(surface)
        for other_ball in balls:
            ball.interact(other_ball)
    clock.tick(50)
    pygame.display.update()
