import pygame
import random
import math
from config import FPS, timer, contato, ball_speed, WIDTH, HEIGHT, BLACK, Points,  DONE, PLAYING, GAMEOVER
from assets import load_assets
from sprites import Player, Ball 

def game_screen(window):
    global timer
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    # Criando os jogadores
    player1 = Player(assets['player1_img'],1)
    player2 = Player(assets['player2_img'],2)
    all_sprites.add(player1)
    all_sprites.add(player2)

    # Criando o array das bolas
    all_balls = pygame.sprite.Group()

    #inicia e cria a fonte
    pygame.font.init()
    font = pygame.font.Font(None, 48)

    pont = [0,0] #array de apoio para detectar alteraçao na pontuação

    state = PLAYING
    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while state == PLAYING:
        clock.tick(FPS)
        timer += 1
        if timer > FPS*10: #cria uma nova bola apos o timer
            timer = 0
            bola = Ball(assets['ball_img'])
            #definir a direção e a velocidade inicial da bola
            a = 1 #variavel da direção da bola
            if Points[0] > pont[0]: #se o player 1 acabou de ganhar um ponto, a primeira bola vai ir para seu oposto
                pont[0] += 1
                a = 1
            if Points[1] > pont[1]: #se o player 2 acabou de ganhar um ponto, a primeira bola vai ir para seu oposto
                pont[1] += 1
                a = -1
            if len(all_balls)%2 == 0: #apos a primeira bola, as seguintes apareceram alternando as direções
                bola.speedx = a*ball_speed
            else: 
                bola.speedx = a*ball_speed
            all_sprites.add(bola)
            all_balls.add(bola)

        for bolinha in all_balls: #atualiza as condiçoes das bolinhas
            # colisao da bola com os players, que randomiza os valores da direção
            #player1
            if bolinha.rect.left < player1.rect.right+contato and bolinha.rect.left > player1.rect.right and bolinha.rect.top < player1.rect.bottom and bolinha.rect.bottom > player1.rect.top:
                assets['pew_sound'].play()
                rng = random.randint(12,20)
                angulo = (rng*math.pi)/16
                bolinha.speedx = -(ball_speed*math.cos(angulo))
                bolinha.speedy = ball_speed*math.sin(angulo)
            #player2
            if bolinha.rect.right > player2.rect.left-contato and bolinha.rect.right < player2.rect.left and bolinha.rect.top < player2.rect.bottom and bolinha.rect.bottom > player2.rect.top:
                assets['pew_sound'].play()
                rng = random.randint(12,20)
                angulo = (rng*math.pi)/16
                bolinha.speedx = ball_speed*math.cos(angulo)
                bolinha.speedy = ball_speed*math.sin(angulo)
            #renicia as bolinhas caso alg pontue 
            if bolinha.rect.left > WIDTH: #player 1 ganha ponto
                assets['destroy_sound'].play()
                bolinha.rect.centerx = WIDTH/2
                bolinha.rect.centery = HEIGHT/2
                bolinha.speedx = ball_speed
                bolinha.speedy = 0
                Points[0] += 1
                timer = 8*FPS
                for bolinha in all_balls:
                    bolinha.kill() 
                
            if bolinha.rect.right < 0: #player 2 ganha ponto
                assets['destroy_sound'].play()
                bolinha.rect.centerx = WIDTH/2
                bolinha.rect.centery = HEIGHT/2
                bolinha.speedx = -ball_speed
                bolinha.speedy = 0 
                Points[1] += 1
                timer = 8*FPS
                for bolinha in all_balls:
                    bolinha.kill()

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    #player1
                    if event.key == pygame.K_w:
                        player1.speedy = -10
                    if event.key == pygame.K_s:
                        player1.speedy = 10
                    #player2
                    if event.key == pygame.K_UP:
                        player2.speedy = -10
                    if event.key == pygame.K_DOWN:
                        player2.speedy = 10
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    #player1
                    if event.key == pygame.K_w:
                        player1.speedy = 0
                    if event.key == pygame.K_s:
                        player1.speedy = 0
                    #player2
                    if event.key == pygame.K_UP:
                        player2.speedy = 0
                    if event.key == pygame.K_DOWN:
                        player2.speedy = 0

        # Atualizando a posição dos sprites
        all_sprites.update()

        #atualiza a tela
        window.fill(BLACK)  
        window.blit(assets['background'], (0, 0))
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = font.render("{}   {}".format(Points[0],Points[1]), True, (0, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        #verifica se a quantidade de pontos para dar game over
        for pontos in Points:
            if pontos >= 3:
                state = GAMEOVER
                #reenicia todas as codições dos jogadores
                player1.speedy = 0
                player2.speedy = 0
                player1.rect.centery = HEIGHT/2
                player2.rect.centery = HEIGHT/2
        pygame.display.update()  # Mostra o novo frame para o jogador
    pygame.mixer.music.stop()  #para a musica
    return state
