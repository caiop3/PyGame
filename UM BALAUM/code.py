# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from data import WIDTH, HEIGHT, INIT, GAME, QUIT, OVER
from init_screen import init_screen
from game_screen import game_screen
from final_screen import final_screen

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('UM BALAUM')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == OVER:
        state = final_screen(window)
    else:
        state = QUIT
 
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados