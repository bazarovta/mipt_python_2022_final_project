import pygame
import time
#from pyvidplayer import Video

def draw(screen, image, WIDTH, HEIGHT, balance):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.blit(image[0], (0, 0))
    screen.blit(image[1], (200, 200))
    screen.blit(image[2], (500, 200))
    screen.blit(image[3], (800, 200))
    balance_font = pygame.font.SysFont("comicsansms", 35)
    balance_draw = balance_font.render("Your balance: " + str(balance), True, (255, 255, 0))
    screen.blit(balance_draw, (0, 0))

def wind_2(screen):
    image = pygame.image.load("market/wind_2_van_gogh.jpg")
    screen.fill((255, 255, 204))
    screen.blit(image, (425, 79))
    pygame.display.update()
    time.sleep(3)

def wind_3(screen):
    vid = Video("market/video.mp4")
    vid.set_size((1200, 600))
    start = time.time()
    while True:
        vid.draw(screen, (0, 0))
        pygame.display.update()
        if time.time() - start > 0.5:
            break
    time.sleep(1)


pygame.quit()
def main(balance):   
    WIDTH = 1200
    HEIGHT = 600
    
    image = []
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    image.append(pygame.image.load("market/fon.png"))
    image[0] = pygame.transform.scale(image[0], (WIDTH, HEIGHT))
    image.append(pygame.image.load("market/music.jpg"))
    image[1] = pygame.transform.scale(image[1], (200, 150))
    image.append(pygame.image.load("market/painting.jpg"))
    image[2] = pygame.transform.scale(image[2], (200, 150))
    image.append(pygame.image.load("market/wind_3_albert.jpg"))
    image[3] = pygame.transform.scale(image[3], (200, 150))
    
    buys = [False, False, False]

    finished = False

    while not finished:
        
        price = [30, 30, 30]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] > 200 and event.pos[1] < 350:
                    if event.pos[0] > 200 and event.pos[0] < 400:
                        if balance >= price[0]:
                            buys[0] = True
                            balance -= price[0]
                    elif event.pos[0] > 500 and event.pos[0] < 700:
                        if balance >= price[1]:
                            buys[1] = True
                            wind_2(screen)
                            balance -= price[1]
                    elif event.pos[0] > 800 and event.pos[0] < 1000:
                        if balance >= price[2]:
                            buys[2] = True
                            wind_3(screen)
                            balance -= price[2]

        draw(screen, image, WIDTH, HEIGHT, balance)
        pygame.display.update()
        
    return (balance, buys)





