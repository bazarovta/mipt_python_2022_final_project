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

    def __init__(self, screen, x, height, space, v):
        self.screen = screen

        self.stage = 1

        self.x = x
        self.y = 0

        self.height = height
        self.space = space

        self.v = v
        self.w = 20

        self.image_up = pygame.image.load('quest_2/image_up.png')
        self.image_down = pygame.image.load('quest_2/image_down.png')
        self.width = self.image_up.get_width() // 5
    
    def move(self):
        dt = 0.1

        self.x -= self.v * dt
        
        if self.stage == 2:
            if self.y >= 100 or self.y < 0:
                self.w = - self.w
            self.y += self.w * dt

    def draw(self):
        image_up = pygame.transform.scale(self.image_up,
                        (self.width,
                        self.height + self.y))

        image_down = pygame.transform.scale(self.image_down,
                        (self.width,
                        600 - self.height - self.space - self.y))

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
    
    def __init__(self, screen, x=32, y=450):
        super().__init__(screen, x, y)

        self.image = pygame.image.load("move/down.png")
        self.im_size = 32
        self.image = pygame.transform.scale(self.image, 
                                           (self.im_size, self.im_size))

        self.up = 10
        self.down = 10

    def move(self, keys):
        if keys[pygame.K_SPACE]:
            self.y += self.up
        else:
            self.y -= self.down

    def draw(self):
        self.screen.blit(self.image, (self.x - self.im_size/2,
                                      self.y - self.im_size/2))

    def get_pos(self):
        return (self.x - self.im_size/2, self.y - self.im_size/2,
                self.x + self.im_size/2, self.y + self.im_size/2)

def game_loop(screen, player):
    status = True

    start = time.time()
    prev = time.time()

    clock = pygame.time.Clock()
    FPS = 30

    obstacles = [Obstacle(screen, 1200, 200, 200, 50)]

    delta_t = 3
    time_font = pygame.font.SysFont("comicsansms", 35)

    win = False

    while status:
        clock.tick(FPS)
        
        screen.fill('WHITE')
        
        pressed_keys = pygame.key.get_pressed()
        player.move(pressed_keys)
        player.draw()
        pos = player.get_pos()

        curr = time.time() 
        if curr-prev >= delta_t:
            prev = curr
            if curr-start <= 20:
                height = random.randint(100, 200)
                space = random.randint(200, 300)
                v = 50
            elif curr-start > 20 and curr-start <= 40:
                obj.stage = 2
                height = random.randint(100, 250)
                space = random.randint(200, 250)
                v = 75
                delta_t = 2
            elif curr-start > 40 and curr - start < 60:
                height = random.randint(100, 300)
                space = random.randint(150, 200)
                v = 100
                delta_t = 1
            if curr - start <= 60:
                wall = Obstacle(screen, 1200, height, space, v)
                obstacles.append(wall)

        if curr - start >= 63:
            win = True
            status = False
            
        obj_remove = []
        for obj in obstacles:
            flag1 = 0
            flag2 = 0
            flag3 = 0
            flag4 = 0
            if pos[0] < obj.x and pos[2] > obj.x:
                flag1 = 1
            if pos[0] < obj.x + obj.width and pos[2] > obj.x + obj.width:
                flag2 = 1
            if pos[3] > obj.y + obj.height + obj.space:
                flag3 = 1
            if pos[1] < obj.height + obj.y:
                flag4 = 1
            if flag4 + flag3 != 0 and flag2 + flag1 != 0:
                status = False
            if player.y < 32 or player.y > 900 - 32:
                status = False
            if obj.x < -32:
                obj_remove.append(obj)
            obj.draw()
            obj.move()

        if player.y < 32 or player.y > 600 - 32:
            status = False

        time_draw = time_font.render("Time: " + str(int(curr - start)),
                                    True, (0, 255, 0))
        screen.blit(time_draw, (0, 0))

        for obj in obj_remove:
            obstacles.remove(obj)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            
        pygame.display.update()

    if win:
        return 1
    else:
        return 0

def main(music):

    WIDTH = 1200
    HEIGHT = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    first_font = pygame.font.SysFont("comicsansms", 35)
    first_page = first_font.render("Press Space", True, (255, 0, 0))
    image = pygame.image.load("quest_2/fon.jpg")
    first_image = pygame.transform.scale(image, (1200, 600))
    screen.blit(first_image, (0,0))
    screen.blit(first_page, (550, 250))
    pygame.display.update()

    if music == True:
        pygame.mixer.music.load('quest_2/Intergalactic Odyssey.ogg')

    pygame.event.clear()
    block = True

    while block:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    block = False
                    if music == True:
                        pygame.mixer.music.play()
    
    player = MyPlayer(screen, 200, 300)
    check = False
    while check != True:
        player.x = 200
        player.y = 300
        player.defoult = 5
        player.jump = 5
        if music == True:
            pygame.mixer.music.play()
        c = game_loop(screen, player)
        if c == 1:
            check = True
        elif c == 0:
            check = False
        else:
            if music == True:
                pygame.mixer.music.pause()
            return False
        if check != True:
            if music == True:
                pygame.mixer.music.pause()
            second_page = first_font.render("Failed", True, (255, 0, 0))
            screen.blit(first_image, (0,0))
            screen.blit(second_page, (550, 250))
            pygame.display.update()
            time.sleep(2)

    screen.blit(first_image, (0, 0))
    if music == True:
        pygame.mixer.music.pause()
    third_page = first_font.render("You Win", True, (0, 255, 255))
    screen.blit(third_page, (550, 300))
    pygame.display.update()
    time.sleep(2)
    
    return check

