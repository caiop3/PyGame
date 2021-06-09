import pygame
import os
from data import WIDTH, HEIGHT, IMG_DIR, FPS, INIT, GAME, QUIT

def final_screen(screen):

    clock = pygame.time.Clock()

    final_screen = pygame.image.load(os.path.join(IMG_DIR, 'sky_fim.png')).convert()
    final_screen = pygame.transform.scale(final_screen, (WIDTH, HEIGHT))

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
        
        screen.blit(final_screen, (0,0))

        pygame.display.flip()
    
    return state
