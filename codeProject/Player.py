import pygame

from codeProject.Const import ENTITY_SPEED, HEIGHT, WIDTH
from codeProject.Entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

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
