import numpy as np
import pygame
import Fonts


class Window(pygame.sprite.Sprite):
    """Окно, появляющиеся внутри главного окна симуляции"""

    def __init__(self, position:np.array, size:np.array):
        """Инициализация окна"""
        super().__init__()
        self.Size = size;
        self.image = pygame.Surface((size[0], size[1]), pygame.SRCALPHA, 32).convert_alpha()
        self._top_border = pygame.Surface((size[0], 1), pygame.SRCALPHA, 32).convert_alpha()
        self._left_border = pygame.Surface((1, size[1]), pygame.SRCALPHA, 32).convert_alpha()
        self._right_border = pygame.Surface((1, size[1]), pygame.SRCALPHA, 32).convert_alpha()
        self._bottom_border:pygame.Surface = pygame.Surface((size[0], 1), pygame.SRCALPHA, 32).convert_alpha()
        self.color = (0, 0, 0, 255)
        self._top_border.fill(self.color)
        self._left_border.fill(self.color)
        self._right_border.fill(self.color)
        self._bottom_border.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.left = position[0]
        self.rect.top = position[1]
        self._show:bool = True

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

    def Border(self):
        """Рисование рамки вокруг окна."""
        monitor_info = pygame.display.Info()
        self.image.blit(self._top_border, (0,0))
        self.image.blit(self._left_border, (0,0))
        self.image.blit(self._right_border, (self.Size[0]-1, 0))
        self.image.blit(self._bottom_border, (0,self.Size[1]-1))

class PauseWindow(Window):
    """Выдаёт окно паузы"""
    def __init__(self):
        monitor_info = pygame.display.Info()
        width = 200
        height = 70
        super().__init__(np.array([(monitor_info.current_w-width) / 2, (monitor_info.current_h-height) / 2]), np.array([width, height]))
        self.image.fill((0, 0, 0, 120)) #0x00000078
        Label = Fonts.LargeFont.render('Пауза', True, (255, 255, 255, 255))
        self.image.blit(Label, ((width - Label.get_width()) / 2, (height - Label.get_height()) / 2))
        self.Border()

class StepsWindow(Window):
    """Показывает колличество ходов, прошедших с начала запуска"""

    def __init__(self):
        monitor_info = pygame.display.Info()
        Label = Fonts.MainFont.render('Ходов: 0', True, (255, 255, 255, 255))
        Label2 = Fonts.MainFont.render('Время: 0 д. 00:00', True, (255, 255, 255, 255)) 
        self.d_h = 4
        self.width = 150
        self.height = Label.get_height() + Label2.get_height() + self.d_h * 3
        self._count:int = 0
        super().__init__(np.array([10, 10]), np.array([self.width, self.height]))
        self.image.fill((0, 0, 0, 120))
        self.image.blit(Label, ((self.width - Label.get_width()) / 2, self.d_h)) 
        self.image.blit(Label2,  ((self.width - Label2.get_width()) / 2, self.d_h * 2 + Label.get_height())) 
        
        


    @property
    def Count(self):
        """Количество ходов"""
        return self._count
    @Count.setter
    def Count(self, value:int):
        try:
            value = int(value)
        except:
            print("StepsWindow.Count не является целым числом")
            return


        self._count = value
        self._count1 = value
        self._count2 = int(self._count1 / 60)
        self._count1 = self._count1 - self._count2 * 60
        self._count3 = int(self._count2 / 24)
        self._count2 = self._count2 - self._count3 * 24

        hours = "0" + str(self._count2) if self._count2 < 10 else str(self._count2)
        minutes  = "0" + str(self._count1) if self._count1 < 10 else str(self._count1)
        
        
        self.image.fill((0, 0, 0, 120))
        Label = Fonts.MainFont.render('Ходов: '+str(self._count), True, (255, 255, 255, 255))
        Label2 = Fonts.MainFont.render('Время: '+str(self._count3) + "д. " + hours + ":" + minutes, True, (255, 255, 255, 255))

        self.image.blit(Label, ((self.width - Label.get_width()) / 2, self.d_h)) 
        self.image.blit(Label2,  ((self.width - Label2.get_width()) / 2, self.d_h * 2 + Label.get_height())) 

        self.Border()
        
        

        
 
        
