import pygame


def draw(screen, image, WIDTH, HEIGHT, balance):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.blit(image[0], (0, 0))
    screen.blit(image[1], (200, 200))
    screen.blit(image[2], (500, 200))
    screen.blit(image[3], (800, 200))
    balance_font = pygame.font.SysFont("comicsansms", 35)
    balance_draw = balance_font.render("Your balance: " + str(balance), True, (255, 255, 0))
    screen.blit(balance_draw, (0, 0))

def main(balance):   
    WIDTH = 1200
    HEIGHT = 600
    
    image = []
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    image.append(pygame.image.load("market/fon.png"))
    image[0] = pygame.transform.scale(image[0], (WIDTH, HEIGHT))
    image.append(pygame.image.load("quest_1/fon.png"))
    image[1] = pygame.transform.scale(image[1], (200, 150))
    image.append(pygame.image.load("quest_2/fon.jpg"))
    image[2] = pygame.transform.scale(image[2], (200, 150))
    image.append(pygame.image.load("quest_3/fon.jpg"))
    image[3] = pygame.transform.scale(image[3], (200, 150))
    
    
    finished = False
    
    while not finished:
        
        price = [1, 1, 1]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] > 200 and event.pos[1] < 350:
                    if event.pos[0] > 200 and event.pos[0] < 400:
                        if balance >= price[0]:
                            #что-нибудь 0
                            balance -= price[0]
                    elif event.pos[0] > 500 and event.pos[0] < 700:
                        if balance >= price[1]:
                            #что-нибудь 1
                            balance -= price[1]
                    elif event.pos[0] > 800 and event.pos[0] < 1000:
                        if balance >= price[2]:
                            #что-нибудь 2
                            balance -= price[2]

        draw(screen, image, WIDTH, HEIGHT, balance)
        pygame.display.update()
        
    return balance





