import pygame


COLOR_PRIMARY = (200, 237, 242)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW =  (255, 255, 0)

WIDTH = 570
HEIGHT = 324

ENEMY_EVENT = pygame.USEREVENT + 1

TIMEOUT_EVENT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'nivel1-0': 0,
    'nivel1-1': 1,
    'nivel1-2': 2,
    'nivel1-3': 3,
    'nivel1-4': 4,
    'nivel2-0': 0,
    'nivel2-1': 1,
    'nivel2-2': 2,
    'nivel2-3': 3,
    'nivel2-4': 4,
    'nivel2-5': 5,
    'nivel2-6': 6,
    'nivel3-0': 0,
    'nivel3-1': 1,
    'nivel3-2': 2,
    'nivel3-3': 3,
    'nivel3-4': 4,
    'nivel3-5': 5,
    'nivel4-0': 0,
    'nivel4-1': 1,
    'nivel4-2': 2,
    'nivel4-3': 3,
    'nivel4-4': 4,
    'nivel4-5': 5,
    'nivel4-6': 6,
    'nivel4-7': 7,
    'Player': 3,
    'PlayerShot': 1,
    'Enemy1': 2,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 2
}

ENTITY_LIFE = {
    'nivel1-0': 999,
    'nivel1-1': 999,
    'nivel1-2': 999,
    'nivel1-3': 999,
    'nivel1-4': 999,
    'nivel2-0': 999,
    'nivel2-1': 999,
    'nivel2-2': 999,
    'nivel2-3': 999,
    'nivel2-4': 999,
    'nivel2-5': 999,
    'nivel2-6': 999,
    'nivel3-0': 999,
    'nivel3-1': 999,
    'nivel3-2': 999,
    'nivel3-3': 999,
    'nivel3-4': 999,
    'nivel3-5': 999,
    'nivel4-0': 999,
    'nivel4-1': 999,
    'nivel4-2': 999,
    'nivel4-3': 999,
    'nivel4-4': 999,
    'nivel4-5': 999,
    'nivel4-6': 999,
    'nivel4-7': 999,
    'Player': 200,
    'PlayerShot': 1,
    'Enemy1': 120,
    'Enemy1Shot': 1,
    'Enemy2': 160,
    'Enemy2Shot': 1
}

ENTITY_SHOT_DELAY = {
    'Player': 20,
    'Enemy1': 40,
    'Enemy2': 80
}

ENTITY_DAMAGE = {
    'nivel1-0': 0,
    'nivel1-1': 0,
    'nivel1-2': 0,
    'nivel1-3': 0,
    'nivel1-4': 0,
    'nivel2-0': 0,
    'nivel2-1': 0,
    'nivel2-2': 0,
    'nivel2-3': 0,
    'nivel2-4': 0,
    'nivel2-5': 0,
    'nivel2-6': 0,
    'nivel3-0': 0,
    'nivel3-1': 0,
    'nivel3-2': 0,
    'nivel3-3': 0,
    'nivel3-4': 0,
    'nivel3-5': 0,
    'nivel4-0': 0,
    'nivel4-1': 0,
    'nivel4-2': 0,
    'nivel4-3': 0,
    'nivel4-4': 0,
    'nivel4-5': 0,
    'nivel4-6': 0,
    'nivel4-7': 0,
    'Player': 1,
    'PlayerShot': 25,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15
}

ENTITY_SCORE = {
    'nivel1-0': 0,
    'nivel1-1': 0,
    'nivel1-2': 0,
    'nivel1-3': 0,
    'nivel1-4': 0,
    'nivel2-0': 0,
    'nivel2-1': 0,
    'nivel2-2': 0,
    'nivel2-3': 0,
    'nivel2-4': 0,
    'nivel2-5': 0,
    'nivel2-6': 0,
    'nivel3-0': 0,
    'nivel3-1': 0,
    'nivel3-2': 0,
    'nivel3-3': 0,
    'nivel3-4': 0,
    'nivel3-5': 0,
    'nivel4-0': 0,
    'nivel4-1': 0,
    'nivel4-2': 0,
    'nivel4-3': 0,
    'nivel4-4': 0,
    'nivel4-5': 0,
    'nivel4-6': 0,
    'nivel4-7': 0,
    'Player': 0,
    'PlayerShot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 120,
    'Enemy2Shot': 0
}

MENU_OPTIONS = ("NOVO JOGO",
                "PONTUAÇÃO",
                "SAIR DO JOGO")

PLAYER_KEY_DISPARO = {'Player': pygame.K_LCTRL}

SCORE_POS = {
    'Title': (WIDTH / 2, 50),
    'EnterName': (WIDTH / 2, 80),
    'Label': (WIDTH / 2, 90),
    'Name': (WIDTH / 2, 110),
    0: (WIDTH / 2, 110),
    1: (WIDTH / 2, 130),
    2: (WIDTH / 2, 150),
    3: (WIDTH / 2, 170),
    4: (WIDTH / 2, 190),
    5: (WIDTH / 2, 210),
    6: (WIDTH / 2, 230),
    7: (WIDTH / 2, 250),
    8: (WIDTH / 2, 270),
    9: (WIDTH / 2, 290),
}

