import pygame
import os
from data import BALLOON_WIDTH, BALLOON_HEIGHT, EAGLE1_WIDTH, EAGLE1_HEIGHT, EAGLE2_WIDTH, EAGLE2_HEIGHT, COVID_WIDTH, COVID_HEIGHT, GEL_WIDTH, GEL_HEIGHT, IMG_DIR

IMAGE = 'image'
BALLOON_IMG = 'balloon_img'
BALLOON_IMG = 'balloon_img'
EAGLE1_IMG = 'eagle1_img'
EAGLE1_IMG = 'eagle1_img'
EAGLE2_IMG = 'eagle2_img'
EAGLE2_IMG = 'eagle2_img'
COVID_IMG = 'covid_img'
COVID_IMG = 'covid_img'
GEL_IMG = 'gel_img'
GEL_IMG = 'gel_img'
SCORE_FONT = 'score_font'
LIFE_FONT = 'life_font'
LIVES_FONT = 'lives_font'
MUSIC = 'music'
BOOM_SOUND = 'boom_sound'
POP_SOUND = 'pop_sound'
PLAYER_SHEET = 'player_sheet'

def load_assets():
    assets = {}
    assets[IMAGE] = pygame.image.load(os.path.join(IMG_DIR, 'sky3.png')).convert()
    assets[BALLOON_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'balloon.png')).convert_alpha()
    assets[BALLOON_IMG] = pygame.transform.scale(assets['balloon_img'], (BALLOON_WIDTH, BALLOON_HEIGHT))
    assets[EAGLE1_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'eagle2.png')).convert_alpha()
    assets[EAGLE1_IMG] = pygame.transform.scale(assets['eagle1_img'], (EAGLE1_WIDTH, EAGLE1_HEIGHT))
    assets[EAGLE2_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'eagle.png')).convert_alpha()
    assets[EAGLE2_IMG] = pygame.transform.scale(assets['eagle2_img'], (EAGLE2_WIDTH, EAGLE2_HEIGHT))
    assets[COVID_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'covid.png')).convert_alpha()
    assets[COVID_IMG] = pygame.transform.scale(assets['covid_img'], (COVID_WIDTH, COVID_HEIGHT)) 
    assets[GEL_IMG ] = pygame.image.load(os.path.join(IMG_DIR, 'gel.png')).convert_alpha()
    assets[GEL_IMG ] = pygame.transform.scale(assets['gel_img'], (GEL_WIDTH, GEL_HEIGHT)) 
    # --- Importa fontes
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(IMG_DIR, 'baloni.ttf'), 38)
    assets[LIFE_FONT] = pygame.font.Font(os.path.join(IMG_DIR, 'baloni.ttf'), 13)
    assets[LIVES_FONT] = pygame.font.Font(os.path.join(IMG_DIR, 'arcade.ttf'), 28)
    # --- Importa o som de fundo
    pygame.mixer.music.load(os.path.join(IMG_DIR, 'musica.mp3'))
    assets[MUSIC] = pygame.mixer.music
    assets[BOOM_SOUND] = pygame.mixer.Sound(os.path.join(IMG_DIR, 'boom.flac'))
    assets[POP_SOUND] = pygame.mixer.Sound(os.path.join(IMG_DIR, 'pop.ogg'))
    # --- Arquivo para animação
    assets[PLAYER_SHEET] = pygame.image.load(os.path.join(IMG_DIR, 'ex.png')).convert_alpha()
    return assets