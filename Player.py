import pygame

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



class Player:
    '''
    Class Player
    var:
        screen; x,y --- player location; stamina; health; 
        orientation --- show where he looking(up right down left);
        attack --- show his condition(True - attack, False - peace);
        weapon --- type of weapon(sword, ...)
    method:
        move --- change player coordinates;
        vector_of_attack --- return coordinates of line along which he make damage
                           and power of hit;
        attacking_on_enemy --- player attacks enemies
        draw - draw a player;
        
    '''
    
    
    def __init__(self, screen, x=450, y=450):
        self.screen = screen

        self.x = x
        self.y = y

        self.health = 100
        self.orientation = 'down'
        self.stamina  = 100
        self.attack = False 
        self.weapon = 'sword'
        self.surface = image['down']
        self.v = 50
        self.r = 32
        #self.cond = False


    def move(self, keys, dt=0.2):
        cond = False

        if keys[pygame.K_d]:
           self.orientation = 'right'
           cond = True
        elif keys[pygame.K_a]:
            self.orientation = 'left'
            cond = True
        elif keys[pygame.K_s]:
            self.orientation = 'down'
            cond = True
        elif keys[pygame.K_w]:
            self.orientation = 'up'
            cond = True

        if cond == True:
            self.x += self.v * movement[self.orientation][0] * dt
            self.y += self.v * movement[self.orientation][1] * dt


    def vector_of_attack(self):
        start = [self.x, self.y]
        end = [0, 0]

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
        im = image[self.orientation]
        self.screen.blit(im, (self.x - 32, self.y - 32))

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
    
    
    def attack_on_enemy(self, obj):
        if self.attack == True:
            start, end, power = self.vector_of_attack()
            if ((obj.x >= start[0] and obj.x <= end[0] and obj.y <= start[1] and obj.y + obj.size >= start[1]) or 
                (obj.x + obj.size <= start[0] and obj.x + obj.size >= end[0] and obj.y <= start[1] and obj.y + obj.size >= start[1]) or 
                (obj.y >= start[1] and obj.y <= end[1] and obj.x <= start[0] and obj.x + obj.size >= start[0]) or 
                (obj.y + obj.size <= start[1] and obj.y + obj.size >= end[1] and obj.x <= start[0] and obj.x + obj.size >= start[0])):
                obj.health -= 10
    
    def get_pos(self):
        return (self.x - 32, self.y - 32, self.x + 32, self.y + 32)
