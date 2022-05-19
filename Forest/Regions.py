import ProgramInterface
import numpy as np
import pygame
import pathlib
import Fonts
from Animals import AnimalDir
from Plants import PlantDir


class Region(ProgramInterface.Window):
    '''Базовый класс области'''

    def __init__(self, position: np.array, size: np.array):
        super().__init__(position, size)
        self._size = size
        self._max: int = 0
        self._number: float = 0.
        self._a: float = 0.
        width = size[0]
        height = size[1]
        x = position[0]
        y = position[1]
        self._object_img = pygame.image.load(pathlib.Path(AnimalDir, "Bunny16x16.png")).convert_alpha()
        self.image.blit(self._object_img,((width - self._object_img.get_width()) / 2, (height - self._object_img.get_height()) / 2))

    @property
    def Max(self):
        '''Максимальное количество особей, которое может выдержать среда'''
        return self._max

    @Max.setter
    def Max(self, value):
        try:
            if value < 0:
                print('Недопустимое значение Regions.Max')
            else:
                self._max = int(value)
        except:
            print('Недопустимое значение Pegions.Max')

    @property
    def Number(self):
        '''Количество особей на данный момент'''
        return self._number

    @Number.setter
    def Number(self, value):
        try:
            if value < 0:
                print('Недопустимое значение Regions.Number')
                return
            if value == 0:
                self.kill()
                return
            self._number = float(value)
        except:
            print('Недопустимое значение Regions.Number')

    @property
    def A(self):
        '''Удельный прирост'''
        return self._a

    @A.setter
    def A(self, value):
        try:
            self._a = float(value)
        except:
            print('Недопустимое значение Regions.A')

    def SetMax(self):
        pass

    def Eat(self):
        pass

    def Multiply(self):
        pass

    def Draw(self, size: np.array):
        width = size[0]
        height = size[1]
        self.image.fill((0, 0, 0, 120))  # 0x00000078
        Label = Fonts.MainFont.render(str(round(self.Number)), True, (255, 255, 255, 255))
        self.image.blit(Label, ((width - Label.get_width()) / 2, (height - Label.get_height()) / 2))
        self.image.blit(self._object_img,((width - self._object_img.get_width()) / 2, (height - self._object_img.get_height()) / 2))
        self.Border()

    def update(self):
        self.SetMax()
        self.Eat()
        self.Multiply()
        self.Draw(self._size)


class Ferhulst(Region):
    def __init__(self, position, size):
        super().__init__(position, size)
        self._size = size
        self.Max = ((self._size[0] * size[1]) / 256)*1000

    def Multiply(self):
        self.Number += self.A * (1 - (self.Number-1) / self.Max) * self.Number

    def update(self):
        self.Multiply()

class Region_Rabit(Ferhulst):
    def __init__(self, position, size):
        super().__init__(position, size)
        self._size = size
        self.Max *= (self._size[0]*size[1])/16

    def Multiply(self):
        self.Number += self.A * (1 - (self.Number-1) / self.Max) * self.Number

    def update(self):
        self.Multiply()
        self.Draw(self._size)

class Region_Grass(Ferhulst):
    def __init__(self, position, size):
        super().__init__(position, size)
        self._size = size
        self._object_img = pygame.image.load(pathlib.Path(PlantDir, "grass.png")).convert_alpha()
        self.Max *= (self._size[0] * size[1]) / 16

    def Multiply(self):
        self.Number += self.A * (1 - (self.Number-1) / self.Max) * self.Number

    def update(self):
        self.Multiply()
        self.Draw(self._size)
