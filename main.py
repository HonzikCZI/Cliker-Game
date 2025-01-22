import pygame

# Inicializace pygame
pygame.init()

# Nastavení obrazovky
width = 1280
height = 720
fullscreen = True
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("CLIKER GAME")

# Nastavení hry
fps = 120
coin = 0
cena_klikani = 50
klikani = 1
#cena_autoclicku = 500 - možná bude ve hře

# Barvy
black = (0, 0, 0)
white = (255, 255, 255)

# Fonty 
big_font = pygame.font.Font("fonts/Emulogic.ttf", 50)
midle_font = pygame.font.Font("fonts/Emulogic.ttf", 30)

# Obrazky
pozadi = pygame.image.load("img/obrazek.png")
pozadi = pygame.transform.scale(pozadi, (width, height))
pozadi_rect = pozadi.get_rect()
pozadi_rect.topleft = (0, 0)

mys = pygame.image.load("img/mouse.png")
mys = pygame.transform.scale(mys, (100, 100))
mys_rect = mys.get_rect()  
mys_rect.center = (width//2, height//2)

# Texty
coin_text = midle_font.render(f"coins: {coin}", True, black)
coin_text_rect = coin_text.get_rect()
coin_text_rect.topleft = (10, 10)

# Frame rate control
clock = pygame.time.Clock()

# Hlavní smyčka hry
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F10:
                running = False
            elif event.key == pygame.K_F5:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((width, height))

    # obrázky
    screen.blit(pozadi, pozadi_rect)
    screen.blit(mys, mys_rect)

    # Update text
    coin_text = midle_font.render(f"coins: {coin}", True, black)
    timeText= midle_font.render(f"Time: {pygame.time.get_ticks()//1000}", True, black)
    
    # texty
    screen.blit(coin_text, coin_text_rect)
    screen.blit(timeText, (10, 50))
    
    # update obrazovky
    pygame.display.update()

    # Control frame rate
    clock.tick(fps)

# Ukončení pygame
pygame.quit()