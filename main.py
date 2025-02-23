import pygame

# Inicializace pygame
pygame.init()

# Nastavení obrazovky
screen_width = 1920
screen_height = 1080
is_fullscreen = False

if is_fullscreen:
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("CLIKER GAME")

# Nastavení hry
fps = 60
coins = 0
click_upgrade_cost = 50
click_power = 1
click_multiplier = 2
autoclicker_cost = 200
deltaTime = 0
autoclicker_coins = 0
autoclicker_multiplier = 2
autoclicker_krater = 2
nasobitel = 10
odpocet = 0

# Barvy
black = (0, 0, 0)
white = (255, 255, 255)

# Fonty 
big_font = pygame.font.Font("fonts/Emulogic.ttf", 50)
middle_font = pygame.font.Font("fonts/Emulogic.ttf", 30)
small_font = pygame.font.Font("fonts/Emulogic.ttf", 15)

# Obrazky
background_image = pygame.image.load("img/obrazek.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

mouse_image = pygame.image.load("img/mouse.png")
mouse_image = pygame.transform.scale(mouse_image, (200, 200))
mouse_rect = mouse_image.get_rect()  
mouse_rect.center = (screen_width // 2, screen_height // 2)

click_upgrade_image = pygame.image.load("img/Terminal.png")
click_upgrade_image = pygame.transform.scale(click_upgrade_image, (128, 128))
click_upgrade_rect = click_upgrade_image.get_rect()
click_upgrade_rect.topright = (screen_width - 20, 20)

autoclicker_image = pygame.image.load("img/Terminal.png")
autoclicker_image = pygame.transform.scale(autoclicker_image, (128, 128))
autoclicker_rect = autoclicker_image.get_rect()
autoclicker_rect.topright = (screen_width - 20, 140)

# Texty
coins_text = middle_font.render(f"Coins: {coins}", True, black)
coins_text_rect = coins_text.get_rect()
coins_text_rect.topleft = (10, 10)

author_text = small_font.render("By HonzikCZI", True, black)
author_text_rect = author_text.get_rect()
author_text_rect.topleft = (10, screen_height - 20)

click_upgrade_text = small_font.render(f"{click_upgrade_cost} Coins", True, black)
click_upgrade_text_rect = click_upgrade_text.get_rect()
click_upgrade_text_rect.topright = (screen_width - 33, 125)

click_power_text = small_font.render(f"X{click_power}", True, white)
click_power_text_rect = click_power_text.get_rect()
click_power_text_rect.topright = (screen_width - 80, 80)

autoclicker_text = small_font.render(f"{autoclicker_cost} Coins", True, black)
autoclicker_text_rect = autoclicker_text.get_rect()
autoclicker_text_rect.topright = (screen_width - 33, 245)

per_second_text = small_font.render(f"{nasobitel}", True, white)
per_second_text_rect = per_second_text.get_rect()
per_second_text_rect.topright = (screen_width - 80, 200)

per_second = middle_font.render(f"Per second: {autoclicker_coins}", True, black)
per_second_rect = per_second.get_rect()
per_second_rect.center = (screen_width //2, 50)

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
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen_width, screen_height))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = event.pos

            if mouse_rect.collidepoint(click_x, click_y):
                coins += 1 * click_power 
                click_sound.play()

            if click_upgrade_rect.collidepoint(click_x, click_y):
                if coins >= click_upgrade_cost:
                    click_sound.play()
                    coins -= click_upgrade_cost
                    click_upgrade_cost *= click_multiplier
                    click_upgrade_cost -= click_upgrade_cost // 3

            if autoclicker_rect.collidepoint(click_x, click_y):
                if coins >= autoclicker_cost:
                    click_sound.play()
                    coins -= autoclicker_cost
                    autoclicker_coins += nasobitel
                    odpocet += 1

                    if odpocet == 5:
                        nasobitel *= autoclicker_krater
                        odpocet = 0 

                    autoclicker_cost *= autoclicker_multiplier
                    autoclicker_cost -= autoclicker_cost // 3

    # per sec
    deltaTime += 1
    if deltaTime >= fps:
        deltaTime = 0
        coins += autoclicker_coins
        #print (deltaTime, autoclicker_coins)
        print (odpocet)
    

       

    # obrázky
    screen.blit(background_image, background_rect)
    screen.blit(mouse_image, mouse_rect)
    screen.blit(click_upgrade_image, click_upgrade_rect)
    screen.blit(autoclicker_image, autoclicker_rect)

    # Update text
    coins_text = middle_font.render(f"Coins: {coins}", True, black)
    time_text = middle_font.render(f"Time: {pygame.time.get_ticks() // 1000}", True, black)
    click_upgrade_text = small_font.render(f"$ {click_upgrade_cost}", True, black)
    click_power_text = small_font.render(f"X{click_power + 1}", True, white)
    autoclicker_text = small_font.render(f"$ {autoclicker_cost}", True, black)
    per_second = middle_font.render(f"Per second: {autoclicker_coins}", True, black)
    per_second_text = small_font.render(f"{nasobitel}", True, white)

    
    # texty
    screen.blit(coins_text, coins_text_rect)
    screen.blit(time_text, (10, 50))
    screen.blit(author_text, author_text_rect)
    screen.blit(click_upgrade_text, click_upgrade_text_rect)
    screen.blit(click_power_text, click_power_text_rect)
    screen.blit(autoclicker_text, autoclicker_text_rect)
    screen.blit(per_second_text, per_second_text_rect)
    screen.blit(per_second, per_second_rect)

    # update obrazovky
    pygame.display.update()

    # Control frame rate
    clock.tick(fps)

# Ukončení pygame
pygame.quit()