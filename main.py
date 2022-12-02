import tkinter
from tkinter.filedialog import *
from Player import *
from Enemy import *


import pygame


pygame.init()

WIDTH = 600
HEIGHT = 600


FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

shells = []


status = True
enemy = Enemy(screen)
player = Player(screen)


while (status):
    del_shells = []
    screen.fill('WHITE')
    for shell in shells:
        shell.draw()
    player.draw()
    player.move()
    enemy.draw()
    pygame.display.update()
    clock.tick(FPS)
    if (player.x - enemy.x) ** 2 + (player.y - enemy.y) ** 2 <= enemy.R ** 2:
        enemy.move_near_player(player)
        if enemy.stamina == 100:
            shells = enemy.fire(shells, player)
            enemy.stamina -= 1
        elif enemy.stamina < 100 and enemy.stamina > 0:
            enemy.stamina -= 1
        elif enemy.stamina <= 0:
            enemy.stamina = 100
    else:
        enemy.move_far_from_player()
    
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
    for i in range(len(shells)):
        sh = shells[i]
        sh.move()
        if sh.hittest(player) and player.live:
            pygame.display.update()
            screen.fill('WHITE')
            #text_score_1 = text.render('score: ' + str(sum_score), True, (139, 0, 255))
            #screen.blit(text_score_1, (20, 30))
            #text_score_2 = text.render('Вы уничтожили цель за ' + str(bullet) + " выстрелов", True, (0, 214, 120))
            #screen.blit(text_score_2, (250, 250))
            #pygame.display.update()
            #clock.tick(1)
            #player.live = 0
            #target.hit()
        if sh.live < 0:
            del_shells.append(i)
    for i in del_shells:
        shells.pop(i)  
    
pygame.quit()
    