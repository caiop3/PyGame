import pygame

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

game = True

eagle_x = 550
eagle_y = 200
eagle_speed = 3

clock = pygame.time.Clock()
FPS = 30

while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    eagle_x -= eagle_speed

    if eagle_x < -50:
        eagle_x = 550
        eagle_y = 200

    window.fill((0, 0, 0))  
    window.blit(image, (0, 0))    
    #window.blit(parachute_img, (210, 30))
    window.blit(eagle_img, (eagle_x, eagle_y))

    pygame.display.update()  

pygame.quit()