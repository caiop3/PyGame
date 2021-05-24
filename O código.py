import pygame

pygame.init()

WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paraquedista')

game = True

image = pygame.image.load('Referencia/montain.jpg').convert()
image = pygame.transform.scale(image, (125, 166))

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.fill((0, 0, 0))  
    window.blit(image, (10, 10))    
    
    pygame.display.update()  

pygame.quit()