import pygame


COLOR_PRIMARY = (200, 237, 242)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)

WIDTH = 570
HEIGHT = 324

ENEMY_EVENT = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'nivel1-0': 0,
    'nivel1-1': 1,
    'nivel1-2': 2,
    'nivel1-3': 3,
    'nivel1-4': 4,
    'Player': 3, #Com esse valor consigo definir a velocidade da minha nave
    'Enemy1': 2,
    'Enemy2': 1
}

MENU_OPTIONS = ("NOVO JOGO",
                "PONTUAÇÃO",
                "SAIR DO JOGO")
