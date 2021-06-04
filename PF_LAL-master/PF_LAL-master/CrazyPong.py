import pygame
from config import WIDTH, HEIGHT, START, PLAYING, DONE, GAMEOVER
from init_screen import init_screen
from game_screen import game_screen
from gameover_screen import gameover_screen

#inicia o mixer e a tela do pygame
pygame.init()
pygame.mixer.init()

#Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CrazyPong')

state = START
while state != DONE:
    if state == START:
        state = init_screen(window) #tela de inicio
    elif state == PLAYING:
        state = game_screen(window) #tela do jogo
    elif state == GAMEOVER:
        state = gameover_screen(window) #tela de gameover
    else:
        state = DONE
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

