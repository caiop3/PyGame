# --- Importações
from os import path

# --- Diretório das imagens, sons e fontes
IMG_DIR = path.join(path.dirname(__file__), 'Efeitos')

# --- Constantes
WIDTH = 900
HEIGHT = 600
FPS = 30

BALLOON_WIDTH = 40
BALLOON_HEIGHT = 50

EAGLE1_WIDTH = 10
EAGLE1_HEIGHT = 10

EAGLE2_WIDTH = 10
EAGLE2_HEIGHT = 10

COVID_WIDTH = 20
COVID_HEIGHT = 20

GEL_WIDTH = 20
GEL_HEIGHT = 20

# --- Máquina de estados
INIT = 0
GAME = 1
QUIT = 2
OVER = 3
PASS = 4
START = 5
WIN = 6

# --- Valor usado na animação, apesar de não ter nenhuma outra animação
STILL = 0