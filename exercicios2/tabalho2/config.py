import pygame
import utils

RESOLUCAO = utils.Ponto(1000, 800)

KEY_UP = 0
KEY_DOWN = 1
KEY_LEFT = 2
KEY_RIGHT = 3

GRID_SIZE = 20
ESPACO_ENTRE_CELULAS = 0

# COLORS
COLORS = [
    (183, 28, 28),  # red darken-4
    (33, 150, 243),  # blue
    (0, 188, 212),  # cyan
    (0, 105, 92),  # teal darken-3
    (255, 111, 0),  # amber_darken-4
    (255, 214, 0)  # yellow accent-4
]

BACKGROUND_COLOR = (224, 247, 250)

# GAME SETTINGS
SCREEN = pygame.display.set_mode(RESOLUCAO.coordenadas())

title = 'Cobrinha Colorida !'
pygame.display.set_caption(title)

GAME_CLOCK = pygame.time.Clock()

# SURFACE DE CADA CELULA DA COBRA
COBRA_CELL_SURFACE = pygame.Surface((GRID_SIZE, GRID_SIZE))
