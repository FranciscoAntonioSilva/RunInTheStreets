import pygame

from codeProject.Const import ENTITY_SPEED, HEIGHT, WIDTH, PLAYER_KEY_DISPARO, ENTITY_SHOT_DELAY
from codeProject.Entity import Entity
from codeProject.PlayerFire import PlayerFire


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.disparo_delay = ENTITY_SHOT_DELAY[self.name]

    #Controle
    def move(self,):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        elif pressed[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        elif pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        elif pressed[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shoot(self):
        self.disparo_delay -= 1
        if self.disparo_delay == 0:
            self.disparo_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_DISPARO[self.name]]:
                #Esse self.name Shot, é referente ao nome do arquivo dos tiros
                return PlayerFire(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
