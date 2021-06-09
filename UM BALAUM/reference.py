import pygame
import os
from data import WIDTH, HEIGHT, BALLOON_WIDTH, BALLOON_HEIGHT, EAGLE1_WIDTH, EAGLE1_HEIGHT, EAGLE2_WIDTH, EAGLE2_HEIGHT, COVID_WIDTH, COVID_HEIGHT, GEL_WIDTH, GEL_HEIGHT, IMG_DIR

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
EAGLE_SOUND = 'eagle_sound'
BACOV_SOUND = 'bacov_sound'
GECOV_SOUND = 'gecov_sound'
LEVEL_UP_SOUND = 'level_up_sound'
PLAYER_SHEET = 'player_sheet'

def load_assets():
    assets = {}
    assets[IMAGE] = pygame.image.load(os.path.join(IMG_DIR, 'sky3.png')).convert()
    assets[IMAGE] = pygame.transform.scale(assets[IMAGE], (WIDTH, HEIGHT))
    assets[BALLOON_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'balloon.png')).convert_alpha()
    assets[BALLOON_IMG] = pygame.transform.scale(assets[BALLOON_IMG], (BALLOON_WIDTH, BALLOON_HEIGHT))
    assets[EAGLE1_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'eagle2.png')).convert_alpha()
    assets[EAGLE1_IMG] = pygame.transform.scale(assets[EAGLE1_IMG], (EAGLE1_WIDTH, EAGLE1_HEIGHT))
    assets[EAGLE2_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'eagle.png')).convert_alpha()
    assets[EAGLE2_IMG] = pygame.transform.scale(assets[EAGLE2_IMG], (EAGLE2_WIDTH, EAGLE2_HEIGHT))
    assets[COVID_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'covid.png')).convert_alpha()
    assets[COVID_IMG] = pygame.transform.scale(assets[COVID_IMG], (COVID_WIDTH, COVID_HEIGHT)) 
    assets[GEL_IMG ] = pygame.image.load(os.path.join(IMG_DIR, 'gel.png')).convert_alpha()
    assets[GEL_IMG ] = pygame.transform.scale(assets[GEL_IMG ], (GEL_WIDTH, GEL_HEIGHT)) 
    # --- Importa fontes
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(IMG_DIR, 'baloni.ttf'), 38)
    assets[LIFE_FONT] = pygame.font.Font(os.path.join(IMG_DIR, 'baloni.ttf'), 13)
    assets[LIVES_FONT] = pygame.font.Font(os.path.join(IMG_DIR, 'arcade.ttf'), 28)
    # --- Importa o som de fundo
    pygame.mixer.music.load(os.path.join(IMG_DIR, 'musica.mp3'))
    assets[MUSIC] = pygame.mixer.music
    assets[BOOM_SOUND] = pygame.mixer.Sound(os.path.join(IMG_DIR, 'boom.flac'))
    assets[POP_SOUND] = pygame.mixer.Sound(os.path.join(IMG_DIR, 'pop.ogg'))
    assets[EAGLE_SOUND] = pygame.mixer.Sound(os.path.join(IMG_DIR, 'es.wav'))
    assets[EAGLE_SOUND].set_volume(0.2)
    assets[BACOV_SOUND] = pygame.mixer.Sound(os.path.join(IMG_DIR, 'contam.wav'))
    assets[BACOV_SOUND].set_volume(0.2)
    assets[GECOV_SOUND] = pygame.mixer.Sound(os.path.join(IMG_DIR, '1up.mp3'))
    assets[LEVEL_UP_SOUND] = pygame.mixer.Sound(os.path.join(IMG_DIR, 'level_up.wav'))
    assets[LEVEL_UP_SOUND].set_volume(0.2)
    # --- Arquivo para animação
    assets[PLAYER_SHEET] = pygame.image.load(os.path.join(IMG_DIR, 'ex.png')).convert_alpha()
    return assets