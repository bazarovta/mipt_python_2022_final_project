import tkinter
from tkinter.filedialog import *
from Player import *
from Enemy import *

import random

import pygame


pygame.init()

WIDTH = 800
HEIGHT = 600


FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
text = pygame.font.Font(None, 50)
text_data = pygame.font.Font(None, 30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

shells = []


status = True

#N = random.randint(1, 4)
N = 2

enemies = []

for i in range(N):
    enemies.append(Enemy(screen))


player = Player(screen)


while (status):
    del_shells = []
    del_enemies = []
    screen.fill('WHITE')
    for shell in shells:
        shell.draw()
    player.draw()
    player.move()
    for enemy in enemies:
        enemy.draw()
    text_health_player = text_data.render(str(player.health), True, (0, 255, 0))
    screen.blit(text_health_player, (20, 30))
    for i in range(len(enemies)):
        enemy = enemies[i]
        text_health_enemy = text_data.render(str(enemy.health), True, (255, 0, 0))
        screen.blit(text_health_enemy, (30 + 60 * (i + 1), 30))
    pygame.display.update()
    clock.tick(FPS)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        elif event.type == pygame.KEYDOWN:
            player.move_on()
            player.take_orientation(event)
        elif event.type == pygame.KEYUP:
            player.move_off()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.attack = True
            for enemy in enemies:
                player.attack_on_enemy(enemy)
        elif event.type == pygame.MOUSEBUTTONUP:
            player.attack = False
            
        
    for i in range(len(enemies)):
        enemy = enemies[i]
        if (player.x - enemy.x - enemy.size/2) ** 2 + (player.y - enemy.y - enemy.size/2) ** 2 <= enemy.R ** 2:
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
        if enemy.health <= 0:
            del_enemies.append(i) 
    for i in range(len(del_enemies)):
        enemies.pop(i)
        
    for j in range(len(shells)):
        sh = shells[j]
        sh.move()
        if sh.hittest(player) and player.health > 0 and sh.live > 0:
            player.health -= 1
            sh.live = 0
        elif player.health <= 0:
            screen.fill('RED')
            text_score_2 = text.render('GAME OVER', True, (0, 0, 0))
            screen.blit(text_score_2, (WIDTH / 2 - 105, HEIGHT / 2 - 50))
            pygame.display.update()
            while status:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        status = False
        if sh.live < 0 and status:
            del_shells.append(j)
    for j in range(len(del_shells)):
        shells.pop(j)   
             
    if player.health > 0 and len(enemies) <= 0:
        screen.fill('GREEN')
        text_score_2 = text.render('YOU WIN', True, (0, 0, 0))
        screen.blit(text_score_2, (WIDTH / 2 - 100, HEIGHT / 2 - 50))
        pygame.display.update()
        while status:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    status = False

pygame.quit()
    