import pygame

pygame.init()

WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paraquedista')

game = True

image = pygame.image.load('Referencia/montain.jpg').convert()
image = pygame.transform.scale(image, (500, 400))
parachute_img = pygame.image.load('Referencia/parachute.png').convert_alpha()
parachute_img = pygame.transform.scale(parachute_img, (100, 100))

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.fill((0, 0, 0))  
    window.blit(image, (0, 0))    
    window.blit(parachute_img, (210, 30))

    pygame.display.update()  

pygame.quit()