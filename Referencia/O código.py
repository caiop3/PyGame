import pygame
import random

pygame.init()

WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paraquedista')

y_imagem_de_fundo = 0
y_imagem_de_fundo1 = HEIGHT

image = pygame.image.load('Efeitos/sky3.png').convert()
image = pygame.transform.scale(image, (500, 400))

balloon_img = pygame.image.load('Efeitos/balloon.png').convert_alpha()
balloon_img = pygame.transform.scale(balloon_img, (40, 50))

eagle1_img = pygame.image.load('Efeitos/eagle2.png').convert_alpha()
eagle1_img = pygame.transform.scale(eagle1_img, (10, 10))

eagle2_img = pygame.image.load('Efeitos/eagle.png').convert_alpha()
eagle2_img = pygame.transform.scale(eagle2_img, (10, 10))

covid_img = pygame.image.load('Efeitos/covid.png').convert_alpha()
covid_img = pygame.transform.scale(covid_img, (20, 20))

# covid_img2 = pygame.image.load('Efeitos/covid2.png').convert_alpha()
# covid_img2 = pygame.transform.scale(covid_img2, (25, 25))
# covid_img3 = pygame.image.load('Efeitos/covid3.png').convert_alpha()
# covid_img3 = pygame.transform.scale(covid_img3, (25, 25))

gel_img = pygame.image.load('Efeitos/gel.png').convert_alpha()
gel_img = pygame.transform.scale(gel_img, (35, 35))

pygame.mixer.music.load('Efeitos/musica.mp3')
pygame.mixer.music.play()

class Covid(pygame.sprite.Sprite):
    def __init__(self, img):
            
        pygame.sprite.Sprite.__init__(self)

        self.image = img
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

class Balao(pygame.sprite.Sprite):
    def __init__(self,img,all_sprites,all_gels,gel_img):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2 
        self.rect.bottom = HEIGHT / 2 
        self.speedx = 0
        self.speedy = 0
        self.all_sprites = all_sprites
        self.all_gels = all_gels
        self.gel_img = gel_img

    def update(self):
        # Atualização da posição da nave
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
        gel = Gel(self.gel_img, self.rect.bottom, self.rect.centerx)
        self.all_sprites.add(gel)
        self.all_gels.add(gel)
        
class Eagle1(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
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
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
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

class Gel(pygame.sprite.Sprite):
    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = 10  # Velocidade fixa para cima

    def update(self):
        self.rect.y += self.speedy

# Criando um grupo para cada obstáculo
all_sprites = pygame.sprite.Group()
aguias = pygame.sprite.Group()
covides = pygame.sprite.Group()
all_gels = pygame.sprite.Group()

# Criando o jogador
balao = Balao(balloon_img, all_sprites, all_gels, gel_img)
all_sprites.add(balao)

covid = Covid(covid_img)
all_sprites.add(covid)
covides.add(covid)

game = True

clock = pygame.time.Clock()
FPS = 30

for i in range(10):
    eagle1 = Eagle1(eagle1_img)
    eagle2 = Eagle2(eagle2_img)
    all_sprites.add(eagle1)
    all_sprites.add(eagle2)
    aguias.add(eagle1)
    aguias.add(eagle2)
    
while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                balao.speedx -= 5
            if event.key == pygame.K_RIGHT:
                balao.speedx += 5
            if event.key == pygame.K_UP:
                balao.speedy -= 3.5
            if event.key == pygame.K_DOWN:
                balao.speedy += 3.5
            if event.key == pygame.K_SPACE:
                balao.shoot()
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                balao.speedx += 5
            if event.key == pygame.K_RIGHT:
                balao.speedx -= 5
            if event.key == pygame.K_UP:
                balao.speedy += 3.5
            if event.key == pygame.K_DOWN:
                balao.speedy -= 3.5

    all_sprites.update()
    # aguias.update()

    # Tratamento de colisões
    colisao1 = pygame.sprite.spritecollide(balao, aguias, True)
    for aguia in colisao1:
        m = Eagle1(eagle1_img)
        all_sprites.add(m)
        aguias.add(m)    
        balao.kill()
        game = False
    
    colisao2 = pygame.sprite.spritecollide(balao, aguias, True)
    for aguia in colisao2:
        m = Eagle2(eagle1_img)
        all_sprites.add(m) 
        aguias.add(m)   
        balao.kill()
        game = False
    
    colisao3 = pygame.sprite.spritecollide(balao, covides, True)
    for covid in colisao3:
        m = Covid(covid_img)
        all_sprites.add(m)
        covides.add(m)
    vida = 10
    colisao4 = pygame.sprite.spritecollide(covid, all_gels, True)
    if len(colisao4) > 0:
        vida -= 1
        if vida == 0:
            covid.kill()
            m = Covid(covid_img)
            all_sprites.add(m)
            covides.add(m)
            vida = 10  
           
    window.fill((0, 0, 0)) 
    window.blit(image, (0,y_imagem_de_fundo))
    window.blit(image, (0,y_imagem_de_fundo1)) 
    window.blit(eagle1.image, eagle1.rect)
    window.blit(eagle2.image, eagle2.rect)

    # Mudando as posições da imagem de fundo:
    y_imagem_de_fundo -= 2
    y_imagem_de_fundo1 -= 2

    # plotar novamente após sair da tela
    if y_imagem_de_fundo1 <= -HEIGHT:
        y_imagem_de_fundo1= HEIGHT

    if y_imagem_de_fundo <= -HEIGHT:
        y_imagem_de_fundo= HEIGHT

    all_sprites.draw(window)
    pygame.display.update()  

pygame.quit()

