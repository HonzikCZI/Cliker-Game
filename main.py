import pygame

# Inicializace pygame
pygame.init()

# Nastavení obrazovky

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CLIKER GAME")

# Nestavení hry
fps = 120
coin = 0
cena_klikání = 50
klikání = 1
#cena_autoclicku = 500 - možná bude ve hře

# Barvy
black = (0, 0, 0)
white = (255, 255, 255)

# Fonty 
big_font = pygame.font.Font("fonts/Emulogic.ttf", 50)
midle_font = pygame.font.Font("fonts/Emulogic.ttf", 30)

# Obrazky
pozadí = pygame.image.load("img/obrazek.png")
pozadí = pygame.transform.scale(pozadí, (width, height))
pozadí_rect = pozadí.get_rect()
pozadí_rect.topleft = (0, 0)

myš = pygame.image.load("img/mouse.png")
myš = pygame.transform.scale(myš, (100, 100))
myš_rect = myš.get_rect()  
myš_rect.center = (width//2, height//2)

# Texty
coin_text = midle_font.render(f"coins: {coin}", True, black)
coin_text_rect = coin_text.get_rect()
coin_text_rect.topleft = (10, 10)

# Frame rate control
clock = pygame.time.Clock()

# Hlavní cyklus
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # obrázky
    screen.blit(pozadí, pozadí_rect)
    screen.blit(myš, myš_rect)

    # Update text
    coin_text = midle_font.render(f"coins: {coin}", True, black)
    
    # texty
    screen.blit(coin_text, coin_text_rect)
    
    # update obrazovky
    pygame.display.update()

    # Control frame rate
    clock.tick(fps)

# Ukončení pygame
pygame.quit()