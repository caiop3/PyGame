import pygame
from random import *
from reference import COVID_IMG, BALLOON_IMG, GEL_IMG, EAGLE1_IMG, EAGLE2_IMG, POP_SOUND
from data import WIDTH, HEIGHT, STILL
# --- Cria a classe Covid
class Covid(pygame.sprite.Sprite):
    def __init__(self, assets):
            
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[COVID_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        # self.rect.x = -1000
        # self.rect.y = randint(80, 380)
        # self.speed_x = 5
        self.rect.x = randint(60, 420)
        self.rect.y = choice([800, 1000, 1200])
        self.speed_y = randint(6, 6)

    def update(self):

        self.rect.y -= self.speed_y 

        if self.rect.top < -850:
            self.rect.x = randint(60, 420)
            self.rect.y = choice([800, 1000, 1200])
            self.speed_y = randint(4, 6)

# --- Cria a classe do balão, que será movimentado pelo jogador
class Balao(pygame.sprite.Sprite):
    def __init__(self,groups,assets,lives):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets[BALLOON_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2 
        self.rect.bottom = HEIGHT / 2 
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
        self.lives = lives

        self.shot = pygame.time.get_ticks()
        self.shot_tick = 200

    def update(self):
        # Atualiza da posição do balão
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            
    def shoot(self):
        # A nova bala vai ser criada logo embaixo e no centro do balão
        now = pygame.time.get_ticks()

        elapsed_ticks = now - self.shot

        if elapsed_ticks > self.shot_tick:
            self.shot = now
            # A nova bala vai ser criada logo embaixo e no centro do balão
            gel = Gel(self.assets, self.rect.bottom, self.rect.centerx)
            self.groups['all_sprites'].add(gel)
            self.groups['gels'].add(gel)
            self.assets['pop_sound'].play()

class Life(pygame.sprite.Sprite):
    def __init__(self, balao, assets):

        pygame.sprite.Sprite.__init__(self)

        self.balao = balao
        self.assets = assets
        life = self.assets['life_font'].render('{:04d}'.format(self.balao.lives), True, (255, 255, 0))
        self.image = life
        self.rect = self.image.get_rect()
        self.rect.centerx = self.balao.rect.centerx
        self.rect.bottom =  self.balao.rect.bottom - 47
    
    def update(self):

        life = self.assets['life_font'].render('{:04d}'.format(self.balao.lives), True, (255, 255, 0))
        self.image = life
        self.rect = self.image.get_rect()
        self.rect.centerx = self.balao.rect.centerx
        self.rect.bottom = self.balao.rect.bottom - 47

# --- Cria as classes das águias, uma para cada águia dependendo do lado da tela em que surge        
class Eagle1(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[EAGLE1_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -50
        self.rect.y = randint(200, 300)
        self.speed_x = randint(2, 6)
        self.speed_y = randint(-7, 4)
    
    def update(self):

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top > 400 or self.rect.left > 500:
            self.rect.x = -50
            self.rect.y = randint(200, 300)
            self.speed_x = randint(2, 6)
            self.speed_y = randint(-7, 4)

class Eagle2(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[EAGLE2_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = randint(200, 300)
        self.speed_x = randint(2, 6)
        self.speed_y = randint(-7, 4)
    
    def update(self):

        self.rect.x -= self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top > 400 or self.rect.right < -50:
            self.rect.x = 550
            self.rect.y = randint(200, 300)
            self.speed_x = randint(2, 6)
            self.speed_y = randint(-7, 4)

# --- Cria classe para o gel, que pode matar o covid 
class Gel(pygame.sprite.Sprite):
    def __init__(self, assets, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[GEL_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = 10  # Velocidade fixa para cima

    def update(self):
        self.rect.y += self.speedy

def load_spritesheet(spritesheet, rows, columns):
    # Calcula a largura e altura de cada sprite.
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    
    # Percorre todos os sprites adicionando em uma lista.
    sprites = []
    for row in range(rows):
        for column in range(columns):
            # Calcula posição do sprite atual
            x = column * sprite_width
            y = row * sprite_height
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            # Cria uma imagem vazia do tamanho do sprite
            image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites

# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, center, player_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        player_sheet = pygame.transform.scale(player_sheet, (640, 640))

        # Define sequências de sprites de cada animação
        spritesheet = load_spritesheet(player_sheet, 8, 5)
        self.animations = {STILL: spritesheet[0:39]}
        # Define estado atual (que define qual animação deve ser mostrada)
        self.state = STILL
        # Define animação atual
        self.animation = self.animations[self.state]
        # Inicializa o primeiro quadro da animação
        self.frame = 0
        self.image = self.animation[self.frame]
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect.center = center
        # Centraliza na tela.
        # self.rect.centerx = WIDTH / 2
        # self.rect.centery = HEIGHT / 2

        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 30
        
    # Metodo que atualiza a posição do personagem
    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Atualiza animação atual
            self.animation = self.animations[self.state]
            
            if self.frame == len(self.animation):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.animation[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center