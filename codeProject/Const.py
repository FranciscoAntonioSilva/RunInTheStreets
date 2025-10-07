import pygame


COLOR_PRIMARY = (200, 237, 242)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW =  (255, 255, 0) #Pode ser que eu mude essa variável para vermelho

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
    'nivel2-0': 999,
    'nivel2-1': 999,
    'nivel2-2': 999,
    'nivel2-3': 999,
    'nivel2-4': 999,
    'nivel2-5': 999,
    'nivel2-6': 999,
    'Player': 300,
    'PlayerShot': 1,
    'Enemy1': 80,
    'Enemy1Shot': 1,
    'Enemy2': 120,
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
