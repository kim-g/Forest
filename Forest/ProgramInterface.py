import numpy as np
import pygame
import Fonts


class Window(pygame.sprite.Sprite):
    """Окно, появляющиеся внутри главного окна симуляции"""

    def __init__(self, position: np.array, size: np.array):
        """Инициализация окна"""
        super().__init__()
        self.image = pygame.Surface((size[0], size[1]), pygame.SRCALPHA, 32).convert_alpha()
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

class PauseWindow(Window):
    """Выдаёт окно паузы"""
    def __init__(self):
        monitor_info = pygame.display.Info()
        width = 200
        height = 70
        super().__init__(np.array([(monitor_info.current_w-width) / 2, (monitor_info.current_h-height) / 2]), np.array([width, height]))
        self.image.fill((0, 0, 0, 120))#0x00000078
        Label = Fonts.LargeFont.render('Пауза', True, (255, 255, 255, 255))
        self.image.blit(Label, ((width - Label.get_width()) / 2, (height - Label.get_height()) / 2))

class StepsWindow(Window):
    """Показывает колличество ходов, прошедших с начала запуска"""

    def __init__(self):
        monitor_info = pygame.display.Info()
        Label = Fonts.MainFont.render('Ходов:', True, (255, 255, 255, 255))
        d_h = 4
        self.width = 150
        self.height = Label.get_height() + d_h * 2
        self._count:int = 0
        super().__init__(np.array([10, monitor_info.current_h - self.height - 10]), np.array([self.width, self.height]))
        self.image.fill((0, 0, 0, 120))
        self.image.blit(Label, ((self.width - Label.get_width()) / 2, (self.height - Label.get_height()) / 2))

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
        self.image.fill((0, 0, 0, 120))
        Label = Fonts.MainFont.render('Ходов: '+str(self._count), True, (255, 255, 255, 255))
        self.image.blit(Label, ((self.width - Label.get_width()) / 2, (self.height - Label.get_height()) / 2))


class BiomassCount(Window):
    def __init__(self):
        self._all_bio_count = 0.
        monitor_info = pygame.display.Info()
        Label = Fonts.MainFont.render('общ кол-во биомассы:', True, (255, 255, 255, 255))

        self.width = 300
        self.height = 20
        super().__init__(np.array([monitor_info.current_w - self.width - 10, 10]), np.array([self.width, self.height]))
        self.image.fill((0, 0, 0, 120))
        self.image.blit(Label, ((self.width - Label.get_width()) / 2, (self.height - Label.get_height()) / 2))

    @property
    def All_Bio_Count(self):
        return int(self._all_bio_count)

    @All_Bio_Count.setter
    def All_Bio_Count(self, value: float):
        try:
            value = float(value)
        except:
            print("BiomassCount.All_Bio_Count не является float")
            return
        self._all_bio_count = int(value)
        self.image.fill((0, 0, 0, 120))
        Label = Fonts.MainFont.render('общ кол-во биомассы: ' + str(self._all_bio_count), True, (255, 255, 255, 255))
        self.image.blit(Label, ((self.width - Label.get_width()) / 2, (self.height - Label.get_height()) / 2))



class BiomassCountAnimal(Window):
    def __init__(self):
        self._animals_bio_count = 0.
        monitor_info = pygame.display.Info()
        Label = Fonts.MainFont.render('общ кол-во биомассы животного:', True, (255, 255, 255, 255))
        self.width = 300
        self.height = 20
        super().__init__(np.array([monitor_info.current_w - self.width - 10, 30]),np.array([self.width, self.height]))
        self.image.fill((0, 0, 0, 120))
        self.image.blit(Label, ((self.width - Label.get_width()) / 2, (self.height - Label.get_height()) / 2))

    @property
    def Animal_Bio_Count(self):
        return self._animals_bio_count

    @Animal_Bio_Count.setter
    def Animal_Bio_Count(self, value: float):
        try:
            value = float(value)
        except:
            print("BiomassCount.All_Bio_Count не является float")
            return
        self._animals_bio_count = int(value)
        self.image.fill((0, 0, 0, 120))
        Label = Fonts.MainFont.render('общ кол-во биомассы животного: ' + str(self._animals_bio_count), True,
                                      (255, 255, 255, 255))
        self.image.blit(Label, ((self.width - Label.get_width()) / 2, (self.height - Label.get_height()) / 2))

class BiomassCountPlants(Window):
    def __init__(self):
        self._plants_bio_count = 0.
        monitor_info = pygame.display.Info()
        Label = Fonts.MainFont.render('общ кол-во биомассы растения:', True, (255, 255, 255, 255))
        self.width = 300
        self.height = 20
        super().__init__(np.array([monitor_info.current_w - self.width - 10, 50]), np.array([self.width, self.height]))
        self.image.fill((0, 0, 0, 120))
        self.image.blit(Label, ((self.width - Label.get_width()) / 2, (self.height - Label.get_height()) / 2))

    @property
    def Plants_Bio_Count(self):
        return int(self._plants_bio_count)

    @Plants_Bio_Count.setter
    def Plants_Bio_Count(self, value: float):
        try:
            value = float(value)
        except:
            print("")
            return
        self._plants_bio_count = int(value)
        self.image.fill((0, 0, 0, 120))
        Label = Fonts.MainFont.render('общ кол-во биомассы растения: ' + str(self._plants_bio_count), True,
                                      (255, 255, 255, 255))
        self.image.blit(Label, ((self.width - Label.get_width()) / 2, (self.height - Label.get_height()) / 2))



class Region(Window):
    '''базовый класс области'''
    def __init__(self,position: np.array, size: np.array):
        self._specific_increase = 0.
        super().__init__(position,size)
    @property
    def Specific_Increase(self):
        return self._specific_increase
    @Specific_Increase.setter
    def Specific_Increase(self,value: float):
        try:
            self._specific_increase=float(value)
        except:
            print("Region.Specific_Increase не является float")
