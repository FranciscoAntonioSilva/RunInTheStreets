import pygame

from codeProject.Const import WIDTH, HEIGHT, MENU_OPTIONS
from codeProject.Level import Level
from codeProject.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIDTH, HEIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTIONS[0]:
                # Como o game não vai ter modo competitivo, não vou usar o menu_return
                level = Level(self.window, 'Level 1')
                level_return = level.run()
            elif menu_return == MENU_OPTIONS[2]:
                pygame.quit()
                quit() #Vai sair do game
            else:
                pass




