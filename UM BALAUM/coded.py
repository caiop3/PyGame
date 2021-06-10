# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import time
from data import WIDTH, HEIGHT, INIT, GAME, QUIT, OVER, PASS, START, WIN
from init_screen import init_screen
from game_screen import game_screen
from final_screen import final_screen, win_screen
from start_screen import start_screen, start2_screen

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('UM BALAUM')

# --- Loop principal da máquina de estados
fase = 1
state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == START:
        state = start_screen(window)
        state = start2_screen(window)
    elif state == GAME:
        state = game_screen(window, fase)
        if state == PASS:
            fase += 1
            state = GAME
    elif state == WIN:
        fase = 1
        state = win_screen(window)
    elif state == OVER:
        fase = 1
        state = final_screen(window)
    else:
        state = QUIT
 
# ===== Finalização =====
pygame.quit() 