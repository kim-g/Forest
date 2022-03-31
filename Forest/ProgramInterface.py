import numpy as np
import pygame
import Fonts


class Window(pygame.sprite.Sprite):
    """Окно, появляющиеся внутри главного окна симуляции"""

    def __init__(self, position: np.array, size: np.array):
        """Инициализация окна"""
        super().__init__()
        self.Size = size;
        self.image = pygame.Surface((size[0], size[1]), pygame.SRCALPHA, 32).convert_alpha()
        self._top_border = pygame.Surface((size[0], 1), pygame.SRCALPHA, 32).convert_alpha()
        self._left_border = pygame.Surface((1, size[1]), pygame.SRCALPHA, 32).convert_alpha()#
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
        self.image.fill((0, 0, 0, 120))#0x00000078
        Label = Fonts.LargeFont.render('Пауза', True, (255, 255, 255, 255))
        self.image.blit(Label, ((width - Label.get_width()) / 2, (height - Label.get_height()) / 2))
        self.Border()

class AliveCountWindow(Window):
    '''Выдаёт окно, считающее количество животных и растений всего и каждого вида'''
    def __init__(self):
        monitor_info = pygame.display.Info()
        self._plants =  Fonts.MainFont.render('Растений:', True, (255, 255, 255, 255))
        self._turtles = Fonts.MainFont.render('Черепах:', True, (255, 255, 255, 255))
        self._wolves = Fonts.MainFont.render('Волков:', True, (255, 255, 255, 255))
        self._rabbits = Fonts.MainFont.render('Кроликов:', True, (255, 255, 255, 255)) #из Террарии
        self._animals = Fonts.MainFont.render('Животных:', True, (255, 255, 255, 255))
        self._plants_count:int = 0
        self._turtles_count:int = 0
        self._wolves_count:int = 0
        self._rabbit_count:int = 0
        self._animals_count:int = 0
        width = max(self._plants.get_width(), self._turtles.get_width(), self._wolves.get_width(), self._rabbits.get_width()) + 20
        height = int(self._plants.get_height()) + int(self._turtles.get_height()) + int(self._wolves.get_height()) + int(self._rabbits.get_height()) + 10 + self._animals.get_height()
        super().__init__(np.array([10, monitor_info.current_h - height - 10]), np.array([width, height]))
        self.image.fill((0, 0, 0, 120)) #0x00000078
        self.image.blit(self._animals, ((width - self._animals.get_width()) / 2, (height - self._animals.get_height()) / 10))
        self.image.blit(self._plants, ((width - self._plants.get_width()) / 2, (height - self._plants.get_height()) / 3.3))
        self.image.blit(self._turtles, ((width - self._turtles.get_width()) / 2, (height - self._turtles.get_height()) / 2))
        self.image.blit(self._wolves, ((width - self._wolves.get_width()) / 2, (height - self._wolves.get_height()) / 1.4))
        self.image.blit(self._rabbits, ((width - self._rabbits.get_width()) / 2, (height - self._rabbits.get_height()) / 1.1))

        @property
        def PlantsCount(self):
            return self._plants_count
        @PlantsCount.setter
        def PlantsCount(self, value:int):
            try:
                value = int(value)
            except:
                print("AliveCountWindow.PlantsCount не является целым числом")
                return

            self._plants_count = value
            self.image.fill((0, 0, 0, 120))
            Label = Fonts.MainFont.render('Растений: ' + str(self._plants_count), True, (255, 255, 255, 255))
            self.image.blit(Label, ((width - Label.get_width()) / 2, (height - Label.get_height()) / 2))

        @property
        def AnimalsCount(self):
            return self._animals_count
        @AnimalsCount.setter
        def AnimalsCount(self, value:int):
            try:
                value = int(value)
            except:
                print("AliveCountWindow.AnimalsCount не является целым числом")
                return

            self._animals_count = value
            self.image.fill((0, 0, 0, 120))
            Label = Fonts.MainFont.render('Животных: ' + str(self._animals_count), True, (255, 255, 255, 255))
            self.image.blit(Label, ((width - Label.get_width()) / 2, (height - Label.get_height()) / 2))

        @property
        def WolvesCount(self):
            return self._wolves_count
        @WolvesCount.setter
        def WolvesCount(self, value:int):
            try:
                value = int(value)
            except:
                print("AliveCountWindow.WolvesCount не является целым числом")
                return

            self._wolves_count = value
            self.image.fill((0, 0, 0, 120))
            Label = Fonts.MainFont.render('Волков: '+str(self._wolves_count), True, (255, 255, 255, 255))
            self.image.blit(Label, ((width - Label.get_width()) / 2, (height - Label.get_height()) / 2))

        @property
        def RabbitsCount(self):
            return self._rabbits_count
        @RabbitsCount.setter
        def PlantsCount(self, value:int):
            try:
                value = int(value)
            except:
                print("AliveCountWindow.RabbitsCount не является целым числом")
                return

            self._rabbits_count = value
            self.image.fill((0, 0, 0, 120))
            Label = Fonts.MainFont.render('Кроликов: '+str(self._rabbits_count), True, (255, 255, 255, 255))
            self.image.blit(Label, ((width - Label.get_width()) / 2, (height - Label.get_height()) / 2))

        @property
        def TurtlesCount(self):
            return self._turtles_count
        @TurtlesCount.setter
        def TurtlesCount(self, value:int):
            try:
                value = int(value)
            except:
                print("AliveCountWindow.TurtlesCount не является целым числом")
                return

            self._turtles_count = value
            self.image.fill((0, 0, 0, 120))
            Label = Fonts.MainFont.render('Черепах: '+str(self._turtles_count), True, (255, 255, 255, 255))
            self.image.blit(Label, ((width - Label.get_width()) / 2, (height - Label.get_height()) / 2))
        

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
