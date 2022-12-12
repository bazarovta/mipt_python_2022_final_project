import math
import pygame

class Agent:
    
    def __init__(self,screen, x, y, v, boundary):
        self.screen = screen
        self.x = x
        self.y = y
        self.v = v
        self.boundary = boundary
        self.r = 70
        self.angle = math.pi/3
        self.direction = math.pi/3
        self.lines = 100
        self.w = math.pi / 10
        self.a = 10

    def draw(self):
        for i in range (self.lines // 2, 2, -1):
            x1 = self.x + self.r * math.cos(self.direction + self.angle / i)
            x2 = self.x + self.r * math.cos(self.direction - self.angle / i)
            y1 = self.y + self.r * math.sin(self.direction + self.angle / i)
            y2 = self.y + self.r * math.sin(self.direction - self.angle / i)
            pygame.draw.line(
                self.screen,
                (153, 0, 0),
                [self.x, self.y],
                [x1, y1]
                )
            pygame.draw.line(
                self.screen,
                (153, 0, 0),
                [self.x, self.y],
                [x2, y2]
                )
        pygame.draw.circle(
                self.screen,
                (255, 100, 100),
                (self.x, self.y),
                self.a
                )
    def move(self):
        dt = 0.1
        if self.boundary[0] == 'y':
            if self.y < self.boundary[1] and self.v < 0:
                self.v = -self.v
            elif self.y > self.boundary[2] and self.v > 0:
                self.v = -self.v
            self.y += self.v * dt
        else:
            if self.x < self.boundary[1] and self.v < 0:
                 self.v = -self.v
            elif self.x > self.boundary[2] and self.v > 0:
                self.v = -self.v
            self.x += self.v * dt
        if self.direction >= 2*math.pi:
            self.direction -= 2*math.pi
        self.direction += self.w * dt

