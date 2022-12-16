import quest_hide as quest_3
import quest_speed as quest_2
import fight as quest_1
import market
import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
image = pygame.image.load("menu/fon.jpg")
image = pygame.transform.scale(image, (WIDTH, HEIGHT))
image_q1 = pygame.image.load("quest_1/fon.png")
image_q1 = pygame.transform.scale(image_q1, (200, 150))
image_q2 = pygame.image.load("quest_2/fon.jpg")
image_q2 = pygame.transform.scale(image_q2, (200, 150))
image_q3 = pygame.image.load("quest_3/fon.jpg")
image_q3 = pygame.transform.scale(image_q3, (200, 150))
image_m = pygame.image.load("market/fon_s.png")
image_m = pygame.transform.scale(image_m, (200, 150))

balance = 0
music = False

def draw():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.blit(image, (0, 0))
    screen.blit(image_q1, (200, 200))
    screen.blit(image_q2, (500, 200))
    screen.blit(image_q3, (800, 200))
    screen.blit(image_m, (500, 400))
    balance_font = pygame.font.SysFont("comicsansms", 35)
    balance_draw = balance_font.render("Your balance: " + str(balance),
                                        True, (255, 255, 0))
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
                    res = quest_1.main()
                    draw()
                elif event.pos[0] > 500 and event.pos[0] < 700:
                    res = quest_2.main(music)
                    music = False
                    draw()
                elif event.pos[0] > 800 and event.pos[0] < 1000:
                    res = quest_3.main()
                    draw()
            if ((event.pos[1] > 400 and event.pos[1] < 550) 
            and (event.pos[0] > 500 and event.pos[0] < 700)):
                market_return = market.main(balance)
                balance = market_return[0]
                music = market_return[1]

    if res == True:
        balance += 100
    
    draw()
    pygame.display.update()
    
pygame.quit()





