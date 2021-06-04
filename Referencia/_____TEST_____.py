import pygame
import random

pygame.init()

WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paraquedista')

y_imagem_de_fundo = 0
y_imagem_de_fundo1 = HEIGHT

image = pygame.image.load('Referencia/sky3.png').convert()
image = pygame.transform.scale(image, (500, 400))

parachute_img = pygame.image.load('Referencia/balloon.png').convert_alpha()
parachute_img = pygame.transform.scale(parachute_img, (70, 90))

eagle1_img = pygame.image.load('Referencia/eagle2.png').convert_alpha()
eagle1_img = pygame.transform.scale(eagle1_img, (50, 50))

eagle2_img = pygame.image.load('Referencia/eagle.png').convert_alpha()
eagle2_img = pygame.transform.scale(eagle2_img, (50, 50))

pygame.mixer.music.load('Referencia/musica.mp3')
pygame.mixer.music.play()

class Balloon(pygame.sprite.Sprite):
    def __init__(self,img):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2 
        self.rect.bottom = HEIGHT / 2 
        self.speedx = 0
        self.speedy = 0

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

# Lista das colisões
Vida = 3

# Criando um grupo para cada obstáculo
all_sprites = pygame.sprite.Group()
all_eagles = pygame.sprite.Group()

# Criando o jogador
balloon = Balloon(parachute_img)
all_sprites.add(balloon)

#criando all_eagles
eagle1 = Eagle1(eagle1_img)
eagle2 = Eagle2(eagle2_img)

for i in range(2):
    eagle1 = Eagle1(eagle1_img)
    eagle2 = Eagle2(eagle2_img)
    all_eagles.add(eagle1)
    all_eagles.add(eagle2)
    all_sprites.add(eagle1)
    all_sprites.add(eagle2)

game = True

clock = pygame.time.Clock()
FPS = 30

while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                balloon.speedx -= 5
            if event.key == pygame.K_RIGHT:
                balloon.speedx += 5
            if event.key == pygame.K_UP:
                balloon.speedy -= 3.5
            if event.key == pygame.K_DOWN:
                balloon.speedy += 3.5
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                balloon.speedx += 5
            if event.key == pygame.K_RIGHT:
                balloon.speedx -= 5
            if event.key == pygame.K_UP:
                balloon.speedy += 3.5
            if event.key == pygame.K_DOWN:
                balloon.speedy -= 3.5

    all_sprites.update()
    # all_eagles.update()

    # Tratamento de colisões
    colisao1 = pygame.sprite.spritecollide(balloon, all_eagles, True)  
    if len(colisao1) > 0:
        balloon.kill()
        game = False

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



