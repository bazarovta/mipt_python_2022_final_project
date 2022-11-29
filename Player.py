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
class Player:
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
        
    '''
    
    def __init__(self, screen):
        self.screen = screen
        self.x = 300
        self.y = 300
        self.stamina = 100.
        self.health = 100.
        self.orientation = 'down' 
        self.attack = False 
        self.weapon = 'sword'
        self.surface = image['down']
    def move(self, event):
        if event.key == pygame.K_d:
            self.orientation = 'right'
            self.x += 10
        elif event.key == pygame.K_a:
            self.orientation = 'left'
            self.x -= 10
        elif event.key == pygame.K_s:
            self.orientation = 'down'
            self.y += 10
        elif event.key == pygame.K_w:
            self.orientation = 'up'
            self.y -= 10

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
 
pygame.init()
X = 600
Y = 600
screen = pygame.display.set_mode((X, Y))
status = True
player = Player(screen)
while (status):
    screen.fill('WHITE')
    player.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        elif event.type == pygame.KEYDOWN:
            player.move(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.attack = True
        elif event.type == pygame.MOUSEBUTTONUP:
            player.attack = False
    
    pygame.display.update()
 

