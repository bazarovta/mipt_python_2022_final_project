import pygame
import time
import agent
import Player 

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
                (255, 255, 0),
                [(pos[0]*50, pos[1]*50),
                 (pos[0]*50+50, pos[1]*50),
                 (pos[0]*50+50, pos[1]*50+50),
                 (pos[0]*50, pos[1]*50+50)]
        )
  
    pygame.display.update()
    
def game_loop(screen, blocks, agents, player):
    clock = pygame.time.Clock()
    FPS = 10
    finished = True
    while finished:
        clock.tick(FPS)
        screen.fill((255,255,255))
        player.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = False
        player.move(pygame.key.get_pressed())
        for obj in agents:
            obj.move()
            obj.draw()
        draw_chart(screen, blocks)
        pygame.display.update()

def main():
    blocks = create_chart()
    WIDTH = 900
    HEIGHT = 900
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    agents = [agent.Agent(screen, 150, 300, 20, ('x', 100, 200)),
             agent.Agent(screen, 600, 400, 20, ('y', 350, 450))]
    player = Player.Player(screen, 32, 900-32)
    game_loop(screen, blocks, agents, player)

main()
pygame.quit()
