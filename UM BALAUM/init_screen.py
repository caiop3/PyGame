# --- Importações
import pygame
import os
from data import WIDTH, HEIGHT, IMG_DIR, FPS, INIT, GAME, QUIT, START

# --- Tela de início
def init_screen(screen):

    clock = pygame.time.Clock()

    init_screen = pygame.image.load(os.path.join(IMG_DIR, 'sky_capa.png')).convert()
    init_screen = pygame.transform.scale(init_screen, (WIDTH, HEIGHT))
    
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
                    state = START
                    start = False
        
        screen.blit(init_screen, (0,0))

        pygame.display.flip()
    
    return state






