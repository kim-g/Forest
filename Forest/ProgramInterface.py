import numpy as np
import pygame
import Fonts


class Window(pygame.sprite.Sprite):
    """Окно, появляющиеся внутри главного окна симуляции"""

    def __init__(self, position:np.array, size:np.array):
        """Инициализация окна"""
        super().__init__()
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
        width = 200
        height = 70
        super().__init__(np.array([(monitor_info.current_w-width) / 2, (monitor_info.current_h-height) / 2]), np.array([width, height]))
        self.image.fill((0, 0, 0, 120)) #0x00000078
        Label = Fonts.LargeFont.render('Пауза', True, (255, 255, 255, 255))
        self.image.blit(Label, ((width - Label.get_width()) / 2, (height - Label.get_height()) / 2))

class StepsWindow(Window):
    """Показывает колличество ходов, прошедших с начала запуска"""

    def __init__(self):
        monitor_info = pygame.display.Info()
        Label = Fonts.MainFont.render('Ходов: , ', True, (255, 255, 255, 255))
        Label2 = Fonts.MainFont.render('ВремяМ: , ', True, (255, 255, 255, 255)) 
        Label3 = Fonts.MainFont.render('ХодовЧ: , ', True, (255, 255, 255, 255))
        Label4 = Fonts.MainFont.render('ВремяД: , ', True, (255, 255, 255, 255))
        d_h = 4
        self.width = 150
        self.height = Label2.get_height() + d_h * 14
        self._count:int = 0
        super().__init__(np.array([10, monitor_info.current_h - self.height - 800]), np.array([self.width, self.height]))
        self.image.fill((0, 0, 0, 120))
        self.image.blit(Label,  ((self.width - Label.get_width()) / 2, (self.height - Label.get_height()) / 2)) 
        self.image.blit(Label2,  ((self.width - Label2.get_width()) / 2, (self.height - Label2.get_height()) / 2)) 
        
        


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
        self._count1=value
        self._count2=int(self._count1/60)
        self._count1 = self._count1 - self._count2 * 60
        self._count3=int(self._count2/24)
        self._count2 = self._count2- self._count3* 24
        
        
        self.image.fill((0, 0, 0, 120))
        Label = Fonts.MainFont.render('Ходов: '+str(self._count), True, (255, 255, 255, 255))
        Label2 = Fonts.MainFont.render('Время: '+str(self._count3) + "д" + ":" + str(self._count2) + "ч" + ":" + str(self._count1) + "м", True, (255, 255, 255, 255))

        self.image.blit(Label, ((self.width - Label2.get_width()) / 2, (self.height - Label2.get_height()) / 4)) 
        self.image.blit(Label2,  ((self.width - Label2.get_width()) / 2, (self.height - Label2.get_height()) / 2)) 
        
        

        
 
        
