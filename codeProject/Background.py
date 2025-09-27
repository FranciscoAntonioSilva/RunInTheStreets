from codeProject.Const import WIDTH, ENTITY_SPEED
from codeProject.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name] #Velocidade das imagens
        if self.rect.right <= 0:
            self.rect.left = WIDTH
