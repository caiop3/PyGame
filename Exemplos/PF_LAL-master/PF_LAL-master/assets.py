import pygame
import os
from config import  WIDTH, HEIGHT, ball_WIDTH, ball_HEIGHT, player_WIDTH, player_HEIGHT

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

def load_assets():
    assets = {}
    #carrega as telas
    assets['background'] = pygame.image.load(os.path.join('img/tela_terra.jpg')).convert()
    assets['background'] = pygame.transform.scale(assets['background'], (WIDTH,HEIGHT))
    assets['inicio'] = pygame.image.load(os.path.join('img/inicio.png')).convert()
    assets['inicio'] = pygame.transform.scale(assets['inicio'], (WIDTH,HEIGHT))
    assets['inicio_rect'] = assets['background'].get_rect()
    assets['gameover'] = pygame.image.load(os.path.join('img/gameover.png')).convert()
    assets['gameover'] = pygame.transform.scale(assets['gameover'], (WIDTH,HEIGHT))
    assets['gameover_rect'] = assets['background'].get_rect()
    #carrega os sprites
    assets['ball_img'] = pygame.image.load(os.path.join('img/fire_ball.png')).convert_alpha()
    assets['ball_img'] = pygame.transform.scale(assets['ball_img'], (ball_WIDTH, ball_HEIGHT))
    assets['player1_img'] = pygame.image.load(os.path.join('img/player1.png')).convert_alpha()
    assets['player1_img'] = pygame.transform.scale(assets['player1_img'], (player_WIDTH, player_HEIGHT))
    assets['player2_img'] = pygame.image.load(os.path.join('img/player2.png')).convert_alpha()
    assets['player2_img'] = pygame.transform.scale(assets['player2_img'], (player_WIDTH, player_HEIGHT))
    #carrega os sons do jogo
    pygame.mixer.music.load('snd/avicci.mp3')
    pygame.mixer.music.set_volume(0.5)
    assets['destroy_sound'] = pygame.mixer.Sound('snd/expl6.wav')
    assets['pew_sound'] = pygame.mixer.Sound('snd/pew.wav')
    return assets