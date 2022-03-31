import ProgramInterface
import numpy as np
import pygame
import pathlib
import Fonts

AnimalDir = pathlib.Path("sprites", "animals")

class Region(ProgramInterface.Window):
    '''ÐÐ°Ð·Ð¾Ð²ÑÐ¹ ÐºÐ»Ð°ÑÑ Ð¾Ð±Ð»Ð°ÑÑÐ¸'''
    def __init__(self, position:np.array, size:np.array):
        super().__init__([230, 230], [100, 100])
        self._max:int = 0
        self._number:float = 0.
        self._a:float = 0.
        width = size[0]
        height = size[1]
        x = position[0]
        y = position[1]
        object_img = pygame.image.load(pathlib.Path(AnimalDir, "Bunny16x16.png")).convert_alpha()
        object_count = self.Number

    @property
    def Max(self):
        '''ÐÐ°ÐºÑÐ¸Ð¼Ð°Ð»ÑÐ½Ð¾Ðµ ÐºÐ¾Ð»Ð¸ÑÐµÑÑÐ²Ð¾ Ð¾ÑÐ¾Ð±ÐµÐ¹, ÐºÐ¾ÑÐ¾ÑÐ¾Ðµ Ð¼Ð¾Ð¶ÐµÑ Ð²ÑÐ´ÐµÑÐ¶Ð°ÑÑ ÑÑÐµÐ´Ð°'''
        return self._max
    @Max.setter
    def Max(self, value):
        try:
            if value < 0:
                print('ÐÐµÐ´Ð¾Ð¿ÑÑÑÐ¸Ð¼Ð¾Ðµ Ð·Ð½Ð°ÑÐµÐ½Ð¸Ðµ Regions.Max')
            else:
                self._max = int(value)
        except:
            print('ÐÐµÐ´Ð¾Ð¿ÑÑÑÐ¸Ð¼Ð¾Ðµ Ð·Ð½Ð°ÑÐµÐ½Ð¸Ðµ Pegions.Max')

    @property
    def Number(self):
        '''ÐÐ¾Ð»Ð¸ÑÐµÑÑÐ²Ð¾ Ð¾ÑÐ¾Ð±ÐµÐ¹ Ð½Ð° Ð´Ð°Ð½Ð½ÑÐ¹ Ð¼Ð¾Ð¼ÐµÐ½Ñ'''
        return int(self._number)
    @Number.setter
    def Number(self, value):
        try:
            if value < 0:
                print('ÐÐµÐ´Ð¾Ð¿ÑÑÑÐ¸Ð¼Ð¾Ðµ Ð·Ð½Ð°ÑÐµÐ½Ð¸Ðµ Regions.Number')
                return
            if value == 0:
                self.kill()
                return
            self._number = float(value)
        except:
            print('ÐÐµÐ´Ð¾Ð¿ÑÑÑÐ¸Ð¼Ð¾Ðµ Ð·Ð½Ð°ÑÐµÐ½Ð¸Ðµ Regions.Number')

    @property
    def A(self):
        '''Ð£Ð´ÐµÐ»ÑÐ½ÑÐ¹ Ð¿ÑÐ¸ÑÐ¾ÑÑ'''
        return self._a
    @A.setter
    def A(self, value):
        try:
            self._a = float(value)
        except:
            print('ÐÐµÐ´Ð¾Ð¿ÑÑÑÐ¸Ð¼Ð¾Ðµ Ð·Ð½Ð°ÑÐµÐ½Ð¸Ðµ Regions.A')

    def SetMax(self):
        pass        
    
    def Eat(self):
        pass

    def Multiply(self):
        pass

    def Draw(self, size:np.array):
        width = size[0]
        height = size[1]
        self.image.fill((0, 0, 0, 120)) #0x00000078
        Label = Fonts.MainFont.render(str(self.Number), True, (255, 255, 255, 255))
        self.image.blit(Label, ((width - Label.get_width()) / 2, (height - Label.get_height()) / 2))
        self.Border()

    def update(self):
        self.SetMax()
        self.Eat()
        self.Multiply()
        self.Draw([23, 23])
