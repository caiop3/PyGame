import pygame
from config import WIDTH, HEIGHT, espaço_da_tela
from assets import load_assets

# Carrega os asssets
assets = load_assets()

class Player(pygame.sprite.Sprite): 
    def __init__(self, img, player):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        if player == 1:
            self.rect.left = espaço_da_tela
        if player == 2:
            self.rect.right = WIDTH - espaço_da_tela
        self.rect.centery = HEIGHT/2
        self.speedy = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.y += self.speedy
        # Mantem dentro da tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Ball(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2 
        self.speedy = 0

    def update(self):
        # Atualizando a posição da bola
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se a bola toca no teto ou no fundo, ela inverte a velocidade
        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.speedy *= -1