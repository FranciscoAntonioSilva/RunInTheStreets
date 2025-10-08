import datetime
import sys

import pygame
from pygame import Surface, Rect, K_DOWN, K_RETURN, K_BACKSPACE, KEYDOWN, K_ESCAPE
from pygame.font import Font

from codeProject.Const import COLOR_YELLOW, SCORE_POS, MENU_OPTIONS, COLOR_WHITE
from codeProject.DBProxy import DBProxy


class Score:


    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/Score.png').convert_alpha()
        self.rect = self.surf.get_rect()
        pass

    def save_score(self, menu_return: str, player_pontuacao: list[int]):
        pygame.mixer_music.load('./assets/score.wav')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!', COLOR_YELLOW, SCORE_POS['Title'])
            if menu_return == MENU_OPTIONS[0]:
                score = player_pontuacao[0]
                text = 'Player entre com seu nome (4 caracteres): '
            self.score_text(20, text, COLOR_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show_score()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, COLOR_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show_score(self):
        pygame.mixer_music.load('./assets/score.wav')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10!', COLOR_YELLOW, SCORE_POS['Title'])
        self.score_text(28, 'NAME           SCORE           DATE        ', COLOR_YELLOW, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id, name, score, date = player_score
            self.score_text(24, f'{name}              {score :05d}              {date}', COLOR_YELLOW,
                            SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()



    def score_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typerwriter', size= text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest= text_rect)


def get_formatted_date():
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d:%m %y")
    return f'{current_time} - {current_date}'
