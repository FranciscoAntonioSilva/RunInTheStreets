import random

from codeProject.Background import Background
from codeProject.Const import WIDTH, HEIGHT
from codeProject.Enemy import Enemy
from codeProject.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case "nivel1-":
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'nivel1-{i}', (0, 0)))
                    list_bg.append(Background(f'nivel1-{i}', (WIDTH, 0)))
                return list_bg
            case "Player":
                return Player('Player', (10, HEIGHT / 2))
            case "Enemy1":
                return Enemy('Enemy1', (WIDTH + 20, random.randint(20, HEIGHT - 20)))
            case "Enemy2":
                return Enemy('Enemy2', (WIDTH + 20, random.randint(20, HEIGHT - 20)))

