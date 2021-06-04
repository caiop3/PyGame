import pygame
from config import FPS, BLACK, DONE, PLAYING
from assets import load_assets

def init_screen (window): 
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega os asssets
    assets = load_assets()
    # ===== Loop principal =====
    inicio = True
    while inicio:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
                inicio = False

            if event.type == pygame.KEYUP:
                state = PLAYING
                inicio = False

        #atualiza a tela
        window.fill(BLACK) 
        window.blit(assets['inicio'], assets['inicio_rect'])
        pygame.display.flip()  
    return state

