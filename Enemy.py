import pygame
import random


WIDTH = 600
HEIGHT = 600

image = {} #размер каждой картинки 64x64
image['down'] = pygame.image.load("move/down.png")
image['up'] = pygame.image.load("move/up.png")
image['left'] = pygame.image.load("move/left.png")
image['right'] = pygame.image.load("move/right.png")
sword = {}
sword['down'] = pygame.image.load("sword/down.png") #24x44
sword['up'] = pygame.image.load("sword/up.png") #24x44
sword['left'] = pygame.image.load("sword/left.png") #44x24
sword['right'] = pygame.image.load("sword/right.png") #44x24
movement = {'right': [1, 0], 'left': [-1, 0],
            'down': [0, 1], 'up': [0, -1]}


class Enemy:
    '''
    Class Player
    var:
        screen; x,y - player location; stamina; health; 
        orientation - show where he looking(up right down left);
        attack - show his condition(True - attack, False - peace);
        weapon - type of weapon(sword, ...)
    method:
        move - change player coordinates;
        vector_of_attack - return coordinates of line along which he make damage
                           and power of hit;
        draw - draw a player;
        
        0 - right
        1 - up
        
    '''
    
    def __init__(self, screen, x=450, y=450):
        self.screen = screen
        self.x = x
        self.y = y
        self.stamina = 100.
        self.health = 100.
        self.orientation = 0
        self.attack = False 
        self.weapon = 'sword'
        self.surface = image['down']
        self.v = 0
        self.cond = False
        self.step = 0
        

    
    def move(self):
        if self.step <= 0:
            self.step = random.randint(0, 50)
            self.v = random.randint(-10, 10)
            self.orientation = random.randint(0, 1)
        if self.orientation == 0:
            if self.x + self.v < WIDTH and self.x + self.v > 0:
                self.x += self.v
                self.step -= 1
            else: 
                self.step -= 1
        if self.orientation == 1:
            if self.y + self.v < HEIGHT and self.y + self.v > 0:
                self.y += self.v
                self.step -= 1
            else:
                self.step -= 1


    def vector_of_attack(self):
        start = (self.x, self.y)
        end = (0,0)
        if self.weapon == 'sword':
            if self.orientation == 'left':
                end[0] = self.x - 32 - 44
                end[1] = self.y
            elif self.orientation == 'right':
                end[0] = self.x + 32 + 44
                end[1] = self.y
            elif self.orientation == 'up':
                end[0] = self.x
                end[1] = self.y - 32 - 44
            else:
                end[0] = self.x
                end[1] = self.y + 32 + 44
        power = 5 * self.stamina/100
        return (start, end, power)

    def draw(self):
        im = image['down']
        self.screen.blit(im, (self.x - 32, self.y - 32))
        '''
        if self.attack == True:
            im_w = sword[self.orientation]
            if self.orientation == 'left':
                self.screen.blit(im_w, (self.x - 32 - 44, self.y - 11))
            elif self.orientation == 'right':
                self.screen.blit(im_w, (self.x + 32, self.y - 11))
            elif self.orientation == 'down':
                self.screen.blit(im_w, (self.x - 11, self.y + 32))
            elif self.orientation == 'up':
                self.screen.blit(im_w, (self.x - 11, self.y - 32 - 44))   
        ''' 
    
    def get_pos(self):
        return (self.x - 32, self.y - 32, self.x + 32, self.y + 32)

    def move_on(self):
        self.cond = True
    
    def move_off(self):
        self.cond = False
        
pygame.init()


FPS = 30

X = 600
Y = 600
screen = pygame.display.set_mode((X, Y))

pygame.display.update()
clock = pygame.time.Clock()
finished = False


status = True
player = Enemy(screen)
while (status):
    clock.tick(FPS)
    screen.fill('WHITE')
    player.draw()
    player.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        elif event.type == pygame.KEYDOWN:
            player.move_on()
            player.take_orientation(event)
        elif event.type == pygame.KEYUP:
            player.move_off()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.attack = True
        elif event.type == pygame.MOUSEBUTTONUP:
            player.attack = False
    
    pygame.display.update()