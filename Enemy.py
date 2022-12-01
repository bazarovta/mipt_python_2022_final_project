import pygame
import random



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
    
    def __init__(self, screen, x=100, y=100):
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
        self.vx = 0
        self.vy = 0
        self.cond = False
        self.step = 0
        self.R = 300
        self.r = 150
        self.WIDTH = 600
        self.HEIGHT = 600
        self.image = pygame.image.load("monsters/bamboo.png")
        self.image = pygame.transform.scale(self.image,
                    (self.image.get_width() // 1.5, self.image.get_height() // 1.5))
    
    def move_far_from_player(self):
        if self.step <= 0:
            self.step = random.randint(0, 50)
            self.v = random.randint(-1, 1)
            self.orientation = random.randint(0, 1)
        if self.orientation == 0:
            if self.x + self.v < self.WIDTH and self.x + self.v > 0:
                self.x += self.v
                self.step -= 1
            else: 
                self.step -= 1
        if self.orientation == 1:
            if self.y + self.v < self.HEIGHT and self.y + self.v > 0:
                self.y += self.v
                self.step -= 1
            else:
                self.step -= 1
    
    def move_near_player(self, obj):
        '''
        if obj.x - self.x < - self.R:
            self.vx = - 1
        elif obj.x - self.x > self.R:
            self.vx = 1
        elif abs(obj.x - self.x) < self.R:
            self.vx = 0
        
        if obj.y - self.y < - self.R:
            self.vy = - 1
        elif obj.y - self.y > self.R:
            self.vy = 1
        elif abs(obj.y - self.y) < self.R:
            self.vy = 0
        '''
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < self.R ** 2 and (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 > self.r ** 2:
            if obj.x - self.x < 0:
                self.vx = - 1
            elif obj.x - self.x > 0:
                self.vx = 1
                
            if obj.y - self.y < 0:
                self.vy = - 1
            elif obj.y - self.y > 0:
                self.vy = 1
                
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < self.r ** 2:
            if obj.x - self.x < 0:
                self.vx =  1
            elif obj.x - self.x > 0:
                self.vx = -1
                
            if obj.y - self.y < 0:
                self.vy = 1
            elif obj.y - self.y > 0:
                self.vy = -1
            
        if self.x + self.vx < self.WIDTH and self.x + self.vx > 0:
                self.x += self.vx
        if self.y + self.vy < self.HEIGHT and self.y + self.vy > 0:
                self.y += self.vy
        

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
        self.screen.blit(self.image, (self.x - 32, self.y - 32))
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
        
