from codeProject.Const import ENTITY_SPEED
from codeProject.Entity import Entity


class EnemyFire(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
