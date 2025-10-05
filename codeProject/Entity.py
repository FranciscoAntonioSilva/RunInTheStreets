from abc import ABC, abstractmethod

import pygame.image

from codeProject.Const import ENTITY_LIFE, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.life = ENTITY_LIFE[self.name] #Esse trecho trata da questão da vida
        self.dano = ENTITY_DAMAGE[self.name]
        self.pontuacao = ENTITY_SCORE[self.name] #Esse trecho no exemplo do professor está como score
        self.last_dano = 'None'

    @abstractmethod
    def move(self):
        pass
