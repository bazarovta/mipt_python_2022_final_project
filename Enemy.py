import pygame
from pygame.draw import *
import random
import numpy as np
import math



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


class Shell:
    def __init__(self, screen: pygame.Surface, x, y):
        
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0.
        self.vy = 0.
        self.color = 'RED'
        self.WIDTH = 600
        self.HEIGHT = 600
        self.live = 60
        
    def move(self):
        if self.x + self.vx + self.r >= self.WIDTH or self.x + self.vx - self.r <= 0:
            self.vx = -self.vx // np.sqrt(3)
        if self.y + self.vy + self.r >= self.HEIGHT or self.y + self.vy - self.r <= 0:
            self.vy = -self.vy // np.sqrt(3)
        self.x += self.vx
        self.y += self.vy
        self.live -= 1
        
    def draw(self):
        
        """
        Drawing the Ball
        """
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Enemy:
    '''
    Class Enemy
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
        self.stamina = 100.
        self.health = 100
        self.orientation = 0
        self.attack = False 
        self.weapon = 'sword'
        self.surface = image['down']
        self.v = 0
        self.vx = 0
        self.vy = 0
        self.size = 120
        self.cond = False
        self.step = 0
        self.R = 300
        self.r = 200
        self.WIDTH = 800
        self.HEIGHT = 600
        self.x = random.randint(0, self.WIDTH - self.size)
        self.y = random.randint(0, self.HEIGHT - self.size)
        self.power = 20
        self.an = 0
        self.image = pygame.image.load("monsters/bamboo.png")
        self.image = pygame.transform.scale(self.image,
                    (self.image.get_width() // 1.5, self.image.get_height() // 1.5))
    
    def move_far_from_player(self):
        if self.step <= 0:
            self.step = random.randint(0, 50)
            self.v = random.randint(-5, 5)
            self.orientation = random.randint(0, 1)
        if self.orientation == 0:
            if self.x + self.v + self.size < self.WIDTH and self.x + self.v > 0:
                self.x += self.v
                self.step -= 1
            else: 
                self.step -= 1
        if self.orientation == 1:
            if self.y + self.v + self.size < self.HEIGHT and self.y + self.v > 0:
                self.y += self.v
                self.step -= 1
            else:
                self.step -= 1
    
    def move_near_player(self, obj):
        if (self.x + self.size/2 - obj.x) ** 2 + (self.y + self.size/2 - obj.y) ** 2 < self.R ** 2 and (self.x + self.size/2 - obj.x) ** 2 + (self.y + self.size/2 - obj.y) ** 2 > self.r ** 2:
            if obj.x - self.x < 0:
                self.vx = - 5
            elif obj.x - self.x > 0:
                self.vx = 5
                
            if obj.y - self.y < 0:
                self.vy = - 5
            elif obj.y - self.y > 0:
                self.vy = 5
                
        if (self.x + self.size/2 - obj.x) ** 2 + (self.y + self.size/2 - obj.y) ** 2 < self.r ** 2:
            if obj.x - self.x < 0:
                self.vx =  5
            elif obj.x - self.x > 0:
                self.vx = -5
                
            if obj.y - self.y < 0:
                self.vy = 5
            elif obj.y - self.y > 0:
                self.vy = -5
            
        if self.x + self.vx + self.size < self.WIDTH and self.x + self.vx > 0:
                self.x += self.vx
        if self.y + self.vy + self.size < self.HEIGHT and self.y + self.vy > 0:
                self.y += self.vy
        
    def fire(self, shells, obj):  
        '''
        Firing into the player
        Return list of shells
        '''
        if obj.x - self.x - self.size/2 == 0:
            if obj.y > self.y + self.size/2:
                self.an = math.asin(1)
            else:
                self.an = math.asin(1) + np.pi
        elif obj.x - self.x > 0:
            self.an = math.atan((obj.y - self.y - self.size/2) / (obj.x - self.x - self.size/2))
        elif obj.x - self.x - self.size/2 < 0:
            self.an = math.atan((obj.y - self.y - self.size/2) / (obj.x - self.x - self.size/2)) + np.pi
            
        new_shell = Shell(self.screen, self.x + self.size/2, self.y + self.size/2)
        new_shell.vx = self.power * math.cos(self.an) // 2
        new_shell.vy = self.power * math.sin(self.an) // 2
        shells.append(new_shell)
        return shells     
        

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
    
    '''
    def get_pos(self):
        return (self.x - 32, self.y - 32, self.x + 32, self.y + 32)
    '''
        
