import quest_hide as quest_3
import quest_speed as quest_2
#import main as quest_1
import pygame

pygame.init()
balance = 0
WIDTH = 1200
HEIGHT = 800
image = pygame.image.load("menu/fon.jpg")
image = pygame.transform.scale(image, (WIDTH, HEIGHT))
image_q1 = pygame.image.load("quest_1/fon.png")
image_q1 = pygame.transform.scale(image_q1, (200, 150))
image_q2 = pygame.image.load("quest_2/fon.jpg")
image_q2 = pygame.transform.scale(image_q2, (200, 150))
image_q3 = pygame.image.load("quest_3/fon.jpg")
image_q3 = pygame.transform.scale(image_q3, (200, 150))

def draw():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.blit(image, (0, 0))
    screen.blit(image_q1, (200, 200))
    screen.blit(image_q2, (500, 200))
    screen.blit(image_q3, (800, 200))
    balance_font = pygame.font.SysFont("comicsansms", 35)
    balance_draw = balance_font.render("Your balance: " + str(balance), True, (255, 255, 0))
    screen.blit(balance_draw, (0, 0))
finished = True
draw()
while finished:
    res = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] > 200 and event.pos[1] < 350:
                if event.pos[0] > 200 and event.pos[0] < 400:
                    #quest_1.main()
                    continue
                elif event.pos[0] > 500 and event.pos[0] < 700:
                    res = quest_2.main()
                    draw()
                elif event.pos[0] > 800 and event.pos[0] < 1000:
                    res = quest_3.main()
                    draw()
    if res == True:
        balance += 100
    draw()
    pygame.display.update()




