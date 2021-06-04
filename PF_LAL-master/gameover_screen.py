import pygame
from config import FPS, BLACK, Points, PLAYING, DONE
from assets import load_assets

def gameover_screen (window): 
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega os assets
    assets = load_assets()
    # ===== Loop principal =====
    gameover = True
    while gameover:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
                gameover = False

            if event.type == pygame.KEYUP:
                state = PLAYING
                Points[0] = 0
                Points[1] = 0
                gameover = False

        #atualiza a tela
        window.fill(BLACK)  
        window.blit(assets['gameover'], assets['gameover_rect'])
        pygame.display.flip()
    return state