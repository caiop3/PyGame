import pygame
from random import *
from reference import COVID_IMG, BALLOON_IMG, GEL_IMG, EAGLE1_IMG, EAGLE2_IMG, POP_SOUND
from data import WIDTH, HEIGHT, STILL

# --- Cria a classe do balão, que será movimentado pelo jogador
class Balao(pygame.sprite.Sprite):
    """ Seta o balão"""
    def __init__(self,groups,assets,lives):
        """Recebe e define dados iniciais do balão""" 
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
        """Atualiza a posição do balão e o mantém dentro da tela"""
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            
    def shoot(self):
        """ Álcool em gel criado logo abaixo do balão"""
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.shot

        if elapsed_ticks > self.shot_tick:
            self.shot = now
            gel = Gel(self.assets, self.rect.bottom, self.rect.centerx)
            self.groups['all_sprites'].add(gel)
            self.groups['gels'].add(gel)
            self.assets['pop_sound'].play()

# --- Cria classe para a vida do balão, que se movimenta em função do balão
class Life(pygame.sprite.Sprite):
    """Seta a vida do balão"""
    def __init__(self, balao, assets):
        """Recebe e define dados iniciais da vida do balão""" 
        pygame.sprite.Sprite.__init__(self)

        self.balao = balao
        self.assets = assets
        life = self.assets['life_font'].render('{:04d}'.format(self.balao.lives), True, (255, 255, 0))
        self.image = life
        self.rect = self.image.get_rect()
        self.rect.centerx = self.balao.rect.centerx
        self.rect.bottom =  self.balao.rect.bottom - 47
    
    def update(self):
        """Atualiza a posição da vida do balão de acordo com a posição do balão"""

        life = self.assets['life_font'].render('{:04d}'.format(self.balao.lives), True, (255, 255, 0))
        self.image = life
        self.rect = self.image.get_rect()
        self.rect.centerx = self.balao.rect.centerx
        self.rect.bottom = self.balao.rect.bottom - 47

# --- Cria as classes das águias, uma para cada águia dependendo do lado da tela em que surge        
class Eagle1(pygame.sprite.Sprite):
    """Seta as águias que surgirão do lado esquerdo da tela"""
    def __init__(self, assets):
        """Recebe e define os dados iniciais dessas águias"""
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[EAGLE1_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -50
        self.rect.y = randint(200, 400)
        self.speed_x = randint(2, 6)
        self.speed_y = randint(-7, 7)
    
    def update(self):
        """Atualiza a posição dessas águias"""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top > 600 or self.rect.left > 900:
            self.rect.x = -50
            self.rect.y = randint(200, 400)
            self.speed_x = randint(2, 6)
            self.speed_y = randint(-7, 7)

class Eagle2(pygame.sprite.Sprite):
    """Seta as águias que surgirão do lado direito da tela"""
    def __init__(self, assets):
        """Recebe e define os dados iniciais dessas águias"""
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[EAGLE2_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 950
        self.rect.y = randint(200, 400)
        self.speed_x = randint(2, 6)
        self.speed_y = randint(-7, 7)
    
    def update(self):
        """Atualiza a posição dessas águias"""
        self.rect.x -= self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top > 600 or self.rect.right < -50:
            self.rect.x = 950
            self.rect.y = randint(200, 400)
            self.speed_x = randint(2, 6)
            self.speed_y = randint(-7, 7)

# --- Cria a classe Covid, pensada como uma maneira do jogador interagir melhor com o jogo
class Covid(pygame.sprite.Sprite):
    """ Seta a(s) covid(es)"""
    def __init__(self, assets):
        """Recebe e define dados iniciais da covid""" 
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[COVID_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = randint(60, 520)
        self.rect.y = choice([800, 1000, 1200])
        self.speed_y = randint(1, 3)

    def update(self):
        """Atualiza a posição da covid"""
        self.rect.y -= self.speed_y 

        if self.rect.top < -850:
            self.rect.x = randint(60, 520)
            self.rect.y = choice([800, 1000, 1200])
            self.speed_y = randint(1, 3)

# --- Cria classe para o gel, que pode matar o covid 
class Gel(pygame.sprite.Sprite):
    """Seta gotas de álcool em gel"""
    def __init__(self, assets, bottom, centerx):
        """Recebe e define os dados iniciais dessas gotas"""
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[GEL_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = 10  

    def update(self):
        """Atualiza a posição dessas"""
        self.rect.y += self.speedy

def load_spritesheet(spritesheet, rows, columns):
    """Função que recebe um spritesheet e retorna os sprites que serão utilizados numa animação"""
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    
    sprites = []
    for row in range(rows):
        for column in range(columns):
            x = column * sprite_width
            y = row * sprite_height
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites

# --- Classe da explosão do balão, que também representa a sua animação 
class Player(pygame.sprite.Sprite):
    """Seta uma ou várias animações"""
    def __init__(self, center, player_sheet):
        """Recebe um spritesheet para a confecção da animação""" 
        pygame.sprite.Sprite.__init__(self)
        
        player_sheet = pygame.transform.scale(player_sheet, (640, 640))
        spritesheet = load_spritesheet(player_sheet, 8, 5)
        self.animations = {STILL: spritesheet[0:39]}
        self.state = STILL
        self.animation = self.animations[self.state]
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 30
        
    def update(self):
        """Atualiza posição e frames da animação"""
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            self.animation = self.animations[self.state]
            
            if self.frame == len(self.animation):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.animation[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
