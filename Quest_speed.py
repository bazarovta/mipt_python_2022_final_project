import pygame
import Player
import time
import random


class Obstacle:
    '''
    Class Obstacle
    args:
        screen; height - length of up pipe;
        space - length between up and down pipes;
        x - ox cord; y - additional length of height;
        v - ox speed; w - oy speed; image_up - picture
        of up pipe; image_down - picture of down pipe;
        width - width of pipe
    methods:
        move - change x and y of object;
        draw - draw obstacle
    '''

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
    '''
    class Player heritage from Player.Player
    args:
        image - picture of player
    methods:
        move - change y-coordinate of player;
        draw - draw player
    '''

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

def game_loop(screen, player):
    status = True;
    start = time.time()
    clock = pygame.time.Clock()
    FPS = 30
    obstacles = []
    pygame.event.clear()
    check = True
    while status:
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
            wall = Obstacle(screen, 1600, height, space)
            obstacles.append(wall)
        obj_remove = []
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
                check = False
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
            elif event.type == pygame.KEYUP:
                player.move_off()
        pygame.display.update()
    return check

def main():
    pygame.init()
    X = 1600
    Y = 900
    screen = pygame.display.set_mode((X,Y))
    player = MyPlayer(screen, 100, 450)
    first_font = pygame.font.SysFont("comicsansms", 35)
    first_page = first_font.render("Press Space", True, (255, 0, 0))
    image = pygame.image.load("quest_2/fon.jpg")
    first_image = pygame.transform.scale(image, (1600, 900))
    screen.blit(first_image, (0,0))
    screen.blit(first_page, (700, 400))
    pygame.display.update()
    pygame.event.clear()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                break
    check = game_loop(screen, player)
    while check != True:
        second_page = first_font.render("Failed", True, (255, 0, 0))
        screen.blit(first_image, (0,0))
        screen.blit(second_page, (700, 400))
        pygame.display.update()
        time.sleep(2)
        check = game_loop(screen, player)



main()
pygame.quit()
