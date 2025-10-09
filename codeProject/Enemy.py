from codeProject.Const import ENTITY_SPEED, WIDTH, ENTITY_SHOT_DELAY
from codeProject.EnemyFire import EnemyFire
from codeProject.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.disparo_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self ):
        self.disparo_delay -= 1
        if self.disparo_delay == 0:
            self.disparo_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyFire(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        return None

