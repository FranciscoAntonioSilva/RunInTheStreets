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
    'Player': 3,#Com esse valor consigo definir a velocidade da minha nave
    'PlayerShot': 1,
    'Enemy1': 2, #Velocida do inimigo 1
    'Enemy1Shot': 5, #Disparo do inimigo 1
    'Enemy2': 1, #Velocidade do inimigo 2
    'Enemy2Shot': 2 #Disparo do inimigo 2
}

ENTITY_LIFE = {
    'nivel1-0': 999,
    'nivel1-1': 999,
    'nivel1-2': 999,
    'nivel1-3': 999,
    'nivel1-4': 999,
    'Player': 300,
    'PlayerShot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1
}

ENTITY_SHOT_DELAY = {
    'Player': 20,
    'Enemy1': 40,
    'Enemy2': 80
}

MENU_OPTIONS = ("NOVO JOGO",
                "PONTUAÇÃO",
                "SAIR DO JOGO")

PLAYER_KEY_DISPARO = {'Player': pygame.K_LCTRL}
