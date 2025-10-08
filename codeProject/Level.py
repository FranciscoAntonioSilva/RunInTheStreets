import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from codeProject.Const import COLOR_WHITE, WIDTH, HEIGHT, ENEMY_EVENT, COLOR_GREEN, COLOR_YELLOW, TIMEOUT_EVENT
from codeProject.Enemy import Enemy
from codeProject.Entity import Entity
from codeProject.EntityFactory import EntityFactory
from codeProject.EntityMediator import EntityMediator
from codeProject.Player import Player


class Level:

    def __init__(self, window: Surface, name: str, game_mode: str, player_pontuacao: list[int]):
        self.timeout = 20000 #20 segundos será a duração da fase
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name)) #Problema resolvido
        player = EntityFactory.get_entity('Player')
        player.score = player_pontuacao[0]
        self.entity_list.append(player)
        self.timeout = 10000 #20 segundos duração da fase
        pygame.time.set_timer(ENEMY_EVENT, 4000) #Tempo de spawn dos inimigos
        pygame.time.set_timer(TIMEOUT_EVENT, 100) #A cada 100 milisegundos quero checar a condição de vitória


    def run(self, player_pontuacao: list[int]):
        pygame.mixer_music.load(f'./assets/{self.name}.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60) #fps do jogo. Quanto mais, mais rápido será o jogo
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()#Observação
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player':
                    self.level_text(16, f'Jogador-Vida:{ent.life}', COLOR_GREEN, (10, 20))
                    self.level_text(16, f'Pontuação:{ent.pontuacao}', COLOR_YELLOW, (10, 35))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == ENEMY_EVENT:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == TIMEOUT_EVENT:
                    self.timeout -= 100 #Vai decrementar o tempo da fase em 100ms
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player':
                                player_pontuacao[0] = ent.pontuacao
                        return True

                found_player = False
                for ent in self.entity_list:
                    if ent in self.entity_list:
                        found_player = True

                    if not found_player:
                        return False

            #Texto da tela
            self.level_text(16, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(16, f'fps: {clock.get_fps() : .0f}', COLOR_WHITE, (10, HEIGHT - 35))
            self.level_text(16, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, HEIGHT - 20))
            pygame.display.flip()
            #Colisões
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_life(entity_list=self.entity_list)


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typerwriter', size= text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest= text_rect)

