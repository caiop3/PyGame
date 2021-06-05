# ===== INÍCIO =====
# --- Importações e pacotes do pygame  
import pygame
import random
import time
from os import path

img_dir = path.join(path.dirname(__file__), 'Efeitos')

pygame.init()

# --- Tela principal
WIDTH = 500
HEIGHT = 400
move_image_1 = 0
move_image_2 = HEIGHT
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paraquedista')

# --- Importa imagem de fundo e os ícones
assets = {}

assets['image'] = pygame.image.load('Efeitos/sky3.png').convert()
assets['image'] = pygame.transform.scale(assets['image'], (500, 400))

assets['balloon_img'] = pygame.image.load('Efeitos/balloon.png').convert_alpha()
assets['balloon_img'] = pygame.transform.scale(assets['balloon_img'], (40, 50))

assets['eagle1_img'] = pygame.image.load('Efeitos/eagle2.png').convert_alpha()
assets['eagle1_img'] = pygame.transform.scale(assets['eagle1_img'], (10, 10))

assets['eagle2_img'] = pygame.image.load('Efeitos/eagle.png').convert_alpha()
assets['eagle2_img'] = pygame.transform.scale(assets['eagle2_img'], (10, 10))

assets['covid_img'] = pygame.image.load('Efeitos/covid.png').convert_alpha()
assets['covid_img'] = pygame.transform.scale(assets['covid_img'], (20, 20))

assets['gel_img'] = pygame.image.load('Efeitos/gel.png').convert_alpha()
assets['gel_img'] = pygame.transform.scale(assets['gel_img'], (20, 20))

# --- Importa o som de fundo
pygame.mixer.music.load('Efeitos/musica.mp3')
pygame.mixer.music.play()
boom_sound = pygame.mixer.Sound('Efeitos/boom.flac')
pop_sound = pygame.mixer.Sound('Efeitos/pop.ogg')

# --- Cria a classe Covid
class Covid(pygame.sprite.Sprite):
    def __init__(self, assets):
            
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['covid_img']
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = random.randint(80, 380)
        self.speed_x = 5

    def update(self):

        self.rect.x += self.speed_x

        if self.rect.right > 1000:
            self.rect.x = -100
            self.rect.y = random.randint(200, 300)
            self.speed_x = 5

# --- Cria a classe do balão, que será movimentado pelo jogador
class Balao(pygame.sprite.Sprite):
    def __init__(self,groups,assets):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets['balloon_img']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2 
        self.rect.bottom = HEIGHT / 2 
        self.speedx = 0
        self.speedy = 0
        self.all_sprites = all_sprites
        self.gels = gels
        self.groups = groups
        self.assets = assets

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
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        gel = Gel(self.assets, self.rect.bottom, self.rect.centerx)
        self.groups['all_sprites'].add(gel)
        self.groups['gels'].add(gel)
        pop_sound.play()

# --- Cria as classes das águias, uma para cada águia dependendo do lado da tela em que surge        
class Eagle1(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['eagle1_img']
        self.rect = self.image.get_rect()
        self.rect.x = -50
        self.rect.y = random.randint(200, 300)
        self.speed_x = random.randint(2, 6)
        self.speed_y = random.randint(-7, 4)
    
    def update(self):

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top > 400 or self.rect.left > 500:
            self.rect.x = -50
            self.rect.y = random.randint(200, 300)
            self.speed_x = random.randint(2, 6)
            self.speed_y = random.randint(-7, 4)

class Eagle2(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['eagle2_img']
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = random.randint(200, 300)
        self.speed_x = random.randint(2, 6)
        self.speed_y = random.randint(-7, 4)
    
    def update(self):

        self.rect.x -= self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top > 400 or self.rect.right < -50:
            self.rect.x = 550
            self.rect.y = random.randint(200, 300)
            self.speed_x = random.randint(2, 6)
            self.speed_y = random.randint(-7, 4)

# --- Cria classe para o gel, que pode matar o covid 
class Gel(pygame.sprite.Sprite):
    def __init__(self, assets, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['gel_img']
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
STILL = 0
# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, player_sheet):
        
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
        
        # Centraliza na tela.
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2

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
            # Reinicia a animação caso o índice da imagem atual seja inválido
            # if self.frame >= len(self.animation):
            #     self.frame = 0
            
            # Armazena a posição do centro da imagem
            center = self.rect.center
            # Atualiza imagem atual
            self.image = self.animation[self.frame]
            # Atualiza os detalhes de posicionamento
            self.rect = self.image.get_rect()
            self.rect.center = center

# --- Cria um grupo de sprites geral e para cada obstáculo
all_sprites = pygame.sprite.Group()
aguias = pygame.sprite.Group()
covides = pygame.sprite.Group()
gels = pygame.sprite.Group()

groups = {}
groups['all_sprites'] = all_sprites
groups['aguias'] = aguias
groups['covides'] = covides
groups['gels'] = gels

# --- Cria o jogador (balão)
balao = Balao(groups, assets)
all_sprites.add(balao)

# --- Cria as covides
covid = Covid(assets)
all_sprites.add(covid)
covides.add(covid)

# --- Cria as águias e suas quantidades 
for i in range(8):
    eagle1 = Eagle1(assets)
    eagle2 = Eagle2(assets)
    all_sprites.add(eagle1)
    all_sprites.add(eagle2)
    aguias.add(eagle1)
    aguias.add(eagle2)

game = True

# --- Variável para o ajuste da velocidade
clock = pygame.time.Clock()
FPS = 25

player_sheet = pygame.image.load(path.join(img_dir, 'ex.png')).convert_alpha()

# ===== LOOP PRRINCIPAL =====    
while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla
        if event.type == pygame.KEYDOWN: # Dependendo da tecla, altera a velocidade
            if event.key == pygame.K_LEFT:
                balao.speedx -= 5
            if event.key == pygame.K_RIGHT:
                balao.speedx += 5
            if event.key == pygame.K_UP:
                balao.speedy -= 3.5
            if event.key == pygame.K_DOWN:
                balao.speedy += 3.5
            if event.key == pygame.K_SPACE: # Atira álcool em gel
                balao.shoot()
        # Verifica se soltou alguma tecla
        if event.type == pygame.KEYUP: # Dependendo da tecla, altera a velocidade
            if event.key == pygame.K_LEFT:
                balao.speedx += 5
            if event.key == pygame.K_RIGHT:
                balao.speedx -= 5
            if event.key == pygame.K_UP:
                balao.speedy += 3.5
            if event.key == pygame.K_DOWN:
                balao.speedy -= 3.5

    # --- Atualiza os sprites
    all_sprites.update()
    #aguias.update()

    # --- Trata colisões
    colisao1 = pygame.sprite.spritecollide(balao, aguias, True)
    for aguia in colisao1:
        m = Eagle1(assets)
        all_sprites.add(m)
        aguias.add(m)  
    
        balao.kill()
        player = Player(player_sheet)
        all_sprites.add(player)
        boom_sound.play()
        pygame.mixer.music.stop()
        # game = False
        # time.sleep(2)
    
    colisao2 = pygame.sprite.spritecollide(balao, aguias, True)
    for aguia in colisao2:
        m = Eagle2(assets)
        all_sprites.add(m) 
        aguias.add(m)

        balao.kill()
        player = Player(player_sheet)
        all_sprites.add(player)
        boom_sound.play()
        pygame.mixer.music.stop()
        # game = False
        # time.sleep(2)
    
    colisao3 = pygame.sprite.spritecollide(balao, covides, True)
    for covid in colisao3:
        m = Covid(assets)
        all_sprites.add(m)
        covides.add(m)

    vida = 10
    colisao4 = pygame.sprite.spritecollide(covid, gels, True)
    if len(colisao4) > 0:
        vida -= 1
        if vida == 0:
            covid.kill()
            m = Covid(assets)
            all_sprites.add(m)
            covides.add(m)
            vida = 10  
    
    # --- Saídas
    window.fill((0, 0, 0)) # Preenche com a cor branca
    window.blit(assets['image'], (0,move_image_1)) 
    window.blit(assets['image'], (0,move_image_2)) 
    # window.blit(eagle1.image, eagle1.rect)
    # window.blit(eagle2.image, eagle2.rect)

    # Muda as posições da imagem de fundo
    move_image_1 -= 2
    move_image_2 -= 2

    # Plota novamente após sair da tela
    if move_image_2 <= -HEIGHT:
        move_image_2 = HEIGHT
    if move_image_1 <= -HEIGHT:
        move_image_1 = HEIGHT

    # Desenha todos os sprites
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== FINALIZAÇÃO =====
pygame.quit()  # Finaliza os recursos utilizados



