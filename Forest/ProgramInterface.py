import numpy as np
import pygame
import Fonts


class Window(pygame.sprite.Sprite):
    """Окно, появляющиеся внутри главного окна симуляции"""

    def __init__(self, position:np.array, size:np.array):
        """Инициализация окна"""
        super().__init__()
        self._myrect:pygame.Surface = None
        self.image = pygame.Surface((size[0], size[1]), pygame.SRCALPHA, 32).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = position[0]
        self.rect.top = position[1]
        self._show:bool = True;

    @property 
    def Show(self):
        """Определяет, показывать ли элемент"""
        return self._show
    @Show.setter
    def Show(self, value:bool):
        self._show = bool(value)
        if self._show:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(0)

class PauseWindow(Window):
    """Выдаёт окно паузы"""
    def __init__(self):
        monitor_info = pygame.display.Info()
        width = 150
        height = 70
        super().__init__(np.array([(monitor_info.current_w-width) / 2, (monitor_info.current_h-height) / 2]), np.array([width, height]))
        self.image.fill((0, 0, 0, 120))
        Label = Fonts.LargeFont.render('Пауза', False, (255, 255, 255))
        self.image.blit(Label, ((width - Label.get_width()) / 2, (height - Label.get_height()) / 2))
