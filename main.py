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
    
    player.draw()
    player.move()
    enemy.draw()
    pygame.display.update()
    clock.tick(FPS)
    if (player.x - enemy.x) ** 2 + (player.y - enemy.y) ** 2 <= enemy.R ** 2:
        enemy.move_near_player(player)
        
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
    
    
    