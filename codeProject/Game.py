import pygame

from codeProject.Const import WIDTH, HEIGHT
from codeProject.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIDTH, HEIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



