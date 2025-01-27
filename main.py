import pygame

# Inicializace pygame
pygame.init()

# Nastavení obrazovky
width = 1920
height = 1080
fullscreen = True
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("CLIKER GAME")

# Nastavení hry
fps = 120
coin = 0
cena_klikani = 50
klikani = 1
krater = 2
cena_autoclicku = 500 

# Barvy
black = (0, 0, 0)
white = (255, 255, 255)

# Fonty 
big_font = pygame.font.Font("fonts/Emulogic.ttf", 50)
midle_font = pygame.font.Font("fonts/Emulogic.ttf", 30)
small_font = pygame.font.Font("fonts/Emulogic.ttf",15)

# Obrazky
pozadi = pygame.image.load("img/obrazek.png")
pozadi = pygame.transform.scale(pozadi, (width, height))
pozadi_rect = pozadi.get_rect()
pozadi_rect.topleft = (0, 0)

mys = pygame.image.load("img/mouse.png")
mys = pygame.transform.scale(mys, (200, 200))
mys_rect = mys.get_rect()  
mys_rect.center = (width//2, height//2)

obchodnik_1 = pygame.image.load("img/Terminal.png")
obchodnik_1 = pygame.transform.scale(obchodnik_1, (128, 128))
obchodnik_1_rect = obchodnik_1.get_rect()
obchodnik_1_rect.topright = (width-20, 20)

obchodnik_2 = pygame.image.load("img/Terminal.png")
obchodnik_2 = pygame.transform.scale(obchodnik_1, (128, 128))
obchodnik_2_rect = obchodnik_1.get_rect()
obchodnik_2_rect.topright = (width-20, 140)

# Texty
coin_text = midle_font.render(f"coins: {coin}", True, black)
coin_text_rect = coin_text.get_rect()
coin_text_rect.topleft = (10, 10)

my_mane = small_font.render("By HonzikCZI", True, black)
my_mane_rect = my_mane.get_rect()
my_mane_rect.topleft = (10, height-20)

obchodnik_text = small_font.render(f"{cena_klikani} Coin", True, black)
obchodnik_text_rect = obchodnik_text.get_rect()
obchodnik_text_rect.topright = (width-33, 125)

klikani_text = small_font.render(f"X{klikani}", True, white)
klikani_text_rect = klikani_text.get_rect()
klikani_text_rect.topright=(width-80,80)

obchodnik_text2 = small_font.render(f"{cena_autoclicku} Coin", True, black)
obchodnik_text_rect2 = obchodnik_text.get_rect()
obchodnik_text_rect2.topright = (width-33, 245)

per_second_text = small_font.render("10", True, white)
per_second_text_rect = per_second_text.get_rect()
per_second_text_rect.topright = (width-80, 200)

# Frame rate control
clock = pygame.time.Clock()

# zvuky
click_sound = pygame.mixer.Sound("songs/click_sound.mp3")
pygame.mixer.music.load("songs/music_pozadi.mp3")
pygame.mixer.music.set_volume(0.5)
click_sound.set_volume(0.4)

####################
# Hlavní smyčka hry#
####################
running = True
pygame.mixer.music.play(-1, 0.0)
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

        # Check for mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = event.pos

            # Bylo kliknuto na myš
            if mys_rect.collidepoint(click_x, click_y):
                coin += 1*klikani 
                click_sound.play()

            if obchodnik_1_rect.collidepoint(click_x, click_y):
                if coin >= cena_klikani:
                    click_sound.play()
                    coin -= cena_klikani
                    cena_klikani *= krater
                    cena_klikani -= cena_klikani // 3
                    klikani += 1


    # obrázky
    screen.blit(pozadi, pozadi_rect)
    screen.blit(mys, mys_rect)
    screen.blit(obchodnik_1, obchodnik_1_rect)
    screen.blit(obchodnik_2, obchodnik_2_rect)

    # Update text
    coin_text = midle_font.render(f"Coins: {coin}", True, black)
    timeText = midle_font.render(f"Time: {pygame.time.get_ticks()//1000}", True, black)
    obchodnik_text = small_font.render(f"$ {cena_klikani}", True, black)
    klikani_text = small_font.render(f"X{klikani+1}", True, white)
    obchodnik_text2 = small_font.render(f"$ {cena_autoclicku}", True, black)
    
    # texty
    screen.blit(coin_text, coin_text_rect)
    screen.blit(timeText, (10, 50))
    screen.blit(my_mane, my_mane_rect)
    screen.blit(obchodnik_text, obchodnik_text_rect)
    screen.blit(klikani_text, klikani_text_rect)
    screen.blit(obchodnik_text2, obchodnik_text_rect2)
    screen.blit(per_second_text, per_second_text_rect)

    
    # update obrazovky
    pygame.display.update()

    # Control frame rate
    clock.tick(fps)

# Ukončení pygame
pygame.quit()