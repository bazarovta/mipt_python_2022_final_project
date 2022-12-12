import pygame
import time
import agent
import Player
import math

class Hero(Player.Player):
    
    def draw(self):
        pygame.draw.circle(
                self.screen,
                (0, 255, 255),
                (self.x, self.y),
                10
                )
    def move(self, blocks, keys):
        c = False
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        flag = False
        for pos in blocks:
            if self.y > pos[1] * 50 and self.y < pos[1] * 50 + 50:
                if self.x + 15 - pos[0] * 50 < 50 and self.x + 15 - pos[0] * 50 > 0:
                    flag1 = True
                    flag = True
                elif self.x - 15 - pos[0] * 50 < 50 and self.x - 15 - pos[0] * 50 > 0:
                    flag2 = True
                    flag = True
            if self.x > pos[0] * 50 and self.x < pos[0] * 50 + 50:
                if self.y + 15 - pos[1] * 50  < 50 and self.y + 15 - pos[1] * 50 > 0:
                    flag3 = True
                    flag = True
                elif pos[1] * 50 + 50 - (self.y-15) < 50 and pos[1] * 50 + 50 - (self.y-15) > 0:
                    flag4 = True
                    flag = True
        if flag1 and keys[pygame.K_a]:
            self.x -= 5
        if flag2 and keys[pygame.K_d]:
            self.x += 5
        if flag3 and keys[pygame.K_w]:
            self.y -= 5
        if flag4 and keys[pygame.K_s]:
            self.y += 5
        if flag == False:
            super().move(keys, 0.1)

def create_chart():
    chart = [ 
      'bbbbbbbbbbbbbbbbbb',
      'b****************b',
      'b****************b',
      'b****b********b**b',
      'b****bbbbbbbbbb**b',
      'b****b*****b*****b',
      'b****b*****b*****b',
      'b****************b',
      'bbbbbb****bbbbbbbb',
      'b****************b',
      'b****************b',
      'b**bbb****bbbbbbbb',
      'b****b***********b',
      'b****b***********b',
      'b**bbbbbbb***bbbbb',
      'b****************b',
      'b****************b',
      'bbbbbbbbbbbbbbbbbb'
      ]
    blocks = []
    for y, line in enumerate(chart):
        for x, obj in enumerate(line):
            if obj == 'b':
                blocks.append((x, y))
    return blocks

def draw_chart(screen, blocks):
    
    for pos in blocks:
        pygame.draw.polygon(
                screen,
                (155, 76, 0),
                [(pos[0]*50, pos[1]*50),
                 (pos[0]*50+50, pos[1]*50),
                 (pos[0]*50+50, pos[1]*50+50),
                 (pos[0]*50, pos[1]*50+50)]
        )
  
    pygame.display.update()
    
def game_loop(screen, blocks, agents, player):
    clock = pygame.time.Clock()
    FPS = 30
    finished = True
    lose = True
    while finished:
        clock.tick(FPS)
        screen.fill((255,255,255))
        draw_chart(screen, blocks)
        pressed_keys = pygame.key.get_pressed()
        player.move(blocks, pressed_keys)
        player.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = False
        for obj in agents:
            dist = ((player.x - obj.x)**2 + (player.y - obj.y)**2)**0.5
            if player.x == obj.x:
                if player.y < obj.y:
                    angle = -math.pi / 2
                else:
                    angle = math.pi / 2
            elif player.x > obj.x:
                angle = -math.atan((player.y - obj.y)/(player.x - obj.x))
            else:
                angle = math.pi - math.atan((player.y - obj.y)/(player.x - obj.x))
            if (dist < obj.r and angle > obj.direction - obj.angle 
                and angle < obj.direction + obj.angle):
                lose = False
                finished = False
        for obj in agents:
            obj.move()
            obj.draw()
        pygame.display.update()
    return lose

def main():
    pygame.init()
    blocks = create_chart()
    WIDTH = 900
    HEIGHT = 900
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    first_font = pygame.font.SysFont("comicsansms", 35)
    first_page = first_font.render("Press Space", True, (255, 0, 0))
    image = pygame.image.load("quest_3/fon.jpg")
    first_image = pygame.transform.scale(image, (900, 900))
    screen.blit(first_image, (0,0))
    screen.blit(first_page, (350, 350))
    pygame.display.update()
    pygame.event.clear()
    agents = [agent.Agent(screen, 150, 300, 20, ('x', 100, 200)),
             agent.Agent(screen, 700, 350, 20, ('y', 325, 375)),
             agent.Agent(screen, 600, 820, 20, ('x', 550, 650)),
             agent.Agent(screen, 150, 650, 20, ('x', 125, 175))]
    player = Hero(screen, 100, 800)
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                break
    check = game_loop(screen, blocks, agents, player)
    while check != True:
        player.x = 100
        player.y = 800
        second_page = first_font.render("Failed", True, (255, 0, 0))
        screen.blit(first_image, (0,0))
        screen.blit(second_page, (700, 400))
        pygame.display.update()
        time.sleep(2)
        check = game_loop(screen, blocks, agents, player )

