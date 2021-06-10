# --- Importações
import pygame
import time
import os
from data import WIDTH, HEIGHT, IMG_DIR, FPS, INIT, GAME, QUIT, START

# --- Tela de contexto do jogo
def start_screen(screen):

    clock = pygame.time.Clock()

    start_screen = pygame.image.load(os.path.join(IMG_DIR, 'sky_context.png')).convert()
    start_screen = pygame.transform.scale(start_screen, (WIDTH, HEIGHT))

    start = True
    while start:

        clock.tick(FPS)

        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                start = False
                return state

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    start = False
        
        screen.blit(start_screen, (0,0))

        pygame.display.flip()

# --- Tela de instruções
def start2_screen(screen):

    clock = pygame.time.Clock()

    start2_screen = pygame.image.load(os.path.join(IMG_DIR, 'sky_rules.png')).convert()
    start2_screen = pygame.transform.scale(start2_screen, (WIDTH, HEIGHT))

    start = True
    while start:

        clock.tick(FPS)

        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                start = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    state = GAME
                    start = False
        
        screen.blit(start2_screen, (0,0))

        pygame.display.flip()
    
    return state