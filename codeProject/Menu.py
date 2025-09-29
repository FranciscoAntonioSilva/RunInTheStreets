import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from codeProject.Const import WIDTH, COLOR_PRIMARY, MENU_OPTIONS, COLOR_WHITE, COLOR_BLUE


class Menu:

    def __init__(self, window):
        self.window = window
        # Definindo imagem de fundo para menu
        self.surf = pygame.image.load('./assets/menu.png').convert_alpha()
        # Retângulo para receber a imagem
        self.rect = self.surf.get_rect()


    def run(self, ):
        menu_option = 0
        # Definindo música e depois colocando para tocar
        # Com o parâmetro -1, a música vai recomeçar toda vez que acabar
        pygame.mixer_music.load('./assets/menu.wav')
        pygame.mixer_music.play(-1)

        while True:
            # O blit() vai desenhar a imagem no surfe e mandar para o rect
            self.window.blit(source=self.surf, dest=self.rect)
            # Titulo do jogo e suas definições
            self.menu_info(50, "AirCombat", COLOR_PRIMARY, ((WIDTH / 2), 100))

            # Definindo as informações do menu com um laço
            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_info(20, '> ' + MENU_OPTIONS[i] + ' <', COLOR_BLUE, ((WIDTH / 2), 200 + 35 * i))
                else:
                    self.menu_info(20, MENU_OPTIONS[i], COLOR_WHITE, ((WIDTH / 2), 200 + 35 * i))

            pygame.display.flip()

            # Checando todos os eventos
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                 if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_DOWN: #Tecla para baixo
                         if menu_option < len(MENU_OPTIONS) -1:
                             menu_option += 1
                         else:
                             menu_option = 0

                     if event.key == pygame.K_UP:  # Tecla para cima
                         if menu_option > 0:
                             menu_option -= 1
                         else:
                             menu_option = len(MENU_OPTIONS) - 1

                     if event.key == pygame.K_RETURN: #Enter
                         return MENU_OPTIONS[menu_option]



    def menu_info(self, text_size: int, text: str, color: tuple, text_align: tuple):
        text_font: Font = pygame.font.SysFont("Impact, sans-serif", size=text_size)
        text_surf: Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_align)
        self.window.blit(source=text_surf, dest=text_rect)

