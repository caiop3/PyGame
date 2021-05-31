import pygame
import random

pygame.init()

WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paraquedista')
y_imagem_de_fundo= 0
y_imagem_de_fundo1= HEIGHT

image = pygame.image.load('Referencia/sky3.png').convert()
image = pygame.transform.scale(image, (500, 400))

parachute_img = pygame.image.load('Referencia/parachute.png').convert_alpha()
parachute_img = pygame.transform.scale(parachute_img, (120, 120))

eagle1_img = pygame.image.load('Referencia/eagle2.png').convert_alpha()
eagle1_img = pygame.transform.scale(eagle1_img, (50, 50))

eagle2_img = pygame.image.load('Referencia/eagle.png').convert_alpha()
eagle2_img = pygame.transform.scale(eagle2_img, (50, 50))

class Eagle1(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = -50
        self.rect.y = random.randint(200, 300)
        self.speed_x = random.randint(2, 6)
        self.speed_y = random.randint(-7, -1)
    
    def update(self):

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top > 400 or self.rect.left > 500:
            self.rect.x = -50
            self.rect.y = random.randint(200, 300)
            self.speed_x = random.randint(2, 6)
            self.speed_y = random.randint(-7, -1)

class Eagle2(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = random.randint(200, 300)
        self.speed_x = random.randint(2, 6)
        self.speed_y = random.randint(-7, -1)
    
    def update(self):

        self.rect.x -= self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top > 400 or self.rect.right < -50:
            self.rect.x = 550
            self.rect.y = random.randint(200, 300)
            self.speed_x = random.randint(2, 6)
            self.speed_y = random.randint(-7, -1)

game = True

clock = pygame.time.Clock()
FPS = 30

eagle1 = Eagle1(eagle1_img)
eagle2 = Eagle2(eagle2_img)



while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    eagle1.update()
    eagle2.update()

    window.fill((0, 0, 0)) 
    window.blit(image, (0,y_imagem_de_fundo))
    window.blit(image, (0,y_imagem_de_fundo1)) 
    #window.blit(image, (0, 0))    
    window.blit(parachute_img, (210, 30))
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


    pygame.display.update()  

pygame.quit()




