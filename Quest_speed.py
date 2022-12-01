import pygame
import Player
import time
import random


class Obstacle:
    
    def __init__(self, screen, x, height, space):
        self.screen = screen
        self.x = x
        self.y = 0
        self.height = height
        self.space = space
        self.v = 50
        self.w = 20
        self.image_up = pygame.image.load('quest_2/image_up.png')
        self.image_down = pygame.image.load('quest_2/image_down.png')
        self.width = self.image_up.get_width() // 5
    def move(self):
        dt = 0.1
        self.x -= self.v * dt
        if self.y >= 100 or self.y < 0:
            self.w = - self.w
        self.y += self.w * dt

    def draw(self):
        a = 10
        image_up = pygame.transform.scale(self.image_up,
                        (self.image_up.get_width() // 5,
                        self.height + self.y))
        image_down = pygame.transform.scale(self.image_down,
                        (self.image_down.get_width() // 5,
                        900 - self.height - self.space - self.y))
        self.screen.blit(image_up, (self.x, 0))
        self.screen.blit(image_down,
                        (self.x, self.y + self.height + self.space))

class MyPlayer(Player.Player):
    
    def __init__(self, screen, x=32, y=450, v=10):
        super().__init__(screen, x, y)
        self.cond = False
        self.v = v
        self.image = pygame.image.load("move/down.png")

    def move(self):
        dt = 0.1
        if self.cond == True:
            self.y -= 100* dt
        else:
            self.y += 100 * dt

    def draw(self):
        self.screen.blit(self.image, (self.x - 32, self.y - 32))

pygame.init()
clock = pygame.time.Clock()
FPS = 30
X = 1600
Y = 900
screen = pygame.display.set_mode((X,Y))
obstacles = []
start = time.time()
player = MyPlayer(screen, 100, 450)
status = True
while (status):
    clock.tick(FPS)
    screen.fill('WHITE')
    player.move()
    player.draw()
    pos = player.get_pos()
    curr = time.time()
    if curr-start >= 3:
        start = curr
        height = random.randint(200, 400)
        space = random.randint(200, 300)
        x = 1600
        wall = Obstacle(screen, x, height, space)
        obstacles.append(wall)
    obj_remove = []
    alive = True
    for obj in obstacles:
        obj.draw()
        obj.move()
        flag1 = 0
        flag2 = 0
        flag3 = 0
        flag4 = 0
        if pos[0] < obj.x and pos[2] > obj.x:
            flag1 = 1
        if pos[0] > obj.x and pos[2] < obj.x + obj.width:
            flag2 = 1
        if pos[3] > obj.y + obj.height + obj.space:
            flag3 = 1
        if pos[1] < obj.height + obj.y:
            flag4 = 1
        if flag4 + flag3 != 0 and flag2 + flag1 != 0:
            status = False
        if obj.x < -32:
            obj_remove.append(obj)
    for obj in obj_remove:
        obstacles.remove(obj)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        elif event.type == pygame.KEYDOWN:
            player.move_on()
            player.move_on()
        elif event.type == pygame.KEYUP:
            player.move_off()
    
    pygame.display.update() 

screen.fill('RED')
pygame.display.update()
time.sleep(5)
