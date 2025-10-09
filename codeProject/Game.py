import pygame

from codeProject.Const import WIDTH, HEIGHT, MENU_OPTIONS
from codeProject.Level import Level
from codeProject.Menu import Menu
from codeProject.Score import Score

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIDTH, HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTIONS[0]:
                player_pontuacao = [0]
                level = Level(self.window, 'nivel1-', menu_return, player_pontuacao)
                level_return = level.run(player_pontuacao)

                if level_return:
                    level = Level(self.window, 'nivel2-', menu_return, player_pontuacao)
                    level_return = level.run(player_pontuacao)

                    if level_return:
                        level = Level(self.window, 'nivel3-', menu_return, player_pontuacao)
                        level_return = level.run(player_pontuacao)

                        if level_return:
                            level = Level(self.window, 'nivel4-', menu_return, player_pontuacao)
                            level_return = level.run(player_pontuacao)

                            if level_return:
                                score.save_score(menu_return, player_pontuacao)

            elif menu_return == MENU_OPTIONS[1]:
                score.show_score()
            elif menu_return == MENU_OPTIONS[2]:
                pygame.quit()
                quit()
            else:
                pass




