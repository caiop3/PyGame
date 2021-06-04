#informaçoes base
WIDTH = 700 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Dados gerais do jogo.
Points = [0,0] #pontos dos jogadores
timer = FPS*10 #tempo para aparecer uma nova bolinha
espaço_da_tela = 10  #distancia do jogador de sua parede
ball_speed = 2.5 #velocidade das bolas
contato = 8 #define a largura da regiao de colisao que fica na frente do retangulo

# Define tamanhos
ball_WIDTH = 35
ball_HEIGHT = 35
player_WIDTH = 20
player_HEIGHT = 100

# Define as básicas
BLACK = (0, 0, 0)

# Estados para controle do fluxo da aplicação
DONE = 0
START = 1
PLAYING = 2
GAMEOVER = 3


