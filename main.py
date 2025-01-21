import pygame

# Inicializace pygame
pygame.init()

# Nastavení obrazovky

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CLIKER GAME")

# Hlavní cyklus
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False




# Ukončení pygame
pygame.QUIT