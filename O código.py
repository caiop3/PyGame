import pygame
import random

pygame.init()

WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paraquedista')

image = pygame.image.load('C:/Users/caior/OneDrive/Documentos/Vs Code/PyGame/Referencia/montain.jpg').convert()
image = pygame.transform.scale(image, (500, 400))

parachute_img = pygame.image.load('C:/Users/caior/OneDrive/Documentos/Vs Code/PyGame/Referencia/parachute.png').convert_alpha()
parachute_img = pygame.transform.scale(parachute_img, (120, 120))

eagle_img = pygame.image.load('C:/Users/caior/OneDrive/Documentos/Vs Code/PyGame/Referencia/eagle.png').convert_alpha()
eagle_img = pygame.transform.scale(eagle_img, (50, 50))

eagle2_img = pygame.image.load('C:/Users/caior/OneDrive/Documentos/Vs Code/PyGame/Referencia/eagle2.png').convert_alpha()
eagle2_img = pygame.transform.scale(eagle2_img, (50, 50))

game = True

eagle_x = 550
eagle_y = random.randint(100, 300)
eagle_speed_x = random.randint(3, 6)
eagle_speed_y = random.randint(-2, 2)
eagle2_x = -50
eagle2_y = random.randint(100, 300)
eagle2_speed_x = random.randint(3, 7)
eagle2_speed_y = random.randint(-2, 2)

clock = pygame.time.Clock()
FPS = 30

while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    eagle_x -= eagle_speed_x
    eagle_y += eagle_speed_y 
    eagle2_x += eagle2_speed_x
    eagle2_y += eagle2_speed_y 

    if eagle_x < -50 or eagle_y > 450 or eagle_y < -50: 
        eagle_x = 550
        eagle_y = random.randint(100, 300)
        eagle_speed_x = random.randint(3, 6)
        eagle_speed_y = random.randint(-2, 2)

    if eagle2_x > 500 or eagle2_y > 450 or eagle2_y < -50:
        eagle2_x = -50
        eagle2_y = random.randint(100, 300)
        eagle2_speed_x = random.randint(3, 6)
        eagle2_speed_y = random.randint(-2, 2)

    window.fill((0, 0, 0))  
    window.blit(image, (0, 0))    
    #window.blit(parachute_img, (210, 30))
    window.blit(eagle_img, (eagle_x, eagle_y))
    window.blit(eagle2_img, (eagle2_x, eagle2_y))

    pygame.display.update()  

pygame.quit()

